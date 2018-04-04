def isPalindrome(phrase):
    
    phrase_letters = [c for c in phrase.lower() if c.isalpha()]
    print phrase_letters  # test
    return phrase_letters == phrase_letters[::-1]


inputPhrase = raw_input("Enter a Sentence:")

if isPalindrome(inputPhrase):
    print '"%s" is a palindrome' % inputPhrase
else:
    print '"%s" is not a palindrome' % inputPhrase

