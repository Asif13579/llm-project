import requests
import json
import os, sys 
import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger=logging.getLogger(__name__)

# Prompt for LLM
#prompt="Explain quantum computing in simple terms."
prompt = """
You are an expert science tutor.

Explain quantum computing in simple, beginner-friendly terms.
Use real-world analogies and avoid complex mathematical jargon.
Keep the explanation concise and easy to understand.
"""
url="http://localhost:11434/api/generate"

payload={
    "model":"deepseek-r1:1.5b",
    "prompt":prompt,
    "stream": False # Set to false for a complete response in one JSON object
}

try:
    # for non-streaming response
    logger.info("Sending request to Ollama API...")
    response=requests.post(url,json=payload)
    response.raise_for_status()
    result=response.json()
    logger.info("Response received successfully")
    print("\nResponse from Ollama:\n")
    print(result.get("response", ""))

except requests.exceptions.ConnectionError as e:
    logger.error(f'Connection Error: {e}')
    sys.exit(1)

except requests.exceptions.HTTPError as e:
    logger.error(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    logger.error(f"Request Failed: {e}")
    print(f"Errors: {e}")
    sys.exit(1)

except Exception as e:
    logger.exception(f"Unexpected Error: {e}")
    sys.exit(1)