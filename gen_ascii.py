from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import json

img = Image.open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\founder.jpeg')
w, h = img.size
crop = img.crop((w*0.1, h*0.05, w*0.9, h*0.50))

e = ImageEnhance.Contrast(crop)
high = e.enhance(1.8)
e2 = ImageEnhance.Sharpness(high)
sharp = e2.enhance(2.0)
gray = sharp.convert('L')
edges = gray.filter(ImageFilter.FIND_EDGES)
edges_sharp = edges.filter(ImageFilter.SHARPEN)

g = np.array(gray, dtype=float)
ed = np.array(edges_sharp, dtype=float)
blend = g * 0.7 + ed * 0.3
blend = blend.clip(0, 255).astype(np.uint8)
blend_img = Image.fromarray(blend)
rgb = np.array(sharp)

cols, rows = 50, 42
small = blend_img.resize((cols, rows), Image.LANCZOS)
small_color = Image.fromarray(rgb).resize((cols, rows), Image.LANCZOS)
s = np.array(small)
sc = np.array(small_color)

mn, mx = s.min(), s.max()
stretched = ((s.astype(float) - mn) / (mx - mn + 1) * 255).clip(0, 255).astype(np.uint8)
gamma = 0.8
corrected = (255 * (stretched / 255) ** gamma).clip(0, 255).astype(np.uint8)

ramp = '@%#*+=-:. '
compact = []

for y in range(rows):
    row_str = ''
    color_str = ''
    row_vals = corrected[y]
    med = np.median(row_vals)
    bg_thresh = med + 20
    for x in range(cols):
        val = corrected[y, x]
        r, gv, bv = sc[y, x]
        is_bg = val > bg_thresh and val > 160
        if is_bg:
            row_str += ' '
            color_str += 't,'
        else:
            normalized = val / 255.0
            idx = int(normalized * (len(ramp) - 1))
            idx = max(0, min(len(ramp) - 1, idx))
            char = ramp[idx]
            darken = 1.0 - (1.0 - normalized) * 0.3
            row_str += char
            color_str += f'{int(r*darken):02x}{int(gv*darken):02x}{int(bv*darken):02x},'
    compact.append({'chars': row_str, 'colors': color_str.rstrip(',')})

with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\ascii_compact.json', 'w') as f:
    json.dump({'rows': rows, 'cols': cols, 'data': compact, 'ramp': ramp}, f)

for y in range(rows):
    print(f'{y:2d}: |{compact[y]["chars"]}|')
print('Saved to ascii_compact.json')
