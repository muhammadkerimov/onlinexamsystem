from django.test import TestCase

n = int(input('count: '))
my_list = []
max_salary = 0

for i in range(n):
    a, b = map(int, input().split())
    my_list.append((b, a))  # Using tuple for (salary, count)

my_list.sort(reverse=True)  # Sort in descending order by salary

for k in range(len(my_list)):
    salary_f = my_list[k][0] * my_list[k][1]
    max_salary += salary_f

    # Reduce the count by 1 for all elements
    my_list = [(salary, count - 1) for (salary, count) in my_list]

# Remove elements with count <= 0
my_list = [(salary, count) for (salary, count) in my_list if count > 0]

print(max_salary)
