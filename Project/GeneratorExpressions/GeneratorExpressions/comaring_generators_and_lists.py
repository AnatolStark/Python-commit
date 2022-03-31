import time

# print(sum([number for number in range(10)]))
#  45
# print(sum(number for number in range(10))) #  menshe nagruska
#  45

list_start_time = time.time()
print(sum([number for number in range(100000000)]))
list_processing_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum(number for number in range(100000000)))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')
#  4999999950000000
# Processing with list is 874.7480773925781
print(f'Processing with generator is {gen_processing_time}')
#  4999999950000000
#  Processing with generator is 30.290488481521606


