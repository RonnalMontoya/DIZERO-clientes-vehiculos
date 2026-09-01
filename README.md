# Sistema de Gestión para el Taller Mecánico Automotriz DIZERO

## Módulo seleccionado
**Gestión de Clientes y Vehículos**

Este repositorio contiene la estructura inicial del módulo **Gestión de Clientes y Vehículos** del Sistema de Gestión para el Taller Mecánico Automotriz DIZERO.

### Requerimientos del SRS atendidos
- **RF-01:** registrar clientes con sus datos principales.
- **RF-02:** registrar uno o varios vehículos asociados a un cliente.
- **RF-03:** validar que no se repitan la identificación del cliente ni la placa del vehículo.
- **RF-04:** consultar y actualizar la información de clientes y vehículos.

## Integrantes
- Ronnal Eulogio Montoya Zamora
- Anthony Sebastian Rubio Flores
- Dina Maria Tanguila Vargas

**Grupo:** 18  
**Asignatura:** Ingeniería de Software

## Stack tecnológico seleccionado
- **Lenguaje:** Python
- **Framework:** Django
- **Control de versiones:** Git + GitHub
- **Integración continua:** GitHub Actions

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

Se utilizará un flujo simple basado en **GitHub Flow**:

1. La rama **`main`** se mantiene estable e integrable.
2. Cada cambio se desarrolla en una rama independiente creada desde `main`.
3. Las ramas de funcionalidad usarán el prefijo **`feature/`**. Ejemplo: `feature/estructura-clientes-vehiculos`.
4. Los errores o correcciones podrán usar el prefijo **`fix/`**.
5. Cada cambio debe registrarse mediante commits con mensajes claros.
6. Antes de integrar una rama a `main`, se abrirá un **Pull Request**.
7. El Pull Request debe verificar que el flujo de CI finalice correctamente antes de fusionarse.
8. Una vez aprobado y fusionado el Pull Request, se eliminará la rama de trabajo si ya no es necesaria.

### Ejemplo de comandos para una rama de trabajo

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
