

# PensionCalculatorPro

## Por:
Juliana Casas Ramírez
Natalia Florez Guzmán

## ¿Qué es?

La calculadora de pensiones es una herramienta digital que ayuda a las personas a estimar el monto de sus pensiones futuras. Utilizando información como la edad actual, el género, el salario actual, las semanas laboradas, el ahorro acumulado, la rentabilidad del fondo de pensiones y la tasa de administración del mismo, esta herramienta proporciona una proyección del ingreso que recibirán durante su jubilación.

## Propósito
El propósito de la calculadora de pensiones es permitir a los usuarios planificar su futuro financiero durante la jubilación. Al proporcionar una estimación del ingreso futuro, los individuos pueden tomar decisiones informadas sobre ahorros y contribuciones al fondo de pensiones, así como ajustar su planificación financiera para asegurar un retiro cómodo y sin preocupaciones.

## ¿Cómo lo haces funcionar?

### Prerequisitos

Antes de ejecutar este proyecto, asegúrate de tener instalado Python en tu sistema. Puedes descargarlo e instalarlo desde python.org.

### Ejecución:
Descarga el archivo del proyecto o clona el repositorio desde el cual obtuviste el código.

Abre una terminal o línea de comandos en tu sistema operativo.

Navega hasta el directorio donde se encuentra el código del proyecto.

Ejecuta el siguiente comando para iniciar la calculadora de pensiones python PensionCalculatorPro.py

## ¿Cómo está hecho?

El proyecto PensionCalculatorPro sigue una arquitectura simple y modular, con una separación clara entre la lógica del negocio, la interfaz de usuario y las pruebas unitarias. A continuación aquí está una descripción más detallada de la arquitectura, las bibliotecas utilizadas y las dependencias:

Arquitectura del Proyecto
El proyecto sigue una arquitectura de tres capas, con una estructura de carpetas organizada para separar claramente las diferentes partes del código:

Capa de Interfaz de Usuario (UI):

La carpeta Console contiene los archivos relacionados con la interfaz de consola del programa.
PensionCalculatorConsole.py implementa las funciones para interactuar con el usuario, mostrar menús y obtener datos de entrada.

Capa de Lógica de la calculadora:

La carpeta PensionCalculator alberga la lógica principal del programa.
PensionCalculator.py contiene la implementación de la lógica para calcular la pensión del usuario.

Capa de Pruebas Unitarias:

La carpeta test contiene los archivos de pruebas unitarias para validar el funcionamiento correcto del programa.
PensionCalculatorTests.py proporciona las pruebas para verificar la funcionalidad de las funciones en PensionCalculator.py.

Bibliotecas Utilizadas:
El proyecto hace uso de las siguientes bibliotecas estándar de Python:

unittest: Utilizada para escribir y ejecutar pruebas unitarias.

Dependencias de Otros Proyectos:
El proyecto no tiene dependencias externas a otros proyectos. Todas las funcionalidades están implementadas dentro del propio proyecto sin requerir bibliotecas externas.

Esquema de la modularidad:

PensionCalculatorPro/
│
├── src/
│   ├── Console/
│   │   └── PensionCalculatorConsole.py
│   │
│   └── PensionCalculator/
│       └── PensionCalculator.py
│
├── test/
│   └── PensionCalculatorTests.py
│
└── main.py




#
