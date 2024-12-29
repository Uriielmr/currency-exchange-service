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

## Instalación y Configuración

### Clonar el repositorio
https://github.com/Uriielmr/currency-exchange-service.git

```bash
git clone https://github.com/Uriielmr/currency-exchange-service.git
```

## Configuración con Docker

```bash
docker build -t service .
```

### Construir la imagen Docker:

```bash
docker run -p 8000:8000 service .
```