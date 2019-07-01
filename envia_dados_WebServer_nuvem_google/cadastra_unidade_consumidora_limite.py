import requests

#coding: utf-8

print("=====================================================")
print("-------------- INTERFACE DE CADASTRO ----------------")
print("=====================================================")  
print("")
unit = input("Informe a Unidade Consumidora: ")
limit = input("Informe o Valor Limite do kW/h: ")
print("")
print("---------------------------------------")
print("Unidade e limite cadastrado com sucesso")
print("---------------------------------------")
print("")

#url='http://localhost:5000/limit'
url='http://35.211.13.184/limit'
json={"consumer_unity":unit, "limit":limit}

requests.post(url,json=json)
