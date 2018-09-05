from create_user import collect_user_information, create_user

number_of_users = int(input("How many users do you want to create? "))
users = []

for _ in range(number_of_users):
    user_data = collect_user_information()
    user = create_user(user_data)
    users.append(user)
    print("---")

print(users)