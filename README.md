<p align="center">
  <!-- Animated gradient header using SVG -->
  <svg width="800" height="80" viewBox="0 0 800 80">
    <defs>
      <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#ff6b6b;stop-opacity:1">
          <animate attributeName="stop-color" values="#ff6b6b;#48dbfb;#ff9ff3;#ff6b6b" dur="6s" repeatCount="indefinite"/>
        </stop>
        <stop offset="50%" style="stop-color:#48dbfb;stop-opacity:1">
          <animate attributeName="stop-color" values="#48dbfb;#ff9ff3;#ff6b6b;#48dbfb" dur="6s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" style="stop-color:#ff9ff3;stop-opacity:1">
          <animate attributeName="stop-color" values="#ff9ff3;#ff6b6b;#48dbfb;#ff9ff3" dur="6s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
      <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#48dbfb"/>
        <stop offset="100%" style="stop-color:#ff9ff3"/>
      </linearGradient>
      <filter id="glow">
        <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <text x="400" y="48" font-family="'Segoe UI',Arial,sans-serif" font-size="36" font-weight="800" fill="url(#grad)" text-anchor="middle" filter="url(#glow)">Hariharan S</text>
    <text x="400" y="70" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#8892b0" text-anchor="middle" opacity="0.9">Founder @ Skyrovix · Full Stack Engineer · React Developer</text>
  </svg>
</p>

<!-- Animated typing subtitle as SVG -->
<p align="center">
  <svg width="500" height="40" viewBox="0 0 500 40">
    <rect x="0" y="5" width="500" height="30" rx="15" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" stroke-dasharray="800" stroke-dashoffset="800">
      <animate attributeName="stroke-dashoffset" from="800" to="0" dur="2s" fill="freeze"/>
    </rect>
    <text x="250" y="26" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#ccd6f6" text-anchor="middle" opacity="0">
      🚀 Building modern web apps · ⚛️ React · 🤖 AI · 🌍 Open Source
      <animate attributeName="opacity" from="0" to="1" dur="1s" begin="1.5s" fill="freeze"/>
    </text>
  </svg>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Visitor-0891b2?style=flat-square&logo=github&logoColor=white" alt="Visitor" style="border-radius:8px"/>
  <a href="https://github.com/hariharan1022?tab=followers">
    <img src="https://img.shields.io/github/followers/hariharan1022?style=flat-square&logo=github&logoColor=white&color=0891b2" alt="Followers"/>
  </a>
  <a href="https://github.com/hariharan1022">
    <img src="https://img.shields.io/github/stars/hariharan1022?style=flat-square&logo=github&logoColor=white&color=0891b2" alt="Stars"/>
  </a>
</div>

<!-- Modern 3D-style divider SVG -->
<p align="center">
  <svg width="90%" height="30" viewBox="0 0 800 30">
    <line x1="50" y1="15" x2="350" y2="15" stroke="#48dbfb" stroke-width="1" opacity="0.4"/>
    <circle cx="400" cy="15" r="4" fill="#ff6b6b">
      <animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="15" x2="750" y2="15" stroke="#ff9ff3" stroke-width="1" opacity="0.4"/>
  </svg>
</p>

<!-- MODERN GLASSMORPHISM CARDS SECTION (rendered with HTML + SVG) -->
<table>
  <tr>
    <td width="50%" valign="top">

