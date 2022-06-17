tickets = 100
available_ticket_id_numbers = [num for num in range(1, 101)]
parking_spaces = 100
issued_tickets = {"id_number": [], "paid": []}



def take_ticket():
    global tickets, parking_spaces, available_ticket_id_numbers

    tickets -= 1
    parking_spaces -= 1
    current_ticket_id = available_ticket_id_numbers.pop(0)
    issued_tickets["id_number"].append(current_ticket_id)
    issued_tickets["paid"].append(False)
    print(available_ticket_id_numbers)
    print(f"""
Tickets Remaining: {tickets}""")
    print(f"""
Parking Spaces Remaining: {parking_spaces}""")
    print(f"""
Next available ticket id number: {available_ticket_id_numbers[0]}
""")
    print(issued_tickets)


take_ticket()
take_ticket()


def pay_ticket():

    global tickets, parking_spaces, available_ticket_id_numbers

    id_number_paying = int(input("What is your ticket id number? "))
    paid = False
    while paid == False: 
        amount_paid = int(
            input("Your ticket costs $10. How much are you paying? "))
        if amount_paid > 10:
            print("Please take your change. You have 15 minutes to exit the parking garage.")
            paid = True
        elif amount_paid < 10:
            print("Please pay your remaining balance.")
        else:
            print("Thank you for your payment. You have 15 minutes to exit the parking garage.")
            paid = True
            
    issued_tickets["paid"][id_number_paying - 1] = True
    print(issued_tickets)
    paid_id_number = issued_tickets['id_number'][id_number_paying - 1]
    print(paid_id_number)

pay_ticket()
