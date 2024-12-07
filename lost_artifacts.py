# You've come across ancient scrolls containing encrypted messages about the locations of these artifacts. To discover where each artifact is hidden, you must decode these messages by following specific rules:
# •	Artifact Name:
# o	Surrounded by one or more "*" or "^" (they don't have to be the same on both sides).
# o	Consists only of mixed case alphabetical letters and can include spaces.
# o	Must be at least 6 characters long including the spaces.
# •	Coordinates:
# o	Always positioned after the artifact name.
# o	There may or may not be other non-alphabetic, non-digit characters between the artifact name and the coordinates. If there are alphabetic or digit characters directly separating them, the message is considered corrupted.
# o	Enclosed by sequences of the symbol "+".
# o	Contains comma-separated values (digits, decimal separator ".", or "-") representing latitude and longitude (e.g., 34.807,-40.479).
# •	Message validity: If either the artifact name or the coordinates are not valid according to the rules, the entire message is disregarded.
# Examples of valid messages: *Lost Crown*+++34.807,-40.479+++, ^Ancient Sword^++++48.8566,2.3522++++,
# *Golden Statue^!!!+12.492,99.901+
# Examples of invalid messages: Idol++48.858,2.294++, ^Relic^48.853,-2.3498+,
# Mysterious Relic+++120,200+++
# Read through the provided message and identify all valid messages.
# Print each found message in the format: "Found {artifact name} at coordinates {coordinates}."
# If the message contains no valid artifacts, print "No valid artifacts found.".
# Examples
# •	You will receive a string.
# •	Print the proper output messages in the proper cases as described in the problem description.


import re
def find_artifacts(message):
    
    pattern = r'[*^]([A-Za-z\s]{6,})[*^][^A-Za-z0-9]*\++([-\d.,]+)\++'

    matches = re.finditer(pattern, message)
    found_artifacts = False

    for match in matches:
        artifact_name = match.group(1)
        coordinates = match.group(2)

        coord_pattern = r'^-?\d+\.?\d*,-?\d+\.?\d*$'
        if re.match(coord_pattern, coordinates):
            print(f"Found {artifact_name} at coordinates {coordinates}.")
            found_artifacts = True

    if not found_artifacts:
        print("No valid artifacts found.")


message = input()
find_artifacts(message)
