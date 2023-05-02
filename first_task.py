def true_brackets(brackets):
    open_bracket = ''
    close_bracket = ''

    for i in brackets:
        if i == '(':
            open_bracket += i
        elif i == ')':
            close_bracket += i
    if len(open_bracket) == len(close_bracket):
        return True
    else:
        return False
