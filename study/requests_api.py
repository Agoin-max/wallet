import requests


def api_server():
    headers = {"authorization": ""}
    url = "http://127.0.0.1:8000" + "/api/user/register"
    params = {"validate": "1657003834000", }
    response = requests.post(url, data=params, headers=headers)
    # response = requests.get(url, params=params, headers=headers)
    print(response.content.decode('utf-8'))


if __name__ == '__main__':
    api_server()
