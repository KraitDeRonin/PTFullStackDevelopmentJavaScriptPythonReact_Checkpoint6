# Checkpoint 6

## Teoría

### 1. ¿Para qué usamos Clases en Python?

Una Clase es un tipo de dato abstracto definido por el usuario que encapsula un estado (atributos) y un comportamiento (métodos). Una clase es la definición de un concepto o entidad, mientras que los elementos dentro de ella se denominan objetos o instancias.
En la Programación Orientada a Objetos , la clase actúa como la infraestructura que permite la abstracción, permitiendo al desarrollador modelar sistemas complejos de forma cercana a la realidad, traduciendo entidades del mundo real en componentes de software reutilizables.

|Traducción |
| ----- |
|Para crear algo, por ejemplo, un coche o un programa, primero se define ese algo, se hace un plano (blueprint) donde definir y detallar ese algo (un coche, un pulperro* o un programa). Ese plano es la clase y los elementos, funcionalidades, características (el tipo de motor del coche, el color, si es automático o manual, etc) son los atributos y métodos incluidos dentro del plano (clase).| 

Las clases se implementan para:

**Encapsular de Entidades**: Para agrupar datos y funciones relacionadas bajo una misma unidad lógica, se evita la dispersión de variables globales.

**Gestionar Instancias**: Permite que múltiples objetos compartan la misma estructura lógica pero mantengan estados (datos) independientes entre sí.

**Modularizar el Sistema**: Facilita la división del código en componentes desacoplados, lo que optimiza el mantenimiento y la escalabilidad de la aplicación.

Su adopción responde a la necesidad de crear software robusto y mantenible. Al utilizar clases:

**Reducir la complejidad**: La abstracción  permite centrarse en las acciones y propiedades relevantes de un objeto, ignorando detalles de implementación irrelevantes.

**Promover la reutilización**: Mediante técnicas como la composición, se construyen clases nuevas utilizando otras existentes como componentes (relación del tipo "tiene un"). Esto permite que el código fuente sea reciclable y modular.

**Facilitar el mantenimiento**: Cualquier modificación en la lógica de una entidad se centraliza en su definición de clase, impactando de forma coherente a todas sus instancias.

**Muestra de código**

```Python
class Coche:
    ruedas = 4

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.en_marcha = False

    def arrancar(self):
        self.en_marcha = True
        return f"El {self.marca} {self.modelo} ha arrancado."

    def pitar(self):
        return "¡Beep beep!"

mi_coche = Coche("Toyota", "Corolla", "Rojo")
tu_coche = Coche("Tesla", "Model 3", "Blanco")

print(mi_coche.arrancar())  # Resultado: El Toyota Corolla ha arrancado.
print(tu_coche.pitar())     # Resultado: ¡Beep beep!
```
***
### 2. ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

El método es ```__init__```. Al trabajar con Python, se le denomina habitualmente como el constructor, aunque  su función es la de un inicializador y podemos verlo nombrado de esa manera en algunos manuales.

Su rol es crítico porque define el estado inicial del objeto. Sin este método, habría objetos "vacíos" a los que  asignar valores uno a uno manualmente después de crearlos.

Al crear algo como ```mi_objeto = Clase(valor)```, Python realiza internamente dos pasos: reserva espacio en memoria para el objeto y, acto seguido, invoca a ```__init__``` con los argumentos que hayamos definido.

**El parámetro ```self```**: Es la pieza clave. Representa a la instancia específica que se está fabricando en ese momento. Al usar ```self.atributo = valor```, equivale a: "Guarda este dato precisamente en este objeto y no en otro".

Automatización: No es necesario llamar al método explícitamente (como se haría con un método normal). Su ejecución es parte del ciclo de vida natural de cualquier objeto en Python.

**Muestra de código**

```Python
class Usuario:
    def __init__(self, username, email):
        # Asigna los parámetros recibidos a los atributos de la instancia
        self.username = username
        self.email = email
        
# Al crear la instancia, el método __init__ se ejecuta solo:
nuevo_usuario = Usuario("coder_pro", "contacto@ejemplo.com")

print(f"Usuario {nuevo_usuario.username} creado con éxito.")
```
***
### 3. ¿Cuáles son los tres verbos fundamentales de una API?

