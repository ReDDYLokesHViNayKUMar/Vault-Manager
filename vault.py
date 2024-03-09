import random
import getpass
from customer import Customer
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

console = Console()

class Vault:

    def __init__(self, vault_id:str, rows:int, boxes_per_row:int):
        self.vault_id = vault_id
        self.rows = rows
        self.boxes_per_row = boxes_per_row
        self.vault = {}
        self.vault_arr = []
        for i in range(rows):
            row_arr= []
            for j in range(boxes_per_row):
                code = vault_id + "-" + str(i+1) + "-" + str(j+1)
                self.vault[code] = {'status': 0}
                row_arr.append(code)
            self.vault_arr.append(row_arr)    
        
    def __str__(self):
        return f"{self.vault}"

    def get_available_boxes(self):
        available_box_ids = []
        for k, v in self.vault.items():
            if v['status'] != 1 :
                available_box_ids.append(k)
        return available_box_ids
    
    def get_booked_boxes(self):
        booked_box_ids = []
        for k, v in self.vault.items():
            if v['status'] == 1 :
                booked_box_ids.append(k)
        return booked_box_ids
    
    def get_all_boxes(self):
        box_ids = []
        for k, v in self.vault.items():
            box_ids.append(k)
        return box_ids
    
    def get_boxes_count(self):
        total = len(self.vault)
        available_boxes = len(self.get_available_boxes())
        unavailable_boxes = total - available_boxes
        return f"Total Boxes: {total}\nAvailable Boxes: {available_boxes}\nBooked Boxes: {unavailable_boxes}"

    def open_deposit_box(self):
        available_box_ids = self.get_available_boxes()
        if len(available_box_ids) > 0:
            name = passkey = ''
            while not name:
                name = input("Enter name: ")

            while not passkey:
                passkey = getpass.getpass("Enter passkey: ")

            customer = Customer(name, passkey)
            available_box_ids = self.get_available_boxes()
            generated_id = random.choice(available_box_ids)
            if(generated_id in available_box_ids):
                self.vault[generated_id]['status'] = 1
                self.vault[generated_id]['name'] = customer.name
                self.vault[generated_id]['passkey'] = customer.passkey
                return generated_id
            else:
                console.print("[red][bold white]{generated_id}[/] is not available![/]")
        else:
            console.print("[bold green]Vault is FULL!![/]")
    
    def close_deposit_box(self, box_id):
        passkey = getpass.getpass("Enter passkey: ")
        if box_id not in self.get_available_boxes():
            if self.vault[box_id]['passkey'] == passkey:
                self.vault[box_id] = {'status': 0} # Reset Box
                return box_id 
            else:
                console.print("[bold red]Incorrect Passkey![/]")
        else:
            console.print(f"[red][bold white]{box_id}[/] not found in Vault![/]")
    
    def update_deposit_box_passkey(self, box_id):
        passkey = getpass.getpass("Enter current passkey: ")
        if box_id not in self.get_available_boxes():
            if self.vault[box_id]['passkey'] == passkey:
                new_passkey = getpass.getpass("Enter new passkey: ")
                if new_passkey:
                    self.vault[box_id]['passkey'] = new_passkey # Update Passkey
                    return box_id
                else:
                    console.print("New Passkey cannot be blank![/]") 
            else:
                console.print("[bold red]Incorrect Passkey![/]")
        else:
            console.print("[bold red][bold white]{box_id}[/] not found in Vault![/]")

    def get_content(self, box_id):
        box = self.vault[box_id]

        if(box['status'] == 1):
            return f"[b]{box_id}[/b]\n[b]{box['name']}[/b]\n[yellow]{'🔴'}"
        else:
            return f"[b]{box_id}[/b]\n{'🟢'}"

    def display_vault(self):
        for row in self.vault_arr:
            box_details = [Panel(self.get_content(box), expand=True) for box in row]
            console.print(Columns(box_details))
        console.print(self.get_boxes_count())

    def display_vault_by_id(self, box_id):
        if box_id in self.get_booked_boxes():
            console.print(f"\n[bold white]Box ID:[/] [bold cyan]{box_id}[/]\n[bold white]Name:[/] [bold cyan]{self.vault[box_id]['name']}[/]")
