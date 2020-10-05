TICKET_PRICE = 10
ANSWER_PURCHASE_TICKETS = "yes"

tickets_remaining = 100  

# Create calculate_price function.
def calculate_price(number_of_tickets):
    # Create a new constant for 2 dollar charge
    # Add service charge to what's due
    service_charge = 2
    return (number_of_tickets * TICKET_PRICE) + service_charge

# Run this code continuously until we run out of tickets
while tickets_remaining > 0:

    #Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))
    
    
    #Gather the user's name and assign it to a new variable
    name = input("Please enter your name:  ")
    
    # Prompt the user by name and ask how many tickets they would like
    # Expect a value error to happen
    try:
        number_of_tickets = int(input("Hello {}! How many tickets would you like to buy?   ".format(name)))
        # Raise a ValueError if number of tickets is for more than are available    
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining. Please enter a number equal to or less than the amount remaining".format(tickets_remaining))
    except ValueError as err:
        #Include an error text in the output
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:
    # Calculate the price (number of tickets * price) and assign to a variable
        total_cost = calculate_price(number_of_tickets)
    
    # Output the price to the screen
        print("The total cost for {} tickets is ${}.".format(number_of_tickets, total_cost))
        
        # Prompt user if they want to proceed. Y/N
        purchase_tickets = input("Would you like to proceed with the purchase of these tickets, {}? (Enter yes or no)  ".format(name)).lower()
        
        #If they want to proceed
            # print out to the screen "SOLD!" to confirm purchase 
            # and then decrement by the tickets remaining by the number of tickets puchased
            #TODO: Gather credit card information and process it.
            
        if purchase_tickets == ANSWER_PURCHASE_TICKETS:
            print("SOLD!")
            tickets_remaining -= number_of_tickets
            print("There are", tickets_remaining, "tickets left.")
        # Otherwise, thank them
        else:
            print("Thank you for coming, {}! Hope to see you again.".format(name))

# Notify that tickets have sold out
print("All tickets are now sold out.")
