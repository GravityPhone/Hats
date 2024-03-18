import requests


def print_assistant_api_response():
    response = requests.get('http://example.com/api/assistant')
    print("API Response:", response.json())

if __name__ == "__main__":
    print_assistant_api_response()
