def decode(string):
    if len(string) <= 1:    return string
    output = ""
    digits = ""
    if string[0].isdigit():
        digits += string[0]
    else:
        output += string[0]
    for i in range(1, len(string)):
        if string[i].isdigit():
            digits += string[i]
        else:
            if digits == "":
                output += string[i]
            else:
                n = int(digits)
                for cnt in range(0, n):
                    output += string[i]
            digits = ""
    return output
def encode(string):
    if len(string) <= 1:    return string
    output = ""
    char_running = string[0]
    cnt_char_running = 1
    for i in range(1, len(string)):
        if string[i] != char_running:
            if cnt_char_running == 1:
                output += char_running
            else:
                output += str(cnt_char_running) + char_running
            char_running = string[i]
            cnt_char_running = 1
        else:
            cnt_char_running += 1
    if cnt_char_running == 1:
        output += char_running
    else:
        output += str(cnt_char_running) + char_running
    return output 