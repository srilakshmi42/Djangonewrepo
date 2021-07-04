import requests
import json
def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "sender_id=TXTIND&message="+message+" &route=v3&numbers="+contactno
    headers = {
        'authorization': "1acLRDN3geuHwjq58oA4pBZ6U0SrWQbTyEIznMX2FfsdxtYlhKq8UgGaZsM9KDOvAW205hmdtoEl7nfB",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    dict_data=json.loads(response.text)

    return dict_data['return']