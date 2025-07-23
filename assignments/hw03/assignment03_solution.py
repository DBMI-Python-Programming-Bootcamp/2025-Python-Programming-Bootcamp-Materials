# Part 1 : set up a list of tuples
vacc_counties = [('Pulaski', 42.7),
                 ('Benton', 41.4),
                 ('Fulton', 22.1),
                 ('Miller', 9.6),
                 ('Mississippi', 29.4)]

# Add tuple
vacc_counties.append(('Scott', 28.1))

# Part 2 loop:
print("Starting part 2")
# Go through vacc_counties and print out a message for those counties that
# have a higher than 30% vaccination rate
for county_info in vacc_counties:
    name = county_info[0]
    num = county_info[1]
    if num > 30:
        print(f"{name} is doing ok, with a rate of: {num}")


# Part 3 loop:
# Print out a message for every county, but prints different messages if the rate is above or below 30
print("Starting part 3")
for county_info in vacc_counties:
    if county_info[1] > 30:
        print(f"{county_info[0]} is doing ok, with a rate of {county_info[1]}")
    else:
        print(f"{county_info[0]} is doing less ok, with a rate of {county_info[1]}")


# Bonus round
# To get the mean, we add all the values and then divide by the number of values
rate_sum = 0
for county_info in vacc_counties:
    rate_sum = rate_sum + county_info[1]
mean_rate = rate_sum / len(vacc_counties)
print(f"The mean vaccination rate across {len(vacc_counties)} is {mean_rate}")