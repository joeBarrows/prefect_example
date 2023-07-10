import requests
import random
from prefect import flow, task
from prefect.artifacts import create_markdown_artifact

@task
def get_data(url):
    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Access the response content in JSON format
        data = response.json()

    except e:
        print(f"Error: {e}")

    return data

@task
def update_data(data):
    for record in data:
        record['update'] = int((random.random() * 100))
    return data

@task
def print_data(data):
    for record in data:
        print(f"Post ID: {record['id']}")
        print(f"Title: {record['title']}")
        print(f"Body: {record['body']}")
        print(f"This is the UPDATE: {record['update']}")
        print('---')

@flow
def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = get_data(url)
    if data:
        data = update_data(data)
        print_data(data)


if __name__ == '__main__':
    main()

