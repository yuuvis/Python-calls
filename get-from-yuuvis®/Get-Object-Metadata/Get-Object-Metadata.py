import requests

key = ""
object_id = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Ocp-Apim-Subscription-Key'
header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/dms/objects/'+object_id), headers=header_dict)
print(response.text)
