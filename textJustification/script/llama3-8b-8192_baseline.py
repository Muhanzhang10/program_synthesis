def func(words, maxWidth):
    res = []
    curLine = []
    curWidth = 0
    for word in words:
        if curWidth + len(word) + len(curLine) > maxWidth:
            for i in range(maxWidth - curWidth):
                if curLine:
                    curLine[-1] += ' '
            res.append(' '.join(curLine))
            curLine = []
            curWidth = 0
        curLine.append(word)
        curWidth += len(word)
    if curLine:
        for i in range(maxWidth - curWidth):
            curLine[-1] += ' '
        res.append(' '.join(curLine))
    return res