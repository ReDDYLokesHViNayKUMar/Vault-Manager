from rich.console import Console
from vault import Vault

console = Console()
VAULT_IDENTIFIER, VAULT_ROWS, VAULT_SLOTS_PER_ROW = ('VK', 2, 3)
vault = Vault(VAULT_IDENTIFIER, VAULT_ROWS, VAULT_SLOTS_PER_ROW)

def main():
    console.print("\n[bold yellow]*** Vault Manager ***[/]")
    display_commands()
    execute = True
    
    while execute:
        command = get_input_command()

        if command == "open":
            box_id = open_deposit_box()
            if box_id:
                console.print(f"[bold white]Assigned Box ID:[/] [bold cyan]{box_id}[/]")
        elif command == "close":
            box_id = input_box_id()
            if box_id:
                closed_box_id = close_deposit_box(box_id)
                if closed_box_id:
                    console.print(f"[bold white]Closed Box ID:[/] [bold cyan]{closed_box_id}[/]")
        elif command == "view":
            box_id = input_box_id()
            if box_id:
                view_by_id(box_id)
        elif command == "view-all":
            view_all()
        elif command == "update-passkey":
            box_id = input_box_id()
            if box_id:
                updated_box_id = update_passkey(box_id)
                if updated_box_id:
                    console.print(f"[bold white]Updated passkey for Box ID:[/] [bold cyan]{updated_box_id}[/]")
        elif command == "help":
            display_commands()
        else:
            execute = False

def get_commands_list():
    commands = [{"command": "open", "description": "Open Deposit Box"},
            {"command": "close", "description": "Close Deposit Box"},
            {"command": "view", "description": "View Specific Box"},
            {"command": "view-all", "description": "View All Boxes"},
            {"command": "update-passkey", "description": "Update Passkey for Specific Box"},
            {"command": "help", "description": "Display all Commands"},
            {"command": "quit", "description": "Quit"}]
    return commands

def display_commands():
    commands = get_commands_list()
    console.print("\n[bold yellow]Commands:[/]")
    for h in commands:
        console.print(f"[bold green]{h['command']}[/] - [bold white]{h['description']}[/]")   

def get_input_command():
    commands = get_commands_list()
    valid_commands = [c['command'] for c in commands]
    
    while True:    
        command = input("\nEnter command: ").strip().lower()
        if command in valid_commands:
            return command
        else:
            console.print("[bold red]Please enter valid command![/]")

def input_box_id():
    box_id = ''
    while not box_id:
        box_id = input("Enter Box ID: ").strip().upper()
        if box_id:
            if box_id in vault.get_booked_boxes():
                return box_id
            else:
                console.print("[bold red]Please re-check and enter Box ID[/]")
                box_id = ''
        else:
            console.print("[bold red]Box ID cannot be blank![/]")

def view_all():
    vault.display_vault()

def view_by_id(box_id):
    vault.display_vault_by_id(box_id)

def close_deposit_box(box_id):
    closed_box_id = vault.close_deposit_box(box_id)
    return closed_box_id

def open_deposit_box():
    box_id = vault.open_deposit_box()
    return box_id

def update_passkey(box_id):
    updated_box_id = vault.update_deposit_box_passkey(box_id)
    return updated_box_id

def get_all_box_ids():
    return vault.get_all_boxes()
    
if __name__ == "__main__":
    main()