import json
import random

with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\ascii_compact.json', 'r') as f:
    ascii_data = json.load(f)

ROWS = ascii_data['rows']
COLS = ascii_data['cols']
DATA = ascii_data['data']

W, H = 1180, 610
LEFT_W = int(W * 0.38)
RIGHT_W = W - LEFT_W
FONT_SIZE = 8.5
CHAR_W = FONT_SIZE * 0.6
CHAR_H = FONT_SIZE * 1.05
ASCII_W = COLS * CHAR_W
ASCII_H = ROWS * CHAR_H
AX = LEFT_W // 2 - ASCII_W // 2
AY = H // 2 - ASCII_H // 2 + FONT_SIZE
RX = LEFT_W + 40

def esc(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace("'",'&apos;')

def pick(b, p):
    if b < 0.2: return p[0]
    if b < 0.35: return p[2]
    if b < 0.5: return p[1]
    if b < 0.65: return p[4]
    return p[3]

# ── Defs ──
def defs(dark):
    g1,g2,g3 = ("#7C3AED","#22D3EE","#10B981") if dark else ("#2563EB","#06B6D4","#10B981")
    return f'''  <defs>
    <radialGradient id="g1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{g1}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{g1}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{g2}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{g2}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{g3}" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="{g3}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="refl" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="50%" stop-color="white" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <filter id="nz">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <clipPath id="mc"><rect width="1180" height="610" rx="16"/></clipPath>
  </defs>'''

# ── Background ──
def bg(dark):
    if dark:
        _bg,_pan,_border,_ac = "#030712","#0F172A","rgba(255,255,255,0.08)","#22D3EE"
        nop = 0.025
    else:
        _bg,_pan,_border,_ac = "#FFFFFF","#F8FAFC","rgba(15,23,42,0.08)","#06B6D4"
        nop = 0.015
    random.seed(42)
    cols = ["#7C3AED","#22D3EE","#10B981"] if dark else ["#2563EB","#06B6D4","#10B981"]
    pts = []
    for i in range(18):
        px,py = random.randint(40,W-40), random.randint(40,H-40)
        pr,pdur,pdelay = random.uniform(1,2.5), random.uniform(4,10), random.uniform(0,5)
        pc = random.choice(cols)
        pts.append(f'    <circle cx="{px}" cy="{py}" r="{pr:.1f}" fill="{pc}" opacity="0">'
            f'<animate attributeName="opacity" values="0;0.3;0" dur="{pdur:.1f}s" begin="{pdelay:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="cy" values="{py};{py-30};{py}" dur="{pdur:.1f}s" begin="{pdelay:.1f}s" repeatCount="indefinite"/></circle>')
    return f'''    <rect width="1180" height="610" rx="16" fill="{_bg}"/>
    <g clip-path="url(#mc)">
    <rect x="20" y="20" width="{LEFT_W-40}" height="570" rx="12" fill="{_pan}" stroke="{_border}" stroke-width="1"/>
    <rect x="{LEFT_W}" y="20" width="{RIGHT_W-20}" height="570" rx="12" fill="{_pan}" stroke="{_border}" stroke-width="1"/>
    <circle cx="200" cy="300" r="250" fill="url(#g1)" opacity="0.15"><animateTransform attributeName="transform" type="translate" values="0,0;15,-10;0,0" dur="8s" repeatCount="indefinite"/></circle>
    <circle cx="{LEFT_W+400}" cy="200" r="200" fill="url(#g2)" opacity="0.12"><animateTransform attributeName="transform" type="translate" values="0,0;-10,12;0,0" dur="10s" repeatCount="indefinite"/></circle>
    <circle cx="100" cy="500" r="150" fill="url(#g3)" opacity="0.08"><animateTransform attributeName="transform" type="translate" values="0,0;8,5;0,0" dur="12s" repeatCount="indefinite"/></circle>
{chr(10).join(pts)}
    <rect x="-200" y="0" width="300" height="610" fill="url(#refl)" opacity="0">
      <animate attributeName="opacity" values="0;0.04;0" dur="6s" begin="1s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="-200,0;1400,0" dur="6s" begin="1s" repeatCount="indefinite"/>
    </rect>
    <rect width="1180" height="2" fill="{_ac}" opacity="0">
      <animate attributeName="opacity" values="0;0.035;0" dur="4s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="0,0;0,608" dur="4s" repeatCount="indefinite"/>
    </rect>
    <rect x="0" y="0" width="1180" height="610" rx="16" fill="none" stroke="{_ac}" stroke-width="1.5" stroke-dasharray="300 600" opacity="0">
      <animate attributeName="opacity" values="0;0.12;0" dur="5s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" from="0" to="1800" dur="3s" begin="0.5s" repeatCount="indefinite"/>
    </rect>
    </g>
    <rect width="1180" height="610" rx="16" fill="url(#nz)" opacity="{nop}" style="pointer-events:none"/>'''

# ── ASCII Portrait ──
def ascii(dark):
    p = ["#22D3EE","#67E8F9","#A78BFA","#E0F2FE","#60A5FA"] if dark else ["#0284C7","#0891B2","#1D4ED8","#0F172A","#2563EB"]
    els = []
    for y in range(ROWS):
        row = DATA[y]['chars']
        cl = DATA[y]['colors'].split(',')
        delay = y / ROWS * 3.0
        sp = []
        for x in range(COLS):
            ch = row[x]
            if ch == ' ': sp.append(' '); continue
            cs = cl[x] if x < len(cl) else '000000'
            if cs == 't': sp.append(' '); continue
            b = (int(cs[0:2],16)+int(cs[2:4],16)+int(cs[4:6],16))/(3*255)
            c = pick(b, p)
            sp.append(f'<tspan fill="{c}">{esc(ch)}</tspan>')
        yp = AY + y * CHAR_H
        els.append(f'    <text x="{AX:.1f}" y="{yp:.1f}" font-family="\'Courier New\',Consolas,monospace" font-size="{FONT_SIZE}" opacity="0">'
            f'<animate attributeName="opacity" from="0" to="1" dur="0.25s" begin="{delay:.2f}s" fill="freeze"/>{"".join(sp)}</text>')
    return '\n'.join(els)

# ── Greeting ──
def greet(dark):
    c1,c2 = ("#F8FAFC","#10B981") if dark else ("#0F172A","#10B981")
    return f'''    <text x="{RX}" y="60" font-family="system-ui,-apple-system,sans-serif" font-size="26" font-weight="600" fill="{c1}" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="0.2s" fill="freeze"/>
      Hi 👋 I&apos;m Hariharan S
    </text>
    <text x="{RX}" y="95" font-family="\'Courier New\',Consolas,monospace" font-size="14" fill="{c2}" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="0.6s" fill="freeze"/>
      <animate attributeName="opacity" values="1;0.6;1" dur="3s" begin="0.6s" repeatCount="indefinite"/>
      $ whoami --professional
    </text>'''

# ── Role Animations ──
def roles(dark):
    roles = ["AI Researcher","Full Stack Developer","Open Source Contributor","UI Engineer","AI Enthusiast"]
    tc = "#22D3EE" if dark else "#06B6D4"
    cycle = 3.2; td = 1.2; pd = 1.2; fd = 0.5
    els = []
    for i, role in enumerate(roles):
        st = i * cycle
        cid = f"rc{i}"
        tw = len(role) * 11.5
        els.append(f'''    <clipPath id="{cid}"><rect x="{RX}" y="135" width="0" height="28"><animate attributeName="width" from="0" to="{tw}" dur="{td}s" begin="{st}s" fill="freeze"/></rect></clipPath>
    <text x="{RX}" y="155" font-family="\'Courier New\',Consolas,monospace" font-size="19" fill="{tc}" clip-path="url(#{cid})" opacity="0" visibility="hidden">
      <animate attributeName="visibility" from="hidden" to="visible" dur="0.01s" begin="{st}s" fill="freeze"/>
      <animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="{st}s" fill="freeze"/>
      <animate attributeName="opacity" from="1" to="0" dur="{fd}s" begin="{st+td+pd}s" fill="freeze"/>
      <animate attributeName="visibility" from="visible" to="hidden" dur="0.01s" begin="{st+td+pd+fd}s" fill="freeze"/>
      {esc(role)}
    </text>''')
    return '\n'.join(els)

# ── Cursor ──
def cursor(dark):
    cc = "#22D3EE" if dark else "#06B6D4"
    roles = ["AI Researcher","Full Stack Developer","Open Source Contributor","UI Engineer","AI Enthusiast"]
    rw = [len(r)*11.5 for r in roles]
    cycle = 3.2; td = 1.2; pd = 1.2; fd = 0.5

    total_dur = len(roles) * cycle  # 16s

    # Build a single combined animation for x position across all roles
    x_vals = []
    kt_vals = []
    for i, w in enumerate(rw):
        st = i * cycle
        start_x = RX
        end_x = RX + w
        # Phase 1: typing - move from start_x to end_x
        t_start = st / total_dur
        t_end_type = (st + td) / total_dur
        t_end_pause = (st + td + pd) / total_dur
        t_end_fade = (st + td + pd + fd) / total_dur

        if i == 0:
            x_vals.append(f'{start_x}')
            kt_vals.append(f'{t_start:.4f}')
        x_vals.append(f'{end_x}')
        kt_vals.append(f'{t_end_type:.4f}')
        x_vals.append(f'{end_x}')
        kt_vals.append(f'{t_end_pause:.4f}')
        x_vals.append(f'{start_x}')
        kt_vals.append(f'{t_end_fade:.4f}')

    return f'''    <text y="155" font-family="\'Courier New\',Consolas,monospace" font-size="19" fill="{cc}" opacity="0">
      <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.08;0.45;0.55;1" dur="1s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="{';'.join(x_vals)}" keyTimes="{';'.join(kt_vals)}" dur="{total_dur}s" repeatCount="indefinite"/>
|
    </text>'''

# ── Profile Info ──
def profile(dark):
    items = [("LOCATION","Tamil Nadu, India"),("EDUCATION","B.Tech Information Technology"),
             ("CURRENT FOCUS","full stack development & python"),("PORTFOLIO","hariharan1022.github.io/hariharan_portfolio"),
             ("EMAIL","hariharanmahesh34@gmail.com")]
    lc = "#94A3B8" if dark else "#475569"
    vc = "#F8FAFC" if dark else "#0F172A"
    els = []
    for i,(l,v) in enumerate(items):
        d = i*0.4; y = 210 + i*28
        els.append(f'''    <text x="{RX}" y="{y}" font-family="system-ui,-apple-system,sans-serif" font-size="12" fill="{lc}" opacity="0" letter-spacing="1">
      <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{d}s" fill="freeze"/>
      {l}
    </text>
    <text x="{RX+140}" y="{y}" font-family="system-ui,-apple-system,sans-serif" font-size="12" fill="{vc}" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{d+0.1}s" fill="freeze"/>
      {esc(v)}
    </text>''')
    return '\n'.join(els)

# ── Skill Pills ──
def skills(dark):
    sk = ["React","Next.js","Node.js","TypeScript","Tailwind","Python","Docker","Postgres","AWS","Git","Figma"]
    if dark:
        bg,bo,tc = "rgba(34,211,238,0.1)","rgba(34,211,238,0.3)","#22D3EE"
    else:
        bg,bo,tc = "rgba(6,182,212,0.08)","rgba(6,182,212,0.25)","#06B6D4"
    r1,r2 = sk[:6],sk[6:]
    pw,ph,gap,rx = 88,30,12,6
    els = []
    for i,s in enumerate(r1):
        d = 0.3+i*0.15; x = RX + i*(pw+gap); y = 375
        els.append(f'''    <g opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{d}s" fill="freeze"/>
      <rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="{rx}" fill="{bg}" stroke="{bo}" stroke-width="1"/>
      <rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="{rx}" fill="{bo}" opacity="0.15"><animate attributeName="opacity" values="0.1;0.3;0.1" dur="3s" begin="{d}s" repeatCount="indefinite"/></rect>
      <text x="{x+pw//2}" y="{y+ph//2+1}" font-family="system-ui,-apple-system,sans-serif" font-size="11" fill="{tc}" text-anchor="middle" dominant-baseline="central">{s}</text>
    </g>''')
    for i,s in enumerate(r2):
        d = 0.3+(len(r1)+i)*0.15; x = RX + i*(pw+gap); y = 375+ph+12
        els.append(f'''    <g opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{d}s" fill="freeze"/>
      <rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="{rx}" fill="{bg}" stroke="{bo}" stroke-width="1"/>
      <rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="{rx}" fill="{bo}" opacity="0.15"><animate attributeName="opacity" values="0.1;0.3;0.1" dur="3s" begin="{d}s" repeatCount="indefinite"/></rect>
      <text x="{x+pw//2}" y="{y+ph//2+1}" font-family="system-ui,-apple-system,sans-serif" font-size="11" fill="{tc}" text-anchor="middle" dominant-baseline="central">{s}</text>
    </g>''')
    return '\n'.join(els)

# ── Social Links ──
def social(dark):
    ic = "#94A3B8" if dark else "#475569"
    y = 540
    gh = "M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.167 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.604-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"
    li = "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"
    tw = "M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"
    pf = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"
    paths = [gh,li,tw,pf]
    labels = ["GitHub","LinkedIn","Twitter / X","Portfolio"]
    els = []
    for i,(lb,pa) in enumerate(zip(labels,paths)):
        x = RX + i*155; d = 1.5 + i*0.2
        els.append(f'''    <g opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{d}s" fill="freeze"/>
      <a target="_blank" rel="noopener noreferrer">
        <rect x="{x-2}" y="{y-16}" width="110" height="28" rx="4" fill="transparent"/>
        <g transform="translate({x},{y-14}) scale(0.75)">
          <path d="{pa}" fill="{ic}"/>
        </g>
        <text x="{x+22}" y="{y}" font-family="system-ui,-apple-system,sans-serif" font-size="12" fill="{ic}" dominant-baseline="central">{lb}</text>
      </a>
    </g>''')
    return '\n'.join(els)

def gen(dark):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610">
{defs(dark)}

<g>
{bg(dark)}
</g>

<g>
  <animateTransform attributeName="transform" type="translate" values="0,0;0,-2;0,0;0,1;0,0" dur="6s" repeatCount="indefinite"/>
{ascii(dark)}
</g>

<g>
{greet(dark)}
{roles(dark)}
{cursor(dark)}
{profile(dark)}
{skills(dark)}
{social(dark)}
</g>
</svg>'''

dark_svg = gen(True)
with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\dark.svg','w',encoding='utf-8') as f: f.write(dark_svg)
print(f"dark.svg: {len(dark_svg)} chars ({len(dark_svg)//1024}KB)")

light_svg = gen(False)
with open(r'C:\Users\HARIHARAN S\OneDrive\Desktop\read me\light.svg','w',encoding='utf-8') as f: f.write(light_svg)
print(f"light.svg: {len(light_svg)} chars ({len(light_svg)//1024}KB)")

print("Done!")
