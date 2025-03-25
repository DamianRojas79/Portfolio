## Portfolio

  

  

  

![image alt](https://github.com/DamianRojas79/Portfolio/blob/main/images-git/potfolio.png)

<br>

  

  

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)![Static Badge](https://img.shields.io/badge/Date_Release-Junio-orange)![Static Badge](https://img.shields.io/badge/API_Contact-%20V1.0.0-blue)

  

  

  

  

## Índice

  

  

  

  

*[Título e imagen de portada](#Título-e-imagen-de-portada)

  

  

  

  

*[Insignias](#insignias)

  

  

  

  

*[Índice]()

  

  

  

  

*[Descripción del proyecto](#descripción-del-proyecto)

  

  

  

  

*[Estado del proyecto](#estado-del-proyecto)

  

  

  

  

*[Características de la aplicación y demostración](#características-de-la-aplicación-y-demostración)

  

  

  

  

*[Acceso al proyecto](#acceso-al-proyecto)

  

  

  

  

*[Tecnologías utilizadas](https://github.com/DamianRojas79/ToDo-List/edit/main/README.md#tecnolog%C3%ADas-utilizadas-heavy_check_mark)

  

  

  

  

*[Personas desarrolladores del proyecto](#personas-desarrolladoras-del-proyecto)

  

  

  

  

*[Licencia](licencia-)

  

  

  

  

*[Conclusión](#conclusión)

  

  

  

  

## Descripción del Proyecto

  

  

  

  

Este es un proyecto creado con Python y Flask en el cual se desarrollo un portafolio con acceso a algunos de mis  proyectos, donde también hay pequeña presentación personal y además un formulario de contacto que se puede enviar por mail. <br><br>

  
<br>
  

  

  

  

  

## Estado del Proyecto

  

  

  

  

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

  

  

<br>

  

## Características de la aplicación y demostración

  

  

  

  

  

:hammer: **Funcionalidades del proyecto**

  

  

- #### **`Menú de Navegación`**

En la parte superior derecha del sitio se encuentra el menú de navegación con el cual se puede dirigir a las diferentes secciones del portafolio.

![image alt]( https://github.com/DamianRojas79/Portfolio/blob/main/images-git/menu-navegacion.png)
  
<br>
  

- #### **`Sección de Presentación`**

En esta sección se muestra una pequeña descripción de la persona.
También existe un botón para dirigirse a la sección de contacto si lo desea.
![image alt](https://github.com/DamianRojas79/Portfolio/blob/main/images-git/seccion-presentacion.png)
  
<br>

- #### **`Sección de Presentación de proyectos`**

Aqui se se presentan los proyectos con una breve descripción de cada uno y un enlace hacia ellos.
![image alt](https://github.com/DamianRojas79/Portfolio/blob/main/images-git/seccion-proyectos.png)

<br>

- #### **`Sección de formulario y envío de mail`**


Es la sección de contacto  donde permite completar un formulario para enviarlo por mail con los campos nombre, correo y un mensaje que se desee enviar. El mail enviado llega al mail configurado en el sistema, y si este se envía correctamente se redirige a una página de "Correo enviado" exitoso con la opción de volver nuevamente a la página de inicio del portafolio. Para la gestión de los mail en este caso se utilizo el servicio de Mailtrap.

  ![image alt](https://github.com/DamianRojas79/Portfolio/blob/main/images-git/seccion-formulario.png)

<br>  

- #### **`Footer y redes sociales`**

En esta sección del footer  se encuentran los links de acceso a las redes sociales
![image alt](https://github.com/DamianRojas79/Portfolio/blob/main/images-git/footer.png)
  
<br><br>


## Acceso al Proyecto

  

  

  

  

  

Para descargar y ejecutar el proyecto se debe realizar los siguientes pasos:

  

  

  

  

  

:file_folder: **Acceso al proyecto**

  

  

  

  

- **Abrir terminal**<br>

  

  

  

  

Primero se debe abrir una terminal para ejecutar los comandos necesarios para descargar y ejecutar el proyecto.

  

  

  

  

  

- **Crear directorio para el proyecto**<br>

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>mkdir proyecto-portfolio</i>

  

  

  

  

  

- **Clonar repositorio**<br>

  

  

  

  

Para clonar el repositorio primero situarse en el directorio creado:<br>

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>cd proyecto-portfolio </i><br>

  

  

  

  

Luego allí clonar el repositorio:<br>

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>git clone git@github.com:DamianRojas79/Portfolio </i>

  

  

  

  

  

:hammer_and_wrench: **Abre y ejecuta el programa**

  

  

  

  

- **Instalar python y modulo venv para crear entornos virtuales si no lo tienes instalado**<br>

  

  

  

  

Para instalar Pyhton

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>sudo apt install python3</i> <br>

  

  

  

  

  

Para instalar venv

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>sudo apt install -y python3-venv</i><br>

  

  

  

  

  

- **Crear entorno virtual para el proyecto**<br>

  

  

  

  

Se crea un entorno virtual para tener allí todos los paquetes necesarios para el proyecto.<br>

  

  

  

  

Para ello primero se debe entrar al directorio clonado.<br>

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>cd proyecto-portfolio </i>

  

  

  

  

  

Luego se crea el entorno virtual:

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>python -m venv env-portfolio</i>

  

  

  

  

  

- **Activar entorno virtual**

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>source env-portfolio/bin/activate</i>

  

  

  

  

  

- **Instalar las dependencias para el proyecto** <br>

  

  

  

  

Se instalan las as dependencias necesarias que se encuentra dentro del archivo requirements.txt.<br>

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>pip install -r requirements.txt</i>

  

  

  

  

  

- **Ejecutar el programa**

  

  

  

  

<ins>Ejecutar</ins>:<br>

  

  

  

  

<i>Python3 app.py</i>

  

  

  

  

  

- **Abrir aplicación en el navegador**<br>

  

  

  

  

En el navegador que desee ingresar la siguiente URL para abrir la aplicación:<br>

  

  

  

  

http://localhost:5000/

  

  

  

<br>

  

## Tecnologías Utilizadas :heavy_check_mark:

  

  

  

- **Python**<br>  

- **Flask**<br>

- **Jinja**<br>

- **CSS**<br>

- **Boostrap**<br>

  


  

  

  

  


  

  

  



  
<br>
  

  

  

## Personas Desarrolladoras del Proyecto

  

  

  

  

[<img src="https://avatars.githubusercontent.com/u/135189204?s=400&u=932907d7db09c6472e34c43c6b5ed27be7342bf4&v=4" width=115><br><sub> Damian Rojas </sub>](https://github.com/DamianRojas79)

  

  

  
<br>
  

## Licencia 📄

  

  

  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

  

  

  

  

Este proyecto cuenta con licencia conforme a los términos de la licencia MIT.

  

<br>

  

## Conclusión

En este proyecto se realizó un portfolio con las características típicas de este, con un menú y secciones de presentación, contacto y accesos a los proyectos. Creo lo importante además de la utilización de las tecnolgías utilizadas en el proyecto es la sección del formulario y contacto, donde se puede enviar un mail y poner en contacto con el cliente o interesado lo cual es el objetivo principal de un portfolio.  
