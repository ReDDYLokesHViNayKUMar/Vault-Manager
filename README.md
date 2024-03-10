# Vault-Manager

A CLI tool to manage Vault Boxes

[Video Demo](https://youtu.be/rIduEqqZKu0)

---

## Folder Contents

- **project.py**: This is the file which contains my `main` function and the other necessary functions to implement the program.
- **vault.py** : This file contains the `Vault` class functions that can be used to perform different actions and manage the vault.
- **customer.py**: This file contains the `Customer` class functions.
- **requirements.txt**: All `pip`-installable libraries that were used for this project.
- **test_project.py**: This file contains my test functions for project.py.

---

## Libraries Used

- `rich` : For generating Rich and Beautiful Text in the Terminal
- `pytest` : For Functional Testing

---

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the packages `rich` and `pytest`

To install Rich, type

```
$ pip install rich
```

To have a quick summary of Rich’s functionalities, type

```
$ python -m rich
```

To install Pytest, type

```
$ pip install pytest
```

- By default, we initialize the Vault with `VAULT_IDENTIFIER` as `VK`, `VAULT_ROWS` as`2` and `VAULT_SLOTS_PER_ROW` as `3`.
- Upon executing the program, you would be displayed with a list of helper commands and then prompted to Enter any command from the list.
- The helper commands would help the user to organize and manage the Vault.

---

## Documentation

### project.py Functions (excluding main)

```python
def get_commands_list():
```

**Description:**

- Returns a list of helper commands to manage the Vault.

**Returns:**

- `list`: returns a list of dictionary, which contains `command` and `description` information

```python
def display_commands():
```

**Description:**

- Prints out the helper commands in text rich format

```python
def get_input_command():
```

**Description:**

- Asks user for input command and return an `str`

**Returns:**

- `str`: returns a `str`

```python
def input_box_id():
```

**Description:**

- Asks user for input `box_id` and return an `str`

**Returns:**

- `str`: returns a `str` (i.e. The input `box_id`)

```python
def view_all():
```

**Description:**

- Prints Vault in text rich format

```python
def view_by_id(box_id):
```

**Description:**

- Prints the corresponding Box Details in text rich format

**Args:**

- `box_id` (`str`): Box ID of the Customer

```python
def close_deposit_box(box_id):
```

**Description:**

- Closes the Deposit Box associated to the entered Box ID

**Args:**

- `box_id` (`str`): Box ID of the Customer

**Returns:**

- `str`: return `str`(i.e. the closed Box ID) if conditions are met, else return `None`

```python
def open_deposit_box():
```

**Description:**

- Opens an Deposit Box in the Vault

**Returns:**

- `str`: return `str`(i.e. the assigned/created Box ID)

```python
def update_passkey(box_id):
```

**Description:**

- Updates the Pass-Key of the Deposit Box associated to the entered Box ID

**Args:**

- `box_id` (`str`): Box ID of the Customer

**Returns:**

- `str`: return `str`(i.e. the updated Box ID) if conditions are met, else return `None`

```python
def get_all_box_ids():
```

**Description:**

- Opens an Deposit Box in the Vault

**Returns:**

- `list`: return `list`(i.e. the list of all Box ID's available in the Vault)

---

## Usage

Use [python](https://www.python.org/) to run the application

````

$ python project.py

```

Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application

```

$ pytest test_project.py

```

---

## Commands List

```

open - Open Deposit Box
close - Close Deposit Box
view - View Specific Box
view-all - View All Boxes
update-passkey - Update Passkey for Specific Box
help - Display all Commands
quit - Quit

```

```
````
