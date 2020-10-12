import requests

key = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/admin'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/metrics'), headers=header_dict)
print(response.text)
