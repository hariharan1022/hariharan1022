with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\light.svg', 'r', encoding='utf-8') as f:
    c = f.read()

print('Light mode verification:')
print(f'  Background #FFFFFF: {"#FFFFFF" in c[:200]}')
print(f'  Panel #F8FAFC: {"#F8FAFC" in c[:400]}')
print(f'  Text #475569: {"#475569" in c}')
print(f'  Role color #06B6D4: {"#06B6D4" in c}')

# Check role texts use light mode color
for r in ['AI Researcher','Full Stack Developer','Open Source Contributor','UI Engineer','AI Enthusiast']:
    idx = c.find(r)
    snippet = c[max(0,idx-200):idx+len(r)]
    has_color = '#06B6D4' in snippet
    print(f'  Role "{r}" uses #06B6D4: {has_color}')

print(f'  Skill pills: {"rgba(6,182,212,0.08)" in c}')
print(f'  Social icons #475569: {"#475569" in c}')
