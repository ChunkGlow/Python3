test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 3, 'Coding' : 1}

print("The Original Dictionary is :" + str(test_dict))

K = 2
res = 0

for key in test_dict:
    if test_dict[key] == K:
        res += 1

print("Frequency of K in the Dictionary is : " + str(res))