"""

Write a program that predicts the approximate size of a population of organisms.
The application should prompt the user to enter the starting number of organisms, 
the average daily population increase (as a percentage), 
and the number of days the organisms will be left to multiply. 
For example, assume the user enters the following values:
Starting number of organisms: 2 
Average daily increase: 30%
Number of days to multiply: 10
The program should display the following table of data:

| Day | Approximate Population
|---|---|
| 1 | 2 |
| 2 | 2.6 |
| 3 | 3.38 |
| 4 | 4.394 |
| 5 | 5.7122 |
| 6 | 7.42586 |
| 7 | 9.653619 |
| 8 | 12.5497 |
| 9 | 16.31462 |
| 10 | 21.209 |

"""

organism_input: str = input('Starting number of organisms: ')
while not organism_input.isdigit() or int(organism_input) < 1:
    print('Please enter a positive number!')
    organism_input = input('Starting number of organisms: ')

start_num_organisms: int = int(organism_input)

increase_input: str = input('Average daily increase (as a percentage): ')
while not increase_input.isdigit() or int(increase_input) < 0:
    print('Please enter zero or a positive number!')
    increase_input = input('Average daily increase (as a percentage): ')

daily_increase: float = 1 + int(increase_input) / 100

days_input: str = input('Number of days to multiply: ')
while not days_input.isdigit() or int(days_input) < 1:
    print('Please enter a positive number!')
    days_input = input('Number of days to multiply: ')

num_days: int = int(days_input)
population: float = start_num_organisms

print('Day Approximate Population')
for day_num in range(1, num_days + 1):
    print(day_num, population)
    population *= daily_increase

print('Christian Ramirez-Flores')