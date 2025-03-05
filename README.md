# Smart Planter Project

## Product Description

### User Need
The Smart Planter is specifically crafted for plant enthusiasts who struggle with the complexities of plant care. Whether due to busy schedules, limited knowledge, or previous unsuccessful attempts, many people find it challenging to maintain the health of their indoor plants. This product ensures that even those without a green thumb can keep their plants thriving and vibrant, making plant care accessible and effortless for everyone.

### Value Proposition
The Smart Planter offers a hands-off approach to gardening by automating the essential aspects of plant care, alerts you for tempature chanegs, humidly changes. It leverages real-time sensor data to update the user based on the plant’s needs, environmental changes, and weather conditions. The digital screen on the planter reacts based on the conditions of the plant, allowing you to know the plant condition based on a glance. 

### Personal Compelling
This project was inspired by a personal experience where I was gifted a really expensive and exotic plant that I was unfortunately unable to maintain due to my lack of proper plant care knowledge and time. This incident was a turning point for me, sparking a desire to ensure that others do not face the same disappointment of losing a cherished plant. It drove me to create a solution that combines technology with a deep love for plants, making it easier for everyone to enjoy the beauty and benefits of plant ownership without the fear of making costly mistakes.

## Reflection
The development of the Smart Planter has been a rewarding journey that challenged my skills in software development, and user-centric design. This project allowed me to dive deep into the realm of IoT devices, pushing the boundaries of what I could achive. Throughout this process, I've learned the importance continuous testing, and adapting to feedback, which are invaluable skills in any technology-driven project.



# How to set it up

This repository contains the backend code for the Smart Planter system, designed to automate plant care through sensors and intelligent controls. The system uses MQTT for device communication and Streamlit for the user interface, along with an HTTP API to bridge the two.

## System Components

- **Streamlit UI (Client)**: A web interface for user interaction.
- **DataService.py**: Bridges HTTP requests to MQTT messages.
- **MQTT Publisher (`pub.py`)**: Handles publishing sensor data from the planter.
- **Gemini LLM API**: Provides NLP capabilities for understanding user queries.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- PIP for Python package management

## Installation

Follow these steps to set up the project environment:

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/AnnieYurongHuang/midterm-smart-planter.git]


2. pip install -r req.txt
3. Setting up MQTT Broker:
    You can use a local or cloud-based MQTT broker.
    For local testing, install and run Mosquitto:

4. Set up necessary environment variables or use a .env to found API keys
5. Publishing Sensor Data first by typing in terminal $python pub.py
6. SUing this command $uvicorn data_service:app to start the DataService.py to handle HTTP to MQTT translation --reload
7. Run Streamlit using $ streamlit run app.py