import requests

def get_gotify_messages(server_url, api_token):
    url = f"{server_url}/message"
    headers = {"X-Gotify-Key": api_token}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Wirft eine Ausnahme für fehlgeschlagene Anfragen
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Fehler: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Verbindungsfehler: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Fehler: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Allgemeiner Fehler: {err}")
    return None

gotify_server_url = "https://gotify.******.de"
gotify_api_token = "******"

messages = get_gotify_messages(gotify_server_url, gotify_api_token)

if messages:
    print (messages)
    print("Empfangene Nachrichten:")
    for message in messages:
        print(message)