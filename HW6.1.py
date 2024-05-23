import string

str = input("Enter a string: ")
letters = str.split("-")
AsciiLetters = string.ascii_letters

start = AsciiLetters.find(letters[0])
end = AsciiLetters.find(letters[1])
print(AsciiLetters[start:end + 1])

