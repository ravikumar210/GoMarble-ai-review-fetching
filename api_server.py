from flask import Flask, request, jsonify
from scraper import website_scraping, extract_body_content, clean_body_content, split_dom_content, combine_chunks
from parse import parse_with_ollama

app = Flask(__name__)

@app.route('/api/reviews', methods=['GET'])
def extract_reviews():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    try:
        # Step 1: Scrape the webpage
        raw_html = website_scraping(url)
        body_content = extract_body_content(raw_html)
        cleaned_content = clean_body_content(body_content)

        # Step 2: Split content for processing
        dom_chunks = combine_chunks(split_dom_content(cleaned_content))

        # Step 3: Parse with LLM
        parse_description = "Extract reviews and pagination links from the provided product page content."
        parsed_data = parse_with_ollama(dom_chunks, parse_description)

        return jsonify(parsed_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
