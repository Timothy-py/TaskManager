# TASK MANAGER API

## Description

A simple task manager implementation that can be used to manage tasks.

## APPS

### Task Resources
### Notification Resources

## APIs

- Create a task
- Get a list of tasks
- Get a task details
- Update a task status
- Delete a task

## Tech Stacks

- Language -> Python
- Backend Framework -> FastAPI
- Database -> Mongodb
- Cache - > Redis
- Message Broker -> Apache Kafka

## Setup & Installation
- Clone the project
- cd into the project directory
- Install the packages in requirements.txt file
```bash
$ pip3 install -r requirements.txt
```

## Environment Setup

Create '.env' file in the root directory and use the '.env.example' file to configure the necessary environment variables or use the defaults.

## Running the app

```bash
$ uvicorn main:app

# watch mode
$ uvicorn main:app --reload
```

## Swagger API
Checkout the API @ the url below.  
APP_PORT is default to 8000

```
http://localhost:8000/docs
```

## Stay in touch

- _contact me @ adeyeyetimothy33@gmail.com_
