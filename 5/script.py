numbers1 = {10,20,30}
numbers2 = {40,50,60}

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  

###########################################################

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def sq(n):
    return n * n

squared = list(map(sq, nums))
print(squared) 
