def print_seperator(msg: str):
    sep = "="
    msg = msg.upper()
    msg = msg.center(len(msg)+2)
    msg = sep*5 + msg
    msg = msg.ljust(80, sep)
    print()
    print(msg)


print_seperator("original")
welcome_msg = "welcome to class python software developers"
print(welcome_msg)

print_seperator("upper case")
welcome_msg_cap = welcome_msg.upper()
print(welcome_msg_cap)

print_seperator("title")
welcome_msg_title = welcome_msg.title()
print(welcome_msg_title)

