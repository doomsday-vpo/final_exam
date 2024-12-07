# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# •	JavaScript: you will receive a list of strings
# •	An index is valid if it is between the first and the last element index (inclusive) in the sequence.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description

def world_tour(stops):
    while True:
        command = input()

        if command == "Travel":
            break

        tokens = command.split(":")
        action = tokens[0]

        if action == "Add Stop":
            index = int(tokens[1])
            string = tokens[2]

            if 0 <= index < len(stops):
                stops = stops[:index] + string + stops[index:]

        elif action == "Remove Stop":
            start_index = int(tokens[1])
            end_index = int(tokens[2])

            if 0 <= start_index <= end_index < len(stops):
                stops = stops[:start_index] + stops[end_index + 1:]

        elif action == "Switch":
            old_string = tokens[1]
            new_string = tokens[2]

            if old_string in stops:
                stops = stops.replace(old_string, new_string)

        print(stops)

    print(f"Ready for world tour! Planned stops: {stops}")


# Main program
initial_stops = input()
world_tour(initial_stops)
