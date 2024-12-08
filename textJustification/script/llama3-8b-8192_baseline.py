def func(words, maxWidth):
    res = []
    curr_line = []
    curr_len = 0
    for word in words:
        if curr_len + len(word) + len(curr_line) > maxWidth:
            if len(curr_line) == 1:
                res.append(curr_line[0] + ' ' * (maxWidth - len(curr_line[0])))
            else:
                extra_spaces = maxWidth - curr_len
                space_between_words = extra_spaces // (len(curr_line) - 1)
                remaining_spaces = extra_spaces % (len(curr_line) - 1)
                line = ''
                for i, word in enumerate(curr_line):
                    line += word
                    if i < len(curr_line) - 1:
                        line += ' ' * (space_between_words + (1 if i < remaining_spaces else 0))
                res.append(line)
            curr_line = [word]
            curr_len = len(word)
        else:
            curr_line.append(word)
            curr_len += len(word)
    res.append(' '.join(curr_line) + ' ' * (maxWidth - len(' '.join(curr_line))))
    return res