# Currency Exchange API

Proyecto es un API simulando un intercambio de Divisas, usando swagger para documentar el API de manera eficiente

## Características principales

* Recurso para cotizar el intercambio de monedas tomando en cuenta el tipo de cambio de un servicio de terceros (https://v6.exchangerate-api.com) 
* Recurso para intercambiar las monedas deseadas 
* Recurso para visualizar los movimientos que el usuario ha realizado con filtrado 
* Realizar 3 pruebas unitarias por cada servicio 

### Caracteristicas extras

* Se crea servicio para Crear usuario nuevo
* Se crea servio para obtener el listado de usuarios registrados

## Requisitos Previos

- Docker
- Docker Compose (opcional, si usas servicios adicionales como bases de datos)
- Python 3.11 (opcional, si ejecutas localmente)
- Base URL http://127.0.0.1:8000/docs#/


## Instalación y Configuración

### Clonar el repositorio

```bash
git clone https://github.com/Uriielmr/currency-exchange-service.git
```

## Configuración con Docker

```bash
docker build -t exchange-service .
```

### Construir la imagen Docker:

```bash
docker run -p 8000:8000 exchange-service .
```

## Tecnologias usadas

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="200" height="50" style="margin: 30px 0px 0px 40px;"><img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" width="110" height="50" style="margin: 30px 0px 0px 40px;"><img src="https://www.sqlite.org/images/sqlite370_banner.svg" width="200" height="50" style="margin: 30px 0px 0px 40px;"><img src="https://www.uvicorn.org/uvicorn.png" height="80" style="margin: 30px 0px 0px 40px;">

