# FastAPI Bot Notifier

This project is a FastAPI-based application that sends messages to a chat based on the message type. If the message type is `Warning`, it will be forwarded to chat; otherwise, it will be ignored.

## Purpose
This project was developed as a test assignment for a job application.

## Installation and Setup

### Requirements
- Python 3.7+
- Virtual environment

### Steps to Set Up

1. Extract the ZIP file.
2. Open a terminal or command prompt in the extracted folder.
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