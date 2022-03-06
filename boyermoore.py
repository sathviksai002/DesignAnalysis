total_chars = 256  # for a bad character heuristic


def badCharacterTable(string, size):
    # initialise all occurances as 1
    badchar = [-1] * total_chars

    # fill the actual value for the last occurance
    for i in range(size):
        badchar[ord(string[i])] = i;

    return badchar


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badchar = badCharacterTable(pat, m)

    s = 0      # index of pattern with respect to text
    while s <= n-m:
        j = m-1

        # keep reducing the index j of pattern while characters of pattern and text are matching at shift s

        while j>=0 and pat[j] == txt[s+j]:
            j -= 1

        if j<0:
            print("Pattern occur at shift ={}".format(s))

            s += (m-badchar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j - badchar[ord(txt[s + j])])


txt = "ABAAABCD"
pat = "ABC"
search(txt, pat)
