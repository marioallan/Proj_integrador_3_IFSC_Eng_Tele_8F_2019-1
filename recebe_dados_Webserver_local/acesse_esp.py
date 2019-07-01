import requests

end='http://localhost:5000/check'
#end='http://35.211.13.184/check'

unit = '?consumer_unit=Barra'
#unit = '?consumer_unit=Palhoça'
url = end + unit

a = requests.get(url)
print(a)

#curl -X GET http://localhost:5000/check?consumer_unit=Barra
