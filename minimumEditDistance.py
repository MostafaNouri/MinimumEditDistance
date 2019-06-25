import re

enEditDistance = open("EditDistance.en", "r")
arr = []

for line in enEditDistance:
    s = re.split(r'\t', line)
    arr.append([s[0], s[1].split('\n')[0]])

faEditDistance = open("EditDistance.fa", "r", encoding="utf8")
faArr = []

for line in faEditDistance:
    s = re.split(r'\t', line)
    faArr.append([s[0], s[1].split('\n')[0]])


def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

faOutput = open("output/94463165_Assignment3_Part1_FA.fa", "w+", encoding="utf-8")
enOutput = open("output/94463165_Assignment3_Part1_EN.en", "w+", encoding="utf-8")

# English words
for st in arr:
    enOutput.write(st[0] + '    ' + st[1] + '    ' + str(editDistDP(st[0], st[1], len(st[0]), len(st[1]))) + '\n')

# Persian words
for st in faArr:
    faOutput.write(st[0] + '    ' + st[1] + '    ' + str(editDistDP(st[0], st[1], len(st[0]), len(st[1]))) + '\n')