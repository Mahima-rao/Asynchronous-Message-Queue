# Stryker Technical Challenge: Asynchronous Message Queue Abstraction Library

This repository contains a solution for the Stryker technical challenge. It implements an asynchronous message queue abstraction and two FastAPI microservices that interact through the queue.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Running the Solution](#running-the-solution)
- [Testing](#testing)


## Overview

This solution consists of:
1. **A Message Queue Abstraction Library**  A Message Queue Abstraction Library that uses Redis for queue management, providing a persistent, distributed queuing system. It ensures scalability, fault tolerance, and seamless integration with asynchronous applications
2. **Service A** that publishes messages to the shared message queue.
3. **Service B** that subscribes to the queue and processes the messages.
4. A **setup script** to automate the setup and execution of both services.

## Installation

1. **Clone the repository**:
   - git clone https://github.com/Mahima-rao/stryker.git
   - cd stryker-assignment
2. **Create a virtual environment**:
   - .\venv\Scripts\activate
3. **Activate the virtual environment**:
   - .\venv\Scripts\activate
4. **Install depencies**:
   - pip install -r requirements.txt

## Running the solution:
   - python setup_and_run.py

**This script will**:
1. Set up the environment.
2. Install dependencies.
3. Start Service A on port 8000 and Service B on port 8001.
4. Service A will be available at http://127.0.0.1:8000.
5. Service B will be available at http://127.0.0.1:8001.

**Service A - Endpoint**:
- POST /publish/

**Service B**:
- Listens to the shared queue and processes messages in the background.

## Redis Server Setup:
- In order for the services to interact via the message queue, Redis must be running locally.
**Steps to Start Redis**:
- Download the Redis Windows version from [here](https://github.com/microsoftarchive/redis/releases). 
- Start Redis server:
   - redis-server

## Testing:
 **Run unit tests**:
 - pytest tests/

**This will run the tests for**:
1. The message queue (publish and subscribe functionality).
2. Service A (publishing messages).
3. Service B (subscribing and processing messages).

