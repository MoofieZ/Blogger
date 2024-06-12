import googleapiclient.discovery
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2 import credentials
import google.auth
import requests

def get_sensitive_data(key):
    sensitive_data = {
        'BLOG_ID': 'BLOG ID',  # Replace with your blog ID
        'BEARER_TOKEN': '',  # Replace with your OAUTH token
        'OPENAI_API_KEY': ''  # Replace with your OpenAI API key
    }
    return sensitive_data[key]

TITLE = 'Sample Blog Post via API'
CONTENT = '<p>This is a sample blog post created via the Blogger API.</p>'

def create_post(bearer_token, blog_id, title, content):
    credentials = google.oauth2.credentials.Credentials(bearer_token)
    service = googleapiclient.discovery.build('blogger', 'v3', credentials=credentials)
    body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content,
        'labels': ['Label1', 'Label2', 'Label3'] 
    }
    posts = service.posts()
    request = posts.insert(blogId=blog_id, body=body, isDraft=False)
    response = request.execute()
    print(response)

# Usage
def openai(message):
    openai_api_key = get_sensitive_data('OPENAI_API_KEY')
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 0.2,
        "max_tokens": 4095,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print("Error:", response.status_code, response.text)

def create():
    message = "Give me a joke"
    resp = openai(message)
    for i in range(1, 6):
        create_post(get_sensitive_data('BEARER_TOKEN'), get_sensitive_data('BLOG_ID'), i, resp)

create()
