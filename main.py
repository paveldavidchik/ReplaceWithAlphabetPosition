
def alphabet_position(text):
    return ' '.join([str(ord(ch) - 96) for ch in text.lower() if 'a' <= ch <= 'z'])


print(alphabet_position("The sunset sets at twelve o' clock."))
