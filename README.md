# 🌦️ Smart Weather AI - Backend

API desenvolvida em Python utilizando FastAPI que integra dados meteorológicos com Inteligência Artificial para gerar relatórios personalizados.

---

## 🚀 Funcionalidades

- Consulta clima em tempo real via OpenWeather API
- Geração de recomendações inteligentes com OpenAI
- Envio opcional de relatório por email (Resend)
- API REST pronta para integração com frontend

---

## 🧠 Tecnologias

- Python
- FastAPI
- OpenWeather API
- OpenAI API
- Resend API
- Uvicorn

---

## 📡 Endpoint principal

### POST `/generate-report`

Gera um relatório inteligente do clima.

#### Request:

```json
{
  "city": "Lisboa",
  "email": "email@exemplo.com"
}

#### Response:
{
  "city": "Lisboa",
  "temperature": 22,
  "humidity": 60,
  "condition": "céu limpo",
  "report": "Hoje será um dia agradável..."
}



