import duckdb
import pandas as pd
from pathlib import Path

# ========================================
# CARGAR DATOS EN DUCKDB
# ========================================

# Crear una conección de DuckDB in-memory
con = duckdb.connect()

# Otra alternativa sería crear una base de datos DuckDB persistente mediante:
# con = duckdb.connect('my_database.db')

# Leer archivos JSON directamente con DuckDB
con.execute("""
            CREATE TABLE access_logs AS
            SELECT * FROM read_json_auto('logs/access_logs.json')
""")

# Verificar que se cargó correctamente
print("Total de filas:", con.execute("SELECT COUNT(*) FROM access_logs").fetchone()[0])

# Mostrar estructura y tipo de datos de la tabla

print("\nCantidad de columnas:")
for col in con.execute("DESCRIBE access_logs").fetchall():
    print(f"    {col[0]}: {col[1]}")

# Ver las primeras tres filas
print("\nLas primeras tres filas son:")
print(con.execute("SELECT * FROM access_logs LIMIT 3").fetchdf())

# ========================================
# EXPLORACIÓN INICIAL
# ========================================

df1 = con.execute(
    """WITH cte AS (
        SELECT
            MIN(timestamp) as fecha_inicial,
            MAX(timestamp) as fecha_final,
            COUNT(*) as cantidad_filas,
            COUNT(DISTINCT client_ip) as ip_unicas,
            COUNT(DISTINCT user_id) as id_unicos,
        FROM access_logs)
    SELECT
        fecha_inicial as "FECHA INICIAL",
        fecha_final as "FECHA FINAL",
        (fecha_final - fecha_inicial) as DURACION,
        cantidad_filas as "CANTIDAD FILAS",
        ip_unicas as "CANT IP UNICAS",
        id_unicos as "CANT ID UNICOS"
    FROM cte"""
).fetchdf()

# ========================================
# ENDPOINTS MÁS USADOS
# ========================================

df2 = con.execute(
    """SELECT
            endpoint as ENDPOINT,
            COUNT(*) as "CANT PETICIONES",
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM access_logs), 2) as PORCENTAJE           
        FROM access_logs
        GROUP BY endpoint
        ORDER BY "CANT PETICIONES" DESC        
    """
).fetchdf()

# ========================================
# ANALISIS DE ERRORES
# ========================================

df3 = con.execute(
    """
    SELECT
        endpoint as ENDPOINT,
        COUNT(*) as "ERRORES TOTALES",
        COUNT(DISTINCT user_id) as "USUARIOS AFECTADOS",
        ROUND(AVG(response_time_ms),2) as "RESPONSE TIME PROMEDIO",
        status_code as STATUS_CODE
    FROM access_logs
    WHERE status_code >= 400
    GROUP BY endpoint, status_code
    ORDER BY "ERRORES TOTALES" DESC
    """
).fetchdf()

# ========================================
# PERFORMANCE POR ENDPOINT
# ========================================

df4 = con.execute(
    """
    SELECT
        endpoint as ENDPOINT,
        COUNT(*) as "CANT REQUESTS",
        PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY response_time_ms) as "p90 RANK",
        PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY response_time_ms) as "p95 RANK",
        MAX(response_time_ms) as "TIEMPO MAXIMO"  
    FROM access_logs
    WHERE status_code < 400 -- Filtro requests exitosos
    GROUP BY endpoint
    ORDER BY "p95 RANK" DESC
    """
).fetchdf()

# ========================================
# TENDENCIA HORARIA
# ========================================
# Identificar picos de tráfico según la hora para planificar capacidad y poder escalar a futuro.
# Para esto busco la hora a la cual se da la mayor cantidad de requests y el mayor tiempo de respuesta para cada endpoint

df5 = con.execute(
    """
    SELECT
        EXTRACT(HOUR FROM timestamp) AS HORA,
        endpoint as ENDPOINT,
        COUNT(*) AS "CANT REQUESTS",
        ROUND(AVG(response_time_ms),2) AS "RESPONSE TIME AVG"
    FROM access_logs
    GROUP BY HORA, ENDPOINT
    ORDER BY "CANT REQUESTS" DESC;
    """
).fetchdf()

# ========================================
# RANKING DE REQUESTS (EXITOSOS) MÁS LENTOS
# ========================================

df6 = con.execute(
    """
    WITH ranking AS (
        SELECT
            timestamp as TIMESTAMP,
            endpoint as ENDPOINT,
            response_time_ms as "RESPONSE TIME",
            user_id as USER_ID,
            ROW_NUMBER() OVER(PARTITION BY endpoint ORDER BY response_time_ms DESC) as RN
        FROM access_logs
        WHERE status_code < 400    
    )
    SELECT * FROM ranking
    WHERE RN <= 3
    ORDER BY endpoint, RN DESC
    """
).fetchdf()

# ========================================
# COMPARACION CON EL PERÍODO ANTERIOR
# ========================================

df7 = con.execute(
    """
    WITH calculo AS (
        SELECT
            DATE(timestamp) as fecha,
            endpoint,
            response_time_ms,
            status_code,
            LAG(response_time_ms, 1) OVER(PARTITION BY endpoint ORDER BY fecha DESC) as response_prev
        FROM access_logs
        ORDER BY fecha
    ) SELECT
        fecha as FECHA,
        endpoint as ENDPOINT,
        response_time_ms as "RESPONSE TIME ACTUAL",
        response_prev as "PERIODO ANTERIOR",
        response_time_ms - response_prev as DIFFERENCE
    FROM calculo
    WHERE status_code < 400
    ORDER BY fecha
    """
).fetchdf()

# Leer la plantilla dentro de la carpeta de templates
template = Path("templates/report.md").read_text(encoding="utf8")

# Convertir los DataFrames en Markdown para exportar
report = template.format(
    query1=df1.to_markdown(index=False),
    query2=df2.to_markdown(index=False),
    query3=df3.to_markdown(index=False),
    query4=df4.to_markdown(index=False),
    query5=df5.to_markdown(index=False),
    query6=df6.to_markdown(index=False),
    query7=df7.to_markdown(index=False),
    
    recommendations="""
1. Hallazgo: /api/search presenta un p95 de 2.5 s durante las horas pico (14:00–16:00), concentrando además el mayor volumen de solicitudes.
Impacto potencial: Un aumento en la latencia sobre este endpoint puede degradar la experiencia de la mayoría de los usuarios y aumentar el consumo de recursos del backend.
Recomendación: Evaluar la incorporación de un mecanismo de caché para respuestas frecuentes y revisar el plan de ejecución de las consultas a la base de datos para reducir el tiempo de respuesta en las horas de mayor carga.

2. Prueba de recomendacion 2

3. Prueba de recomendacion 3
"""
)

# Guardar resultados en un reporte con formato markdown
Path("outputs/report.md").write_text(report, encoding="utf8")