class Category ():
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.avalaible = 0
        self.spent = 0
    
    def check_funds(self, amount):
        return amount <= self.avalaible
    
    def get_balance(self):
        return self.avalaible
    
    def deposit(self, amount, description = ''):
        if amount > 0:
            self.ledger.append({"amount": amount, "description": description})
            self.avalaible += amount

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.avalaible -= amount
            self.spent += amount
        return self.check_funds(amount)
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}") 
        return self.check_funds(amount)
    
    def __str__(self):
        title = self.name.center(30,'*')+'\n'
        movements = ''
        for operation in self.ledger:
            movement = operation['description']
            amount = "{:.7}".format("{:.2f}".format(operation['amount']))
            movement = "{:.23}".format(movement)
            spaces = ' ' * (30 - len(movement) - len(amount))
            movements += movement + spaces + amount + '\n'
        total = f'Total: {self.avalaible}'
        return title + movements + total
    
    def __repr__(self) -> str:
        return f'{self.__str__()}'

def create_spend_chart (categories):
    names = [category.name for category in categories] # Names of categories
    maxim = max([len(name) for name in names]) # Max lenght of the list of names
    total = sum([category.spent for category in categories]) # Total amount spent for all categories
    result = 'Percentage spent by category\n' # Title of the chart
    for i in range (10, -1, -1):
        markers = ['o' if round(category.spent / total * 10) >= i else ' ' for category in categories] # Markers of categories if category have spent at least that percentage
        number = ' '*(3 - len(str(i * 10))) + str(i * 10) # String of the number of percentage
        result += number + '| ' + '  '.join(markers) + '  \n'# String complete of the number + markers
    result += ' '*4 + '-' * (len(categories) * 3) + '-\n' #Line that separates percentages from categories
    # To represent the name of all categories in vertical style
    for i in range(maxim):
        letters = [name[i] if len(name)>i else ' ' for name in names]
        result += ' '*5 + '  '.join(letters) + '  '
        if i != maxim - 1:
            result += '\n'
    return result


        

food = Category("Food")
# print(create_spend_chart([food, clothing, auto]))
entertainment = Category("Entertainment")
business = Category("Buinsess")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(create_spend_chart([business, food,entertainment]))