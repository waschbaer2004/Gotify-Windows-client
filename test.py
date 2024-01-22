import tkinter as tk

def zeige_ausgabe():
    ausgabe_text = "Hallo, dies ist eine Ausgabe!"
    ausgabe_label.config(text=ausgabe_text)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Ausgabe-Fenster")

# Button erstellen, der die Ausgabe auslöst
button = tk.Button(root, text="Zeige Ausgabe", command=zeige_ausgabe)
button.pack(pady=10)

# Label erstellen, um die Ausgabe anzuzeigen
ausgabe_label = tk.Label(root, text="")
ausgabe_label.pack()

# Hauptloop starten
root.mainloop()


