import random


# prizes for winning numbers
def prizes(no_of_winning_numbers):
    winnings = {3: "£20", 4: "£40", 5: "100", 6: "£10000", 7: "£10000000"}
    return winnings[no_of_winning_numbers]


# players ticker of 7 selected unique numbers
def players_ticket(winning_ticket):
    lottery_ticket = []
    count = 0

    # User input repeats until 7 unique numbers are selected
    while True:
        while len(lottery_ticket) < 7:
            try:
                ticket_number = int(input("Enter a number between 1 and 49: "))

                if 1 <= ticket_number <= 49:
                    # Checks if number has previously been entered
                    if ticket_number not in lottery_ticket:
                        lottery_ticket.append(ticket_number)
                        # If the number selected matches the winning ticket, increase count
                        if ticket_number in winning_ticket:
                            count += 1
                    else:
                        print("Number already chosen. Try again: ")
                else:
                    print("Try again. Enter a number between 1 and 49: ")
            except ValueError:
                print("Try again. Number is not a valid lottery number between 1 and 49.")

        return count, lottery_ticket


def ticket_output_message(winning_ticket, no_of_winning_numbers, lottery_ticket):
    print(f"Winning numbers: {winning_ticket}\n"
          f"Your lottery numbers are: {lottery_ticket}")

    if no_of_winning_numbers >= 3:  # or if count in prizes
        print(f"You win {prizes(no_of_winning_numbers)} for {no_of_winning_numbers} matching numbers")
    else:
        print(f"Not a winner. You only had {no_of_winning_numbers} matching number(s).")


def run():
    # Random winning ticket with 7 unique numbers
    winning_ticket = random.sample(range(1, 50), 7)

    print(f"Winning numbers: {winning_ticket}")  # uncomment to test

    no_of_winning_numbers, lottery_ticket = players_ticket(winning_ticket)
    ticket_output_message(winning_ticket, no_of_winning_numbers, lottery_ticket)


run()
