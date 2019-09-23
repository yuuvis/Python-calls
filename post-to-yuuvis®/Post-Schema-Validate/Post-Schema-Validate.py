import requests

key = ""
#relative path to your schema files
schema_file_path = '/path/to/your/schema.xml'

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io'

header_dict['Content-Type'] = 'application/xml'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.post(str(base_url+'/admin/schema/validate'), data=open(schema_file_path, 'rb'), headers=header_dict)
print(response.json())
