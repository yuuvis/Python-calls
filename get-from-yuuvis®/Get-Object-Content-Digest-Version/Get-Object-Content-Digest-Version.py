import requests

key = ""
object_id = ""
version_nr = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/objects/'+object_id+'/versions/'+version_nr+'/actions/validate/digest'), headers=header_dict)
print(response)
