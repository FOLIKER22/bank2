import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash__password(password)

    @staticmethod
    def __hash__password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.__password == self.__hash__password(password)
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.__password 
            }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(data["username"], "temp")
        user.__password = data["password"]
        return user
    
class Account:
    bank_name = "Monobank"
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("❌ Недостатньо коштів")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance
    
    def calculate_interest(self):
        return 0
    
    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "owner": self.owner,
            "balance": self._balance
        }
    
    @classmethod
    def from_dict(cls, data):
        if data["type"] == "SavingsAccount":
            return SavingsAccount(data["owner"], data['balance'])
        return Account(data["owner"], data['balance'])
    
    def __str__(self):
        return f"{self.owner} Balance: {self._balance} hrn"
    
class SavingsAccount(Account):
    
    def calculate_interest(self):
        return self._balance * 0.05
    


        
        
    
    