<!-- About Me Card -->
<svg width="100%" height="220" viewBox="0 0 380 220">
  <defs>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#112240;stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:#0a192f;stop-opacity:0.95"/>
    </linearGradient>
    <linearGradient id="accent1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#48dbfb"/>
      <stop offset="100%" style="stop-color:#ff6b6b"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="380" height="220" rx="16" fill="url(#cardGrad1)" stroke="#1d3461" stroke-width="1"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="url(#accent1)"/>
  <text x="20" y="35" font-family="'Segoe UI',Arial,sans-serif" font-size="18" font-weight="700" fill="#ccd6f6">🧑‍💻 About Me</text>
  <text x="20" y="60" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0">Name: <tspan fill="#ccd6f6" font-weight="600">Hariharan S</tspan></text>
  <text x="20" y="82" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0">Role: <tspan fill="#64ffda" font-weight="600">Founder &amp; Lead Developer @ Skyrovix</tspan></text>
  <text x="20" y="104" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0">Education: <tspan fill="#ccd6f6">B.Tech IT — Mount Zion College (2022–2026)</tspan></text>
  <text x="20" y="126" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0">Location: <tspan fill="#ccd6f6">📍 India</tspan></text>
  <text x="20" y="148" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0">Goal: <tspan fill="#48dbfb">"Build products that make a difference"</tspan></text>
  <!-- Animated pulse dot -->
  <circle cx="350" cy="20" r="4" fill="#64ffda">
    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <!-- Tech tags -->
  <rect x="20" y="165" width="55" height="22" rx="6" fill="#48dbfb" opacity="0.15"/>
  <text x="26" y="181" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#48dbfb">React</text>
  <rect x="83" y="165" width="55" height="22" rx="6" fill="#64ffda" opacity="0.15"/>
  <text x="89" y="181" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#64ffda">Node.js</text>
  <rect x="146" y="165" width="55" height="22" rx="6" fill="#ff6b6b" opacity="0.15"/>
  <text x="152" y="181" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#ff6b6b">Python</text>
  <rect x="209" y="165" width="70" height="22" rx="6" fill="#ff9ff3" opacity="0.15"/>
  <text x="215" y="181" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#ff9ff3">TypeScript</text>
  <rect x="287" y="165" width="65" height="22" rx="6" fill="#feca57" opacity="0.15"/>
  <text x="293" y="181" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#feca57">Supabase</text>
  <!-- Bottom glow -->
  <rect x="0" y="216" width="380" height="4" rx="2" fill="url(#accent1)" opacity="0.3"/>
</svg>

    </td>
    <td width="50%" valign="top">

<!-- Connect & Focus Card -->
<svg width="100%" height="220" viewBox="0 0 380 220">
  <defs>
    <linearGradient id="cardGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#112240;stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:#0a192f;stop-opacity:0.95"/>
    </linearGradient>
    <linearGradient id="accent2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff9ff3"/>
      <stop offset="100%" style="stop-color:#feca57"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="380" height="220" rx="16" fill="url(#cardGrad2)" stroke="#1d3461" stroke-width="1"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="url(#accent2)"/>
  <text x="20" y="35" font-family="'Segoe UI',Arial,sans-serif" font-size="18" font-weight="700" fill="#ccd6f6">🌐 Connect &amp; Focus</text>

  <!-- Connect buttons -->
  <a href="https://skyrovix.online">
    <rect x="20" y="52" width="160" height="30" rx="8" fill="#2d4059" stroke="#48dbfb" stroke-width="0.5">
      <animate attributeName="fill" values="#2d4059;#1d3461;#2d4059" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="60" y="72" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#48dbfb">🌍 skyrovix.online</text>
  </a>
  <a href="mailto:hariharanmahesh34@gmail.com">
    <rect x="195" y="52" width="160" height="30" rx="8" fill="#2d4059" stroke="#ff6b6b" stroke-width="0.5"/>
    <text x="235" y="72" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ff6b6b">✉️ Email</text>
  </a>

  <!-- Focus items with animated progress bars -->
  <text x="20" y="105" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#ccd6f6">🚀 Building Skyrovix</text>
  <rect x="20" y="112" width="330" height="4" rx="2" fill="#1d3461"/>
  <rect x="20" y="112" width="310" height="4" rx="2" fill="#48dbfb">
    <animate attributeName="width" from="0" to="310" dur="1.5s" fill="freeze"/>
  </rect>

  <text x="20" y="135" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#ccd6f6">⚛️ Mastering React &amp; Full Stack</text>
  <rect x="20" y="142" width="330" height="4" rx="2" fill="#1d3461"/>
  <rect x="20" y="142" width="280" height="4" rx="2" fill="#64ffda">
    <animate attributeName="width" from="0" to="280" dur="1.5s" begin="0.3s" fill="freeze"/>
  </rect>

  <text x="20" y="165" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#ccd6f6">🤖 Exploring AI-powered Web Apps</text>
  <rect x="20" y="172" width="330" height="4" rx="2" fill="#1d3461"/>
  <rect x="20" y="172" width="230" height="4" rx="2" fill="#ff6b6b">
    <animate attributeName="width" from="0" to="230" dur="1.5s" begin="0.6s" fill="freeze"/>
  </rect>

  <text x="20" y="195" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#ccd6f6">🌍 Contributing to Open Source</text>
  <rect x="20" y="202" width="330" height="4" rx="2" fill="#1d3461"/>
  <rect x="20" y="202" width="200" height="4" rx="2" fill="#ff9ff3">
    <animate attributeName="width" from="0" to="200" dur="1.5s" begin="0.9s" fill="freeze"/>
  </rect>
