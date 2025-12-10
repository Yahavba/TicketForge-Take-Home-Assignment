from rich.console import Console
from rich.panel import Panel
from tickets_manager.tickets_manager import (register, login, create_ticket,
                                             get_ticket, get_tickets,
                                             update_ticket)


console = Console()
status_options = {"In Progress": "in_progress",
                  "Review": "review", "Closed": "closed", "Open": "open"}


def cli_register(username, password):
    try:

        if register(username, password):
            console.print("[green]Registration completed successfully.[/]")
            return True
        else:
            console.print("[red]Registration failed.[/]")
            return False

    except Exception as e:
        console.print(f"[red]An error occurred during registration: {e}[/]")
        return False


def cli_login(username, password):
    try:

        if login(username, password):
            console.print("[green]Login completed successfully.[/]")
            return True
        else:
            console.print("[red]Login failed.[/]")
            return False

    except Exception as e:
        console.print(f"[red]An error occurred during login: {e}[/]")
        return False


def cli_create_ticket(username, password):
    try:
        title = console.input("[cyan]Enter title: [/]")
        description = console.input("[cyan]Enter description: [/]")
        depends_on = console.input(
            "[cyan]Enter depends on (ticket ID or leave blank): [/]")
        priority = console.input("[cyan]Enter priority: [/]")

        payload = {
            "title": title,
            "description": description,
            "customFields": {
                "priotiyu": priority},
            "stage": "open"
        }
        if depends_on:
            payload["dependsOn"] = depends_on

        ticket = create_ticket(username, password, payload)
        console.print(
            f"[green]Ticket created successfully: {ticket.get('ref')}[/]")
    except Exception as e:
        console.print(f"[red]An error occurred during ticket creation: {e}[/]")


def cli_get_ticket_by_id(username, password):
    try:
        ticket_id = console.input("[cyan]Enter ticket ID: [/]")
        ticket = get_ticket(username, password, ticket_id)
        console.print(ticket)
    except Exception as e:
        console.print(f"[red]An error occurred while fetching ticket: {e}[/]")


def cli_get_tickets(username, password):
    try:
        tickets = get_tickets(username, password)
        for ticket in tickets:
            console.print(ticket)
    except Exception as e:
        console.print(f"[red]An error occurred while fetching tickets: {e}[/]")


def cli_update_ticket(username, password):
    try:
        ticket_id = console.input("[cyan]Enter ticket ID: [/]")
        title = console.input("[cyan]Enter new title: [/]")
        description = console.input("[cyan]Enter new description: [/]")
        stage = console.input(
            "[cyan]Enter new stage (Open / In Progress / Review / Closed): [/]"
        )
        if stage not in status_options:
            console.print("[red]Invalid stage entered. Defaulting to Open.[/]")
            stage = "Open"
        depends_on = console.input(
            "[cyan]Enter depends on (ticket ID or leave blank): [/]")
        priority = console.input("[cyan]Enter new priority: [/]")
        payload = {
            "title": title,
            "description": description,
            "stage": status_options[stage],
            "customFields": {
                "priotiyu": priority
            }
        }
        if depends_on:
            payload["dependsOn"] = depends_on
        ticket = update_ticket(username, password, ticket_id, payload)
        console.print(
            f"[green]Ticket updated successfully: {ticket.get('ref')}[/]")
    except Exception as e:
        console.print(f"[red]An error occurred while updating ticket: {e}[/]")


def main():
    user_in_system = False

    while True:
        console.print(Panel("[bold magenta]TicketForge[/]"))
        console.print("[blue]1. Register[/]")
        console.print("[blue]2. Login[/]")
        console.print("[blue]3. Create Ticket[/]")
        console.print("[blue]4. Get Ticket by ID[/]")
        console.print("[blue]5. Get Tickets[/]")
        console.print("[blue]6. Update Ticket[/]")
        console.print("[blue]7. Exit[/]")

        choice = console.input("[cyan]Enter your choice: [/]")
        if choice == "1" or choice.lower() == "register":
            username = console.input("[cyan]Enter username: [/]")
            password = console.input("[cyan]Enter password: [/]")
            if cli_register(username, password):
                user_in_system = True

        elif choice == "2" or choice.lower() == "login":
            username = console.input("[cyan]Enter username: [/]")
            password = console.input("[cyan]Enter password: [/]")
            if cli_login(username, password):
                user_in_system = True

        elif choice == "3" or choice.lower() == "create ticket":
            if user_in_system:
                cli_create_ticket(username, password)
            else:
                console.print("[red]Please register or login first.[/]")

        elif choice == "4" or choice.lower() == "get ticket by id":
            if user_in_system:
                cli_get_ticket_by_id(username, password)
            else:
                console.print("[red]Please register or login first.[/]")

        elif choice == "5" or choice.lower() == "get tickets":
            if user_in_system:
                cli_get_tickets(username, password)
            else:
                console.print("[red]Please register or login first.[/]")

        elif choice == "6" or choice.lower() == "update ticket":
            if user_in_system:
                cli_update_ticket(username, password)
            else:
                console.print("[red]Please register or login first.[/]")

        elif choice == "7" or choice.lower() == "exit":
            console.print("[bold magenta]Goodbye![/]")
            break


if __name__ == "__main__":
    main()
