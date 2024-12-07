# Create a program that executes changes over a string. On the first line, you are going to receive the string. On the
# following lines, you will be receiving commands until the &quot;Done&quot; command. There are six possible commands:
#  &quot;Change {char} {replacement}&quot;
# o Replace all occurrences of the char with the given replacement, then print the string.
#  &quot;Includes {substring}&quot;
# o Check if the string includes the given substring with and print &quot;True&quot; or &quot;False&quot;.
#  &quot;End {substring}&quot;
# o Check if the string ends with the given substring and print &quot;True&quot; or &quot;False&quot;.
#  &quot;Uppercase&quot;
# o Make the whole string uppercased, then print it.
#  &quot;FindIndex {char}&quot;
# o Find the index of the first occurrence of the given char, then print it.
#  &quot;Cut {startIndex} {count}&quot;
# o Remove all characters from the string, except those starting from the given start index and the
# next count of characters. Print only the cut chars.
#
# Input
#  On the first line, you are going to receive the string.
#  On the following lines, until the &quot;Done&quot; command is received, you will be receiving commands.
#  All commands are case-sensitive.
#  The input will always be valid.
# Output
#  Print the output of every command in the format described above.

def process_string_commands():
    # Get initial string
    text = input()

    while True:
        command = input()
        if command == "Done":
            break

        tokens = command.split()
        action = tokens[0]

        if action == "Change":
            char, replacement = tokens[1], tokens[2]
            text = text.replace(char, replacement)
            print(text)

        elif action == "Includes":
            substring = tokens[1]
            print(substring in text)

        elif action == "End":
            substring = tokens[1]
            print(text.endswith(substring))

        elif action == "Uppercase":
            text = text.upper()
            print(text)

        elif action == "FindIndex":
            char = tokens[1]
            print(text.find(char))

        elif action == "Cut":
            start_index = int(tokens[1])
            count = int(tokens[2])
            print(text[start_index:start_index + count])


process_string_commands()
