# -*- coding: utf-8 -*-
# README for ibs_hackathon_sentiment_analysis

# Project Overview
This project is a sentiment analysis tool that utilizes natural language processing (NLP) techniques to analyze text and determine sentiment polarity. It also includes functionality to filter obscene words from the input text.

# Dependencies
The project requires the following Python packages:
- Flask: A micro web framework for Python.
- spaCy: An NLP library for advanced text processing.
- nltk: A library for natural language processing, specifically for sentiment analysis.
- obscenefilter: A library for filtering obscene words from text.

## Installation
To install the required dependencies, run the following command:
```bash
pip install Flask spacy nltk obscenefilter
python -m spacy download en_core_web_sm
```

# Usage
To start the Flask application, run the following command:
```bash
python sentimental_analyser.py
```
The application will be available at `http://127.0.0.1:5000/ibs_hackathon_2018/api/v1.0/sentiment_analyzer`.

# API Endpoint
## POST /ibs_hackathon_2018/api/v1.0/sentiment_analyzer
This endpoint accepts a JSON payload containing text for sentiment analysis. The response will include the sentiment polarity scores.

### Request Example
```json
{
    "text": "I love programming!"
}
```

### Response Example
```json
{
    "neg": 0.0,
    "neu": 0.5,
    "pos": 0.5,
    "compound": 0.6369
}
```

# Documentation
The documentation has been updated to reflect the current architecture and dependencies of the project. It accurately describes the system's functionality and provides clear instructions for installation and usage.

# Testing
Ensure that the application compiles without errors after updating dependencies. Review the documentation for clarity and completeness.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.