import requests


def api_server():
    headers = {"authorization": "Token mSnWXUdSQhAo3EHZe2JC7wLPAtqpMkRGbBxwbiZD"}
    url = "http://127.0.0.1:8000" + "/api/user/register"
    params = {}
    response = requests.post(url, data=params, headers=headers)
    # response = requests.get(url, params=params, headers=headers)
    print(response.content.decode('utf-8'))


if __name__ == '__main__':
    api_server()
