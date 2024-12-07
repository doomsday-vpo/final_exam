def process_message():
    message = input()

    while True:
        command = input()
        if command == "Decode":
            break

        action = command.split("|")

        if action[0] == "Move":
            num_letters = int(action[1])
            message = message[num_letters:] + message[:num_letters]

        elif action[0] == "Insert":
            index = int(action[1])
            value = action[2]
            message = message[:index] + value + message[index:]

        elif action[0] == "ChangeAll":
            substring = action[1]
            replacement = action[2]
            message = message.replace(substring, replacement)

    print(f"The decrypted message is: {message}")


process_message()
