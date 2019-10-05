#fOUR DIFFERENT STAR(*) PYRAMIDS
#use of for loop in different ways:
for g in range (6):  #way 1  loop end at 6
    print(g * ' ' + (6-g) * '*')
for g in range (7,0,-1): #way 2 where -1 is delimiter
    print((7-g) * '*'+g * ' ' )
print(" ")
for g in range (6,0,-1): 
    print(g * '*'+(6-g) * ' ' )
for g in range(0,7):   #loop end at 6
     print((6-g) * " "+ g* "*")