# lead-tech

Este proyecto esta hecho en Flask y en React. El objetivo es subir un archivo csv (que encontramos en el folder cargar-csv), guardarlo en una base, validando si hay o no duplicados, despues de esto poder consultar los primeros 100 registos guardados y mostrarlos en una tabla. Todo se comunica por APIs de Flask.

Para ejecutarlo localmente deben seguirse los siguientes pasos.

## Crear Entorno

Es opcional, pero tambien el metodo mas efectivo para no instalar librerias que no sirvan en el equipo.

```bash
  python -m venv venv
```
Iniciamos el Entorno

En Linux
```bash
  source venv/bin/activate
```
En Windows
```bash
  venv\Scripts\activate
```

## Instalar requerimientos

Instalar las librerias necesarias de python:

```bash
  pip3 install -r requirements.txt
```

Descargar node en la siguiente url según su sistema operativo https://nodejs.org/es/download

Instalamos la siguiente librerias de node 


```bash
npm install axios react-bootstrap react-bootstrap-table2 react-dropzone flask-sqlalchemy flask-cors flask-restful react-router-dom routes react-bootstrap bootstrap
```

## Iniciar Flask

En la consola ejecutamos el siguiente comando para iniciar la app de Flask

```bash
  python main.py
```

#Iniciamos React

En otra consla ejecutamos el siguiente comando para iniciar React
```bash
  npm start
```

Ingresamos a la url 
```bash
http://localhost:3000/
```