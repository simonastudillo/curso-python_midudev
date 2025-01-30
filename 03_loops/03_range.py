###
# 03 - range()
# Permite crear una secuencia de números
###

print("range()")

nums = range(5)

for num in nums:
  print(num)

nums = range(5, 10)
for num in nums:
  print(num)

nums = range(0, 10, 2)
for num in nums:
  print(num)

nums = range(-5, 0)
for num in nums:
  print(num)


nums = range(10, 0, -1)
for num in nums:
  print(num)

nums = range(10)
list_of_nums =  list(nums)
print(list_of_nums)

for _ in range(5):
  print("Hola Mundo")