# Pipeline ETL de Analytics E-commerce

## 🎯 Propósito del Negocio
Centraliza la data de ventas dispersa de múltiples fuentes de e-commerce para reducir el tiempo de generación de reportes de 3 días a 4 horas, mejorando la toma de decisiones comerciales con insights accionables en tiempo real.

## 🏗 Arquitectura de Alto Nivel
Diagrama conceptual para entendimiento rápido:

```
[Fuentes: API REST E-commerce] --> (Ingesta: Airflow) --> (Procesamiento: Spark) --> [DW: Snowflake]
       ↓
[PostgreSQL Transaccional] --> (Validación) --> (Limpieza) --> (Enriquecimiento) --> [S3 Data Lake]
```

## 🚀 Quick Start (Para impacientes)
Comandos exactos para levantar el entorno en menos de 5 minutos:

```bash
$ git clone https://github.com/ciglesiasvera/doc_pres_2.git
$ cd doc_pres_2
$ python -m venv dp_venv
$ source dp_venv/bin/activate
$ pip install -r requirements.txt
$ make setup
$ make run-local
```

## 🔧 Guía de Desarrollo
### Prerrequisitos
- Python 3.9+
- Docker y Docker Compose
- Airflow 2.5+
- Spark 3.3+

### Variables de Entorno
Copiar `.env.example` a `.env` y configurar las credenciales necesarias.

```bash
$ cp .env.example .env
$ nano .env
```

### Estructura del Proyecto
```
doc_pres_2/
├── dags/                    # DAGs de Airflow
├── src/                     # Código fuente Python
├── tests/                   # Pruebas unitarias
├── docs/                    # Documentación adicional
├── docker/                  # Configuración Docker
├── Makefile
├── requirements.txt
└── README.md
```

## ⚠️ Troubleshooting Común
- **Error: Connection refused to PostgreSQL**  
  Verificar que el servicio de PostgreSQL esté corriendo y las credenciales en `.env` sean correctas.

- **Error: Spark session not initialized**  
  Asegurar que las variables de entorno `SPARK_HOME` y `JAVA_HOME` estén configuradas.

- **Error: Airflow scheduler not picking up DAGs**  
  Revisar permisos de archivos en la carpeta `dags/` y reiniciar el scheduler.

---

# Documentación Técnica del Pipeline ETL

## Arquitectura del Pipeline ETL
### Visión General
El pipeline ETL procesa datos de e-commerce para generar insights de negocio, transformando datos crudos en información estructurada lista para análisis.

### Componentes Principales
#### 1. Extracción (Extract)
**Propósito**: Obtener datos desde múltiples fuentes externas.  
**Tecnologías**: SQLAlchemy, Requests, PyArrow.  
**Fuentes**:
- API REST de plataforma e-commerce
- Base de datos transaccional PostgreSQL
- Archivos CSV de proveedores externos

**Características**:
- Extracción incremental para eficiencia
- Reintentos automáticos en caso de fallos
- Validación básica de integridad

#### 2. Transformación (Transform)
**Propósito**: Limpiar, validar y enriquecer datos.  
**Operaciones**:
- Limpieza de valores faltantes y outliers
- Normalización de formatos
- Cálculo de métricas derivadas (total_venta, margen, etc.)
- Validación de reglas de negocio

#### 3. Carga (Load)
**Propósito**: Almacenar datos procesados para consumo.  
**Destinos**:
- Data Warehouse (PostgreSQL dimensional)
- Data Lake (S3 con particionado)
- Cache (Redis para dashboards)

### Flujo de Datos
```
API E-commerce → Validación → Limpieza → Enriquecimiento → DW
       ↓              ↓         ↓            ↓            ↓
PostgreSQL DB → Normalización → Reglas Neg. → Agregaciones → S3
```

### Decisiones Arquitectónicas
#### Escalabilidad
- **Horizontal**: Múltiples workers de Airflow
- **Vertical**: Recursos apropiados por componente
- **Auto-scaling**: Basado en carga de trabajo

#### Fiabilidad
- **Reintentos**: Configurados por tipo de error
- **Circuit breakers**: Para dependencias externas
- **Backups**: Diarios con retención de 30 días

#### Mantenibilidad
- **Modularidad**: Componentes independientes
- **Configuración externa**: Variables de entorno
- **Logging estructurado**: Para debugging

### Métricas de Éxito
#### Performance
- Latencia end-to-end: < 30 minutos
- Throughput: 1000 registros/segundo
- Disponibilidad: 99.9% uptime

#### Calidad
- Completitud: > 99.5% de datos válidos
- Exactitud: < 0.1% error rate
- Consistencia: Validaciones automáticas

## Runbook Operativo
### Inicio Diario
1. Verificar conectividad de fuentes
2. Validar espacio en disco (> 20% libre)
3. Check health de servicios críticos
4. Ejecutar pipeline manual si automático falla

### Monitoreo
- Dashboard Grafana con métricas en tiempo real
- Alertas PagerDuty para incidentes críticos
- Logs centralizados en ELK stack

### Recuperación de Desastres
- Backups diarios del DW
- Reprocesamiento histórico posible
- Failover automático entre regiones

---

## 👥 Autores
- **Cristian Iglesias Vera** - [ciglesiasvera](https://github.com/ciglesiasvera) - ciglesiasvera@gmail.com

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, lee `CONTRIBUTING.md` para detalles sobre el proceso de contribución.