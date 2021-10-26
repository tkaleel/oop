# #print integers from 1-150
# y = 1
# while y <= 150:
#     print(y)
#     y = y+1

# #print multiples of 5 from 5-1,000
# y = 5
# while y <= 1000:
#     print(y)
#     y = y+5

# #print 1-100; if divisible by 5 print "Coding"; if divisible by 10 print "Coding Dojo"
# y = 1
# while y<=100:
#     if y%10==0:
#         print("Coding Dojo")
#     elif y%5==0:
#         print("Coding")
#     else:
#         print(y)
#     y=y+1

# #add odd integers from 0 to 500,000, print sum
# y=0
# sum=0
# while y<=500000:
#     if y%2!=0:
#         sum=sum+y
#     y=y+1
# print(sum)

# #countdown from 2018 by intervals of 4
# y=2018
# while y>0:
#     print(y)
#     y=y-4

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult
lowNum=2
highNum=9
mult=3

while lowNum<=highNum:
    if lowNum%mult==0:
        print(lowNum)
    lowNum=lowNum+1