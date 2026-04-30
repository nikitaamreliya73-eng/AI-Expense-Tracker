<<<<<<< HEAD
class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
=======
class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | ₹{self.amount} | {self.description}"
>>>>>>> cf4a782663c4ad0b009758a3bb656d3c6ff35356
