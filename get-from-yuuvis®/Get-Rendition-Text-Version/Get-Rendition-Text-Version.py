import requests

key = ""
object_id = ""
versionNr = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/dms/objects/'+object_id+'/versions/'+versionNr+'/contents/renditions/text'), headers=header_dict)
print(response.text)
