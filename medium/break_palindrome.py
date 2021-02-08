def _all_chars_same(s):
    return s == len(s) * s[0]

def _insert(s, index, char):
    temp_string = s[index:]
    temp_string2 = s[:index]
    return temp_string + char + temp_string2

def breakPalindrome(s):
    size = len(s)
    if size == 1 or _all_chars_same(s):
        return 'IMPOSSIBLE'
    else:
        for k, v in enumerate (s[:len(s)//2]):
            if v != 'a':
                s = _insert(s, k, 'a')
        s = _insert(s, -1, 'b')
