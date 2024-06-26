#Question 3 task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 
93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print(second_week)


#Question 3 task 2
# over_100 = temperatures[-7:-1] not sure why this does not work here. I thought
# that "-1" when slicing referred to the last item in a list, but for some reason -7 and -1 are leaving out the last number, 106.

count = len(temperatures)
print(count)

over_100 = temperatures[23:]
print(over_100)