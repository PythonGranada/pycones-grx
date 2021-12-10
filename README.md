# Web PyconES 2022


### Creador de contenidos o editor

Aquí no necesitas tener grandes conocimientos técnicos, solo necesitamos creatividad.
Todos los contenidos se escriben usando [Markdown](https://markdown.es/) y no tienes que pelearte con HTML ni CSS, solo darle rienda suelta a tu imaginación.

### Web developer

Si tienes conocimientos de maquetación web y un poco de gusto estético, puedes ayudar a mejorar aspectos de diseño o usabilidad de la web.
En principio estamos usando [Bulma Framework](https://bulma.io/), pero siempre se puede cambiar a algo más avanzado si merece la pena.


## Al cacharreo

La web es generada usando [Pelican](https://blog.getpelican.com/), que nos ahorra hacer trabajo aburrido, tener que usar copy/paste constantemente y otras muchas magias divertidas con Python que poco a poco irás descubriendo.


### Estructura del proyecto

El proyecto queda estructurado en los siguientes directorios:
Divido los directorios en tres **categorías**.

1. **Infra**, su propósito es preparar el entorno, instalar las dependencias y otras magias.
2. **UI / UX**, contiene el código para darle forma y color a la web, generalmente HTML, CSS.
3. **Content**, contiene artículos y publicaciones en markdown.
4. **Code**, contiene scripts en python para hacer pequeñas magias con Pelican y Python.

Y tendríamos los siguientes directorios:

- **.github** (infra) Aquí se definen las cosas referentes a la integración continua, (mejor no tocarlo mucho xD)
- **compose** (infra) Aquí se definen los manifiestos Docker, que preparan todo lo necesario para que funcione en tu localhost.
- **content** (content) Aquí se alojan los articulos y publicaciones en formato Markdown.
- **plugins** (code) Plugins de Pelican.
- **themes** (ui/ux) Código HTML y CSS que pone bonita la web.
- **output** (autogenerado) Aquí se guarda el código de la web compilado, se genera automáticamente, por lo tanto **no modifiques manualmente**.


### Localhost

Para arrancar este proyecto en local, independientemente del sistema operativo que uses, tienes dos alternativas


#### Docker

Para ello necesitas [Docker](https://www.docker.com/get-started) y [docker-compose](https://docs.docker.com/compose/install/).

```sh
docker-compose up --build
```

Accede con tu navegador a la url [localhost:8080](http://localhost:8080)

#### Python & Virtualenv

Debes tener instalado Python >= 3.6 y [virtualenv](https://virtualenv.pypa.io/en/latest/) y seguir los siguientes pasos:

1. Crear un virtualenv propio para este proyecto y activarlo

```bash
virtualenv venv
source ./venv/bin/activate
```

2. Instalar las dependencias Python necesarias

```bash
pip install -r requirements.txt
```

3. Iniciar el servidor web en local con el script o con make indicando de forma opcional el puerto deseado (por defecto 8000)

- Opción 1
```bash
./develop_server.sh start {PORT}
```

- Opción 2
```bash
 make devserver PORT={PORT}
```

## Flag del evento

Como sabemos cualquier evento o congreso pasa por diferentes etapas, donde la información a mostrar en la web debe ser diferente.
Para facilitar el trabajo contamos con el archivo **pelicanconf_flags.py** donde el organizador puede habilitar y deshabilitar elementos de la web.


| Variable                  | Descripción                                                  |
| ------------------------- | ------------------------------------------------------------ |
| LANDING_MODE              | Habilita el modo landing-page de la web, para poder tener una presentación reducida o completa de la web. |
| ENABLED_TICKETS           | Habilita links a la tienda de las entradas del evento.       |
| ENABLED_CALL_FOR_PAPERS   | Habilita bloque que hace la llamada a los ponentes.          |
| ENABLED_KEYNOTERS         | Hablita bloque que muestra los oradores plenarios del evento. |
| ENABLED_SPEAKERS          | Habilita pantalla de ponentes.                               |
| ENABLED_SPONSORSHIPS      | Habilita bloque con todos los patrocinadores.                |
| ENABLED_CALL_FOR_SPONSORS | Habilita bloque con llamamiento a patrocinadores             |
| ENABLED_SCHEDULE          | Habilita la vista del calendario del evento.                 |
| ENABLED_BLOG              | Habilita la funcionalidad de blog de contenidos de la web.   |
