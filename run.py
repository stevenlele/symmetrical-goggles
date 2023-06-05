import base64
import os
import pickle

import httpx

config = os.getenv('CONFIG')
token, pairs = pickle.loads(base64.b64decode(config.encode()))
headers = {'Authorization': f'Token {token}'}

success = True

with httpx.Client(headers=headers) as client:
    for url, value in pairs:
        payload = {'state': 20, 'target': [value]}
        response = client.patch(url, json=payload)
        code = response.status_code
        success = success and (code == 200 or code == 403)

if not success:
    exit(1)
