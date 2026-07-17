<p align="center">
  <svg width="100%" height="160" viewBox="0 0 800 160">
    <defs>
      <linearGradient id="rainbow" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ff6b6b">
          <animate attributeName="stop-color" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="4s" repeatCount="indefinite"/>
        </stop>
        <stop offset="25%" stop-color="#feca57">
          <animate attributeName="stop-color" values="#feca57;#48dbfb;#ff9ff3;#ff6b6b;#feca57" dur="4s" repeatCount="indefinite"/>
        </stop>
        <stop offset="50%" stop-color="#48dbfb">
          <animate attributeName="stop-color" values="#48dbfb;#ff9ff3;#ff6b6b;#feca57;#48dbfb" dur="4s" repeatCount="indefinite"/>
        </stop>
        <stop offset="75%" stop-color="#ff9ff3">
          <animate attributeName="stop-color" values="#ff9ff3;#ff6b6b;#feca57;#48dbfb;#ff9ff3" dur="4s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" stop-color="#ff6b6b">
          <animate attributeName="stop-color" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="4s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
      <linearGradient id="rainbow2" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#48dbfb">
          <animate attributeName="stop-color" values="#48dbfb;#ff9ff3;#ff6b6b;#feca57;#48dbfb" dur="5s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" stop-color="#ff6b6b">
          <animate attributeName="stop-color" values="#ff6b6b;#48dbfb;#feca57;#ff9ff3;#ff6b6b" dur="5s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
      <linearGradient id="shine" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="rgba(255,255,255,0)"/>
        <stop offset="50%" stop-color="rgba(255,255,255,0.3)"/>
        <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
        <animateTransform attributeName="gradientTransform" type="translate" from="-1 0" to="1 0" dur="2s" repeatCount="indefinite"/>
      </linearGradient>
      <filter id="glow">
        <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <!-- Floating background circles -->
    <circle cx="100" cy="30" r="3" fill="#ff6b6b" opacity="0.6">
      <animate attributeName="cy" values="30;20;30" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="700" cy="40" r="4" fill="#48dbfb" opacity="0.5">
      <animate attributeName="cy" values="40;25;40" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="400" cy="120" r="2" fill="#feca57" opacity="0.6">
      <animate attributeName="cy" values="120;110;120" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="200" cy="100" r="3" fill="#ff9ff3" opacity="0.4">
      <animate attributeName="cy" values="100;85;100" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="600" cy="20" r="2" fill="#64ffda" opacity="0.5">
      <animate attributeName="cy" values="20;10;20" dur="3.2s" repeatCount="indefinite"/>
    </circle>

    <!-- Main name - rainbow animated -->
    <text x="400" y="65" font-family="'Segoe UI',Arial,sans-serif" font-size="48" font-weight="900" fill="url(#rainbow)" text-anchor="middle" filter="url(#glow)">Hariharan S</text>

    <!-- Role badges with animated colors -->
    <rect x="180" y="85" width="130" height="28" rx="14" fill="#ff6b6b" opacity="0.15" stroke="#ff6b6b" stroke-width="1">
      <animate attributeName="stroke" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="245" y="104" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ff6b6b" text-anchor="middle" font-weight="600">
      <animate attributeName="fill" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="4s" repeatCount="indefinite"/>Founder @ Skyrovix</text>

    <rect x="335" y="85" width="130" height="28" rx="14" fill="#48dbfb" opacity="0.15" stroke="#48dbfb" stroke-width="1">
      <animate attributeName="stroke" values="#48dbfb;#ff9ff3;#ff6b6b;#feca57;#48dbfb" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="400" y="104" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#48dbfb" text-anchor="middle" font-weight="600">
      <animate attributeName="fill" values="#48dbfb;#ff9ff3;#ff6b6b;#feca57;#48dbfb" dur="4s" repeatCount="indefinite"/>Full Stack Engineer</text>

    <rect x="490" y="85" width="130" height="28" rx="14" fill="#ff9ff3" opacity="0.15" stroke="#ff9ff3" stroke-width="1">
      <animate attributeName="stroke" values="#ff9ff3;#ff6b6b;#feca57;#48dbfb;#ff9ff3" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="555" y="104" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ff9ff3" text-anchor="middle" font-weight="600">
      <animate attributeName="fill" values="#ff9ff3;#ff6b6b;#feca57;#48dbfb;#ff9ff3" dur="4s" repeatCount="indefinite"/>React Developer</text>

    <!-- Animated subtitle with typing dots -->
    <text x="400" y="135" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0" text-anchor="middle">
      Building modern web apps
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
    </text>
  </svg>
