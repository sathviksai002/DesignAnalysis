def search(pat, txt):
    m = len(pat)
    n = len(txt)

    for i in range(0, (n-m)+1):
        j = 0
        while j < m:
            if txt[i+j] != pat[j]:
                break
            j += 1

        if j == m:
            print("Pattern found at ", i, "index")


text = input("Enter the text: ")
pattern = input("Enter the pattern to be checked: ")
search(pattern, text)
