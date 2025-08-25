def is_palindrome(s: str) -> bool:
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

def is_palindrome_two_pointers(s: str) -> bool:
    if (len(s) < 2):
        return True
    characters = [ c.lower() for c in s if c.isalnum()]
    head = 0
    tail = len(characters) - 1
    while head <= tail: 
        if characters[head] == characters[tail]:
            head += 1
            tail -= 1
        else:
            return False
    return True