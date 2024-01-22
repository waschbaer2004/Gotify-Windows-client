from datetime import datetime

# Die gegebene JSON-Zeichenkette als Python-Datenstruktur
data = {
    "paging": {
        "size": 2,
        "since": 0,
        "limit": 100
    },
    "messages": [
        {
            "id": 13,
            "appid": 1,
            "message": "```\nThis is a test of the notification target 'gotify'\n```",
            "title": "Test notification",
            "priority": 1,
            "extras": {
                "client::display": {
                    "contentType": "text/markdown"
                }
            },
            "date": "2024-01-22T14:58:38.322338868Z"
        },
        {
            "id": 12,
            "appid": 1,
            "message": "```\nThis is a test of the notification target 'gotify'\n```",
            "title": "Test notification",
            "priority": 1,
            "extras": {
                "client::display": {
                    "contentType": "text/markdown"
                }
            },
            "date": "2024-01-22T14:56:43.387051344Z"
        }
    ]
}

# Nachrichten nach Datum sortieren
sorted_messages = sorted(data["messages"], key=lambda x: x["date"])


print('tesssssttt')
for msg in sorted_messages:
    print(f"{msg['title'].replace('`', '')}")
    print(f"{msg['message'].replace('`', '')}")

    print('')
