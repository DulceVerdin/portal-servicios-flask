# Ciclo técnico de una compra

Cuando el empleado, como *cliente* de la aplicación, escribe
`http://127.0.0.1:5000/compra` en el navegador, este utiliza la
**dirección IP** `127.0.0.1` para localizar el equipo y el *puerto* `5000`
para establecer la comunicación. El navegador prepara una solicitud
*HTTP*. Al abrir la página, envía una petición `GET` a la aplicación.

El *servidor* ejecuta el *backend*, desarrollado en *Python* con
*Flask*, y busca la *ruta* `/compra`. La ruta recibe la petición `GET` y
renderiza el *template* `compra.html`, que compone el *frontend*. El
*HTML* define los campos del formulario, mientras que **CSS** y
*Bootstrap* dan estilo y estructura a la página.  solo
interviene en componentes visuales de Bootstrap, como el menú adaptable, y no
participa en el cálculo.

El empleado ingresa la cantidad y el precio unitario y envía el formulario.
El navegador crea un *request* con método *POST* que contiene esos valores.
Flask recibe los datos en la misma ruta, valida que sean números válidos y no
negativos, y calcula el subtotal. Si el subtotal es mayor que $1000, aplica un
descuento del 10%; de lo contrario, el descuento es cero.

Con los resultados calculados, Flask renderiza de nuevo el template y prepara
una *response* HTTP con la página actualizada. El navegador interpreta el
HTML y muestra la cantidad, el precio unitario, el subtotal, el descuento y
el total al empleado.



```mermaid
flowchart LR
    A["Navegador"] -->|"HTTP POST: cantidad y precio"| B["Servidor Flask: ruta /compra"]
    B --> C["Validación y cálculo en Python"]
    C --> D["Renderizado de compra.html"]
    D -->|"HTTP response con resultado"| A
```

El navegador envía los datos mediante `POST`; Flask procesa el cálculo en el
servidor y devuelve la página renderizada con el resultado visible.



