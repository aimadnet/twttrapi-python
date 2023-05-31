from twttrapi import TwttrAPIClient
from getpass import getpass

api_key = "your_rapidapi_key_here"
client = TwttrAPIClient(api_key)

username = input("Username/Email: ")
password = getpass()

r = client.login_email_username(username, password)

if "success" in r and r["success"] == True:
    print("Session: " + r["session"])

else:
    if "errors" in r:
        print("Error: " + r["errors"][0]["message"])

    elif "login_data" in r:
        while True:
            login_data = r["login_data"]
            resp = getpass(r["message"] + ": ")

            r = client.login_2fa(login_data, resp)

            if "login_data" in r:
                pass
            
            elif r["success"] == True:
                print("Session: " + r["session"])
                break

            else:
                print("Error: " + r["error"])
                break

    else:
        print("Error: Can't login.")

    