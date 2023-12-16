# Every day you rent a car cost you $40. If you rent the car for 7 or more days, you get $50 off your total.
# If you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days rented.

# def rental_car(days):
#     if days >= 7:
#         return 40 * days - 50
#     elif days >= 3:
#         return 40 * days - 20
#     else:
#         return 40 * days

def rental_car(days):
    result = 40 * days
    if days >= 7:
        result -= 50
    elif days >= 3:
        result -= 20
    return result