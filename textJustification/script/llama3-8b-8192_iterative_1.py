def func(words, maxWidth):
    res = []
    curLine = []
    curWidth = 0
    for word in words:
        if curWidth + len(word) + len(curLine) > maxWidth:
            if len(curLine) == 1:
                res.append(curLine[0])
            else:
                numSpaces = maxWidth - curWidth
                numExtraSpaces = numSpaces // (len(curLine) - 1)
                extraSpaces = ' ' * numExtraSpaces
                res.append(' '.join(curLine[:-1] + [curLine[-1] + extraSpaces]))
            curLine = []
            curWidth = 0
        curLine.append(word)
        curWidth += len(word)
    if curLine:
        if len(curLine) == 1:
            res.append(curLine[0])
        else:
            numSpaces = maxWidth - curWidth
            numExtraSpaces = numSpaces // (len(curLine) - 1)
            extraSpaces = ' ' * numExtraSpaces
            res.append(' '.join(curLine) + ' ' * (numSpaces % (len(curLine) - 1)))
    return res