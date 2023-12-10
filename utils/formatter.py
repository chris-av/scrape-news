title_prefix = "##"
paragraph_prefix = "  "


def format_title(txt: str, max_w=80, padding=5) -> str:
    # split text by straight number of characters
    padding_x = padding*2
    space_alloc_x = max_w - padding_x

    words = txt.split(" ")
    title_frame = []
    line = ""
    char_count = 0
    for word in words:
        next_part = f" {word}"
        if (char_count+len(next_part) <= space_alloc_x):
            char_count += len(next_part)
            line += next_part
        else:
            title_frame.append(line.strip())
            line = ""
            char_count = len(next_part)
            line += next_part

    title_frame.append(line.strip())
    split_txt = title_frame
    split_txt = list(map(lambda x: f"{title_prefix} {x}", split_txt))
    for indx, elem in enumerate(split_txt):
        needed_spaces = max_w - len(title_prefix) - len(elem)
        split_txt[indx] = elem + (needed_spaces)*" " + title_prefix
    split_txt = ["#"*max_w] + split_txt + ["#"*max_w]
    return "\n".join(split_txt).upper()

def format_paragraph(txt: str, max_w=80, padding=2) -> str:
    padding_x = padding*2
    space_alloc_x = max_w - padding_x
    split_txt = [txt[i:i+space_alloc_x] for i in range(0, len(txt), space_alloc_x)]
    split_txt = list(map(lambda x: f"{paragraph_prefix} {x}", split_txt))
    for indx, elem in enumerate(split_txt):
        needed_spaces = max_w - len(paragraph_prefix) - len(elem)
        split_txt[indx] = elem + (needed_spaces)*" " + paragraph_prefix
    return "\n".join(split_txt)
