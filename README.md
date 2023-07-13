Este proyecto esta basado en una pastelería
En la página principal del proyecto hay un título y una presentación de la pasteleria.

Principalmente se registran clientes, indicando nombre, apellido, nacimiento, ciudad (precargada), y domicilio.

Una vez registrados los clientes, se pueden registrar productos, para lo cual se debe indicar el nombre del producto, una descripción y el precio.

Cuando ya tenemos al menos un cliente y un producto, se puede realizar un pedido.
Para registrar el pedido únicamente se selecciona el producto a comprar y el cliente que realiza la compra.

Una vez que se encuentran realizados los registros, se puede acceder al listado de los mismos desde los accesos del navegador principal "CLIENTES" "PRODUCTOS" "PEDIDOS"
Y desde cada uno de ellos se puede ingresar a realizar una nueva carga.

Explicación de código realizado:

Se realizaron 4 aplicaciones.
---> MENU: para generar y manejar todas las vistas. De aquí se heredan las plantillas y estilos en las otras aplicaciones. Contiene 4 templates.
---> cliente: contiene clases Cliente y Ciudad. Las ciudades se encuentran pre-cargadas.Contiene un formulario para la carga de los clientes. Contiene 2 templates.
---> producto: contiene modelo Producto. Contiene un formulario para la carga de los productos. Contiene 2 templates.
---> venta: contiene modelo Vender. Contiene un formulario para la carga de las ventas realizadas. Contiene 2 templates.
