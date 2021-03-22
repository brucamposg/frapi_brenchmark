#Desafio Estudar

import json
import requests
import base64
import numpy as np


#funcoes

def similarity_score(data):
    score = 0

    requests_body = {
        "image_b641": data[0],
        "image_b642": data[1],
    }

    resp = requests.post('http://35.237.84.73/frapi/verify/images', json=requests_body)
    if resp.status_code == 200:
        score = (resp.json()['similarity_score'])
        
    return score

def get_base64(image_path):

    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def zeros(x):
    x = int(x)

    if x < 10:
        zero = "000"
    
    if x >= 10 and x < 100:
        zero = "00"

    if x >= 100 and x < 1000:
        zero = "0"
    
    return zero

def paths(arr):

    if len(arr) == 3:
        first_path = "lfw/" + arr[0] + "/" + arr[0] + "_" + zeros(arr[1]) + arr[1] + ".jpg"
        second_path = "lfw/" + arr[0] + "/" + arr[0] + "_" + zeros(arr[2]) + arr[2] + ".jpg"

    else:
        first_path = "lfw/" + arr[0] + "/" + arr[0] + "_" + zeros(arr[2]) + arr[2] + ".jpg"
        second_path = "lfw/" + arr[0] + "/" + arr[0] + "_" + zeros(arr[3]) + arr[3] + ".jpg"


    return first_path, second_path

#main

pairs = np.loadtxt('./pairs.txt', dtype='str', skiprows=1, max_rows=300)
scores = []

print("Loading...")

for pair in pairs:
   
    first_path, second_path = paths(pair)
    image_b641 = get_base64(first_path)
    image_b642 = get_base64(second_path)
    data = [image_b641, image_b642]
    score = similarity_score(data)
    scores.append(score)

np.savetxt('similarity.txt', scores)

print("Done!")
    



