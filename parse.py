from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import json
import re
from concurrent.futures import ThreadPoolExecutor

# Initialize the LLM
model = OllamaLLM(model="llama3.1")

# Define the LLM prompt
template = (
    "You are tasked with extracting reviews from the following product page content: "
    "{dom_content}. "
    "Please extract the following details for each review:\n"
    "- Review title\n"
    "- Review body\n"
    "- Rating\n"
    "- Reviewer name\n"
    "Additionally, identify if there are more pages of reviews and provide the next page URL.\n"
    "Return the output in JSON format as:\n"
    "{{\n"
    "  \"reviews\": [\n"
    "    {{\"title\": \"Review Title\", \"body\": \"Review Body\", \"rating\": 5, \"reviewer\": \"Reviewer Name\"}}\n"
    "  ],\n"
    "  \"next_page_url\": \"Next page URL or null\"\n"
    "}}"
)

def extract_json(response):
    """
    Extract valid JSON from the response text.
    """
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", response, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
        return None


def parse_with_ollama(dom_chunks, parse_description):
    """
    Parses HTML chunks using the LLM to extract review details, in parallel.
    """
    prompt = ChatPromptTemplate.from_template(template)

    def process_chunk(chunk):
        chain = prompt | model
        response = chain.invoke({"dom_content": chunk})
        return extract_json(response)

    # Use ThreadPoolExecutor to parallelize processing
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_chunk, dom_chunks))

    return combine_results([res for res in results if res])  # Filter out None results


def combine_results(parsed_results):
    """
    Combines parsed results into a single JSON structure and limits output.
    """
    combined_reviews = []
    next_page_url = None

    for result in parsed_results:
        if "reviews" in result:
            combined_reviews.extend(result["reviews"])
        if "next_page_url" in result and result["next_page_url"]:
            next_page_url = result["next_page_url"]

    return {
        "reviews": combined_reviews[:10],  # Limit to first 10 reviews
        "next_page_url": next_page_url
    }
