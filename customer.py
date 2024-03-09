class Customer:

    def __init__(self, name, passkey):
        self.name = name
        self.passkey = passkey
    
    def __str__(self):
        return f"{self.name} - {self.passkey}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name
    
    @property
    def passkey(self):
        return self._passkey

    @passkey.setter
    def passkey(self, passkey):
        if not passkey:
            raise ValueError("Invalid Passkey")
        self._passkey = passkey