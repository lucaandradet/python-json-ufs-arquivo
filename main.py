import urllib.request  #importando biblioteca urllib.request
import json #importando biblioteca json

url = 'https://sisu-api-pcr.apps.mec.gov.br/api/v1/oferta/instituicoes' #atribuindo valor link a variável url
resp = urllib.request.urlopen(url+str()).read() #Abrindo e lendo URL - Atribuindo valor a variável resposta
resp = json.loads(resp.decode('utf-8')) #Codificando URL para codificação UTF-8

with open('instituices.csv', 'w') as arquivo:
   for x in resp:  #Percorrendo toda variável resp
      print(x['co_ies'], file=arquivo) #Imprimindo somente os campos necessários