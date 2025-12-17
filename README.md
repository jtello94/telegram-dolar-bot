### 📊 Telegram Dólar Bot

Bot de Telegram desarrollado en Python para consultar cotizaciones del dólar en Argentina.

Permite obtener valores actualizados de:

- Dólar MEP (Bolsa)

- Dólar Cripto

mediante comandos simples desde Telegram.

**Aclaracion: Por el momento solo devuelve el precio de estos dos valores, proximamente se agregarán los demas.**

### 🚀 Funcionalidades

- /mep → muestra cotización del dólar MEP

- /cripto → muestra cotización del dólar cripto

- Conversión de fecha a hora local de Argentina

- Indicación clara de la fuente de datos

- Desplegado como servicio 24/7

### 🛠️ Tecnologías utilizadas

- Python

- python-telegram-bot

- Requests

- Docker

- Railway

- API pública de cotizaciones

### 📦 Deploy

El bot está deployado usando Docker en Railway, lo que garantiza un entorno reproducible y estable.

Las variables sensibles (como el token del bot) se gestionan mediante variables de entorno.

### ✨ Nota personal

Este proyecto forma parte de mi proceso de aprendizaje en desarrollo backend, automatización y despliegue de servicios.
Asimismo también sirvió para aplicar los conocimientos aprendidos durante el año de cursada, agregando también lectura de documentacion y videos.
El foco estuvo en entender cómo funcionan las herramientas, no solo en que “ande”.