En el estándar **REST** (**Representational State Transfer**), los verbos HTTP definen la acción que se desea realizar sobre un recurso en el servidor. Aunque el protocolo incluye diversos métodos, los tres pilares para construir la mayoría de las interacciones son ```GET```, ```POST``` y ```DELETE```, cada uno con una semántica específica que se debe respetar para asegurar la interoperabilidad y la predictibilidad del sistema.

Para garantizar la integridad de estos procesos, se aplica el principio de **Idempotencia** (o Resultado Único), el cual asegura que realizar una misma operación varias veces produzca el mismo efecto que una sola vez. Mientras que los métodos **```GET``` y ```DELETE``` son idempotentes**  para evitar duplicados o errores accidentales ante reintentos de red, el **método ```POST``` no lo es**, ya que su función es generar un nuevo recurso con cada ejecución.

**El método ```GET```: Recuperar información**

El verbo GET se utiliza para consultar o leer datos. Es importante que realizar una petición GET no modifique el estado, ni los datos existentes; es una operación de "solo lectura". 


|Ejemplo |
|-|
|Cuando una aplicación móvil solicita la lista de productos disponibles en una tienda, utiliza un GET. Como buena práctica, nunca se debe enviar información sensible (como contraseñas) a través de un GET, ya que los parámetros suelen viajar en la URL y quedan registrados en el historial del navegador o en los logs del servidor.| 

**Muestra de código**

```Python
import requests

# Consulta de los datos de un coche específico por su ID
response = requests.get('https://api.garaje.com/v1/coches/7')

if response.status_code == 200:
    datos_coche = response.json()
    # Se accede a los atributos que definidos en la clase Coche
    print(f"Coche recuperado: {datos_coche['marca']} {datos_coche['modelo']}")
```

**El método ```POST```: Crear recursos**

Se utiliza para enviar información al servidor con el fin de crear un nuevo recurso (como un registro de un Coche o un *pulperro*). Los datos se transmiten en el cuerpo de la petición y, tras una ejecución exitosa, el servidor suele responder con un código 201 Created. 

A diferencia de otros métodos, cada petición ```POST``` genera un nuevo elemento, por lo que no garantiza un resultado único si se repite.

|Ejemplo |
| ----- |
|El registro de un nuevo usuario: los datos se empaquetan en el cuerpo de la petición (body) y se envían al endpoint correspondiente. Como mejor práctica, tras una creación exitosa con POST, el servidor debería responder con un código de estado 201 Created, confirmando que el recurso ha sido generado correctamente.| 

**Muestra de código**

```Python
import requests

# Definir los datos del Pulperro
nuevo_pulperro = {
    "nombre": "Pulpito",
    "tentaculos": 8,
    "color_tentaculos": "Turquesa",
    "hambre": 10
}

# Petición para crear el recurso en la API
response = requests.post('https://api.mascotas.com/v1/pulperros', json=nuevo_pulperro)

if response.status_code == 201:
    print("El Pulperro ha sido registrado exitosamente en el servidor.")
```

**El método ```DELETE```: Eliminar recursos** 

El verbo ```DELETE``` se utiliza para dar de baja o destruir un recurso específico identificado por su URI. Al igual que ```GET```, es  un método *idempotente*, si intentamos borrar el mismo recurso varias veces, el resultado final en el servidor es el mismo (el recurso ya no existe), aunque el código de respuesta pueda variar entre un 204 No Content (éxito) o un 404 Not Found (si ya fue borrado). Una práctica fundamental en seguridad es restringir el acceso a este verbo mediante sistemas de autenticación y autorización robustos, para evitar que usuarios no autorizados eliminen información crítica.

**Muestra de código**

```Python
import requests

# ID del coche que deseamos eliminar
coche_id = 7
response = requests.delete(f'https://api.garaje.com/v1/coches/{coche_id}')

if response.status_code == 204:
    print("El registro del coche ha sido eliminado permanentemente.")
```
***
### 4. ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL (Not Only SQL). A diferencia de las bases de datos relacionales tradicionales (SQL) como MySQL o PostgreSQL, que organizan la información en tablas rígidas de filas y columnas, MongoDB es de tipo orientada a documentos. Esto significa que almacena la información en estructuras flexibles llamadas BSON (una variante binaria de JSON), lo que permite que cada registro pueda tener una estructura distinta sin necesidad de seguir un esquema predefinido y estricto.

**Diferencias fundamentales y ventajas**

