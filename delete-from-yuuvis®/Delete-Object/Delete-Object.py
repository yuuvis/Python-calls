import requests

key = ""
object_id = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.delete(str(base_url+'/dms/objects/'+object_id), headers=header_dict)
print(response)
