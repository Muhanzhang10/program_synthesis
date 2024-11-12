def func(words, maxWidth):
    res = []
    curLine = []
    curWidth = 0
    for word in words:
        if curWidth + len(word) + len(curLine) > maxWidth:
            if len(curLine) == 1:
                res.append(curLine[0] + ' ' * (maxWidth - len(curLine[0])))
            else:
                remainSpaces = maxWidth - curWidth
                extraSpaces = remainSpaces - (len(curLine) - 1)
                for i in range(remainSpaces - extraSpaces):
                    curLine[-1] += ' '
                for i in range(extraSpaces):
                    curLine[-2] += ' '
                res.append(' '.join(curLine))
                curLine = []
                curWidth = 0
        curLine.append(word)
        curWidth += len(word)
    if curLine:
        res.append(' '.join(curLine).ljust(maxWidth))
    return res