def func(words, maxWidth):
    res = []
    curLine = []
    curWidth = 0
    for word in words:
        if curWidth + len(word) + len(curLine) > maxWidth:
            if len(curLine) == 1:
                res.append(curLine[0].rjust(maxWidth))
            else:
                numSpaces = maxWidth - curWidth
                extraSpaces = ' ' * (numSpaces // (len(curLine) - 1))
                res.append(extraSpaces.join(curLine).ljust(maxWidth))
            curLine = []
            curWidth = 0
        curLine.append(word)
        curWidth += len(word)
    if curLine:
        if len(curLine) == 1:
            res.append(curLine[0].rjust(maxWidth))
        else:
            numSpaces = maxWidth - curWidth
            extraSpaces = ' ' * (numSpaces // (len(curLine) - 1))
            res.append(extraSpaces.join(curLine).ljust(maxWidth))
            if numSpaces % (len(curLine) - 1) != 0:
                res[-1] += ' '
    return res