# Guía de Usuario: Analytics E-commerce

## ¿Qué es este sistema?
Una plataforma self-service que te permite acceder a datos actualizados de ventas, clientes y productos sin depender de IT. Transforma datos crudos de múltiples fuentes en insights visuales y reportes accionables.

## Primeros Pasos
### Acceso al Sistema
1. **URL del Dashboard**: https://analytics.empresa.com
2. **Credenciales**: Usa tu correo corporativo y contraseña de dominio
3. **Soporte**: Para problemas de acceso, contacta a it-support@empresa.com

### Configuración Inicial
- **Perfil de Usuario**: Completa tu perfil con departamento y rol
- **Preferencias**: Configura zona horaria y moneda local
- **Favoritos**: Marca los dashboards más relevantes para tu rol

## Cómo usar los dashboards

### Dashboard Ejecutivo (Resumen diario)
**Propósito**: Visión general del rendimiento del negocio

- **Métrica principal**: Ventas totales del día
- **Filtros disponibles**: 
  - Por región (Norte, Sur, Centro, Internacional)
  - Por categoría de producto
  - Por canal de venta (Online, Tienda física)
- **Frescura de datos**: Actualizado cada 15 minutos
- **Uso recomendado**: Revisión matutina de performance

**Cómo interpretar**:
- Gráfico de líneas: Tendencia de ventas últimos 30 días
- Tarjetas KPI: Comparativa día anterior vs. mismo día semana pasada
- Tabla de productos top 10: Identifica best-sellers

### Dashboard de Productos
**Propósito**: Analizar rendimiento por SKU y categoría

- **Vista**: Rendimiento por SKU
- **Métricas clave**:
  - Unidades vendidas
  - Margen bruto
  - Rotación de inventario
  - Tasa de conversión
- **Drill-down**:
  - Por tienda específica
  - Por período de tiempo (día, semana, mes)
  - Por segmento de cliente
- **Alertas configurables**:
  - Productos con bajo rendimiento (< 10 unidades/día)
  - Stock bajo (< 20 unidades)
  - Margen negativo

### Dashboard de Clientes
**Propósito**: Segmentación y análisis de comportamiento de clientes

- **Segmentación**:
  - VIP (Top 5% en gasto)
  - Regular (25-75% percentil)
  - Nuevo (primer compra < 30 días)
  - Inactivo (sin compras > 90 días)
- **Métricas**:
  - LTV (Lifetime Value)
  - Frecuencia de compra
  - Churn rate (tasa de abandono)
  - Ticket promedio
- **Análisis avanzado**:
  - Comportamiento por cohorte (mes de primera compra)
  - Heatmap de horas de compra
  - Recomendaciones de cross-selling

## Preguntas comunes

### **¿Con qué frecuencia se actualizan los datos?**
- **Datos transaccionales**: Cada 15 minutos
- **Agregados diarios**: 6:00 AM (hora local)
- **Reportes mensuales**: Primer día del mes a las 8:00 AM
- **Datos históricos**: Reprocesamiento nocturno

### **¿Qué hago si veo datos extraños o inconsistentes?**
Sigue este proceso de troubleshooting:

1. **Verificar fecha del último update**
   - Chequea el timestamp en la esquina superior derecha
   - Si muestra "Hace más de 1 hora", puede haber un problema

2. **Comparar con períodos anteriores**
   - Usa el filtro de fecha para comparar con semana pasada
   - Verifica si el patrón es consistente

3. **Reportar el problema**
   - Envía email a data@empresa.com
   - Incluye screenshots con:
     - URL completa del dashboard
     - Filtros aplicados
     - Lo que esperabas vs. lo que ves
     - Hora de la consulta

### **¿Puedo crear mis propios reportes personalizados?**
Sí, usando la herramienta de ad-hoc queries:

1. **Acceso**: Contacta a tu administrador para permisos
2. **Interfaz**: Editor SQL con autocompletado
3. **Limitaciones**: 
   - Consultas limitadas a 10 minutos
   - Resultados máximos: 10,000 filas
   - Solo datos históricos (no tiempo real)

### **¿Cómo exporto datos para Excel?**
- **Dashboards**: Botón "Exportar" en esquina superior derecha
- **Formatos disponibles**: CSV, Excel, PDF
- **Límites**: Hasta 50,000 filas por exportación

## Mejores Prácticas

### Para Equipos Comerciales
1. **Reunión diaria**: Revisa dashboard ejecutivo a las 9:00 AM
2. **Alertas proactivas**: Configura notificaciones para caídas >10% en ventas
3. **Análisis de productos**: Semanalmente revisa dashboard de productos
4. **Segmentación**: Mensualmente analiza comportamiento de clientes

### Para Gerentes
1. **KPIs personalizados**: Define 3-5 métricas clave para tu área
2. **Reportes automáticos**: Programa envío semanal a tu email
3. **Comparativas**: Usa benchmarking entre regiones/equipos
4. **Planning**: Usa datos históricos para proyecciones

### Para Analistas
1. **Exploración**: Usa ad-hoc queries para hipótesis
2. **Validación**: Cross-check con fuentes originales
3. **Documentación**: Anota hallazgos en la wiki interna
4. **Colaboración**: Comparte dashboards con colegas

## Contactos de soporte

### Por tipo de problema:
- **Problemas técnicos** (login, error 500, página no carga):
  - Email: it-support@empresa.com
  - Teléfono: +56 2 1234 5678 (opción 1)
  - Horario: L-V 8:00-20:00

- **Preguntas de negocio** (interpretación de datos, métricas):
  - Email: data-team@empresa.com
  - Teléfono: +56 2 1234 5678 (opción 2)
  - Reuniones: Agendar via calendario

- **Solicitudes nuevas** (nuevos dashboards, métricas, fuentes):
  - Email: product-analytics@empresa.com
  - Formulario: https://forms.empresa.com/nueva-solicitud
  - Tiempo respuesta: 3-5 días hábiles

- **Capacitación** (training, workshops):
  - Email: training@empresa.com
  - Calendario: Sesiones quincenales
  - Material: https://wiki.empresa.com/analytics-training

## Glosario de Términos

- **ETL**: Extract, Transform, Load - proceso de mover datos
- **KPI**: Key Performance Indicator - métrica clave
- **LTV**: Lifetime Value - valor de vida del cliente
- **Churn Rate**: Tasa de abandono de clientes
- **ROI**: Return on Investment - retorno de inversión
- **Data Warehouse**: Almacén centralizado de datos
- **Dashboard**: Panel visual de métricas
- **Drill-down**: Navegar de resumen a detalle

## Recursos Adicionales

- **Video tutoriales**: https://youtube.empresa.com/analytics
- **Documentación técnica**: https://docs.empresa.com/data-platform
- **Comunidad interna**: Slack #analytics-ecommerce
- **Roadmap producto**: https://trello.empresa.com/analytics-roadmap

---

*Última actualización: Enero 2026*  
*Para sugerencias de mejora: feedback-analytics@empresa.com*