from PIL import Image
import os
import glob

src_dir = r"C:\Users\manu1\.gemini\antigravity-ide\brain\b6ad1488-3c8d-4783-acbb-0bad3dd80dc4"
dst_dir = r"c:\Users\manu1\OneDrive\Desktop\Cyber Intiligence"

# Map generated images to target filenames
image_map = {
    "hero_cyber_": "hero-cyber.webp",
    "stackly_logo_": "logo.webp",
    "cloud_soc_": "cloud-soc.webp",
    "onprem_security_": "onprem-security.webp",
    "spotlight_cyber_": "spotlight-cyber.webp",
    "cyber_ops_": "cyber-ops.webp",
    "team_1_": "team-1.webp",
    "team_2_": "team-2.webp",
    "team_3_": "team-3.webp",
    "team_4_": "team-4.webp",
    "blog_featured_": "blog-1.webp",
}

MAX_SIZE = 95 * 1024  # 95KB to be safe under 100KB

for prefix, target_name in image_map.items():
    # Find the source file
    matches = glob.glob(os.path.join(src_dir, prefix + "*.png"))
    if not matches:
        print(f"WARNING: No source found for {prefix}")
        continue
    
    src_path = matches[0]
    dst_path = os.path.join(dst_dir, target_name)
    
    img = Image.open(src_path)
    # Resize to reasonable dimensions first
    max_dim = 800
    if target_name == "logo.webp":
        max_dim = 200
    
    ratio = min(max_dim / img.width, max_dim / img.height)
    if ratio < 1:
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)
    
    # Convert to RGB if RGBA
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (10, 14, 26))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Try different quality levels to stay under 100KB
    for quality in [85, 75, 65, 55, 45, 35, 25]:
        img.save(dst_path, 'WEBP', quality=quality)
        size = os.path.getsize(dst_path)
        if size <= MAX_SIZE:
            break
    
    size_kb = os.path.getsize(dst_path) / 1024
    print(f"Converted {target_name}: {size_kb:.1f}KB (quality={quality})")

print("\nAll images converted!")
