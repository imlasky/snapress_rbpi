import requests
from dotenv import load_dotenv
import os
import subprocess



def getAuth(email, password): 

    url = 'https://api.snapress.com/api/collections/users/auth-with-password'
    payload = {
        'identity': email,
        'password': password
    }

    response = requests.post(url, json=payload)

    return response.json()

def getPics(token):

    url = 'https://api.snapress.com/api/collections/pics/records'

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)

    pics = response.json()

    if pics['totalItems'] > 0: 
        for pic in pics['items']:
            pic_url = f"https://api.snapress.com/api/files/{pic['collectionId']}/{pic['id']}/{pic['pic']}"
            img_data = requests.get(pic_url).content
            with open(pic['pic'], 'wb') as handler:
                handler.write(img_data)

            response = requests.delete(url+f"/{pic['id']}", headers=headers)
            command = ['lp', pic['pic']]
            subprocess.run(command, check=True)
            
            command = ['rm', pic['pic']]
            subprocess.run(command, check=True)
            

if __name__ == "__main__":
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    
    auth = getAuth(email, password)
    pics = getPics(auth['token'])