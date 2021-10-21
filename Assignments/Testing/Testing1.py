user_values = [2, 5, 7, 3]
max_value = user_values[0]
for i in range(len(user_values)):
    if user_values[i] >= max_value:
        max_value = user_values[i]
        print(max_value)