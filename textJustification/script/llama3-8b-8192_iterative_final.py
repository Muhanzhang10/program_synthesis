def func(words, maxWidth):
    result = []
    curr_line = []
    curr_line_len = 0
    for word in words:
        if curr_line_len + len(word) + len(curr_line) > maxWidth:
            if len(curr_line) == 1:
                result.append(curr_line[0] + ' ' * (maxWidth - len(curr_line[0])))
            else:
                num_spaces = maxWidth - curr_line_len
                space_between_words = num_spaces // (len(curr_line) - 1)
                extra_spaces = num_spaces % (len(curr_line) - 1)
                line = ''
                for i, w in enumerate(curr_line):
                    line += w
                    if i < len(curr_line) - 1:
                        line += ' ' * (space_between_words + (1 if i < extra_spaces else 0))
                result.append(line)
            curr_line = [word]
            curr_line_len = len(word)
        else:
            curr_line.append(word)
            curr_line_len += len(word)
    if curr_line:
        if len(curr_line) == 1:
            result.append(curr_line[0])
        else:
            line = ' '.join(curr_line)
            result.append(line.ljust(maxWidth))
    return result