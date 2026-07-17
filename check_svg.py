with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\dark.svg', 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('viewBox="0 0 1180 610"', 'viewBox'),
    ('clipPath id="mc"', 'main clip path'),
    ('clipPath id="rc', 'role clip paths'),
    ('animateTransform', 'cursor animation'),
    ('target="_blank"', 'social links'),
    ('<defs>', 'defs opening'),
    ('</defs>', 'defs closing'),
    ('<tspan fill=', 'colored ASCII'),
    ('Hi 👋', 'greeting with wave'),
    ('$ whoami --professional', 'command'),
    ('AI Researcher', 'role 1'),
    ('Full Stack Developer', 'role 2'),
    ('Open Source Contributor', 'role 3'),
    ('UI Engineer', 'role 4'),
    ('AI Enthusiast', 'role 5'),
    ('LOCATION', 'profile location'),
    ('EDUCATION', 'profile education'),
    ('CURRENT FOCUS', 'profile focus'),
    ('PORTFOLIO', 'profile portfolio'),
    ('EMAIL', 'profile email'),
    ('React', 'skill React'),
    ('Next.js', 'skill Next.js'),
    ('GitHub', 'social GitHub'),
    ('LinkedIn', 'social LinkedIn'),
]

all_pass = True
for pattern, name in checks:
    if pattern in content:
        print(f'PASS: {name}')
    else:
        print(f'FAIL: {name} - missing "{pattern}"')
        all_pass = False

# Structural checks
if content.count('<defs>') == 1 and content.count('</defs>') == 1:
    print('PASS: single defs pair')
else:
    print(f'FAIL: defs count = {content.count("<defs>")} open, {content.count("</defs>")} close')

# Check role opacity
for r in ['AI Researcher', 'Full Stack Developer', 'Open Source Contributor', 'UI Engineer', 'AI Enthusiast']:
    c = content.count(r)
    if c >= 1:
        print(f'PASS: role "{r}" present ({c}x)')
    else:
        print(f'FAIL: role "{r}" missing')

# Count animations
import re
anim_count = len(re.findall(r'<animate[\s>]', content))
at_count = len(re.findall(r'<animateTransform[\s>]', content))
print(f'\nAnimate elements: {anim_count}')
print(f'AnimateTransform elements: {at_count}')
print(f'Total size: {len(content)} chars ({len(content)//1024}KB)')

if all_pass:
    print('\nALL CHECKS PASSED!')
else:
    print('\nSOME CHECKS FAILED!')
