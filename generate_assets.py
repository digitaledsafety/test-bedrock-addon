import os

def create_placeholder_png(path, color):
    # This is a hack because we don't have PIL/ImageMagick
    # A 1x1 PNG file with a single pixel of 'color'
    # For now, I'll just create a text file that says it's a PNG
    # Actually, I'll try to use a minimal base64 encoded PNG

    # Red 1x1 PNG
    if color == "red":
        data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xff\xff? \x05\xfe\x02\xfe\xdcD\x05\x00\x00\x00\x00IEND\xaeB`\x82'
    # Blue 1x1 PNG
    elif color == "blue":
        data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xff\xff\xff\x7f\x06\x03\x05\xfe\x01\xfe\x8e\x04\x05\x00\x00\x00\x00IEND\xaeB`\x82'
    # Green 1x1 PNG
    else:
        data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\x00\xff\x00\x00\x03\x00\x01\xfe\x10\x10\x01\x00\x00\x00\x00IEND\xaeB`\x82'

    with open(path, "wb") as f:
        f.write(data)

os.makedirs("resource_pack/textures/items", exist_ok=True)
os.makedirs("resource_pack/textures/blocks", exist_ok=True)
os.makedirs("resource_pack/textures/entity", exist_ok=True)

create_placeholder_png("resource_pack/textures/items/ruby.png", "red")
create_placeholder_png("resource_pack/textures/items/magic_wand.png", "blue")
create_placeholder_png("resource_pack/textures/blocks/ruby_block.png", "red")
create_placeholder_png("resource_pack/textures/entity/companion.png", "green")

print("Placeholder assets generated.")
