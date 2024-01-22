from pickle import FALSE


x=2
print (x==2)
print(x==3)
print (x<3)
#
name = 'john'
age = 23
if name == 'john'and age == 23:
    print('your name is john and your age 23 years ')
if name == 'john' or name =='Rock':
    print (' your are john are you are rick ')
if name in ['john','rick']:
    print (' your are john are you are rick')


###############################
statment = False
another_statment = True
if statment is True :
    pass
elif another_statment is True:
    pass
else:
    pass
####################################################
x = 2
if x== 2:
    print (" x equal to two ")
else:
    print (" x didn't equal to two. ")
##################################################
x = [1,2,3]
y = [1,2,3]
print (x==y)
print (x is y)
####################################################
print (not False)
print ((not False)==(False))