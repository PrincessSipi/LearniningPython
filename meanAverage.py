"""
The mean average of even numbers will be defined as the
sum of the even numbers divided by the count of the even numbers,
so we keep track of both sum and count
we iterate through each number in the array and if we encounter
an even number we modify the sum and the count
"""
def mean_average(array):
    sum = 0.0
    count = 0
    for number in len(array):
        if number % 2 == 0:
            sum += number
            ++count_of_even_numbers
    return sum / count

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(mean_average(l))

for i in range(20):
    print(mean_average(i))

# fix this code it doesntt work
