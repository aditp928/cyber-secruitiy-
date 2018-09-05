from create_user import collect_user_information, create_user

number_of_users = int(input("How many users do you want to create? "))
users = []

for _ in range(number_of_users):
    users.append(create_user(collect_user_information))
    print("---")
