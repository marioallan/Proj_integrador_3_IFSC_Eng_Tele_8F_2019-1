import requests

end='http://localhost:5000/image_update'

unit = '?consumer_unit=Barra'
#unit = '?consumer_unit=Palhoça'
url = end + unit
files={'file': open('img.jpg','rb')}
#files={'file': open('img.png','rb')}

requests.post(url,files=files)

