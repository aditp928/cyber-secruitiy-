# Dictionary full of info
my_info = {
    "name": "Sawyer",
    "occupation": "dog",
    "age": 4,
    "hobbies": ["walking", "eating", "sleeping", "loving my owner"],
    "wake-up": {
        "weekdays": 5,
        "weekends": 9
    }
}

# Print out results are stored in the dictionary
print("Hello I am " + my_info["name"] + " and I am a " + my_info["occupation"])
print("I have " + str(len(my_info["hobbies"])) + " hobbies!")
print("On the weekends I get up at " + str(my_info["wake-up"]["weekends"]))

# add and remove from the dictionary
print("-----")
del my_info["age"]
my_info["weapon"] = "puppy dog eyes"
print(my_info)

# equivalent using f-strings
print("-----")
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["weekends"]}')
