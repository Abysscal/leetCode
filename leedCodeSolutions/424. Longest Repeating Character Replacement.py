import re

def solu(s,k) -> int:
    #using a sliding window
    highest = 0
    maxf =0
    # map to count all the occurances
    count = {}
    # L R pointers for window
    l =0
    # going through the string
    for r in range(len(s)):
        # add the counter of the letter, else default is 0
        count[s[r]] = 1 + count.get(s[r],0)
        # get the max freq of the current letter vs the max
        maxf = max(maxf, count[s[r]])

        # if window size - highest occurance > K, meaning letters needed to switch is more than what is allowed(K)
        if r - l + 1 - max(count.values()) > k:
            # increase L by 1, remove that one from the current count
            count[s[l]] -= 1
            l += 1

        # get highest subarray
        highest = max(highest, r-l + 1)

    return highest


input = "AABABBA"
k = 1
print(solu(input,k))
