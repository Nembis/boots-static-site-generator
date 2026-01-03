from markdown_blocks import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("#"):
            return block.replace("#", "").strip()
    raise Exception("No title found")
