# random number create between two number

# we use random module
import random
number1=int(input('ENTER THE LOWER NUMBER:'))
number2=int(input('ENTER THE UPPER NUMBER:'))
random_number=random.randint(number1,number2)

print('RANDOM NUMBER {} AND {} IS {} ' .format(number1,number2,random_number))
#thanks akhalakansari94@gmail.com