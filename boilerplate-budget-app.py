class Category:
    category = str()
    funds = True
    balance = int()
    transactions = str()

    def __init__(self, category):
        self.category = str(category)
        self.ledger = list()

    def __str__(self):
        len_cat_name = int(len(self.category)/2)
        stars = '*' * (15 - len_cat_name)
        self.budget = str()

        self.budget = stars + self.category + stars + '\n' + self.transactions + 'Total: {}'.format(str(round(self.balance,2)))



        return self.budget

    def budget_update(self, description, amount):
        amount = str(round(amount, 2))
        amnt_len = len(str(amount))
        desc_len = len(description[:23])
        space = ' ' * (30 - desc_len - amnt_len )

        self.transactions = self.transactions + description[:23] + space + amount[:7] + '\n'

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.budget_update(description, amount)
        self.balance = self.balance + amount

    def withdraw(self, amount, description=''):
        amount = 0 - amount

        if self.balance + amount < 0:
            self.funds = False

        if self.funds is True:
            self.ledger.append({'amount': amount, 'description': description})
            self.budget_update(description, amount)
            self.balance = self.balance + amount
            withdraw = True
        else:
            withdraw = False

        return withdraw

    def get_balance(self):
        balance = str(self.balance)

        return balance

    def transfer(self, amount, budget):
        self.withdraw(amount, 'Transfer to {}.'.format(budget.category))
        budget.deposit(amount, 'Transfer from {}'.format(self.category))

    def check_funds(self, amount):
        founds_check = bool()
        founds = self.balance - amount
        if founds < 0:
            founds_check = False
        else:
            founds_check = True

        return founds_check

def create_spend_chart(categories):
    chart_plot = str()
    spend_category = list()
    spend_amount = list()
    percentage = list()
    scale = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    for category in categories:

        ledger = category.ledger
        amounts = list()
        negative = int()
        for transaction in ledger:
            amount = (transaction['amount'])
            if amount < 0:
                amounts.append(amount)

        for i in amounts:
            negative += i
        spend_category.append(category.category)
        spend_amount.append(negative)

    total_spent = int()
    for i in range(len(spend_category)):
        total_spent = total_spent + int(spend_amount[i])

    for t in range(len(spend_category)):
        percentage.append(int(round((spend_amount[t]/total_spent)*10)))
    chart_plot = 'Percentage spent by category \n'
    for num in scale:
        if num == 0:
            chart_plot = chart_plot + '  ' + str(num) + '| '
        elif num == 100:
            chart_plot = chart_plot + str(num) + '| '
        else:
            chart_plot = chart_plot + ' ' + str(num) + '| '

        for i in percentage:
            if (i * 10) >= num:
                chart_plot = chart_plot + 'o '
            else:
                chart_plot = chart_plot +'  '
        chart_plot = chart_plot + '\n'

    chart_plot = chart_plot + '    ' + '--' * int(len(spend_category)) + '-' + '\n'

    long = len(max(spend_category, key=len))
    for i in range(long):
        chart_plot = chart_plot + ' '*5
        for word in spend_category:

            if i >= len(word):
                chart_plot = chart_plot + ' ' + ' '
            else:
                chart_plot = chart_plot + word[i] + ' '
        chart_plot = chart_plot + '\n'

    return chart_plot




Food = Category('Food')
Sport = Category('Sport')
Other = Category('Other')

Food.deposit(1000, 'Transeferncia y otras cosas que tengo que poner para hacer')
Sport.deposit(1000)
Other.deposit(10)
Food.withdraw(160.512, 'Pizza')
Food.withdraw(50)
Sport.deposit(45)
Sport.withdraw(250, 'Shoes')
Sport.withdraw(50, 'Trousers')
Other.withdraw(650, 'Traveling')

print(Food)
print(Sport)
print(Other)
print(Other.balance)
print(Other.funds)
Lista = [Food, Sport, Other]
print(create_spend_chart(Lista))

