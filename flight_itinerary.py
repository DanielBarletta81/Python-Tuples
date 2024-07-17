#Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 

# # Each tuple contains information about a flight itinerary: 
# 
# (traveler_name, origin, destination). The function should format and return a string
#  that lists each itinerary.
# 
#  For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:

#"Itinerary 1: Alice - From New York to London
 #Itinerary 2: Bob - From Tokyo to San Francisco"

#Python function, list of tuples as an argument

itinerary_list = [("Daniel", "Boston", "San Jose"), ("Cal", "Providence", "Stockholm")]

client1, client2 = itinerary_list

def display_itineraries(first, second ):
   
    print(f'Itinerary 1 : {first[0]} is traveling from {first[1]} and will arrive in {first[2]}')
    print(f'Itinerary 2 : {second[0]} is traveling from {second[1]} and will arrive in {second[2]}')

display_itineraries(client1, client2)




""" def add_itinerary():
    customer = input("Enter the customer's name. ")
    origin = input("Where are they departing from? ")
    destination = input("What is the destination? ")

    itinerary_list.append((customer, origin, destination))
    print(f'{itinerary_list} Itinerary added to list.')

add_itinerary() """



