
#       yearly commute means
# daily distance traveled 60,
# 2 is the distance from 2 sides.
# 1.609 converting distance from miles to km
# 5 is the weekly working days
# 52 are the weeks in an year





daily_travel = float(input('Enter the distance you travel dialy (Km): '))

no_days_in_week = float(input('How many days in week?: '))

yealy_commute = daily_travel*no_days_in_week*52

distance_to_moon = 383400*2

total_years = distance_to_moon/yealy_commute

rounded = round(total_years,2)
print(f'It will take you {rounded} years to go to moon and come back.')