# Automated Review Scraper

This project is a web-based application that extracts reviews from product pages using a combination of Selenium for web scraping, Flask for API hosting, and an LLM for content parsing.

## Features

- Web scraping to extract raw HTML from product pages.
- Parsing reviews and metadata using an AI model.
- REST API for review extraction.
- Error handling and content cleaning.

## Prerequisites

Ensure the following tools and libraries are installed:

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver compatible with your Chrome version

### Python Libraries

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Download the Llama 3.1 Model

This project requires the Llama 3.1 model. Download it from the official source and ensure it is correctly configured for use with the `langchain-ollama` library. Refer to the [Llama documentation](https://ollama.ai) for setup details.

### For Faster Response

For faster response times, download a higher-capacity, compatible LLM if your system supports it. Check compatibility and download details in the [Ollama documentation](https://ollama.ai).

### Environment Variables

Create a `.env` file in the root directory with the following content (update the values as needed):

```
SBR_WEBDRIVER=./chromedriver.exe
OPENAI_API_KEY=<your_openai_api_key>
```

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Set up the ChromeDriver:

   - Place the `chromedriver.exe` file in the project directory or update the path in the `.env` file.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
project-root/
|-- api_server.py        # Flask API server
|-- scraper.py           # Web scraping functions
|-- parse.py             # Parsing logic using LLM
|-- .env                 # Environment variables
|-- chromedriver.exe     # ChromeDriver for Selenium
|-- requirements.txt     # Python dependencies
|-- README.md            # Project documentation
```

## Usage

### Step 1: Start the API Server

Run the API server locally:

```bash
python api_server.py
```

The server will be available at `http://0.0.0.0:8000`.

### Step 2: Extract Reviews via API

Use the `/api/reviews` endpoint to extract reviews from a product page. Send a GET request with the `url` parameter:

```bash
curl "http://0.0.0.0:8000/api/reviews?url=<product_page_url>"
```

### Step 3: Review Output

The API will return the extracted reviews and the next page URL (if available) in JSON format:

```json
{
  "reviews": [
    {
      "title": "Review Title",
      "body": "Review Body",
      "rating": 5,
      "reviewer": "Reviewer Name"
    }
  ],
  "next_page_url": "Next page URL or null"
}
```

## Additional Notes

- Ensure your `chromedriver.exe` version matches your Google Chrome version.
- Monitor the server logs for troubleshooting errors.
- Adjust Selenium's wait times in `scraper.py` if required for slower websites.

## License

This project is licensed under the MIT License.

## Support

For any issues or questions, please open an issue in this repository or contact the project maintainer.

