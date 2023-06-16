"""
Create a function based on the input and output. Look at the examples, there is a pattern.

Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"
Notes
Input is a string.

"""

def secret(s):
    tag, *classes = s.split('.')
    class_str = ' '.join(classes)
    return f"<{tag} class='{class_str}'></{tag}>"

print(secret("p.one.two.three"))
# Output: "<p class='one two three'></p>"

print(secret("p.one"))
# Output: "<p class='one'></p>"

print(secret("p.four.five"))
# Output: "<p class='four five'></p>"
