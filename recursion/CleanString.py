import string


def clean_str_loop(s: str) -> str:
    new_s = ""
    for ch in s:
        if ch not in string.punctuation + string.whitespace:
            new_s += ch

    return new_s


def clean_str_recursive(s: str) -> str:
    if len(s) == 0:
        return ""
    else:
        first_char = s[0]
        clean_remain = clean_str_loop(s[1:])
        if first_char not in string.punctuation + string.whitespace:
            return first_char + clean_remain
        else:
            return clean_remain


test_str = "Hel$$  lo!!"
print(clean_str_loop(test_str))
print(clean_str_recursive(test_str))
