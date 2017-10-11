def palindrome(string):
    temp = string
    isPalin = True
    for i in range(0,len(string)-1):
        if string[len(string)-1-i] != string[i]:
            isPalin = False
            break
    if isPalin:
        print('The given string',string,'is a palindrome')
    else:
        print('The given string',string,'is not a palindrome')


palindrome('adam')

palindrome('madam')

