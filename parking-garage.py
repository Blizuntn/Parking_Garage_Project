# Create Garage Class
class Garage:
    def __init__(self, parking_spaces, tickets):
        self.parking_spaces = parking_spaces
        self.tickets = tickets
        
Garage(100, 100)


# Create Ticket Class and inherit Garage Class attributes
class Ticket(Garage):
    def __init__(self, id_number, paid, parking_spaces, tickets):
        super().__init__(parking_spaces, tickets)
        self.id_number = id_number
        self.paid = paid
        
# List Available Ticket Id's
available_ticket_id_numbers = [num for num in range(1, 101)]

# Track issued ticket id's and payment
issued_tickets = {"id_number": [], "paid": []}

# Start with 100 tickets and spaces in garage
tickets = 100
parking_spaces = 100

# Function for driver taking a ticket
def take_ticket():
    global tickets, parking_spaces, available_ticket_id_numbers, issued_tickets
    parking_spaces -= 1
    tickets -= 1
    
    current_ticket_id = 0
    
    # Loop through available id's for first available
    for each in available_ticket_id_numbers:
        if each != '_' and current_ticket_id == 0:
            current_ticket_id = each
    
    # Instantiate a ticket
    Ticket(current_ticket_id, False, parking_spaces, tickets)

    available_ticket_id_numbers[current_ticket_id - 1] = '_'
    issued_tickets["id_number"].append(current_ticket_id)
    issued_tickets["paid"].append(False)
    print(f"""
Available Ticket ID Numbers: {available_ticket_id_numbers}
""")
    print(f"""
Tickets Remaining: {tickets}
""")
    print(f"""
Parking Spaces Remaining: {parking_spaces}
""")

    print(f"""
Issued Tickets: {issued_tickets}
""")


def pay_ticket():

    global tickets, parking_spaces, available_ticket_id_numbers, issued_tickets, issued_tickets_list
    issued_tickets["id_number"].sort()
    print(f"""
Issued Tickets: {issued_tickets}
""")
    id_number_paying = int(input("What is your ticket id number? "))
    paid = False
    while paid == False:
        amount_paid = int(
            input("Your ticket costs $10. How much are you paying? "))
        if amount_paid > 10:
            print("""
Please take your change. You have 15 minutes to exit the parking garage.
""")
            paid = True
        elif amount_paid < 10:
            print("""
Please pay your remaining balance.""")
        else:
            print("""
Thank you for your payment. You have 15 minutes to exit the parking garage.""")
            paid = True
    tickets += 1
    parking_spaces += 1
    issued_tickets["paid"][id_number_paying - 1] = True
    print(f"""
Issued Tickets: {issued_tickets}""")
    paid_id_number = issued_tickets['id_number'][id_number_paying - 1]
    print(f"""
Paid id number: {paid_id_number}""")
    del issued_tickets["id_number"][paid_id_number-1]
    del issued_tickets['paid'][paid_id_number - 1]
    print(f"""
Issued Tickets: {issued_tickets}""")
    available_ticket_id_numbers[paid_id_number - 1] = paid_id_number
    print(f"""
Available Ticket ID Numbers: {available_ticket_id_numbers}""")


def control_panel():
    closed = False
    while closed == False:
        choice = input("""
    Hello! Welcome to Better Parking Garage!!!
    Select one of the following:
    To take a ticket, type 'take',
    To pay for a ticket, type 'pay,
    or if you are management, type 'close' to close the garage for the night: """).lower()
        if choice == 'take':
            take_ticket()
        elif choice == 'pay':
            pay_ticket()
        elif choice == 'close':
            closed = True
        else:
            print("That was not a valid response. Try again.")


control_panel()
