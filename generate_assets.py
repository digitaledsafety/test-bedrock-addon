import os
import urllib.request
from PIL import Image
import io

def download_and_process_icon(url, path, size):
    print(f"Generating {path} from {url}...")
    try:
        # Minecraft icons often look better with NEAREST if they are small and pixelated,
        # but since these are high-res source icons being downscaled to 16x16,
        # LANCZOS might be too blurry. NEAREST or BOX might give a more "Minecraft" feel.
        # However, LANCZOS is generally safer for downscaling.

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read()

        img = Image.open(io.BytesIO(data))
        img = img.resize((size, size), Image.Resampling.LANCZOS)

        # Ensure directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        img.save(path)
        print(f"Successfully saved to {path}")
    except Exception as e:
        print(f"Error generating {path}: {e}")

# Define assets
assets = [
    {
        "url": "https://img.icons8.com/ios-filled/100/FF0000/ruby.png",
        "path": "resource_pack/textures/items/ruby.png",
        "size": 16
    },
    {
        "url": "https://img.icons8.com/ios-filled/100/0000FF/sparkling-diamond.png",
        "path": "resource_pack/textures/items/magic_wand.png",
        "size": 16
    },
    {
        "url": "https://img.icons8.com/ios-filled/100/FF0000/box.png",
        "path": "resource_pack/textures/blocks/ruby_block.png",
        "size": 16
    },
    {
        "url": "https://img.icons8.com/ios-filled/100/00FF00/bot.png",
        "path": "resource_pack/textures/entity/companion.png",
        "size": 16
    },
    {
        "url": "https://img.icons8.com/ios-filled/128/8B4513/package.png",
        "path": "resource_pack/pack_icon.png",
        "size": 128
    },
    {
        "url": "https://img.icons8.com/ios-filled/128/8B4513/package.png",
        "path": "behavior_pack/pack_icon.png",
        "size": 128
    }
]

for asset in assets:
    download_and_process_icon(asset["url"], asset["path"], asset["size"])

print("All assets generated.")
