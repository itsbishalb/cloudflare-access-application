import http.client
import json
email = input("Enter account email: ")
account_key = input("Enter account ID key: ")
api_key = input("Enter API key: ")
applicationIDs = []

while True:
    applicationID = input("Enter Application ID or 'c' to continue: ")
    if str(applicationID).lower() == 'c' or str(applicationID) == '':
        break
    applicationIDs.append(applicationID)

for applicationID in applicationIDs:
    url = f"/client/v4/accounts/{account_key}/access/apps/{applicationID}"
    conn = http.client.HTTPSConnection("api.cloudflare.com")
    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json"
    }
    conn.request("DELETE", url, headers=headers)
    res = conn.getresponse()
    json_data = json.loads(res.read().decode())
    if json_data["success"]:
        print("\nApplication ID({}) Deleted \n".format(
            json_data["result"]["id"]))
    else:
        errors = json_data['errors']
        for error in errors:
            if 'message' in error:
                print("\n"+error['message']+"\n")

