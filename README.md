# Emotion Detector

## Final Project - Emotion Detector

An AI-based web application that detects emotions from a given text using the Watson NLP Emotion Prediction service and provides the dominant emotion.

## Project Objective

The objective of this project is to develop an emotion detection application using Python and the Watson NLP library/service. The application analyzes a text statement and identifies the following emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

It also determines the dominant emotion in the given statement.

## Technologies Used

* Python
* Watson NLP
* Flask
* Requests
* HTML
* CSS
* JavaScript
* unittest
* Pylint

## Project Structure

```text
emotion-detector/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── templates/
│   └── index.html
│
├── test_emotion_detection.py
├── server.py
├── README.md
└── requirements.txt
```

## Features

* Detects five emotions from text.
* Identifies the dominant emotion.
* Provides a Flask-based web interface.
* Handles blank or invalid input.
* Includes unit testing.
* Supports static code analysis using Pylint.

## Application Workflow

1. The user enters a text statement.
2. The Flask application receives the input.
3. The emotion detector sends the text to the Watson NLP service.
4. The service returns emotion scores.
5. The application identifies the dominant emotion.
6. The result is displayed to the user.

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python server.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000
```

## Unit Testing

Run the unit tests using:

```bash
python -m unittest discover -v
```

## Static Code Analysis

Run Pylint using:

```bash
pylint server.py
```

## Error Handling

The application handles invalid or blank input and returns an appropriate error message instead of processing an empty statement.

## Final Project

This project was developed as part of the IBM Skills Network Final Project - Emotion Detector.
