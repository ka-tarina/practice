"""
Divide string so that every character except from space is an element of a tuple.
"""

s = "Gledam fudbal i placem."
s = s.replace(" ", "")
t = tuple(list(s))
print(t)
