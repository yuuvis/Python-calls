import requests

key = ""
#relative path to your content file
content_file_path = '/path/to/your/content.pdf'
#relative path to your metadata file
metadata_file_path = '/path/to/your/metadata.json'

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key


multipart_form_data = {
    'data' :('data.json', open(metadata_file_path, 'rb'), 'application/json'),
    'cid_63apple' : ('content.pdf', open(content_file_path, 'rb'), 'application/pdf')
}

response = requests.post(str(base_url+'/objects'), files=multipart_form_data, headers=header_dict)
print(response.json())
