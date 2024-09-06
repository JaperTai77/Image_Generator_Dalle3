from openai import AzureOpenAI
import json
from io import BytesIO
import requests
import re
import streamlit as st

def get_client():
    client = AzureOpenAI(
        api_version="2024-05-01-preview",
        azure_endpoint=st.secrets['endpoint'],
        api_key=st.secrets['key'],
    )
    return client

def generate_image(prompt):
    client = get_client()
    result = client.images.generate(
        model="Dalle3",
        prompt=prompt,
        n=1
    )

    image_url = json.loads(result.model_dump_json())['data'][0]['url']
    result = requests.get(image_url)
    return BytesIO(result.content)

def generate_image_prompt(prompt):
    payload = {
        "messages": [
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You give a few examples of english prompts that help generate image base on user's input. Return prompts in bullet point"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt
                }
            ]
            }
        ],
        "temperature": 0.9,
        "top_p": 0.95,
        "max_tokens": 800
    }

    response = requests.post(st.secrets['completionendpoint'], headers={"Content-Type": "application/json", "api-key": st.secrets['key']}, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()['choices'][0]['message']['content']

def process_image_prompt(response):
    response = response.split('\n')
    response = [re.sub(r"(?<!\\)['\"](.*?)(?<!\\)['\"]", r"\1", response[i]) for i in range(len(response))]
    return response

if __name__ == "__main__":
    response = generate_image_prompt('halong bay, vietnam')
    response = process_image_prompt(response)
    