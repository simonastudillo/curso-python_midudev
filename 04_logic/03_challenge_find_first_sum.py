"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
#Mi función
def find_first_sum(nums, goal):
  indices = None
  for index, i in enumerate(nums):
    for j in range(index+1, len(nums)):
      if i + nums[j] == goal:
        return [index, j]
  return indices

# Función midu
def find_first(nums, goal):
  for i in range(len(nums)):
    for j in range( i+1, len(nums)):
      if nums[i] + nums[j] == goal:
        return [i, j]
  return None

def find_with_dict(nums, goal):
  seen = {} # guardar los índices ya visitados
  for index, value in enumerate(nums):
    missing = goal - value
    if missing in seen:
      return [seen[missing], index]
    seen[index] = value
  return None


nums = [4, 5, 6, 3, 5, 4]
goal = 8

print(find_first_sum(nums, goal))
print(find_first(nums, goal))
print(find_with_dict(nums, goal))