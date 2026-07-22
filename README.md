# SQL Server Log Analysis 📊

Herramienta para el análisis integral de logs de acceso a servidores web utilizando SQL y DuckDB, generando reportes detallados en Markdown.

---

## 📋 Tabla de Contenidos

- [Objetivo del Proyecto](#objetivo-del-proyecto)
- [Características](#características)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Requisitos Previos](#requisitos-previos)
- [Instalación de Dependencias](#instalación-de-dependencias)
- [Uso](#uso)
- [Análisis Incluidos](#análisis-incluidos)

---

## 🎯 Objetivo del Proyecto

Este proyecto proporciona un sistema automatizado para analizar logs de acceso HTTP de aplicaciones web, identificando:

- **Patrones de tráfico**: Distribución de solicitudes por endpoint
- **Rendimiento de endpoints**: Análisis de percentiles (p90, p95) de tiempo de respuesta
- **Errores y fallos**: Identificación de status codes de error (4xx, 5xx) y usuarios afectados
- **Tendencias horarias**: Picos de tráfico y carga por hora del día
- **Comparativas temporales**: Análisis de evolución del rendimiento entre períodos

El resultado es un reporte completo con visualización en tablas para facilitar la toma de decisiones sobre optimización y escalabilidad de la infraestructura.

---

## ✨ Características

✅ Lectura directa de archivos JSON con DuckDB  
✅ Consultas SQL optimizadas para análisis rápidos  
✅ Generación automática de reportes en Markdown  
✅ Múltiples perspectivas analíticas

---

## 📁 Estructura del Repositorio

```
sql-server-log-analysis/
├── analysis_01.py                 # Script principal de análisis
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Este archivo
│
├── logs/                          # Carpeta de datos de entrada
│   ├── access_logs.json          # Logs de acceso HTTP (principal)
│
├── templates/                     # Plantillas de reportes
│   └── report.md                 # Plantilla Markdown para el reporte
│
└── outputs/                       # Carpeta de salida
    └── report.md                 # Reporte generado
```

### Descripción de Carpetas

| Carpeta | Contenido |
|---------|-----------|
| **logs/** | Archivos JSON con datos sin procesar. El archivo principal es `access_logs.json` que contiene registros HTTP con timestamp, endpoint, status_code, response_time_ms, etc. |
| **templates/** | Plantilla Markdown (`report.md`) que actúa como esqueleto para generar los reportes. Los placeholders `{query1}` a `{query7}` se reemplazan con los resultados del análisis. |
| **outputs/** | Directorio de salida donde se guarda el reporte final (`report.md`) con todos los análisis ejecutados. |

---

## 🔧 Requisitos Previos

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)

---

## 📦 Instalación de Dependencias

### Opción 1: Instalación Global en el Sistema

```bash
pip install -r requirements.txt
```

### Opción 2: Usando Entorno Virtual (Recomendado)

#### En Linux/macOS:
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

#### En Windows (PowerShell):
```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```
---

## ▶️ Uso

### Ejecutar el Análisis

```bash
python analysis_01.py
```

### Flujo de Ejecución

1. **Cargar datos**: Conecta a DuckDB y carga `logs/access_logs.json` en una tabla SQL
2. **Verificar estructura**: Muestra el total de filas, columnas y tipos de datos
3. **Ejecutar 7 análisis**:
   - Exploración inicial (período, cantidad de registros, usuarios únicos)
   - Endpoints más usados
   - Análisis de errores (status code >= 400)
   - Performance de requests exitosos (percentiles p90, p95)
   - Tendencias horarias
   - Top 3 requests más lentos por endpoint
   - Comparación con período anterior

4. **Generar reporte**: Combina resultados con la plantilla y genera `outputs/report.md`

---

## 💡 Casos de Uso

- **Identificar cuellos de botella**: Encuentra los endpoints con peor rendimiento
- **Planificación de capacidad**: Analiza picos de tráfico para escalar infraestructura
- **Debugging de errores**: Identifica endpoints con más fallos y usuarios afectados
- **Monitoreo de SLA**: Verifica cumplimiento de tiempos de respuesta
- **Análisis de tendencias**: Detecta cambios en el rendimiento a lo largo del tiempo

---

## ⚠️ Notas Importantes

- El script utiliza una conexión **in-memory** de DuckDB. Para volúmenes muy grandes de datos, considera usar una base de datos persistente modificando la línea: `con = duckdb.connect('my_database.db')`
- Los archivos JSON deben estar en la carpeta `logs/` con el nombre exacto `access_logs.json`
- El reporte se sobrescribe cada vez que se ejecuta el script
- Se requiere que los datos tengan un formato JSON válido

---

## 🚀 Próximos Pasos

- Exportar reportes a HTML con gráficos visuales
- Integración con dashboards de BI (Power BI, Tableau)
- Alertas automáticas basadas en umbrales
- Análisis de sesiones y comportamiento de usuarios
- Comparativas entre períodos más complejas

---

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT.
