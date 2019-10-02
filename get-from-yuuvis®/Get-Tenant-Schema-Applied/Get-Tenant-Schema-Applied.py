import requests

key = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/schema/native'), headers=header_dict)
print(response.text)
