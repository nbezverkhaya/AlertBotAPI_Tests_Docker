from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['DEFAULT']['TOKEN']
CHAT_ID = config['DEFAULT']['CHAT_ID']
CHANNEL = config['DEFAULT']['CHANNEL']

app = FastAPI()

class Message(BaseModel):
    Type: str
    Name: str
    Description: str

def send_message_to_chanel(channel: str, message: Message):
    if channel == "Telegram":
        return send_to_telegram(message, TOKEN, CHAT_ID)
    else:
        message = {"error": f"channel {channel} not implemented yet"}
        return JSONResponse(content = message, status_code= 501)

def send_to_telegram(message: Message, token: str, chat_id: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    return requests.get(url)

@app.post("/message/")
def send_message(message: Message):
    if message.Type == "Warning":
        response = send_message_to_chanel(CHANNEL, message)
        if response.status_code == 200:
            return JSONResponse(content={"status": "attempt to send message to chat successful"},
                                status_code=response.status_code)
        else:
            print(response.text)
            return JSONResponse(content={"error": f"attempt to send message to chat failed: {response.json().get('description')}"},
                                status_code=response.status_code)
    else:
        return JSONResponse(content={"status": "message acknowledged"}, status_code=200)


