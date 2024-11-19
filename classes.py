from dataclasses import dataclass

@dataclass
class BankAccount:
  customer_name: str = ""
  balance: float = 0.0
  account_number: int|float = 0

  def __init__(self, customer_name, balance, account_number) -> None:
    self.customer_name = customer_name
    self.balance = balance
    self.account_number = account_number
    print("Bank Account constructor called, values initialized")

  def __str__(self) -> str:
    return (f''
            f'customer name: {self.customer_name}, \n'
            f'balance: {self.balance}, \n'
            f'account number: {self.account_number}\n'
    )


surya : BankAccount = BankAccount("Surya", 100, 1234)
print(surya)


