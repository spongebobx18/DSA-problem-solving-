def calc(string, letter):
    totalchar = len(string)
    matching_characters = string.count(letter)
    percentage = (matching_characters / totalchar) * 100
    ppercent= int(percentage)
    return ppercent

# Test the function
string = input("Enter a string: ")
letter = input("Enter a character: ")
percentage = calc(string, letter)
print(f"The percentage of '{letter}' in '{string}'  is: {percentage}%")
