"""
The stores treat a request as live if it carries a truthy value. Implement bool_of(value) and return what Python considers the truth value of value, as a boolean. Remember the surprises: zero and an empty string are False, but any non-zero number is True, and any non-empty string is True even if the text reads False or 0.
"""
def bool_of(value):
   return bool(value)