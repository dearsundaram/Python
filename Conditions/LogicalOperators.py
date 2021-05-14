### NOT ###
print("NOT OPERATOR DEMO")
a = 10
if not a > 1:
    print ("It worked")
else:
    print ("It did not worked")


### AND ###
print ("AND OPERATOR DEMO")
a = 10
b = 20
if (a < b and a < 1):
    print ("a is less than b and a is greater than 1")
elif (a < b and a < 11):
    print("a is less than b and is less than 11")
else:
    print("and operation did not worked")

### NOT + AND is NAND ###
print ("NAND OPERATOR DEMO")
a = 10
b = 20
if (a < b and a < 1):
    print ("a is less than b and a is greater than 1")
elif not(a < b and a < 11):
    print("a is less than b and is less than 11")
else:
    print("NAND operator worked")


### OR ###
print ("OR OPERATOR DEMO")
a = 10
b = 20
if (a < b or b>100):
    print ("a is less than b or b is greater than 100")

else:
    print("NOT operator did not worked")



### NOT + OR is NOR ###
print ("NOR OPERATOR DEMO")
a = 10
b = 20
if not(a < b or a < 1):
    print ("a is less than b and a is than 1")

else:
    print("NOR operator worked")
