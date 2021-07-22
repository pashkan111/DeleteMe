import json, requests
from asgiref.sync import sync_to_async
from flask_restful import Resource, reqparse


headers = {
        "content-type": "application/json"
    }

import requests
import json

HOST = '172.21.0.4:8200/'

@sync_to_async
def check_user(telegram_id):
    req = requests.post(
        url=f'http://{HOST}check-user', 
        headers=headers, 
        data=json.dumps({'telegram_id': telegram_id}))
    if req.status_code == 200:
        data = json.loads(req.content)
        if data['user'] == 'authorized':
            return True
        elif data['user'] == 'unauthorized':
            return False
    else:
        return 400


@sync_to_async
def register_user(data):
    req = requests.post(
        url=f'http://{HOST}register',
        headers=headers, 
        data=json.dumps(data))
    if req.status_code == 200:
        return True
    else:
        return False


@sync_to_async
def post_words(words):
    """Добавляет ключевые слова в базу"""
    req = requests.post(url=f'http://{HOST}check-keywords', headers=headers, data=json.dumps(words))
    # if req.ok:
    #     return True
    # else:
    #     return False
    # return False
    return req


@sync_to_async
def get_result(words):
    """отправляет ключевые слова на сервер и возвращает результат поиска"""
    req = requests.get(url=f'http://{HOST}check-keywords', headers=headers, data=json.dumps(words))
    if req.status_code == 200:
        return True
    else:
        return False



@sync_to_async
def result(data):
    req = requests.get(url=f'http://{HOST}result', headers=headers, data=json.dumps(data))
    try:
        data = json.loads(req.text)
        return json.loads(data)
    except:
        return None


@sync_to_async
def delete_keywords(data):
    req = requests.delete(url=f'http://{HOST}check-keywords', headers=headers, data=json.dumps(data))
    return req.status_code


@sync_to_async
def get_user_data(data):
    req = requests.get(url=f'http://{HOST}user-data', headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        return json.loads(json.loads(req.text))
    else:
        return False


@sync_to_async
def test(data):
    req = requests.delete(url=f'http://{HOST}test', headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        return req.text
    else:
        return False