</p>

<div align="center">
  <a href="https://skyrovix.online"><img src="https://img.shields.io/badge/Website-skyrovix.online-6C63FF?style=for-the-badge&logo=vercel&logoColor=white" alt="Website"/></a>
  <a href="mailto:hariharanmahesh34@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/hariharan1022"><img src="https://img.shields.io/badge/GitHub-hariharan1022-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
</div>

<br/>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=hariharan1022&style=for-the-badge&color=ff6b6b" alt="Views"/>
  <img src="https://img.shields.io/github/followers/hariharan1022?style=for-the-badge&color=feca57" alt="Followers"/>
  <img src="https://img.shields.io/github/stars/hariharan1022?style=for-the-badge&color=48dbfb" alt="Stars"/>
</div>

<!-- Animated rainbow divider -->
<p align="center">
  <svg width="90%" height="40" viewBox="0 0 800 40">
    <line x1="50" y1="20" x2="350" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
    <circle cx="400" cy="20" r="6" fill="#ff6b6b">
      <animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="fill" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="3s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="20" x2="750" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
  </svg>
</p>

<!-- About Me - Animated Card -->
<table>
  <tr>
    <td width="55%" valign="top">

<svg width="100%" height="310" viewBox="0 0 420 310">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#161b22" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff6b6b"/>
      <stop offset="25%" stop-color="#feca57"/>
      <stop offset="50%" stop-color="#48dbfb"/>
      <stop offset="75%" stop-color="#ff9ff3"/>
      <stop offset="100%" stop-color="#64ffda"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="420" height="310" rx="16" fill="url(#cardBg)" stroke="url(#cardBorder)" stroke-width="2"/>
  <!-- Shine effect -->
  <rect x="0" y="0" width="420" height="310" rx="16" fill="url(#shine)"/>

  <!-- Pulse dot -->
  <circle cx="390" cy="25" r="5" fill="#64ffda">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="390" cy="25" r="10" fill="none" stroke="#64ffda" stroke-width="1" opacity="0.3">
    <animate attributeName="r" values="5;15;5" dur="1.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0;0.5" dur="1.5s" repeatCount="indefinite"/>
  </circle>

  <text x="20" y="40" font-family="'Segoe UI',Arial,sans-serif" font-size="22" font-weight="800" fill="url(#rainbow)">🧑‍💻 About Me</text>

  <!-- Animated timeline line -->
  <line x1="20" y1="60" x2="20" y2="280" stroke="#1d3461" stroke-width="2"/>
  <line x1="20" y1="60" x2="20" y2="280" stroke="url(#rainbow2)" stroke-width="2" stroke-dasharray="300" stroke-dashoffset="300">
    <animate attributeName="stroke-dashoffset" from="300" to="0" dur="2s" fill="freeze"/>
  </line>

  <!-- Info items with animated dots -->
  <circle cx="20" cy="78" r="4" fill="#ff6b6b">
    <animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="38" y="83" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#8892b0">Name: <tspan fill="#ccd6f6" font-weight="700">Hariharan S</tspan></text>

  <circle cx="20" cy="108" r="4" fill="#feca57">
    <animate attributeName="r" values="3;5;3" dur="2s" begin="0.3s" repeatCount="indefinite"/>
  </circle>
  <text x="38" y="113" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#8892b0">Role: <tspan fill="#64ffda" font-weight="700">Founder &amp; Lead Developer @ Skyrovix</tspan></text>

  <circle cx="20" cy="138" r="4" fill="#48dbfb">
    <animate attributeName="r" values="3;5;3" dur="2s" begin="0.6s" repeatCount="indefinite"/>
  </circle>
  <text x="38" y="143" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#8892b0">Education: <tspan fill="#ccd6f6">B.Tech IT — Mount Zion College (2022–2026)</tspan></text>

  <circle cx="20" cy="168" r="4" fill="#ff9ff3">
    <animate attributeName="r" values="3;5;3" dur="2s" begin="0.9s" repeatCount="indefinite"/>
  </circle>
  <text x="38" y="173" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#8892b0">Location: <tspan fill="#ccd6f6">📍 India</tspan></text>

  <circle cx="20" cy="198" r="4" fill="#64ffda">
    <animate attributeName="r" values="3;5;3" dur="2s" begin="1.2s" repeatCount="indefinite"/>
  </circle>
  <text x="38" y="203" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#8892b0">Goal: <tspan fill="#48dbfb" font-style="italic">"Build products that make a difference"</tspan></text>

  <!-- Animated skill tags -->
  <g transform="translate(20, 225)">
    <rect x="0" y="0" width="65" height="26" rx="8" fill="#ff6b6b" opacity="0.15">
      <animate attributeName="opacity" values="0.15;0.3;0.15" dur="2s" repeatCount="indefinite"/>
    </rect>
    <text x="32" y="18" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ff6b6b" text-anchor="middle" font-weight="600">JavaScript</text>

    <rect x="73" y="0" width="60" height="26" rx="8" fill="#48dbfb" opacity="0.15">
      <animate attributeName="opacity" values="0.15;0.3;0.15" dur="2s" begin="0.5s" repeatCount="indefinite"/>
    </rect>
    <text x="103" y="18" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#48dbfb" text-anchor="middle" font-weight="600">TypeScript</text>

    <rect x="141" y="0" width="55" height="26" rx="8" fill="#64ffda" opacity="0.15">
      <animate attributeName="opacity" values="0.15;0.3;0.15" dur="2s" begin="1s" repeatCount="indefinite"/>
    </rect>
    <text x="168" y="18" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#64ffda" text-anchor="middle" font-weight="600">React</text>

    <rect x="204" y="0" width="65" height="26" rx="8" fill="#feca57" opacity="0.15">
      <animate attributeName="opacity" values="0.15;0.3;0.15" dur="2s" begin="1.5s" repeatCount="indefinite"/>
    </rect>
    <text x="236" y="18" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#feca57" text-anchor="middle" font-weight="600">Node.js</text>

    <rect x="277" y="0" width="60" height="26" rx="8" fill="#ff9ff3" opacity="0.15">
      <animate attributeName="opacity" values="0.15;0.3;0.15" dur="2s" begin="2s" repeatCount="indefinite"/>
    </rect>
    <text x="307" y="18" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ff9ff3" text-anchor="middle" font-weight="600">Python</text>

    <rect x="0" y="34" width="70" height="26" rx="8" fill="#a29bfe" opacity="0.15"/>
    <text x="35" y="52" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#a29bfe" text-anchor="middle" font-weight="600">Supabase</text>

    <rect x="78" y="34" width="50" height="26" rx="8" fill="#e17055" opacity="0.15"/>
    <text x="103" y="52" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#e17055" text-anchor="middle" font-weight="600">MySQL</text>

    <rect x="136" y="34" width="75" height="26" rx="8" fill="#00cec9" opacity="0.15"/>
    <text x="173" y="52" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#00cec9" text-anchor="middle" font-weight="600">Tailwind</text>

    <rect x="219" y="34" width="40" height="26" rx="8" fill="#fd79a8" opacity="0.15"/>
    <text x="239" y="52" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#fd79a8" text-anchor="middle" font-weight="600">Git</text>
  </g>
