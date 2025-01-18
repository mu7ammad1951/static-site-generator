import re

def markdown_to_blocks(text):
    return list(filter(lambda x: x!="", map(lambda x: x.strip(), text.split("\n\n"))))

def block_to_block_type(text):
    lines = list(filter(lambda x: x != "",list(text.split("\n"))))
    
    if check_heading(text):
        return "heading"
    if check_quotes(lines):
        return "quote"
    if check_code(text):
        return "code"
    if check_unordered_list(lines):
        return "unordered_list"
    if check_ordered_list(lines):
        return "ordered_list"

    return "paragraph"

# Heading
def check_heading(text):
    heading_matcher = re.compile(r"^\s*\#{1,6}\ .*")
    is_heading = True
    if heading_matcher.match(text) is None:
        is_heading = False

    return is_heading

def check_quotes(lines):
    quote_matcher = re.compile(r"^\s*>{1}\ .*")
    is_quote = True
    for line in lines:
        if line == "":
            continue
        if quote_matcher.match(line) is None:
            is_quote = False

    return is_quote

def check_code(text):
    code_matcher = re.match(r"^\s*```[\S\s]*```\s*$", text)
    return code_matcher is not None

def check_unordered_list(lines):
    ulist_matcher = re.compile(r"^\s*[*-]{1}\ .*")
    is_ulist = True
    for line in lines:
        if line == "":
            continue
        if ulist_matcher.match(line) is None:
            is_ulist = False

    return is_ulist

def check_ordered_list(lines):
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return False
        

    return True
