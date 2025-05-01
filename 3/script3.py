SPCMContinent_code = {'North America ' : '1', 'Africa' : '2', 'Southern Europe' : '3', 'Northern Europe' : '4', 'Central & South America' : '5', 'Southeast Asia & Oceania' : '6', 'Northern Asia' : '7', 'Eastern Asia & Bangladesh' : '8', 'South Asia' : '9'}



a = int(input("Enter a Phone Code: "))

if a == 1:
    print("North America : +1")
elif a == 2:
    print("Africa : +2")
elif a == 3:
    print("Southern Europe : +3")
elif a == 4:
    print("Northern Europe  : +4")
elif a == 5:
    print("Central & South America  : +5")
elif a == 6:
    print("Southeast Asia & Oceania : +6")
elif a == 7:
    print("Northern Asia : +7")
elif a == 8:
    print("Eastern Asia & Bangladesh  : +8")
elif a == 9:
    print("South Asia : +9")
else:
    print("Invalid Phone Code ")