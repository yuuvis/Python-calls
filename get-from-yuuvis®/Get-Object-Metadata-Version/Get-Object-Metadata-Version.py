import requests

key = ""
object_id = ""
version_nr = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/dms/objects/'+object_id+'/versions/'+version_nr), headers=header_dict)
print(response.text)
