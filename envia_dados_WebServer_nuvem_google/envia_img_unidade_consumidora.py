import requests

end='http://35.211.13.184/image_update'

unit = '?consumer_unit=Barra'
#unit = '?consumer_unit=Palhoça'
url = end + unit
files={'file': open('img.jpg','rb')}
#files={'file': open('img.png','rb')}

requests.post(url,files=files)