La principal razón para utilizar una base de datos como MongoDB es su escalabilidad horizontal y su flexibilidad. Mientras que en una base de datos SQL, para añadir un nuevo atributo a "Coche" (por ejemplo, techo_solar: True), seria necesario  modificar la estructura de toda la tabla (un proceso llamado migration), en MongoDB simplemente guarda el nuevo documento con ese campo adicional. El motor de la base de datos lo aceptará sin quejas, lo que acelera enormemente el ciclo de desarrollo en entornos ágiles.

Además, MongoDB elimina la necesidad de realizar "JOINs" complejos (uniones de tablas) en muchas situaciones. Al permitir documentos embebidos, se puede guardar, por ejemplo, los datos de un Coche y su Motor dentro de un mismo registro. Esto mejora el rendimiento de lectura, ya que toda la información relacionada se recupera en una sola operación de entrada/salida (I/O), en lugar de tener que buscar en varias tablas dispersas.

**Ejemplo de estructura en MongoDB**

Si se traduce nuestro objeto ***Pulperro*** a un documento de MongoDB, se vería de una casi idéntica a un diccionario de Python:

```
ficha_cliente = {
  "_id": "507f1f77bcf86cd799439011",
  "nombre": "Pulpito",
  "color_tentaculos": "Turquesa",
  "hambre": 10,
  "habilidades": ["nadar", "ladrar", "camuflaje"],
  "propietario": {
    "nombre": "Sheldon Cooper",
    "ciudad": "Pasadena"
  }
}
```

***

### 5. ¿Qué es una API?

Una API (Application Programming Interface) representa el conjunto de definiciones y protocolos que permiten que dos aplicaciones de software se comuniquen entre sí de manera estandarizada. Funciona como una capa de abstracción indispensable: el sistema que solicita la información, al que llamamos **cliente**, no necesita comprender la complejidad interna, el lenguaje de programación o la base de datos que utiliza el **servidor**. Simplemente debe seguir las reglas establecidas en el **contrato** de la API para obtener un resultado previsible. Esta estructura permite que, por ejemplo, una aplicación escrita en Python pueda usar servicios de un servidor programado en Java o interactuar con una base de datos NoSQL como MongoDB sin problemas de compatibilidad.

La importancia de las APIs radica en su capacidad para fomentar el desacoplamiento y la seguridad. Al actuar como un intermediario, la API actúa como una aduana que valida cada solicitud antes de permitir que toque la lógica de negocio o los datos sensibles. Si un usuario intenta acceder a la información de un Coche específico, la API verifica primero sus permisos y la integridad de la petición. Además, facilitan la interconectividad, permitiendo que los desarrolladores integren funciones complejas, como pasarelas de pago o mapas, mediante llamadas a servicios de terceros, lo que ahorra tiempo y recursos al no tener que programar cada componente desde cero.

**Implementación de una API con Python (Flask)**

