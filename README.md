# 🚌 Bondi Bot

Bondi Bot es un chatbot inteligente que te ayuda a moverte por la Ciudad de Buenos Aires usando transporte público. Te sugiere rutas óptimas combinando la API de Google Maps con un modelo de lenguaje gratuito (Groq / LLaMA 3).

---

## 🚀 Funcionalidades

- Consulta de rutas en subte o colectivo en tiempo real
- Interfaz conversacional natural
- Preparado para usar memoria por usuario o por chat
- Docker-ready

---

## ⚙️ Tecnologías

- Python 3.11
- FastAPI
- LangChain
- Groq API (LLaMA 3)
- Google Maps Directions API
- Docker

---

## 🔧 Instalación

1. Cloná el proyecto:

```bash
git clone https://github.com/tuusuario/bondibot.git
cd bondibot
```

2. Configurá las variables de entorno:

```bash
cp .env.example .env
# Luego editá el archivo .env con tus claves reales
```

3. Ejecutá el proyecto:

```bash
docker compose up --build
```

4. Accedé a:

- Documentación Swagger: http://localhost:8000/docs
- Test básico: GET `/` → `{"message": "Bondi Bot está vivo 🚍"}`

---

## 🔐 Variables de entorno

| Variable              | Descripción                              |
|-----------------------|------------------------------------------|
| `GOOGLE_MAPS_API_KEY` | Clave de Google Maps Directions API      |
| `GROQ_API_KEY`        | Clave gratuita de Groq (para LLaMA 3)    |

---

## 📄 Licencia

Este proyecto fue creado por **Andrea Bastidas**.  
No se permite su copia, distribución ni reutilización sin autorización expresa.

Ver [LICENSE.md](./LICENSE.md)
