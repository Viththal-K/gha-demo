def lowercase_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.lower()