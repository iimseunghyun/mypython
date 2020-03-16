def palindrome(str):
    qu = []
    st = []

    for char in str:
        if char.isalpha():
            qu.append(char)
            st.append(char)
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True


a = palindrome("해인사에 사인해")

print(a)