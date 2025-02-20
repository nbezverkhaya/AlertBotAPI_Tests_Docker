# FastAPI Bot Notifier

This project is a FastAPI-based application that sends messages to a chat based on the message type. If the message type is `Warning`, it will be forwarded to chat; otherwise, it will be ignored.

## Purpose
This project was developed as a test assignment for a job application.

## Installation and Setup

### Requirements
- Python 3.7+
- Virtual environment

### Steps to Set Up

1. Clone the repository:
```
git clone https://github.com/nbezverkhaya/AlertBotAPI.git
```
2. Open a terminal or command prompt in the extracted folder.
```
cd AlertBotAPI
```
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```
4. Install dependencies:
```
pip install -r requirements.txt
```
### Telegram Bot Setup

Telegram Bot Setup

To use this bot, you need to create a Telegram bot and obtain the necessary credentials.

1. Create a Telegram Bot

* Open Telegram and search for BotFather.
* Start a chat and use the command /newbot.
* Follow the instructions to set a bot name and username.
* After creation, you will receive a bot token. Save it for later use.

2. Get Your Chat ID

* Start a chat with your bot in Telegram.
* Open the following URL in a browser, replacing <YOUR_BOT_TOKEN> with your actual bot token:
```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```
* Send a message to the bot in Telegram.
* Refresh the URL and look for "chat": {"id": <your_chat_id>} in the JSON response.
* Copy the chat ID for later use.

3. Configure config.ini

* Rename the provided config.example.ini file to config.ini.
* Open config.ini and set your bot token and chat ID:
```
TOKEN = your_bot_token_here
CHAT_ID = your_chat_id_here
```

### Running the Server

Navigate to working folder
Start the FastAPI server with the following command:
```
fastapi run notification_dispatcher.py
```
Swagger UI reference for the send_message endpoint by default can be found here: http://localhost:8000/docs#/default/send_message_message__post

### API Usage
Endpoint: POST /message/
Request Body (JSON format):
```
{
  "Type": "Warning",
  "Name": "Backup Failure",
  "Description": "The backup failed due to a database problem"
}
```
* If Type is "Warning", the message will be sent to Telegram.
* If Type is anything else, the request will be ignored.

## Running Tests
To test the application, run:
```
pytest test_notification.py
```
## Notes

Ensure that your Bot Token and Chat ID are correctly set in config.ini
The application relies on Telegram's API for message delivery, so an active internet connection is required.

## Author

Nataliia Kravchenko.