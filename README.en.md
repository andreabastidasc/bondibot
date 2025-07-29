# 🚌 Bondi Bot

Bondi Bot is a smart chatbot that helps you move around Buenos Aires using public transportation. It suggests optimal routes using the Google Maps API and a free language model (Groq / LLaMA 3).

---

## 🚀 Features

- Real-time subway and bus route suggestions
- Natural language interface
- Ready for per-user or per-chat memory
- Docker-ready

---

## ⚙️ Technologies

- Python 3.11
- FastAPI
- LangChain
- Groq API (LLaMA 3)
- Google Maps Directions API
- Docker

---

## 🔧 Installation

1. Clone the project:

```bash
git clone https://github.com/youruser/bondibot.git
cd bondibot
```

2. Set environment variables:

```bash
cp .env.example .env
# Then edit your actual keys in .env
```

3. Run the project:

```bash
docker compose up --build
```

4. Open:

- Swagger docs: http://localhost:8000/docs
- Basic test: GET `/` → `{"message": "Bondi Bot está vivo 🚍"}`

---

## 🔐 Environment variables

| Variable              | Description                              |
|-----------------------|------------------------------------------|
| `GOOGLE_MAPS_API_KEY` | Google Maps Directions API Key           |
| `GROQ_API_KEY`        | Free Groq API Key (LLaMA 3)              |

---

## 📄 License

This project was created by **Andrea Bastidas**.  
Copying, redistributing or reusing this code is **not allowed** without explicit permission.

See [LICENSE.md](./LICENSE.md)
