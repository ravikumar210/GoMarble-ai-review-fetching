# Review Scraping Application

## Introduction
The *Review Scraping Application* is a powerful tool designed to simplify the extraction of product reviews. Using *Selenium* for scraping, *Flask* for API hosting, and *AI-powered models* for parsing, it delivers clean, structured review data.

---

## Highlights
- *Effortless Scraping*: Gather raw data from product pages with ease.
- *AI-Driven Parsing*: Leverage the Llama 3.1 model to process and structure content.
- *REST API Support*: Seamlessly interact with the application via a RESTful API.
- *Robust Error Management*: Handles a variety of web content challenges gracefully.

---

## System Setup

### Required Software
- *Python*: Version 3.8 or later
- *Google Chrome*: Up-to-date version
- *ChromeDriver*: Matching your Chrome version

### Dependencies
Install the required Python libraries listed in the requirements.txt file:

bash
pip install -r requirements.txt


### AI Model Configuration
Download and set up the Llama 3.1 model following the instructions provided on the [Ollama official website](https://ollama.ai). For advanced systems, refer to compatibility guidelines for larger models.

### Environment Configuration
Create a .env file with the following variables:

env
SBR_WEBDRIVER=./chromedriver.exe
OPENAI_API_KEY=<your_openai_api_key>


---

## Installation Guide

1. *Clone the Repository*

   bash
   git clone <repository_url>
   cd <repository_name>
   

2. *Configure ChromeDriver*

   - Place the chromedriver.exe file in the root directory or update its location in the .env file.

3. *Install Required Libraries*

   bash
   pip install -r requirements.txt
   

4. *Set Up the AI Model*
   
   Follow the official setup instructions for the Llama 3.1 model on the [Ollama website](https://ollama.ai).

---

## Steps to Use

### 1. Launch the API Server
Start the server with:

bash
python api_server.py


The server will run at http://0.0.0.0:8000.

### 2. Request Review Data

Send a GET request to the /api/reviews endpoint with the url parameter:

bash
curl "http://0.0.0.0:8000/api/reviews?url=<product_page_url>"


### 3. View Results
The API will return parsed reviews in JSON format, including navigation details:

json
{
  "reviews": [
    {
      "title": "Amazing Product",
      "body": "Exceeded all my expectations!",
      "rating": 5,
      "reviewer": "John Smith"
    }
  ],
  "next_page_url": "https://example.com/next"
}


---

## Common Issues
- *ChromeDriver Mismatch*: Ensure chromedriver.exe matches your installed Google Chrome version.
- *Slow Websites*: Adjust wait times in scraper.py to accommodate slower page loads.
- *Model Configuration Errors*: Verify the Llama model setup using the langchain-ollama library.

---

## Licensing Information
This project is distributed under the *MIT License*. See the LICENSE file for more details.

---

## Contributing Guidelines
We welcome contributions! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request for review.

---

## Need Help?
For questions or issues, please [submit an issue](https://github.com/<repository>/issues) or contact the maintainer.

---

### Helpful Resources
- [Selenium Guide](https://www.selenium.dev/documentation/)
- [AI Model Setup](https://ollama.ai)
- [Flask API Documentation](https://flask.palletsprojects.com)
