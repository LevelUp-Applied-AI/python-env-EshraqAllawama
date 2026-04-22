# broken_1.py — Fix the SyntaxError
#
# Run this file: python broken/broken_1.py
# Read the traceback. Then fix the bug and run again until it exits with no errors.
#
# Hint: Python requires a colon (:) at the end of every block header.
#       Block headers include: def, if, else, elif, for, while, class.
# Hint: The caret (^) in a SyntaxError traceback points to where Python got confused.
#       The actual mistake is often on that line or the line immediately above it.


# the error is sytnax Error
# How solve it : added a (:) after the gree function and before any beging of bolcks cdoe 
def greet(name): 
    message = f"Hello, {name}! Welcome to the debugging loop."
    return message


if __name__ == "__main__":
    print(greet("engineer"))
