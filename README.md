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

Response:
{
  "city": "Lisboa",
  "temperature": 22,
  "humidity": 60,
  "condition": "céu limpo",
  "report": "Hoje será um dia agradável..."
}

⚙️ Setup local
1. Clonar repositório
git clone https://github.com/douglashnunes/weather-ai-project
cd weather-ai-project
2. Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Criar arquivo .env
OPENAI_KEY=...
OPENWEATHER_KEY=...
RESEND_KEY=...
5. Rodar servidor
uvicorn main:app --reload --host 0.0.0.0 --port 8000

Acesse:

http://localhost:8000/docs
🌐 Deploy

O backend está deployado em:

https://weather-ai-project.onrender.com
⚠️ Observações
O envio de emails via Resend pode exigir domínio verificado em produção
O serviço pode entrar em modo “sleep” no plano gratuito do Render


