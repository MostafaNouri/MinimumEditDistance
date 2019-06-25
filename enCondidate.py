tokens = open("tokens.en", "r")
incorrect = open("incorrect.en", "r")

tokenArr = []
incorrectArr = []
for line in tokens:
    tokenArr.append(line.split('\n')[0])

for line in incorrect:
    incorrectArr.append(line.split('\n')[0])

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



def getCondidateWords(word, tokens):
    editDisArr = []
    for token in tokens:
        editDisArr.append(editDistDP(word, token, len(word), len(token)))

    condidateWords = []
    counter = 0
    while counter < 10:
        index = editDisArr.index(min(editDisArr))
        condidateWords.append(tokens[index])
        editDisArr[index] = 500
        counter += 1

    return condidateWords

enOutput = open("output/94463165_Assignment3_Part2_EN.en", "w+", encoding="utf-8")

for incorrectWord in incorrectArr:
    condidateWords = getCondidateWords(incorrectWord, tokenArr)
    enOutput.write(incorrectWord + ': ')
    for condidateWord in condidateWords:
        enOutput.write(condidateWord + ', ')
    enOutput.write('\n')