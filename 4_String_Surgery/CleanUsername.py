# Implement clean_username(value). The function should remove leading and trailing spaces, convert the text to lowercase, and replace every space with an underscore. Return the cleaned username.
def clean_username(value):
    result = value.strip().lower().replace(" ", "_")
    return result