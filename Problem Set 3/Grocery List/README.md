Grocery List

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called Grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

Hints
 - Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
try:
    item = input()
except EOFError:
    ...

 - Odds are you’ll want to store your grocery list as a dict.
 - Note that a dict comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get, and supports operations like:
d[key]
and

if key in d:
    ...
wherein d is a dict and key is a str.

 - Be sure to avoid or catch any KeyError.
 - Note that you can sort a dictionary’s keys alphabetically by passing that dictionary as an argument to sorted.