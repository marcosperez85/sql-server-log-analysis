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

print("\nPeríodo cubierto y duración total:")
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