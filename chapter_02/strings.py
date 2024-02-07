favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
# rstrip will remove the whitespace from the right side of the string

nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
# removeprefix is a new method that removes the prefic from a string

# Quotes and apostrophes are handled differently in Python
message = "One of Python's strengths is its diverse community."
print(message)

