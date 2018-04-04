print("1: Match a")
print("2: Front x")

CHOICE = int(input("Enter a Number:"))

if CHOICE == int ("1"):
    def match_ends(words):
        ctr = 0

        for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                ctr += 1
        return ctr
    
    x = input("Enter Word:")
    print match_ends(x)


elif CHOICE == int("2"):
    
    def front_x(words):
        xlist = []
        alist = []

        for word in words:
            if word.startswith('x'):
                xlist.append(word)
            else:
                alist.append(word)

        return sorted(xlist) + sorted(alist)
    
    x = input("Enter Word:")
    print front_x(x)

else: 
    print("Invalid Number")
    print("\n")

