def print_error(message):
    print("An error occured: " + message)


def remove_white_chars(line):
    line = line.replace('\t', '')
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    return line


def remove_comments_and_empty_lines(text):
    new_text = ''
    first_line = True
    for line in text.split("\n"):
        line = remove_white_chars(line)
        if len(line) > 0:
            index = line.find('#')
            if index >= 0:
                line = line[:index]
            if first_line:
                new_text = line
                first_line = False
            else:
                new_text += "\n" + line
    return new_text
