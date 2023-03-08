def print_seperator(msg: str):
    sep = "="
    msg = msg.upper()
    msg = msg.center(len(msg)+2)
    msg = sep*5 + msg
    msg = msg.ljust(80, sep)
    print()
    print(msg)
