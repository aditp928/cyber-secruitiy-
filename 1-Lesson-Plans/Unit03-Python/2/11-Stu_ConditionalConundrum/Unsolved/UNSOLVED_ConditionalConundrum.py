# Part 1: Prints?  
pairs = 5
if (2 * pairs > 10):
    print("Too many shoes!")
else:
    print("Not enough shoes!")

# =====================================

# Part 2: Prints? 
policy_length = 10
if (len("p4ssw0rd") < policy_length):
    print("Insecure Password :(")
else:
    print("Secure(ish) Password :)")

# =====================================

# Part 3: Prints?
x = 2
y = 5
if ((x**3 >= y) and (y**2 < 26)):
    print("The math holds up!")
else:
    print("Those values don't meet these condition.")

# =====================================

# Part 4: Prints?
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if (name in group_one):
    print(name + " is in the first group")
elif (name in group_two):
    print(name + " is in group two")
elif (name in group_three):
    print(name + " is in group three")
else:
    print(name + " does not have a group. Poor " + name)

# =====================================

# Part 5: Prints?
height = 66
age = 16
adult_permission = True

if ((height > 70) and (age >= 18)):
    print("Can ride all the roller coasters")
elif ((height > 65) and (age >= 18)):
    print("Can ride moderate roller coasters")
elif ((height > 60) and (age >= 18)):
    print("Can ride light roller coasters")
elif (((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50))):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
