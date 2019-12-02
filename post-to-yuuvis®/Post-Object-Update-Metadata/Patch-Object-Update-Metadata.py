import requests

key = ""
object_id = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key

#relative path to your new metadata file
new_metadata_file_path = '/path/to/your/new/metadata.json'

response = requests.patch(str(base_url+'/objects/'+object_id), data=open(new_metadata_file_path, 'rb'), headers=header_dict)
print(response.text)
