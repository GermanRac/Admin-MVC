# Seccion Diseno de ingenieria 
## _Administración de Usuarios y Administrador en Django_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

En Django, la administración de usuarios se gestiona mediante su sistema de autenticación incorporado. El framework proporciona una interfaz fácil para crear, autenticar, autorizar y administrar usuarios. Además, Django cuenta con un panel de administrador prediseñado que facilita la gestión de los datos del sitio.

Para implementar la administración de usuarios y el panel de administrador en Django, se siguen estos pasos:
- **Definición del Modelo de Usuario:** Django proporciona un modelo de usuario predeterminado, pero se puede personalizar según las necesidades del proyecto.

- **Configuración de Autenticación:** Se configuran las vistas y plantillas de Django para el registro, inicio de sesión, recuperación de contraseñas y otras funcionalidades relacionadas con la autenticación de usuarios.

- **Personalización del Panel de Administrador:** Se pueden personalizar y agregar funcionalidades al panel de administrador de Django para gestionar los modelos de datos del sitio.
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
## _Validación Back-end de Funcionalidades_

> Es crucial validar las funcionalidades fundamentales del core 
> en el controlador en lugar de delegar toda la validación al front-end
>  a través de JavaScript. La validación back-end garantiza la integridad 
> y seguridad de los datos.

En Django, la validación back-end se realiza principalmente en las vistas o controladores. Algunas de las prácticas incluyen:

- **Validación de Datos de Formularios:** Se realizan validaciones en las vistas de Django para asegurar la corrección y coherencia de los datos ingresados por los usuarios.
- **Validación de Permisos y Autorizaciones:** Se controla el acceso a ciertas funcionalidades o datos mediante la validación de permisos dentro de las vistas o controladores.

La validación back-end garantiza que, independientemente de la capa front-end utilizada, las reglas y restricciones críticas del negocio se apliquen correctamente, mejorando la robustez y seguridad de la aplicación.
