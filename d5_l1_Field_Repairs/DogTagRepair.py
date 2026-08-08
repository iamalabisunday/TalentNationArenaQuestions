"""
Before Week 2 you stand on a Field Engineering Detail. Sergeant Kay hands you a clipboard: three pieces of kit have been throwing errors all morning. Read each traceback. The line at the bottom names the fault and points to the line where it happened. Make the smallest change that removes the error and keeps the original behaviour.

FAULT 1. Recruit Idris at the dog-tag desk filed this code on Day 1. It crashes the moment a service number is passed in.

Current code:

    def dog_tag(name, service_number):
        return name + " | SN-" + service_number

Traceback when called with dog_tag("Ada", 7):

    TypeError: can only concatenate str (not "int") to str

The fault is a type mismatch on the last line: the code tries to join a number onto a string with the plus operator, which Python will not do. Repair the function so the same line is produced (the name, a space, a bar, a space, SN- and the service number) without the crash.
"""
def dog_tag(name, service_number):
    return f"{name} | SN-{service_number}"