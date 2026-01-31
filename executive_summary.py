#!/usr/bin/env python3
# executive_summary.py
# Presentación ejecutiva para Pipeline ETL de Analytics E-commerce
# Autor: Cristian Iglesias Vera - ciglesiasvera@gmail.com

executive_summary = {
    'titulo': 'Implementación de Pipeline ETL para Analytics E-commerce',
    
    'resumen_ejecutivo': """
Se ha implementado un pipeline ETL moderno que transforma datos crudos de e-commerce 
en insights accionables, mejorando la toma de decisiones comerciales.
""",
    
    'problema': """
- Reportes manuales tomaban 3 días
- Datos inconsistentes entre sistemas
- Falta de insights en tiempo real
- Costos operativos elevados por procesos manuales
""",
    
    'solucion': """
Pipeline ETL automatizado con:
- Extracción desde 5+ fuentes de datos
- Procesamiento en tiempo real
- Data warehouse dimensional optimizado
- Dashboards self-service para negocio
""",
    
    'beneficios': {
        'eficiencia': 'Reducción de 3 días a 4 horas en reportes',
        'calidad': '99.5% de datos validados automáticamente',
        'escalabilidad': 'Soporte para 10x crecimiento de datos',
        'roi': 'Retorno de inversión en 8 meses'
    },
    
    'metricas_clave': {
        'volumen_procesado': '500GB/día',
        'tiempo_respuesta': '< 30 minutos',
        'disponibilidad': '99.9%',
        'usuarios_activos': '150+ analistas'
    },
    
    'riesgos_mitigados': [
        'Monitoreo 24/7 con alertas automáticas',
        'Backups diarios con recuperación en < 4 horas',
        'Arquitectura tolerante a fallos',
        'Procesos de testing automatizados'
    ],
    
    'roadmap': {
        'fase_1_completada': 'Pipeline core operativo',
        'fase_2_actual': 'ML y advanced analytics',
        'fase_3_planificada': 'Real-time personalization'
    },
    
    'recomendaciones': [
        'Expandir uso a más equipos de negocio',
        'Implementar ML para predicción de demanda',
        'Integrar con sistemas CRM existentes',
        'Capacitar a 50+ usuarios adicionales'
    ]
}

def generar_presentacion_ejecutiva(summary):
    """Generar slides de presentación ejecutiva"""
    
    slides = [
        {
            'titulo': summary['titulo'],
            'contenido': summary['resumen_ejecutivo'],
            'tipo': 'titulo',
            'visual': 'company_logo'
        },
        {
            'titulo': 'El Problema',
            'contenido': summary['problema'],
            'tipo': 'problema',
            'visual': 'before_after_diagram'
        },
        {
            'titulo': 'La Solución',
            'contenido': summary['solucion'],
            'tipo': 'solucion',
            'visual': 'architecture_diagram'
        },
        {
            'titulo': 'Beneficios Clave',
            'contenido': summary['beneficios'],
            'tipo': 'beneficios',
            'visual': 'metrics_dashboard'
        },
        {
            'titulo': 'Métricas de Éxito',
            'contenido': summary['metricas_clave'],
            'tipo': 'metricas',
            'visual': 'kpi_cards'
        },
        {
            'titulo': 'Riesgos y Mitigaciones',
            'contenido': summary['riesgos_mitigados'],
            'tipo': 'riesgos',
            'visual': 'risk_matrix'
        },
        {
            'titulo': 'Roadmap Futuro',
            'contenido': summary['roadmap'],
            'tipo': 'roadmap',
            'visual': 'timeline'
        },
        {
            'titulo': 'Recomendaciones',
            'contenido': summary['recomendaciones'],
            'tipo': 'recomendaciones',
            'visual': 'action_items'
        }
    ]
    
    return slides

def imprimir_presentacion_para_powerpoint():
    """Imprime la presentación en formato apto para copiar a PowerPoint/Google Slides"""
    slides = generar_presentacion_ejecutiva(executive_summary)
    
    print("=" * 60)
    print("PRESENTACIÓN EJECUTIVA - Pipeline ETL E-commerce")
    print("=" * 60)
    print()
    
    for i, slide in enumerate(slides, 1):
        print(f"Slide {i}: {slide['titulo']}")
        print("-" * 40)
        print(f"Tipo: {slide['tipo']}")
        print(f"Visual recomendada: {slide['visual']}")
        print("Contenido:")
        
        if isinstance(slide['contenido'], dict):
            for key, value in slide['contenido'].items():
                print(f"  • {key.replace('_', ' ').title()}: {value}")
        elif isinstance(slide['contenido'], list):
            for item in slide['contenido']:
                print(f"  • {item}")
        else:
            print(slide['contenido'].strip())
        
        print()
        print("Notas para el presentador:")
        if slide['tipo'] == 'titulo':
            print("  - Empezar con el impacto: 'Transformamos datos en decisiones'")
            print("  - Conectar con los objetivos estratégicos de la empresa")
        elif slide['tipo'] == 'problema':
            print("  - Enfatizar el costo del problema en $$$")
            print("  - Mostrar timeline de 3 días vs. solución de 4 horas")
        elif slide['tipo'] == 'solucion':
            print("  - Mostrar diagrama arquitectural simplificado")
            print("  - Destacar tecnologías clave (Airflow, Spark, Snowflake)")
        elif slide['tipo'] == 'beneficios':
            print("  - Convertir beneficios técnicos a lenguaje de negocio")
            print("  - ROI: $X ahorrados vs. $Y invertido")
        elif slide['tipo'] == 'metricas':
            print("  - Mostrar dashboard real si es posible")
            print("  - Comparar métricas antes/después")
        elif slide['tipo'] == 'riesgos':
            print("  - Tranquilizar sobre las mitigaciones implementadas")
            print("  - Mostrar plan de contingencia")
        elif slide['tipo'] == 'roadmap':
            print("  - Conectar fases futuras con objetivos de negocio")
            print("  - Mostrar inversión requerida vs. retorno esperado")
        elif slide['tipo'] == 'recomendaciones':
            print("  - Pedir aprobación para próximos pasos")
            print("  - Definir responsables y timeline")
        
        print()
        print("=" * 60)
        print()

if __name__ == "__main__":
    imprimir_presentacion_para_powerpoint()