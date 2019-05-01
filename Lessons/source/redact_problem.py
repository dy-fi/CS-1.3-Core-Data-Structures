def redact_words(words, banned_words):
    b = set(banned_words)
    new = [word for word in words if word not in b]
    print(new)
    return new
    

if __name__ == '__main__':
    # Test case sensitivity and partial matches. 
    assert redact_words(["That", "hippopotamus", "is", "not", "my", "favorite", "animal"], ["that", "hippo", "not"]) == ["That", "hippopotamus", "is", "my", "favorite", "animal"]
    print("passed 1")
    # twitter simulation
    assert redact_words(["Our", "president", "is", "a", "bleeping", "bleep"], ["bleeping", "bleep"]) == ["Our", "president", "is", "a"]
    print("passed 2")
