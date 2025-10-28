# Movie Ticket Discount Program

# Get user input
try:
    age = int(input("Enter your age: "))
    ticket_price = float(input("Enter the ticket price: "))

    # Validate inputs
    if ticket_price < 0:
        print("INVALID TICKET PRICE")
    elif age < 0:
        print("INVALID AGE")
    else:
        # Determine discount category
        if age <= 12:
            discount_category = "Children"
            discount = 0.5
        elif age <= 17:
            discount_category = "Teenagers"
            discount = 0.25
        else:
            discount_category = "Adults"
            discount = 0.0

        # Calculate discounted price
        discounted_price = ticket_price - (ticket_price * discount)

        # Display output
        print("Category:", discount_category)
        print("Discounted Price: $", format(discounted_price, ".2f"))

except ValueError:
    print("INVALID INPUT — Please enter numeric values only.")
