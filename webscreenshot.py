import requests 

url = "http://perdu.com"

with open('img.jpg', 'wb') as f:
    f.write(requests.get('https://api.apiflash.com/v1/urltoimage?access_key=461580a111f046fdb8bee468e6787818&url='+url).content)