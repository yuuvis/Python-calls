import requests

key = ""
object_id = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/objects/'+object_id+'/actions/validate/digest'), headers=header_dict)
print(response)
