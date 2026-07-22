import duckdb
import pandas as pd


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
# ¿Cuántos registros? ¿Qué período cubren? ¿cuántos usuarios únicos hay?

print("\n\nPeríodo cubierto y duración total:")
print(con.execute(
    """WITH cte AS (
        SELECT
            MIN(timestamp) as fecha_inicial,
            MAX(timestamp) as fecha_final,
            COUNT(*) as cantidad_filas,
            COUNT(DISTINCT client_ip) as ip_unicas,
            COUNT(DISTINCT user_id) as id_unicos,
        FROM access_logs)
    SELECT
        fecha_inicial as FECHA_INICIAL,
        fecha_final as FECHA_FINAL,
        (fecha_final - fecha_inicial) as DURACION,
        cantidad_filas as CANTIDAD_FILAS,
        ip_unicas as CANT_IP_UNICAS,
        id_unicos as CANT_ID_UNICOS
    FROM cte"""
).fetchdf())

# ========================================
# ENDPOINTS MÁS USADOS
# ========================================
# Indicar cuánto es el porcentaje de uso de cada endpoint

print("\n\nLos endpoints más usados son:")
print(con.execute(
    """SELECT
            endpoint as ENDPOINT,
            COUNT(*) as CANT_PETICIONES,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM access_logs), 2) as PORCENTAJE           
        FROM access_logs
        GROUP BY endpoint
        ORDER BY CANT_PETICIONES DESC        
    """
).fetchdf())

# ========================================
# ANALISIS DE ERRORES
# ========================================
# Indicar cuántos usuarios se ven afectados con requests fallidos y la ocurrencia de cada uno

print("\n\nErrores por cada endpoint:")
print(con.execute(
    """
    SELECT
        endpoint as ENDPOINT,
        COUNT(*) as ERRORES_TOTALES,
        COUNT(DISTINCT user_id) as USUARIOS_AFECTADOS,
        ROUND(AVG(response_time_ms),2) as RESPONSE_TIME_PROMEDIO,
        status_code as STATUS_CODE
    FROM access_logs
    WHERE status_code >= 400
    GROUP BY endpoint, status_code
    ORDER BY ERRORES_TOTALES DESC
    """
).fetchdf())

# ========================================
# PERFORMANCE POR ENDPOINT
# ========================================
# Indicar cuánto tarda el 90 y 95% de los requests exitosos

print("\n\nPerformance por cada endpoint:")
print(con.execute(
    """
    SELECT
        endpoint as ENDPOINT,
        COUNT(*) as CANT_REQUESTS,
        PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY response_time_ms) as p90_RANK,
        PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY response_time_ms) as p95_RANK,
        MAX(response_time_ms) as TIEMPO_MAXIMO  
    FROM access_logs
    WHERE status_code < 400 -- Filtro requests exitosos
    GROUP BY endpoint
    ORDER BY p95_RANK DESC
    """
).fetchdf())

# ========================================
# TENDENCIA HORARIA
# ========================================
# Identificar picos de tráfico según la hora para planificar capacidad y poder escalar a futuro.
# Para esto busco la hora a la cual se da la mayor cantidad de requests y el mayor tiempo de respuesta para cada endpoint

print("\n\nLos picos de tráfico según la hora son:")
print(con.execute(
    """
    SELECT
        EXTRACT(HOUR FROM timestamp) AS HORA,
        endpoint as ENDPOINT,
        COUNT(*) AS CANT_REQUESTS,
        ROUND(AVG(response_time_ms),2) AS RESPONSE_TIME_AVG
    FROM access_logs
    GROUP BY HORA, ENDPOINT
    ORDER BY CANT_REQUESTS DESC;
    """
).fetchdf())

# ========================================
# RANKING DE REQUESTS (EXITOSOS) MÁS LENTOS
# ========================================

print("\n\nEl ranking de los endpoints es:")
print(con.execute(
    """
    WITH ranking AS (
        SELECT
            timestamp as TIMESTAMP,
            endpoint as ENDPOINT,
            response_time_ms as RESPONSE_TIME,
            user_id as USER_ID,
            ROW_NUMBER() OVER(PARTITION BY endpoint ORDER BY response_time_ms DESC) as RN
        FROM access_logs
        WHERE status_code < 400    
    )
    SELECT * FROM ranking
    WHERE RN <= 3
    ORDER BY endpoint, RN DESC
    """
).fetchdf())

# ========================================
# COMPARACION CON EL PERÍODO ANTERIOR
# ========================================

print("\n\nComparación del response time de cada endpoint con la fecha anterior registrada:")
print(con.execute(
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
        response_time_ms as RESPONSE_TIME_ACTUAL,
        response_prev as PERIODO_ANTERIOR,
        response_time_ms - response_prev as DIFFERENCE
    FROM calculo
    WHERE status_code < 400
    ORDER BY fecha
    """
).fetchdf())