Para entender cómo se construye este **contrato** en el mundo real, podemos observar un ejemplo sencillo utilizando Flask (un micro-framework de Python diseñado para crear APIs de forma rápida). En el siguiente código, definimos cómo el servidor "escucha" las peticiones y responde ante ellas siguiendo la lógica de nuestras clases.
```Python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulamos una base de datos de nuestros objetos "Coche"
inventario_coches = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla"},
    {"id": 2, "marca": "Tesla", "modelo": "Model 3"}
]

# Definimos el punto de acceso (Endpoint) para consultar los coches
@app.route('/api/coches', methods=['GET'])
def obtener_coches():
    # El servidor responde con los datos en formato JSON
    return jsonify(inventario_coches), 200

# Definimos el punto de acceso para crear un nuevo coche
@app.route('/api/coches', methods=['POST'])
def crear_coche():
    nuevo_coche = request.json
    inventario_coches.append(nuevo_coche)
    return jsonify({"mensaje": "Coche registrado con éxito"}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
En este ejemplo, se han creado dos rutas que actúan como la interfaz de una aplicación. Cuando un cliente realiza una petición ```GET``` a ```/api/coches```, el servidor ejecuta la función asociada y devuelve la lista de vehículos. Si se utiliza un ```POST```, la API toma los datos del cuerpo de la petición (enviados como un diccionario de Python) y los añade al inventario. Este flujo de trabajo es el utilizado por casi cualquier aplicación web o móvil actual, para que la información fluya de manera ordenada y segura entre diferentes plataformas.

***
### 6. ¿Qué es Postman?

Postman es una herramienta de diagnóstico y experimentación para trabajar con servicios web. Postman es el entorno que nos permite probar, documentar y validar el contrato de una API entre dos sistema, comprobando que se esté cumpliendo correctamente sin necesidad de construir una interfaz de usuario completa o escribir código de cliente complejo para hacer una prueba.

Originalmente nació como una extensión de navegador, pero hoy en día es una plataforma que facilita todo el ciclo del desarrollo de una API. Su función principal es permitir enviar peticiones HTTP (como los verbos GET, POST o DELETE que hemos analizado) a un servidor y visualizar la respuesta detallada que este nos devuelve. Esto es fundamental durante la fase de desarrollo del código en Python; por ejemplo, al programar el sistema de registro de un Coche o un Pulperro, podemos usar Postman para enviar los datos y verificar si el servidor responde con un código *201 Created* o si, por el contrario, devuelve un error por falta de algún atributo obligatorio.

Una de las mayores ventajas de Postman es que permite inspeccionar no solo el cuerpo de la respuesta (el JSON o diccionario de datos), sino también las cabeceras (headers), las cookies y el tiempo de respuesta del servidor. Además, permite organizar estas pruebas en Colecciones, lo que facilita el trabajo en equipo y la automatización de flujos. En lugar de usar la terminal con comandos complejos como curl, Postman ofrece una interfaz gráfica donde guardar configuraciones, simular diferentes entornos (como "Desarrollo" o "Producción") y compartir la documentación técnica de forma instantánea.

**Ejemplo de uso práctico con Python**

Tras la puesta en marcha del servidor Flask definido en la sección anterior, se procede a validar el funcionamiento del método de creación de recursos. Para ello, Postman se configura siguiendo estos pasos:

1. Método: Selecciona ```POST``` en el desplegable.

2. URL: Introduce ```http://localhost:5000/api/coches.```

3. Body: En la pestaña "Body", selecciona "raw" y el formato "JSON", introduciendo los datos del objeto:

```
{
  "id": 3,
  "marca": "Ferrari",
  "modelo": "Testarossa"
}

```

4. Envío: Al pulsar "Send", Postman mostrará en el panel inferior si el coche se guardó correctamente, permitiendo depurar fallos en los atributos de la **Clase**.

***
### 7. ¿Qué es el polimorfismo?

El **polimorfismo** es uno de los cuatro pilares fundamentales de la Programación Orientada a Objetos (POO) y, posiblemente, uno de los más potentes para escribir código flexible. Su nombre proviene del griego y significa "muchas formas". En el contexto de Python, se refiere a la capacidad de diferentes objetos de responder a un mismo mensaje (o llamado a un método) de maneras distintas, permitiendo que una sola interfaz o función pueda operar con diversos tipos de datos.

El polimorfismo  permite tratar a objetos de diferentes clases de manera uniforme si comparten un comportamiento común. Su utilidad reside en que se pueden escribir funciones que acepten un "tipo genérico" de objeto y  que cada objeto ejecutará su propia versión de la acción solicitada. En lenguajes como Python, esto se lleva al extremo con el concepto de Duck Typing ("si camina como un pato y grazna como un pato, entonces es un pato"), donde lo que importa no es la clase exacta del objeto, sino que tenga implementados los métodos necesarios.

**Implementación práctica**

Usando planos originales del Coche y el Pulperro como ejemplos. Aunque son entidades completamente distintas, ambas podrían tener un método llamado ```desplazarse()```. El polimorfismo permite recorrer una lista que contenga ambos objetos y pedirles que se desplacen con indiferencia de si uno usa ruedas o tentáculos.

```Python
class Coche:
    def desplazarse(self):
        return "El coche avanza rodando por la carretera."

class Pulperro:
    def desplazarse(self):
        return "El pulperro avanza usando sus tentáculos."

# Función polimórfica: no le importa el tipo de objeto, solo que sepa 'desplazarse'
def realizar_movimiento(entidad):
    print(entidad.desplazarse())

# Creamos las instancias
mi_coche = Coche()
mi_mascota = Pulperro()

# Ambas funcionan con la misma función
realizar_movimiento(mi_coche)   # Resultado: El coche avanza rodando...
realizar_movimiento(mi_mascota) # Resultado: El pulperro avanza gateando...
```
***
### 8. ¿Qué es un método Dunder?

