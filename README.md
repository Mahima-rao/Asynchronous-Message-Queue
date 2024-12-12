# Stryker Technical Challenge: Asynchronous Message Queue Abstraction Library

This repository contains a solution for the Stryker technical challenge. It implements an asynchronous message queue abstraction and two FastAPI microservices that interact through the queue.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Running the Solution](#running-the-solution)
- [Testing](#testing)


## Overview

This solution consists of:
1. **A Message Queue Abstraction Library** that implements an asynchronous message queue using `asyncio.Queue`.
2. **Service A** that publishes messages to the shared message queue.
3. **Service B** that subscribes to the queue and processes the messages.
4. A **setup script** to automate the setup and execution of both services.

## Installation

1. **Clone the repository**:
   git clone https://github.com/yourusername/stryker-assignment.git
   cd stryker-assignment
2. **Create a virtual environment**:
   .\venv\Scripts\activate
3. **Activate the virtual environment**:
   .\venv\Scripts\activate
4. **Install depencies**:
   pip install -r requirements.txt

## Running the solution:
   python setup_and_run.py

**This script will**:
Set up the environment.
Install dependencies.
Start Service A on port 8000 and Service B on port 8001.
Service A will be available at http://127.0.0.1:8000.
Service B will be available at http://127.0.0.1:8001.

**Service A - Endpoint**:
POST /service_a/publish/

**Service B**:
Listens to the shared queue and processes messages in the background.

## Testing:
 **Run unit tests**:
 pytest tests/

**This will run the tests for**:
The message queue (publish and subscribe functionality).
Service A (publishing messages).
Service B (subscribing and processing messages).

