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


gotify_server_url = "https://gotify.***.de"
gotify_api_token = "***"

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


# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Gotify-Win-Client")

# Main Body vom Fenster
label = tk.Label(fenster, text="Bei Klicken des Buttons werden Die Daten abgerufen.")
label.pack(pady=10)

# Button erstellen und in das Fenster platzieren
button = tk.Button(fenster, text="Klick mich!", command=button_click)
button.pack(pady=20)


ausgabe_label = tk.Label(text="Ausgabe:")
ausgabe_label.pack()

ausgabe_label = tk.Label(text=messages)
ausgabe_label.pack()

# Hauptfenster starten
fenster.mainloop()