</svg>

    </td>
    <td width="45%" valign="top">

<svg width="100%" height="310" viewBox="0 0 360 310">
  <defs>
    <linearGradient id="cardBg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#161b22" stop-opacity="0.95"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="360" height="310" rx="16" fill="url(#cardBg2)" stroke="url(#cardBorder)" stroke-width="2"/>
  <rect x="0" y="0" width="360" height="310" rx="16" fill="url(#shine)"/>

  <text x="20" y="40" font-family="'Segoe UI',Arial,sans-serif" font-size="22" font-weight="800" fill="url(#rainbow)">🎯 Current Focus</text>

  <!-- Focus items with animated bars -->
  <text x="20" y="75" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#ccd6f6">🚀 Building Skyrovix</text>
  <rect x="20" y="85" width="320" height="8" rx="4" fill="#1d3461"/>
  <rect x="20" y="85" width="310" height="8" rx="4" fill="#ff6b6b">
    <animate attributeName="width" from="0" to="310" dur="1.5s" fill="freeze"/>
  </rect>
  <text x="340" y="92" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#ff6b6b" text-anchor="end" font-weight="700">95%</text>

  <text x="20" y="115" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#ccd6f6">⚛️ Mastering React &amp; Full Stack</text>
  <rect x="20" y="125" width="320" height="8" rx="4" fill="#1d3461"/>
  <rect x="20" y="125" width="280" height="8" rx="4" fill="#feca57">
    <animate attributeName="width" from="0" to="280" dur="1.5s" begin="0.3s" fill="freeze"/>
  </rect>
  <text x="340" y="132" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#feca57" text-anchor="end" font-weight="700">85%</text>

  <text x="20" y="155" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#ccd6f6">🤖 Exploring AI-powered Web Apps</text>
  <rect x="20" y="165" width="320" height="8" rx="4" fill="#1d3461"/>
  <rect x="20" y="165" width="230" height="8" rx="4" fill="#48dbfb">
    <animate attributeName="width" from="0" to="230" dur="1.5s" begin="0.6s" fill="freeze"/>
  </rect>
  <text x="340" y="172" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#48dbfb" text-anchor="end" font-weight="700">70%</text>

  <text x="20" y="195" font-family="'Segoe UI',Arial,sans-serif" font-size="14" fill="#ccd6f6">🌍 Contributing to Open Source</text>
  <rect x="20" y="205" width="320" height="8" rx="4" fill="#1d3461"/>
  <rect x="20" y="205" width="200" height="8" rx="4" fill="#ff9ff3">
    <animate attributeName="width" from="0" to="200" dur="1.5s" begin="0.9s" fill="freeze"/>
  </rect>
  <text x="340" y="212" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="#ff9ff3" text-anchor="end" font-weight="700">60%</text>

  <!-- Animated spinning ring -->
  <circle cx="300" cy="285" r="20" fill="none" stroke="url(#rainbow)" stroke-width="3" stroke-dasharray="30 80">
    <animateTransform attributeName="transform" type="rotate" from="0 300 285" to="360 300 285" dur="3s" repeatCount="indefinite"/>
  </circle>
  <text x="300" y="290" font-family="'Segoe UI',Arial,sans-serif" font-size="10" fill="#8892b0" text-anchor="middle">⚡</text>

  <!-- Connect heading -->
  <text x="20" y="250" font-family="'Segoe UI',Arial,sans-serif" font-size="16" font-weight="700" fill="url(#rainbow)">📬 Let's Connect</text>

  <a href="https://skyrovix.online">
    <rect x="20" y="265" width="140" height="32" rx="8" fill="#ff6b6b" opacity="0.15" stroke="#ff6b6b" stroke-width="1">
      <animate attributeName="fill" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="4s" repeatCount="indefinite" additive="sum"/>
    </rect>
    <text x="90" y="286" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ccd6f6" text-anchor="middle" font-weight="600">🌍 Website</text>
  </a>

  <a href="mailto:hariharanmahesh34@gmail.com">
    <rect x="175" y="265" width="140" height="32" rx="8" fill="#48dbfb" opacity="0.15" stroke="#48dbfb" stroke-width="1"/>
    <text x="245" y="286" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#ccd6f6" text-anchor="middle" font-weight="600">✉️ Email</text>
  </a>
