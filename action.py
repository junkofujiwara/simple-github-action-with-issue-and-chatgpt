import os
import openai
import requests

body = os.environ.get("BODY")
github_token = os.environ.get("GITHUB_TOKEN")
github_url = os.environ.get("GITHUB_URL")

openai.api_key = os.environ["OPENAI_API_KEY"]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": body},
    ],
)
answer = response.choices[0]["message"]["content"].strip()
print(answer)

headers = {"Authorization": f"bearer {github_token}"}
request = requests.post(github_url, json={'body': answer}, headers=headers)
request.raise_for_status()






