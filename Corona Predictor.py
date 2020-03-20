program_running = True
program2_running = False
daily_cases = []
daily_delta = []
while program_running:
    print('Please enter the current cases for the last three days(in ascending order), hit enter after each input')
    case = int(input())
    daily_cases.append(case)
    if len(daily_cases) == 3:
        program2_running = True
        program_running = False # end when 3 inputs are given
for i in range(2):
    daily_delta.append(1 + ((daily_cases[i+1] - daily_cases[i]) / int(daily_cases[i]))) # calculate rate of growth
average_delta = (daily_delta[0] + daily_delta[1]) / 2
day_x = daily_cases[2]
while program2_running:
    print('How many days ahead would you like a prediction for?')
    days_ahead = int(input())
    day_x = day_x * (average_delta ** days_ahead)
    print(f'In {days_ahead} days, there will be an approximate {int(day_x)} cases in your country.')
    day_x = daily_cases[2]