</svg>

    </td>
  </tr>
</table>

<!-- Animated rainbow divider -->
<p align="center">
  <svg width="90%" height="40" viewBox="0 0 800 40">
    <line x1="50" y1="20" x2="350" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
    <circle cx="400" cy="20" r="6" fill="#64ffda">
      <animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="fill" values="#64ffda;#ff6b6b;#feca57;#48dbfb;#64ffda" dur="3s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="20" x2="750" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
  </svg>
</p>

<!-- Tech Stack -->
<svg width="100%" height="70" viewBox="0 0 800 70">
  <defs>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff6b6b"/>
      <stop offset="33%" stop-color="#feca57"/>
      <stop offset="66%" stop-color="#48dbfb"/>
      <stop offset="100%" stop-color="#ff9ff3"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="5s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="400" y="35" font-family="'Segoe UI',Arial,sans-serif" font-size="24" font-weight="800" fill="url(#titleGrad)" text-anchor="middle">🛠️ Tech Stack</text>
  <text x="400" y="55" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0" text-anchor="middle">
    Tools &amp; technologies I use daily
    <animate attributeName="opacity" values="0.4;1;0.4" dur="3s" repeatCount="indefinite"/>
  </text>
</svg>

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,ts,react,vite,tailwind,nodejs,express,python,supabase,mysql,git,github,vscode,figma,postman&perline=9" alt="Tech Stack"/>
</p>

<!-- Animated rainbow divider -->
<p align="center">
  <svg width="90%" height="40" viewBox="0 0 800 40">
    <line x1="50" y1="20" x2="350" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
    <circle cx="400" cy="20" r="6" fill="#ff9ff3">
      <animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="fill" values="#ff9ff3;#64ffda;#ff6b6b;#feca57;#ff9ff3" dur="3s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="20" x2="750" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
  </svg>
</p>

<!-- GitHub Stats -->
<svg width="100%" height="70" viewBox="0 0 800 70">
  <text x="400" y="35" font-family="'Segoe UI',Arial,sans-serif" font-size="24" font-weight="800" fill="url(#titleGrad)" text-anchor="middle">📊 GitHub Analytics</text>
  <text x="400" y="55" font-family="'Segoe UI',Arial,sans-serif" font-size="13" fill="#8892b0" text-anchor="middle">
    Real-time stats from my activity
    <animate attributeName="opacity" values="0.4;1;0.4" dur="3s" repeatCount="indefinite"/>
  </text>
</svg>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=hariharan1022&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=0D1117&title_color=ff6b6b&text_color=C9D1D9&icon_color=feca57&ring_color=48dbfb"/>
    <img height="170" src="https://github-readme-stats.vercel.app/api?username=hariharan1022&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=0D1117&title_color=ff6b6b&text_color=C9D1D9&icon_color=feca57&ring_color=48dbfb"/>
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=hariharan1022&layout=compact&hide_border=true&bg_color=0D1117&title_color=48dbfb&text_color=C9D1D9&langs_count=6"/>
    <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=hariharan1022&layout=compact&hide_border=true&bg_color=0D1117&title_color=48dbfb&text_color=C9D1D9&langs_count=6"/>
  </picture>
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=hariharan1022&hide_border=true&background=0D1117&stroke=ff6b6b&ring=feca57&fire=ff6b6b&currStreakLabel=48dbfb&sideLabels=C9D1D9"/>
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=hariharan1022&hide_border=true&background=0D1117&stroke=ff6b6b&ring=feca57&fire=ff6b6b&currStreakLabel=48dbfb&sideLabels=C9D1D9"/>
  </picture>
</div>

<!-- Animated rainbow divider -->
<p align="center">
  <svg width="90%" height="40" viewBox="0 0 800 40">
    <line x1="50" y1="20" x2="350" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
    <circle cx="400" cy="20" r="6" fill="#feca57">
      <animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="fill" values="#feca57;#48dbfb;#ff9ff3;#64ffda;#feca57" dur="3s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="20" x2="750" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
  </svg>
</p>

<!-- Achievements & Activity Graph -->
<table>
  <tr>
    <td width="50%" valign="top" align="center">

<svg width="100%" height="55" viewBox="0 0 380 55">
  <text x="190" y="28" font-family="'Segoe UI',Arial,sans-serif" font-size="20" font-weight="800" fill="url(#rainbow)" text-anchor="middle">🏆 Achievements</text>
  <text x="190" y="48" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#8892b0" text-anchor="middle">
    Milestones unlocked
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2.5s" repeatCount="indefinite"/>
  </text>
</svg>

<img src="https://github-profile-trophy.vercel.app/?username=hariharan1022&theme=radical&no-frame=true&column=4&margin-w=15&margin-h=15" alt="Trophies"/>

    </td>
    <td width="50%" valign="top" align="center">

<svg width="100%" height="55" viewBox="0 0 380 55">
  <text x="190" y="28" font-family="'Segoe UI',Arial,sans-serif" font-size="20" font-weight="800" fill="url(#rainbow)" text-anchor="middle">📈 Activity Graph</text>
  <text x="190" y="48" font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#8892b0" text-anchor="middle">
    Coding activity over time
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2.5s" repeatCount="indefinite"/>
  </text>
</svg>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=hariharan1022&theme=github-dark&hide_border=true&area=true&color=48dbfb&line=ff6b6b&point=feca57"/>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=hariharan1022&theme=github-dark&hide_border=true&area=true&color=48dbfb&line=ff6b6b&point=feca57"/>
</picture>

    </td>
  </tr>
</table>

<!-- Animated rainbow divider -->
<p align="center">
  <svg width="90%" height="40" viewBox="0 0 800 40">
    <line x1="50" y1="20" x2="350" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
    <circle cx="400" cy="20" r="6" fill="#48dbfb">
      <animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="fill" values="#48dbfb;#ff9ff3;#64ffda;#ff6b6b;#48dbfb" dur="3s" repeatCount="indefinite"/>
    </circle>
    <line x1="450" y1="20" x2="750" y2="20" stroke="url(#rainbow)" stroke-width="2" stroke-dasharray="8 4"/>
  </svg>
</p>

<!-- Animated Footer -->
<p align="center">
  <svg width="100%" height="180" viewBox="0 0 1000 180" style="display:block">
    <defs>
      <linearGradient id="waveGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ff6b6b">
          <animate attributeName="stop-color" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="6s" repeatCount="indefinite"/>
        </stop>
        <stop offset="50%" stop-color="#48dbfb">
          <animate attributeName="stop-color" values="#48dbfb;#ff9ff3;#ff6b6b;#feca57;#48dbfb" dur="6s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" stop-color="#ff9ff3">
          <animate attributeName="stop-color" values="#ff9ff3;#ff6b6b;#feca57;#48dbfb;#ff9ff3" dur="6s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
      <linearGradient id="waveGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#feca57">
          <animate attributeName="stop-color" values="#feca57;#48dbfb;#ff9ff3;#ff6b6b;#feca57" dur="6s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" stop-color="#ff6b6b">
          <animate attributeName="stop-color" values="#ff6b6b;#feca57;#48dbfb;#ff9ff3;#ff6b6b" dur="6s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
    </defs>
    <!-- Wave 1 -->
    <path d="M0,80 C200,130 400,30 600,90 C800,150 900,40 1000,80 L1000,180 L0,180 Z" fill="url(#waveGrad1)" opacity="0.15">
      <animate attributeName="d" values="M0,80 C200,130 400,30 600,90 C800,150 900,40 1000,80 L1000,180 L0,180 Z;M0,90 C200,40 400,120 600,60 C800,10 900,110 1000,90 L1000,180 L0,180 Z;M0,80 C200,130 400,30 600,90 C800,150 900,40 1000,80 L1000,180 L0,180 Z" dur="6s" repeatCount="indefinite"/>
    </path>
    <!-- Wave 2 -->
    <path d="M0,100 C200,50 400,140 600,80 C800,20 900,100 1000,100 L1000,180 L0,180 Z" fill="url(#waveGrad2)" opacity="0.1">
      <animate attributeName="d" values="M0,100 C200,50 400,140 600,80 C800,20 900,100 1000,100 L1000,180 L0,180 Z;M0,80 C200,120 400,40 600,100 C800,160 900,60 1000,80 L1000,180 L0,180 Z;M0,100 C200,50 400,140 600,80 C800,20 900,100 1000,100 L1000,180 L0,180 Z" dur="6s" begin="1s" repeatCount="indefinite"/>
    </path>
    <!-- Wave 3 -->
    <path d="M0,110 C200,80 400,130 600,70 C800,30 900,120 1000,110 L1000,180 L0,180 Z" fill="url(#rainbow)" opacity="0.08">
      <animate attributeName="d" values="M0,110 C200,80 400,130 600,70 C800,30 900,120 1000,110 L1000,180 L0,180 Z;M0,95 C200,140 400,60 600,110 C800,150 900,70 1000,95 L1000,180 L0,180 Z;M0,110 C200,80 400,130 600,70 C800,30 900,120 1000,110 L1000,180 L0,180 Z" dur="6s" begin="2s" repeatCount="indefinite"/>
    </path>

    <!-- Floating sparkles -->
    <text x="150" y="50" font-size="16" opacity="0.6">✦</text>
  <animate attributeName="y" values="50;30;50" dur="3s" repeatCount="indefinite"/>
  <text x="850" y="40" font-size="12" opacity="0.5">✦
    <animate attributeName="y" values="40;20;40" dur="4s" repeatCount="indefinite"/>
  </text>
  <text x="500" y="60" font-size="10" opacity="0.4">✦
    <animate attributeName="y" values="60;40;60" dur="3.5s" repeatCount="indefinite"/>
  </text>

  <!-- Main footer text -->
  <text x="500" y="150" font-family="'Segoe UI',Arial,sans-serif" font-size="18" font-weight="700" fill="url(#rainbow)" text-anchor="middle">
    ⭐ Thanks for visiting! Let's build something amazing together. ⭐
  </text>
</svg>

<p align="center">
  <svg width="250" height="30" viewBox="0 0 250 30">
    <text x="125" y="20" font-family="monospace" font-size="13" fill="#8892b0" text-anchor="middle" opacity="0.7">
      &lt;/&gt; with ❤️ by Hariharan S
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
    </text>
  </svg>
</p>
