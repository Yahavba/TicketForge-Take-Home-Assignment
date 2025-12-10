import requests
from config.consts import BASE_URL


def register(username, password):
    res = requests.post(f"{BASE_URL}/api/tforge/user/register",
                        json={
                            "username": username,
                            "password": password
                        })
    if (res.status_code == 200 or res.status_code == 201):
        return True
    else:
        raise Exception("Registration failed.")


def login(username, password):
    res = requests.get(f"{BASE_URL}/login", auth=(username, password))
    if (res.status_code == 200):
        return True
    else:
        raise Exception("Login failed.")


def create_ticket(username, password, payload):
    res = requests.post(f"{BASE_URL}/api/tforge/workitem/publish",
                        auth=(username, password),
                        json=payload)
    if res.status_code == 200:
        return res.json()['workitem']
    else:
        raise Exception("Failed to create ticket.")


def get_ticket(username, password, ticket_id):
    res = requests.get(f"{BASE_URL}/api/tforge/workitem/{ticket_id}",
                       auth=(username, password))
    if res.status_code == 200:
        ticket = res.json()
        return ticket
    else:
        raise Exception("Failed to get ticket.")


def get_tickets(username, password):

    res = requests.get(f"{BASE_URL}/api/tforge/workitems/mine",
                       auth=(username, password))
    if res.status_code == 200:
        tickets = res.json()
        return tickets["workitems"]
    else:
        raise Exception("Failed to get tickets.")


def update_ticket(username, password, ticket_id, payload):
    res = requests.put(f"{BASE_URL}/api/tforge/workitem/{ticket_id}",
                       auth=(username, password),
                       json=payload)
    if res.status_code == 200:
        return res.json()['workitem']
    else:
        raise Exception("Failed to update ticket.")
