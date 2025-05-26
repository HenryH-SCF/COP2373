# Henry Huitema
# This program sells exactly 20 cinema tickets. Each buyer can buy up to 4 tickets.
# The program prompts the user for a desired number of tickets and displays the remaining number of tickets
# after each sale, then repeats the process until 20 tickets have been sold. After 20 tickets are sold, the
# program displays the total number of buyers.

def sellTickets(remainingStock, purchasedTickets):
    # First check: Verify the user isn't attempting to purchase too many tickets
    if purchasedTickets >= 5:
        print("Too many tickets in one purchase!")
        return remainingStock
    # Second check: Verify user isn't attempting to purchase 0 tickets, or a negative amount of tickets
    if purchasedTickets <= 0:
        print("Invalid ticket amount!")
        return remainingStock
    # Third check: Verify user isn't attempting to purchase more tickets than are available
    else:
        if purchasedTickets > remainingStock:
            print(f"There are only {remainingStock} ticket(s) left!")
            return remainingStock
        else:
            # If all checks are passed, return number of tickets after a sale is made
            return remainingStock - purchasedTickets

def getInput():
    # Prompt user for input
    userInput = input("""How many tickets would you like to purchase? 
Note: Each buyer can purchase a maximum of four tickets. """)

    # Attempt to convert input into an integer and return it
    try:
        userInput = int(userInput)
        return userInput
    # Print a message and return a default value of 0 if conversion fails
    except:
        print("Failed to convert input into an integer!")
        return 0

def main():
    tickets = 20
    salesMade = 0
    # Use a while loop to continue attempting to sell tickets until no tickets are left
    while tickets > 0:
        ticketsAfterAttemptedSale = sellTickets(tickets, getInput())
        # If tickets after attempted sale is different from the ticket count at the start of the iteration,
        # increment salesMade and update the ticket total
        if ticketsAfterAttemptedSale != tickets:
            salesMade = salesMade + 1
            tickets = ticketsAfterAttemptedSale
            print(f"{tickets} ticket(s) remaining.")

    # Print the value of salesMade after the loop is finished.
    print(f"All twenty tickets were sold to {salesMade} different buyers.")

if __name__ == "__main__":
    main()
