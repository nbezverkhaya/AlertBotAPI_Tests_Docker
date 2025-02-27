# FastAPI Bot Notifier

This project is a FastAPI-based application that sends messages to a chat based on the message type. If the message type is `Warning`, it will be forwarded to chat; otherwise, it will be ignored.
This project includes a Docker setup for easy deployment. You can run it either locally or within a Docker container.

## Purpose
This project was developed as a test assignment for a job application.

## Installation and Local Run

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

5. Open config.ini and set your bot token and chat ID:
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
Swagger UI reference for the send_message endpoint by default can be found here: http://localhost:8000/docs#/default/

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

## Run with Docker
1. Build the Docker image:
````
docker build -t alert_bot_api_tests .
````
2. Run the container:
````
docker run -p 8000:80 alert_bot_api_tests
````

## Running Tests (Local Run)
To test the application, run:

```
pytest test_notification.py  --no-header -vv
```

## Running Tests with Docker
To test the application, run:
````
docker exec -it your_container_name /bin/bash
````
```
pytest test_notification.py  --no-header -vv
```

## Notes

If you don't have a Telegram bot, you can create one by following the instructions:
1. Open Telegram and search for “BotFather” in the search bar.
2. Click on the BotFather account and select “Start.” Follow the prompts to create your bot, including giving it a name and username.
3. Once your bot is created, BotFather will provide you with a token.

## Author

Nataliia Kravchenko.