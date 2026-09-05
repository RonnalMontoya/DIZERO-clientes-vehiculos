# Sistema de Gestión para el Taller Mecánico Automotriz DIZERO

## Descripción
Este repositorio corresponde al módulo **Gestión de Clientes y Vehículos** del Sistema de Gestión para el Taller Mecánico Automotriz **DIZERO**, desarrollado como parte de la asignatura Ingeniería de Software.

El sistema busca digitalizar y organizar los procesos del taller, reduciendo problemas relacionados con registros manuales, duplicación de información, pérdida de datos y dificultad para consultar información de clientes y vehículos.

## Módulo seleccionado
**Gestión de Clientes y Vehículos**
El módulo permite registrar, consultar y actualizar la información de clientes y de los vehículos asociados a cada uno de ellos.

## Requerimientos del SRS atendidos
- **RF-01:** registrar clientes con sus datos principales.
- **RF-02:** registrar uno o varios vehículos asociados a un cliente.
- **RF-03:** validar que no se repitan la identificación del cliente ni la placa del vehículo.
- **RF-04:** consultar y actualizar la información de clientes y vehículos.

## Integrantes
- Ronnal Eulogio Montoya Zamora - Líder de análisis – “feature/estructura-clientes-vehiculos” 
- Anthony Sebastián Rubio Flores - Analista de procesos – “feature/anthony-procesos”
- Dina Maria Tanguila Vargas - Documentador ágil – “feature/dina-documentacion”

**Grupo:** 18  
**Asignatura:** Ingeniería de Software

## Tecnologías utilizadas
- **Lenguaje:** Python
- **Framework:** Django
- **Control de versiones:** Git
- **Repositorio remoto:** GitHub
- **Integración Continua:** GitHub Actions
- **Arquitectura:** Tres capas

La selección de **Python + Django** corresponde a la decisión tecnológica definida para este módulo en la matriz del proyecto.

## Estructura inicial del repositorio

```text
DIZERO_Git_CI/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── clientes_vehiculos/
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── models.py
│   ├── dizero/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Flujo de ramas: GitHub Flow
El proyecto utiliza un flujo de trabajo basado en “GitHub Flow”.

**`main`** se mantiene como la versión estable e integrada del proyecto.

Cada integrante trabaja en una rama independiente:
• feature/estructura-clientes-vehiculos: estructura inicial del módulo y configuración del CI. 
• feature/dina-documentacion: actualización y mantenimiento de la documentación. 
• feature/anthony-procesos: análisis y documentación de los procesos del módulo. 

1. La rama **`main`** se mantiene estable e integrable.
2. Cada cambio se desarrolla en una rama independiente creada desde `main`.
3. Los errores o correcciones podrán usar el prefijo **`fix/`**.
4. Cada cambio debe registrarse mediante commits con mensajes claros.
5. La rama se publica en GitHub mediante push. 
6. Antes de integrar una rama a `main`, se abrirá un **Pull Request**.
7. El Pull Request debe verificar que el flujo de CI finalice correctamente antes de fusionarse.
8. Una vez aprobado y fusionado el Pull Request, se eliminará la rama de trabajo si ya no es necesaria.

## Ejemplos de mensajes de commit:
feat: agregar estructura inicial del modulo
docs: actualizar documentacion del proyecto
fix: corregir validacion de datos

## Integración Continua
- GitHub Actions ejecuta automáticamente el proceso de Integración Continua mediante el archivo: .github/workflows/ci.yml
- El pipeline se ejecuta automáticamente ante eventos de push y pull_request. 

La validación principal se realiza mediante: python src/manage.py check

## Ejemplo de comandos para una rama de trabajo

```bash
git checkout main
git pull origin main
git checkout -b feature/estructura-clientes-vehiculos

# realizar un cambio y luego:
git add .
git commit -m "feat: agregar estructura inicial de clientes y vehiculos"
git push -u origin feature/estructura-clientes-vehiculos
```

Después del `push`, se debe abrir un **Pull Request** en GitHub desde `feature/estructura-clientes-vehiculos` hacia `main`.

## CI básico con GitHub Actions

El archivo `.github/workflows/ci.yml` define una validación automática que se ejecuta en cada `push` y en los Pull Request dirigidos a `main`.







