from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
RESEND_KEY = os.getenv("RESEND_KEY")


class WeatherRequest(BaseModel):
    city: str
    email: str = ""


@app.post("/generate-report")
def generate_report(data: WeatherRequest):

    city = data.city

    # 1. Buscar clima
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric&lang=pt"

    response = requests.get(weather_url).json()

    if "main" not in response:
        return {"error": "Cidade não encontrada"}

    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    condition = response["weather"][0]["description"]

    # 2. Gerar relatório com IA
    data_atual = datetime.now().strftime("%d/%m/%Y")
    prompt = f"""
Gere um relatório curto e bem explicativo sobre o clima atual em {city}.

Data: {data_atual}
Temperatura: {temp}°C
Umidade: {humidity}%
Condição: {condition}

Inclua a data no relatório.
Dê recomendações úteis para o dia, considerando as condições climáticas para Vestimentas mais adequadas, Atividades ao ar livre, Saúde/Hidratação e melhor Transporte.
Termine o relatório com uma frase de incentivo para aproveitar o dia, e cite pontos turíticos da {city} a explorar e conhecer melhor.
"""

    ai = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    report = ai.choices[0].message.content

    # 3. Enviar email (opcional)
    if data.email:
        send_email(data.email, city, report)

    return {
        "city": city,
        "temperature": temp,
        "humidity": humidity,
        "condition": condition,
        "report": report
    }


def send_email(to_email, city, report):

    requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {RESEND_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "from": "onboarding@resend.dev",
            "to": to_email,
            "subject": f"Relatório do clima - {city}",
            "html": f"<h2>Relatório do clima</h2><p>{report}</p>"
        }
    )