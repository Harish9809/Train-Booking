import pandas as pd
import random

# Sample train data
train_data = {
    'Train': ['Shatabdi Express', 'Rajdhani Express', 'Garib Rath', 'Duronto Express'],
    'Sleeper Seats': [100, 150, 200, 120],
    'AC Seats': [50, 75, 60, 40],
    'Sleeper Price': [500, 700, 300, 600],
    'AC Price': [1200, 1500, 800, 1000]
}

# Creating the DataFrame
trains = pd.DataFrame(train_data)

# Function to check seat availability
def check_availability(train, class_type, num_seats):
    if train in trains['Train'].values:
        index = trains[trains['Train'] == train].index[0]
        if class_type == 'Sleeper':
            return trains.loc[index, 'Sleeper Seats'] >= num_seats
        elif class_type == 'AC':
            return trains.loc[index, 'AC Seats'] >= num_seats
    return False

# Function to generate a random PNR number
def generate_pnr():
    return "PNR" + str(random.randint(100000, 999999))

# Function to book tickets
def book_ticket(train, class_type, num_seats, passenger_name):
    if check_availability(train, class_type, num_seats):
        index = trains[trains['Train'] == train].index[0]
        if class_type == 'Sleeper':
            price_per_ticket = trains.loc[index, 'Sleeper Price']
            trains.loc[index, 'Sleeper Seats'] -= num_seats
        elif class_type == 'AC':
            price_per_ticket = trains.loc[index, 'AC Price']
            trains.loc[index, 'AC Seats'] -= num_seats
        else:
            print("Invalid class type.")
            return None

        total_price = price_per_ticket * num_seats
        pnr = generate_pnr()
        print("\nBooking Successful!")
        print(f"Passenger: {passenger_name}")
        print(f"Train: {train}")
        print(f"Class: {class_type}")
        print(f"Seats: {num_seats}")
        print(f"Total Fare: ₹{total_price}")
        print(f"PNR Number: {pnr}")
        return pnr
    else:
        print("Booking Failed! Not enough seats available.")
        return None

# Function to display train details
def show_trains():
    print("\nAvailable Trains and Seat Details:")
    print(trains)

# Function to check PNR status (Mock Function)
def check_pnr_status(pnr):
    print(f"\nChecking PNR status for {pnr}...")
    print("Status: Confirmed")

# Main menu function
def main():
    while True:
        print("\nRailway Ticket Booking System")
        print("1. Show Available Trains")
        print("2. Check Seat Availability")
        print("3. Book Ticket")
        print("4. Check PNR Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_trains()
        elif choice == '2':
            train = input("Enter Train Name: ")
            class_type = input("Enter Class Type (Sleeper/AC): ")
            num_seats = int(input("Enter Number of Seats: "))
            if check_availability(train, class_type, num_seats):
                print("Seats are available!")
            else:
                print("Not enough seats available.")
        elif choice == '3':
            train = input("Enter Train Name: ")
            class_type = input("Enter Class Type (Sleeper/AC): ")
            num_seats = int(input("Enter Number of Seats: "))
            passenger_name = input("Enter Passenger Name: ")
            book_ticket(train, class_type, num_seats, passenger_name)
        elif choice == '4':
            pnr = input("Enter PNR Number: ")
            check_pnr_status(pnr)
        elif choice == '5':
            print("Thank you for using the Railway Ticket Booking System!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    main()
