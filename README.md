# OUTPY
OUTPY es un script que ayuda a la venta progresiva de criptoactivos. Conectado a la API de CoinMarketCap, actualiza los precios de criptomonedas y los guarda en un archivo JSON. Sirve para gestionar y rastrear activos en tiempo real.

# Script OUTPY para la Venta Progresiva de Criptoactivos (DCA_OUT.py)

## Introducción

El script OUTPY (dcaout.py), diseñado para el apoyo en la venta progresiva de criptoactivos mediante dollar cost average, simplifica y automatiza el proceso de venta basado en la fluctuación del precio. Utiliza datos de precios en tiempo real obtenidos de CoinMarketCap para determinar cuándo vender activos, basándose en un umbral predefinido. He creado una versión MVP, pensada para ejecutarse manualmente cada que uno desea hacer una venta. En versiones posteriores, podría implementarse funcionalidades de automatización como recordatorios, y alertas detonadas por movimientos en el precio de los activos. También, por qué no?, integración con exchanges para hacer la venta directamente en nuestra wallet.
Este documento proporciona un análisis detallado de las funcionalidades hasta el momento, el valor y el uso del script.

## Funcionalidades

### 1. **Carga y Actualización de Activos**

- **`load_assets()`**: Carga los activos desde un archivo JSON (`assets.json`), que contiene la información de los criptoactivos, incluyendo su símbolo, cantidad y precio actual.
- **`write_to_assets()`**: Actualiza el archivo JSON con la información más reciente sobre los activos después de cada operación.

### 2. **Obtención de Datos de Precios**

- **`fetch_data()`**: Actualiza los precios de los activos en el archivo JSON llamando a la función `fetch_cryptocurrency_data()` para obtener el precio actual de cada activo.
- **`fetch_cryptocurrency_data(asset)`**: Utiliza la API de CoinMarketCap para obtener el precio actual del activo en USD.

### 3. **Operaciones en la Interfaz de Usuario**

- **`print_header()`**: Muestra un resumen de los activos, su cantidad, precio actual y valor total.
- **`show_salelog()`**: Muestra el historial de ventas almacenado en `salelog.txt`.

### 4. **Validación y Registro de Ventas**

- **`validate_asset(key)`**: Verifica si un activo existe en la lista de activos cargada.
- **`set_salelog(asset, percent, price, quantity_sold)`**: Registra la transacción de venta en `salelog.txt` con detalles de la venta como el porcentaje vendido, el precio y la cantidad.
- **`sell_asset(asset)`**: Calcula la cantidad a vender basada en el precio del activo y el umbral de venta definido. Actualiza la cantidad del activo y escribe en el registro de ventas.

### 5. **Interfaz de Usuario**

- **`main_gui()`**: Proporciona un bucle interactivo que permite al usuario vender activos, ver el registro de ventas o salir del script.

## Manual de Uso

### Requisitos Previos

1. **Archivo de Activos (`assets.json`)**: Debe contener la información de los activos con el siguiente formato:
    ```json
    {
        "BTC": {"symbol": "BTC", "quantity": 1.0, "price": 0},
        "ETH": {"symbol": "ETH", "quantity": 5.0, "price": 0}
    }
    ```
    Al correr el script con simbolos válidos, el precio se actualiza imediatamente en el fichero json. La cantidad en posesión debe ingresarse manualmente para cada activo, pensando a futuro integrar apis de exchanges o wallets para manejar las tenencias de criptoactivos con mayor precisíón.
   
3. **API de CoinMarketCap**: Se necesita una clave API válida. Sustituir `"YOUR FREE COINMARKETCAP API KEY"` con tu clave en el script.

### Ejecución del Script

1. **Ejecuta el script**: Ejecuta el archivo Python principal que contiene el código del script.
    ```bash
    python out.py
    ```
2. **Interacción**: 
    - **Para vender un activo**: Ingresa el símbolo del activo (e.g., `BTC`). Deve estar previamente agregado en el fichero assets.json con un simbolo vádido de coinmarketcap
    - **Para ver el registro de ventas**: Escribe `salelog`.
    - **Para salir**: Escribe `exit`.

### Ejemplo de Uso

1. **Venta de Activo**:
    - El usuario ingresa `BTC` y, si el precio de BTC es mayor que el umbral definifo en el codigo fuente (out.py) como GOLDEN_TARJET (en USD), el script calculará la cantidad a vender basada en el porcentaje de diferencia de precio y actualizará los archivos correspondientes.
    - El porcentaje de venta sugerido debe editarse con base a criterios personales. En mi caso, deseo vender 5% cada vez que ARKM esté en 3USD, y aumente en 5% a partir de ahí. La formula se puede editar en el codigo fuente de out.py
     ```python
    # sell_asset
    def sell_asset(asset):
      price = assets[asset]["price"]
      quantity = assets[asset]["quantity"]

      percent = (price - 2) * 5
    ``` 

2. **Visualización del Registro**:
    - El usuario ingresa `salelog` para ver el historial de ventas, que muestra las transacciones registradas con la fecha, activo, porcentaje vendido, cantidad y precio.

## Valor del Script

- **Automatización**: Automatiza la actualización de precios y la venta de activos, reduciendo el esfuerzo manual requerido para gestionar las transacciones.
- **Registro Detallado**: Mantiene un historial detallado de las ventas para una fácil revisión y seguimiento.
- **Interfaz Simple**: Ofrece una interfaz de usuario basada en texto que es fácil de entender y utilizar.
- **Adaptabilidad**: Se puede ajustar el umbral de venta y otros parámetros según las necesidades del usuario.

## Documentación Adicional

- **API CoinMarketCap**: Documentación de la API y cómo obtener una clave [aquí](https://coinmarketcap.com/api/).
- **Formato del Archivo JSON**: Asegúrate de que el archivo `assets.json` esté correctamente formateado y actualizado para evitar errores en la ejecución.

Este script proporciona una solución eficiente y automatizada para la venta de criptoactivos, facilitando la gestión y optimización de portafolios de inversión en criptomonedas, creado para mi uso personal con animos de compartirlo para aquellos que gusten aportar mejoras o utilizarlo a su conveniencia.
