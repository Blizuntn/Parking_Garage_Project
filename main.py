class ParkingGarage:

    def __init__(self) -> None:
        self.tickets = [100]
        self.parking_spaces = [100]
        self.current_ticket = {}
        self.price = 10.0

    def takeTicket(self):
        self.tickets[0] -= 1
        self.parking_spaces[0] -= 1

    def payForParking(self):
        payment = float(input("How much do you want to pay? "))
        if payment != 0 and payment == self.price:
            self.current_ticket["paid"] = True
            self.takeTicket()
            print("Your ticket has been paid and you 15 min to leave")
        elif payment > self.price:
            self.current_ticket["paid"] = True
            change = payment - self.price
            print(f"Thank you so much for your payment, here is your ${change} in change.\n"
                  f"Your ticket has been paid and you have 15 min to leave")
            self.takeTicket()
        else:
            self.current_ticket["paid"] = False

    def leaveGarage(self):
        if self.current_ticket["paid"] == True:
            print("Thank You, have a nice day.")
        else:
            while self.current_ticket["paid"] != True:

                payment = float(input(f"Im sorry, but in order to leave the garage can you please pay ${self.price}.\n"
                                      f"How much can you pay? "))
                if payment == self.price:
                    self.current_ticket["paid"] = True
                    self.tickets[0] += 1
                    self.parking_spaces[0] += 1
                    print("Thank you have nice day.")
                elif payment > self.price:
                    change = payment - self.price
                    print(f"Thank you so much for your payment, here is your ${change} in change.")
                    self.current_ticket["paid"] = True
                    self.tickets[0] += 1
                    self.parking_spaces[0] += 1
                    print("Thank you again, and have a good day.")


parking1 = ParkingGarage()
parking1.payForParking()
parking1.leaveGarage()