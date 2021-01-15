voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# Retreive each dictionary in the list

# Option 1
for item in voting_data:
    print(item)

# Option 2
for i in range(len(voting_data)):
    print (voting_data[i])

# Retreive only the values of each dictionary
for item in voting_data:
    print(item.values())

for item in voting_data:
    for value in item.values():
        print(value)

# Retreive the key-value pairs of each dictionary
for item in voting_data:
    for key, value in item.items():
        print(key,value)

# Retreive only the county name from each dictionary
for item in voting_data:
    print(item['county']) 

# Print each county and registered voters 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Option 1
for county,voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# Option 2
for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,.2f} registered voters.")

# Print each county and registered voters from the voting_data
for item in voting_data:
    print(f"{item['county']} county has {item['registered_voters']:,} registered voters.")

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)