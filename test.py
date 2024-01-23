import tkinter as tk

import requests
import tkinter as tk

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


gotify_server_url = "https://gotify.****.de"
gotify_api_token = "****"

messages = get_gotify_messages(gotify_server_url, gotify_api_token)




# Die gegebene JSON-Zeichenkette als Python-Datenstruktur
data = messages

# Nachrichten nach Datum sortieren
sorted_messages = sorted(data["messages"], key=lambda x: x["date"])



#print('')
#for msg in sorted_messages:
    #print(f"{msg['title'].replace('`', '')}")
    #print(f"{msg['message'].replace('`', '')}")
    #print('')
    # old coding for later reference...




def button_click():
    for msg in sorted_messages:
        print(f"{msg['title'].replace('`', '')}, {msg['message'].replace('`', '')}")



def button_clickvariable():
    result = ""
    for msg in sorted_messages:
        result += f"{msg['title'].replace('`', '')}, {msg['message'].replace('`', '')}\n"
    return result

print(button_clickvariable)

# Hauptfenster erstellen
def zeige_ausgabe():
    ausgabe_text = "Hallo, dies ist eine Ausgabe!"
    ausgabe_label.config(text=ausgabe_text)
    print("test")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Ausgabe-Fenster")

# Button erstellen, der die Ausgabe auslöst
button = tk.Button(root, text="Zeige Ausgabe", command=zeige_ausgabe)
button.pack(pady=10)


button = tk.Button(root, text="Gotify-Messages", command=button_clickvariable)
button.pack(pady=10)

# Label erstellen, um die Ausgabe anzuzeigen
ausgabe_label = tk.Label(root, text="")
ausgabe_label.pack()

# Hauptloop starten
root.mainloop()



