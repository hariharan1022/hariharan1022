with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\light.svg', 'r', encoding='utf-8') as f:
    c = f.read()

print('light.svg checks:')
print(f'  White background: {"#FFFFFF" in c}')
print(f'  Light panel: {"#F8FAFC" in c}')
print(f'  Dark text: {"#0F172A" in c}')
print(f'  Accent blue: {"#2563EB" in c}')
print(f'  Cyan accent: {"#06B6D4" in c}')
print(f'  Green accent: {"#10B981" in c}')

# Count animations without regex
anim_count = c.count('<animate ')
at_count = c.count('<animateTransform ')
print(f'  animate elements: {anim_count}')
print(f'  animateTransform elements: {at_count}')
print(f'  Total size: {len(c)} chars ({len(c)//1024}KB)')

# Compare structure with dark.svg
with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\dark.svg', 'r', encoding='utf-8') as f:
    d = f.read()

# Check same number of text, clipPath, rect elements
for tag in ['text', 'clipPath', 'rect', 'path', 'tspan', 'animate', 'animateTransform']:
    dc = d.count('<' + tag + ' ')
    lc = c.count('<' + tag + ' ')
    status = 'OK' if dc == lc else 'DIFF'
    print(f'  <{tag}>: dark={dc}, light={lc} {status}')