</svg>

    </td>
  </tr>
</table>

<p align="center">
  <svg width="90%" height="30" viewBox="0 0 800 30">
    <line x1="50" y1="15" x2="350" y2="15" stroke="#48dbfb" stroke-width="1" opacity="0.4"/>
    <circle cx="400" cy="15" r="4" fill="#64ffda">
      <animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="15" x2="750" y2="15" stroke="#ff9ff3" stroke-width="1" opacity="0.4"/>
  </svg>
</p>

<!-- Tech Stack Section -->
<svg width="100%" height="60" viewBox="0 0 800 60">
  <text x="400" y="30" font-family="'Segoe UI',Arial,sans-serif" font-size="20" font-weight="700" fill="#ccd6f6" text-anchor="middle">🛠️ Tech Stack</text>
  <text x="400" y="50" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#8892b0" text-anchor="middle">Technologies I work with daily</text>
</svg>

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,ts,react,vite,tailwind,nodejs,express,python,supabase,mysql,git,github,vscode,figma,postman&perline=9" />
</p>

<p align="center">
  <svg width="90%" height="30" viewBox="0 0 800 30">
    <line x1="50" y1="15" x2="350" y2="15" stroke="#48dbfb" stroke-width="1" opacity="0.4"/>
    <circle cx="400" cy="15" r="4" fill="#ff9ff3">
      <animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="15" x2="750" y2="15" stroke="#ff9ff3" stroke-width="1" opacity="0.4"/>
  </svg>
</p>

<!-- GitHub Analytics Section -->
<svg width="100%" height="60" viewBox="0 0 800 60">
  <text x="400" y="30" font-family="'Segoe UI',Arial,sans-serif" font-size="20" font-weight="700" fill="#ccd6f6" text-anchor="middle">📊 GitHub Analytics</text>
  <text x="400" y="50" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#8892b0" text-anchor="middle">Real-time stats from my GitHub profile</text>
</svg>

<div align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=hariharan1022&show_icons=true&theme=radical&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=48dbfb&icon_color=ff6b6b&text_color=ccd6f6" alt="Stats"/>
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=hariharan1022&layout=compact&theme=radical&hide_border=true&langs_count=6&bg_color=0d1117&title_color=48dbfb&text_color=ccd6f6" alt="Top Langs"/>
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=hariharan1022&theme=radical&hide_border=true&background=0d1117&stroke=48dbfb&ring=ff6b6b&fire=ff6b6b&currStreakLabel=ccd6f6" alt="Streak"/>
</div>

