# Project Title: Sentiment Analysis API

## Overview
This project provides a sentiment analysis API built using Flask. It utilizes Natural Language Processing (NLP) techniques to analyze the sentiment of text input and provides a score indicating the sentiment polarity.

## Installation
To set up the project, ensure you have Python 3.x installed. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Dependencies
- Flask: A lightweight WSGI web application framework.
- spaCy: An NLP library for advanced natural language processing.
- NLTK: A suite of libraries and programs for natural language processing.
- ObsceneFilter: A library to filter out obscene words.

## Usage
To run the application, execute the following command:

```bash
python sentimental_analyser.py
```

The API will be available at `http://127.0.0.1:5000/ibs_hackathon_2018/api/v1.0/sentiment_analyzer`.

### API Endpoint
- **POST /ibs_hackathon_2018/api/v1.0/sentiment_analyzer**
  - **Request Body**: JSON object containing the text to analyze.
  - **Response**: JSON object with sentiment scores.

### Example Request
```json
{
  "text": "I love programming!"
}
```

### Example Response
```json
{
  "neg": 0.0,
  "neu": 0.5,
  "pos": 0.5,
  "compound": 0.6369
}
```

## Error Handling
The API will return appropriate HTTP status codes for different error scenarios:
- **400 Bad Request**: If the request body is missing or improperly formatted.
- **500 Internal Server Error**: For unexpected errors during processing.

## Testing
To ensure the application functions correctly after updates:
1. Run the application and test the API endpoint with various inputs.
2. Check for any conflicts or errors during dependency updates.
3. Review the documentation for clarity and completeness.

## Contribution
Contributions are welcome! Please submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.