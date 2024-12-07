# On the first line of the input, you will be given a text string. You must extract the information about the food and calculate the total calories.
# First, you must extract the food info. It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace
# •	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
# •	The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.
# Input / Constraints
# •	You will receive a single string
# Output
# •	First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# •	The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"


import re


def calculate_days(total_calories):
    return total_calories // 2000


def extract_food_info(text):
    pattern = r'([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
    matches = re.finditer(pattern, text)

    total_calories = 0
    food_items = []

    for match in matches:
        item_name = match.group(2)
        expiration_date = match.group(3)
        calories = int(match.group(4))

        food_items.append({
            'name': item_name,
            'date': expiration_date,
            'calories': calories
        })

        total_calories += calories

    return food_items, total_calories


def main():
    text = input()
    food_items, total_calories = extract_food_info(text)
    days = calculate_days(total_calories)

    print(f"You have food to last you for: {days} days!")

    for item in food_items:
        print(f"Item: {item['name']}, Best before: {item['date']}, Nutrition: {item['calories']}")


main()
