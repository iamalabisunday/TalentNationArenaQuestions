# Registration. Implement dog_tag(name, service_number) and return the recruit's dog tag as one line in this exact shape: the name, a space, a vertical bar, a space, then SN- joined to the service number. For a recruit named Ada with service number 7 the tag is Ada | SN-7. The service number is a whole number; you must place it inside the same line of text as the name. Researching how to build one string from a word and a number is part of the task.

def dog_tag(name, service_number):
    return f"{name} | SN-{service_number}"