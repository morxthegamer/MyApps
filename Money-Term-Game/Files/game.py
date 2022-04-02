from jobs import Jobs
from money import MoneyManagement
from shops import Shops

class Game:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company
        self.jobs = Jobs()
        self.shops = Shops()
        self.money = MoneyManagement()

    def profile(self):
        profile = {
            "Name": self.name,
            "Age": self.age,
            "Company": self.company
        }

        return (
            f"""
            Name: {profile["Name"]}
            Age: {profile["Age"]}
            Your Company: {profile["Company"]}
            """
        )

    def work(self):
        self.jobs.work()

    def spend(self):
        self.shops.spend()