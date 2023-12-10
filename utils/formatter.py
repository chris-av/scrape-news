title_prefix = "##"
paragraph_prefix = "--"


def format_title(txt, max_w=80):
def format_title(txt: str, max_w=80, padding=5) -> str:
    # split text by straight number of characters
    padding_x = max_w - padding*2
    split_txt = [txt[i:i+padding_x] for i in range(0, len(txt), padding_x)]
    split_txt = list(map(lambda x: f"{title_prefix} {x}", split_txt))
    for indx, elem in enumerate(split_txt):
        needed_spaces = max_w - len(title_prefix) - len(elem)
        split_txt[indx] = elem + (needed_spaces)*" " + title_prefix
    split_txt = ["#"*max_w] + split_txt + ["#"*max_w]
    return "\n".join(split_txt).upper()

def format_paragraph(txt: str, max_w=80) -> str:
    split_txt = [txt[i:i+max_w] for i in range(0, len(txt), max_w)]
    split_txt = list(map(lambda x: f"{paragraph_prefix} {x}", split_txt))
    return "\n".join(split_txt)
