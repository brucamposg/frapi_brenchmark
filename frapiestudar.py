#Desafio Estudar

import json
import requests
import base64


#funcoes

def similarity_score(data):
    drop_count = 0
    score = []

    requests_body = {
        "image_b641": data[0],
        "image_b642": data[1],
    }

    resp = requests.get('http://35.237.84.73/frapi/verify/images')
    if resp.status_code == 200:
        score.append(resp.json()['similarity_score'])

    else:
        drop_count +=1
        
    print(f'Drops:{drop_count}')
    print('Done...')
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
    dados = open("./pairs.txt", 'r')
    dados.readline()
    dados = arr

    print(dados)

    if len(arr) == 3:
        linha = dados.readline().split('\t')
        linha[2] = linha[2].replace('\n', '')
        first_path = "./lfw/" + linha[0] + "/" + linha[0] + "_" + zeros(linha[1]) + linha[1] + ".jpg"
        second_path = "./lfw/" + linha[0] + "/" + linha[0] + "_" + zeros(linha[2]) + linha[2] + ".jpg"

    else:
        linha = dados.readline().split('\t')
        linha[3] = linha[3].replace('\n', '')
        first_path = "./lfw/" + linha[0] + "/" + linha[0] + "_" + zeros(linha[2]) + linha[2] + ".jpg"
        second_path = "./lfw/" + linha[0] + "/" + linha[0] + "_" + zeros(linha[3]) + linha[3] + ".jpg"

    data = [first_path, second_path]

    return data

#main


dados = open("./pairs.txt", 'r')
dados.readline()
scores = []

x = 0

while (x < 300):
   
    image_path = paths(dados)
    first_path = image_path[0]
    second_path = image_path[1]
    image_b641 = get_base64(first_path)
    image_b642 = get_base64(second_path)
    data = [image_b641, image_b642]
    score = similarity_score(data)
    scores = score
    x =+ 1

print(scores)
    



