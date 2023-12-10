title_prefix = "##"
paragraph_prefix = "--"


def format_title(txt, max_w=80):
def format_title(txt: str, max_w=80, padding=5) -> str:
    # split text by straight number of characters
    split_txt = list(map(lambda x: f"{title_prefix} {x}", split_txt))
    split_txt = ["#"*max_w] + split_txt + ["#"*max_w]
    return "\n".join(split_txt).upper()

def format_paragraph(txt, max_w=80):
    split_txt = [txt[i:i+max_w] for i in range(0, len(txt), max_w)]
    split_txt = list(map(lambda x: f"{paragraph_prefix} {x}", split_txt))
    return "\n".join(split_txt)
