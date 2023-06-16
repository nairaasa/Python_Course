"""
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
Notes
This is an oversimplification of the English language so no edge cases will appear.
Only focus on whether or not to add an s to the ends of words.
All tests will be valid.
"""

def pluralize(words):
    word_counts = {}
    plural_words = set()
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    for word, count in word_counts.items():
        if count > 1:
            plural_words.add(word + "s")
        else:
            plural_words.add(word)
    
    return plural_words

print(pluralize(["cow", "pig", "cow", "cow"])) # Output: {"cows", "pig"}

print(pluralize(["table", "table", "table"])) # Output: {"tables"}

print(pluralize(["chair", "pencil", "arm"])) # Output: {"chair", "pencil", "arm"}