# large_llama='llama3.1-405b'
# llama='llama3.1-70b'

import json
from llamaapi import LlamaAPI
from dotenv import load_dotenv

import os

load_dotenv()

llama_api_token = os.getenv("LLAMA_API_TOKEN")

# Initialize the SDK
llama = LlamaAPI(llama_api_token)

# Build the API request
api_request_json = {
    "model": "llama3.1-70b",
    "messages": [
        {"role": "user", "content": "What is the weather like in Boston?"},
    ],
    "functions": [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "days": {
                        "type": "number",
                        "description": "for how many days ahead you wants the forecast",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
            },
            "required": ["location", "days"],
        }
    ],
    "stream": False,
    "function_call": "get_current_weather",
}

# Execute the Request
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))
