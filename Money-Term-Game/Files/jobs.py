import random

class Jobs:
    def __init__(self):
        self.jobList = [
        "Lury's Clothes Store",
        "Jack's Car Dealership",
        "Dan's Applicances",
        "Keath's Web Services"
        ]
        self.formatJobList = (
        f"""
        1: {self.jobList[0]}
        2: {self.jobList[1]}
        3: {self.jobList[2]}
        4: {self.jobList[3]}
        """
        )
        self.cash = 0

    def work(self):
        option = input(f"Which company do you want to work for?:\n{self.formatJobList}\nEnter: ")

        if (option == "1"): self.workAtJob1()
        elif (option == "2"): self.workAtJob2()
        elif (option == "3"): self.workAtJob3()
        elif (option == "4"): self.workAtJob4()
        else:
            again = input("Invalid option. Please Try Again: y/n?\n")
            if ("y" in again or "yes" in again): self.work()
            elif ("n" in again or "no" in again): exit()

    def workAtJob1(self):
        clothes = {
            "Red Shirt": 1000,
            "Blue Shirt": 500,
            "Green Shirt": 800,
            "Ganzy": 200,
            "Line-Up Shirt": 2000,
            "Stripe Shirt": 10000
        }

        while (True):
            h = ["Red Shirt", "Blue Shirt", "Green Shirt", "Ganzy", "Line-Up Shirt", "Stripe Shirt"]
            i = random.choice(range(6))
            choice = h[i]
            
            sell = input(f"This person wants a {choice}. Do you want to sell it to them? (y/n): ")

            if (sell == "y" or sell == "yes"):
                self.cash += clothes[choice]
                self.writeMoney(self.cash)
                print(f"Sold! You just earned {str(clothes[choice])}!")
            else:
                print("Not Sold.")

    def workAtJob2(self):
        pass

    def workAtJob3(self):
        pass

    def workAtJob4(self):
        pass

    def writeMoney(self, money):
        with open("Data/money.yaml", "w") as g:
            g.write(f"[MONEY]: {money}")