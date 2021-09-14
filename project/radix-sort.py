import urllib
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def grc(s, c):      #returns the c'th element from the right of string s
    if c < len(s):
        temp = len(s) - (1 + c)
        return s[temp]
    elif c >= len(s):       #returns the first character if c is greater than len(s)
        return s[0]

def radix(I, c = 0):
        Count = [0] * 128       #list to hold the count values
        Out = [0] * len(I)      #list to hold the sorted words


        for x in I:     #iterates over each item in the input array
            i = grc(x, c)       #returns the c'th element from the right of the string
            Count[i] = Count[i] + 1     #increases the count for that letter

        for x in range(1, 128):
            Count[x] += Count[x-1]      #sums the values within the count list

        x = len(I) - 1
        while x >= 0:       #fills each value from the input list into its slot using the values from the Count array
            temp = I[x]
            tempbyte = grc(temp, c)
            Count[tempbyte] -= 1
            Out[Count[tempbyte]] = temp
            x -= 1
        
        maxlength = len(max(I, key=len)) - 1        #calculates the length of the longest word
        if c == maxlength:
            for x in range(0, len(Out)):        #converts the words from bytes back into strings
                Out[x] = Out[x].decode('ascii')
            return Out
        else:       #uses recursion to continue until c reaches the number of characters in the longest word
            c += 1
            return radix(Out, c)

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    Words = book_to_words()
    return radix(Words)

def main():
    result = radix_a_book()
    print(result)


if __name__ == '__main__':
    main()