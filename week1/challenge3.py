wordList = ['hot','dot','dog','lot','log','cog']
beginWord = 'hit'
endWord = 'cog'

# bW = list(beginWord)
#
# e = [j for i in wordList for j in i if j == 't']
#
# for i in range(len(wordList)):
#     wL = tuple(wordList[i])
#     print(wL)

# print(bW)
# print('---------------')
# print(e)

bw = tuple(beginWord)
wl = tuple(wordList[0])
# print(wl)
print(bw)
zp = tuple(zip(bw,wl))
print(zp)
e = [j for i in zp for j in i]
print(e)
