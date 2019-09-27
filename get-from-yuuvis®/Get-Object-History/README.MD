## Meaning of action field values

### ValueDetail	                        Meaning
```
100	CREATE_METADATA	                Document without document file was created
101	CREATE_METADATA_WITH_CONTENT	Document including document file was created
201	DELETE_CONTENT	                Document file was deleted
300	UPDATE_METADATA	                Metadata has been updated
301	UPDATE_CONTENT	                Document file has been updated
302	UPDATE_METADATA_WITH_CONTENT	Index data and document file has been updated
400	GET_CONTENT	                    Document file was downloaded
401	GET_METADATA	                Index data was retrieved
402	GET_TEXT_RENDITION	            Text preview was downloaded
403	GET_PDF_RENDITION	            Document file was downloaded as PDF
404	GET_THUMBNAIL_RENDITION	        Thumbnail preview has been downloaded

```

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/history

## Request headers

| Header                    | Type   | Meaning                                                                                             |
|---------------------------|--------|-----------------------------------------------------------------------------------------------------|
| Ocp-Apim-Subscription-Key | String | Subscription key which provides access to the API. Found on the Subscriptions page of your account. |

[Documentation: Get an objects History entries](https://github.com/yuuvis/Documentation/wiki/Retrieve-history-entries)

[Try out the endpoint in our developer portal](https://ateamk8s.azurewebsites.net/Apis/Endpoints/yadb-api)
