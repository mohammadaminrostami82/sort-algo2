import random
import time
import matplotlib.pyplot as plt


# Given data
data = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

# Expected sorted list
expected_sorted_list = [
    {'First Name': 'Aahana', 'Last Name': 'Arora'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'}
]


# Sorts a list of dictionaries based on 'First Name' and 'Last Name'.
def custom_sort(data):
    sorted_data = sorted(data, key=lambda x: (x['First Name'], x['Last Name']))
    return sorted_data

# Testing the custom_sort function
print(custom_sort(data))

data_to_check = custom_sort(data)

# Check if the sorted list matches the expected result
if data_to_check == expected_sorted_list:
    print("The lists are equal.")
else:
    print("The lists are not equal.")

# Generates random data with the specified size.
def generate_random_data(size):
    first_names = ['Raj', 'Suraj', 'Karan', 'Jade', 'Kiran', 'Armaan', 'Jaya', 'Ingrid', 'Aahana', 'Kumar', 'Seth', 'Canary', 'Galore', 'Thakur']
    last_names = ['Nayyar', 'Sharma', 'Kumar', 'Canary', 'Thakur', 'Sharma', 'Kamla', 'Kumar', 'Sharma', 'Galore', 'Seth', 'Dadra', 'Maverick', 'Arora']

    data = [{'First Name': random.choice(first_names), 'Last Name': random.choice(last_names)} for _ in range(size)]
    return data

# model1= (generate_random_data(10))

# model2= (generate_random_data(500))

# model3= (generate_random_data(1000))

data_sizes = [10, 500, 1000]

# Record execution times for each data size
execution_times = []

for size in data_sizes:
    random_data = generate_random_data(size)
    start_time = time.time()
    custom_sort(random_data)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plot the results
plt.plot(data_sizes, execution_times, marker='o')
plt.xlabel('Data Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.grid(True)
plt.show()

# محمد امین رستمی / MohammadAmin Rostami