<p align="center">
  <svg width="90%" height="30" viewBox="0 0 800 30">
    <line x1="50" y1="15" x2="350" y2="15" stroke="#48dbfb" stroke-width="1" opacity="0.4"/>
    <circle cx="400" cy="15" r="4" fill="#feca57">
      <animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="15" x2="750" y2="15" stroke="#ff9ff3" stroke-width="1" opacity="0.4"/>
  </svg>
</p>

<!-- Achievements & Activity Graph -->
<table>
  <tr>
    <td width="50%" valign="top" align="center">
      <svg width="100%" height="50" viewBox="0 0 380 50">
        <text x="190" y="25" font-family="'Segoe UI',Arial,sans-serif" font-size="18" font-weight="700" fill="#ccd6f6" text-anchor="middle">🏆 Achievements</text>
        <text x="190" y="45" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#8892b0" text-anchor="middle">Milestones &amp; trophies</text>
      </svg>
      <img src="https://github-profile-trophy.vercel.app/?username=hariharan1022&theme=radical&no-frame=true&column=4&margin-w=10&margin-h=10" alt="Trophies"/>
    </td>
    <td width="50%" valign="top" align="center">
      <svg width="100%" height="50" viewBox="0 0 380 50">
        <text x="190" y="25" font-family="'Segoe UI',Arial,sans-serif" font-size="18" font-weight="700" fill="#ccd6f6" text-anchor="middle">📈 Contribution Graph</text>
        <text x="190" y="45" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#8892b0" text-anchor="middle">My coding activity over time</text>
      </svg>
      <img src="https://github-readme-activity-graph.vercel.app/graph?username=hariharan1022&theme=react-dark&hide_border=true&area=true&bg_color=0d1117&color=48dbfb&line=ff6b6b&point=ccd6f6" alt="Contribution Graph"/>
    </td>
  </tr>
</table>

<!-- FOOTER - Animated Waving SVG Footer -->
<p align="center">
  <svg width="100%" height="120" viewBox="0 0 1000 120" style="display:block">
    <defs>
      <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#48dbfb">
          <animate attributeName="stop-color" values="#48dbfb;#ff6b6b;#ff9ff3;#48dbfb" dur="8s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" style="stop-color:#ff6b6b">
          <animate attributeName="stop-color" values="#ff6b6b;#ff9ff3;#48dbfb;#ff6b6b" dur="8s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
    </defs>
    <!-- Wave 1 -->
    <path d="M0,60 C250,100 500,20 1000,60 L1000,120 L0,120 Z" fill="url(#waveGrad)" opacity="0.15">
      <animate attributeName="d" values="M0,60 C250,100 500,20 1000,60 L1000,120 L0,120 Z;M0,70 C250,30 500,90 1000,70 L1000,120 L0,120 Z;M0,60 C250,100 500,20 1000,60 L1000,120 L0,120 Z" dur="5s" repeatCount="indefinite"/>
    </path>
    <!-- Wave 2 -->
    <path d="M0,70 C250,30 500,90 1000,70 L1000,120 L0,120 Z" fill="url(#waveGrad)" opacity="0.1">
      <animate attributeName="d" values="M0,70 C250,30 500,90 1000,70 L1000,120 L0,120 Z;M0,60 C250,100 500,20 1000,60 L1000,120 L0,120 Z;M0,70 C250,30 500,90 1000,70 L1000,120 L0,120 Z" dur="5s" begin="0.5s" repeatCount="indefinite"/>
    </path>
    <!-- Footer text -->
    <text x="500" y="100" font-family="'Segoe UI',Arial,sans-serif" font-size="16" font-weight="600" fill="#ccd6f6" text-anchor="middle" opacity="0.9">
      ⭐ Thanks for visiting! Let's connect and build something amazing.
    </text>
  </svg>
</p>

<p align="center">
  <svg width="200" height="30" viewBox="0 0 200 30">
    <text x="100" y="20" font-family="monospace" font-size="12" fill="#8892b0" text-anchor="middle" opacity="0.7">
      &lt;/&gt; with ❤️ by Hariharan S
    </text>
  </svg>
</p>
