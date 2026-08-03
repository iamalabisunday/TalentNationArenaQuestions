# Implement first_and_last(value). Return a dictionary with two keys: "first" and "last". "first" should contain the first character of the string. "last" should contain the last character of the string. If the string is empty, return {"first": "", "last": ""}.

def first_and_last(value):
    if value == "":
        return {"first": "", "last": ""}
    return {"last":value[len(value)-1],"first":value[0]}