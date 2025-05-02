import array as arr

array1 = arr.array('i', [1, 3, 5, 7, 9, 3])

print("Original array:" +str(array1))

print("Number of occurrences of the number 3 in the said array:"+str(array1.count(3)))

array1.reverse()
print("Reverse the order of the items:")
print(str(array1))