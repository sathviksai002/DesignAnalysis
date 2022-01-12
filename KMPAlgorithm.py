c = 0


def kmpspam(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M              # lps table same length of the pattern.
    j = 0
    global c

    computelps(pat, M, lps)       # method to compute the lps array
    i = 0              # i is for searching in string.   j is for searching in pattern.
    while i < N:            # searches until the end of the string
        if pat[j] == txt[i]:            # if both of them matches, then we need to increment both i and j
            i += 1
            j += 1
        if j == M:                  # if j is reached at end of the pattern.
            c = c+1
            print("Yes, its a SPAM Message. Please Ignore. !!")
            j = lps[j - 1]
            # to check the whole pattern, if any overlapping is present in the system.
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computelps(pat, M, lps):
    len1 = 0
    lps[0] = 0                  # always 0, because first element doesnt have no prefix/suffix
    i = 1
    while i < M:
        if pat[i] == pat[len1]:
            len1 += 1
            lps[i] = len1
            i += 1
        else:
            if len1 != 0:
                len1 = lps[len1 - 1]
            else:
                lps[i] = 0
                i += 1                  # we only increment i, as we don't increment length without finding the suffix


stat = input("Enter the message to check for spam: ")
spams = []
with open("spamcodes.txt", "r") as f:
    for i in f:
        spams.append(i.casefold().strip())
f.close()
for il in spams:
    kmpspam(il, stat)
if c <= 0:
    print("It is not a Spam Message! Continue.....")