El término **Dunder** es una contracción de Double Underscore (doble guion bajo). Se refiere a un conjunto de métodos especiales predefinidos en Python que comienzan y terminan con ```__```, como por ejemplo ```__init__```, ```__str__``` o ```__add__```. Su propósito principal es permitir que nuestras propias clases se comporten como los tipos de datos integrados del lenguaje (como listas, diccionarios o números), facilitando lo que conocemos como sobrecarga de operadores y la emulación de comportamientos nativos.

**¿Por qué son tan importantes?**

En Python, casi todo lo que sucede "detrás de escena" está gestionado por un método dunder. Por ejemplo, cuando usas el símbolo ```+``` entre dos números, Python está llamando internamente al método ```__add__```. Cuando imprimes un objeto con ```print()```, Python busca el método ```__str__``` para saber qué texto debe mostrar. Al implementar estos métodos en nuestras clases, logramos que nuestros objetos sean mucho más intuitivos y fáciles de usar para otros desarrolladores, integrándose perfectamente con las funciones estándar del lenguaje.

**Ejemplo práctico**

Para imprimir una instancia de la clase ```Pulperro``` sin métodos **dunder**, Python devolvería algo poco legible como ```<__main__.Pulperro object at 0x7f... >```. Utilizando el método ´´´__str__´´´, se puede estructurar esa salida:

```Python
class Pulperro:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    # Método Dunder para representar el objeto como texto
    def __str__(self):
        return f"Pulperro(Nombre: {self.nombre}, Color: {self.color})"

    # Método Dunder para comparar si dos pulperros son iguales por nombre
    def __eq__(self, otro):
        return self.nombre == otro.nombre

# Uso de los métodos
mi_mascota = Pulperro("Pulpito", "Turquesa")
otra_mascota = Pulperro("Pulpito", "Rojo")

print(mi_mascota)          # Resultado: Pulperro(Nombre: Pulpito, Color: Turquesa)
print(mi_mascota == otra_mascota) # Resultado: True (porque tienen el mismo nombre)
```
En este ejemplo, al usar ```__str__``` el objeto es capaz de "describirse" a sí mismo, y gracias a ```__eq__```, podemos usar el operador ```==``` para comparar objetos de nuestra clase de forma lógica, en lugar de comparar simplemente su dirección en la memoria.
***

### 9 ¿Qué es un decorador de Python?

Un decorador es una función especial que permite modificar, extender o alterar el comportamiento de otra función o método sin tener que cambiar su código fuente de manera explícita. En Python, las funciones son objetos de "primera clase", lo que significa que pueden pasarse como argumentos a otras funciones. Un decorador aprovecha esta característica: recibe una función, le añade alguna funcionalidad extra (como un envoltorio o wrapper) y devuelve una nueva versión "mejorada" de la misma.

Visualmente, los decoradores se reconocen porque se aplican utilizando el símbolo ```@``` justo encima de la definición de una función. Esta sintaxis es lo que se conoce como "azúcar sintáctico", ya que hace que el código sea mucho más limpio y legible que si se hiciera la asignación de la función manualmente. Son herramientaspara aplicar lógica transversal en un proyecto, como la gestión de permisos, el registro de actividad (logging) o la medición del rendimiento.

**Ejemplo práctico**

Para saber cada vez que se ejecuta un método de una clase, sin llenar cada función con  ```print```. Es posible crear un decorador que "vigile" la ejecución:

```Python
def registro_de_actividad(funcion):
    def envoltura(*args, **kwargs):
        print(f"--- Ejecutando la acción: {funcion.__name__} ---")
        resultado = funcion(*args, **kwargs)
        print("--- Acción finalizada con éxito ---")
        return resultado
    return envoltura

class Pulperro:
    def __init__(self, nombre):
        self.nombre = nombre

    @registro_de_actividad
    def saludar(self):
        return f"¡Hola! Soy {self.nombre} y estoy burbujeando."

# Al llamar al método, el decorador se activa automáticamente
mi_mascota = Pulperro("Pulpito")
print(mi_mascota.saludar())
```
El decorador ```registro_de_actividad``` envuelve al método saludar. Cada vez que se llama a la mascota, el decorador imprime los mensajes de control antes y después de que el Pulperro realmente salude. Esto permite mantener la lógica del "saludo" limpia y separada de la lógica de "registro", facilitando el mantenimiento del código.
