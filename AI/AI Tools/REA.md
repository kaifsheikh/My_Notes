# What is REA:

1. REA – Reverse Engineer Anything by erisvulgaris ek AI-powered reverse engineering toolkit hai. Iska purpose hai kisi existing software, application ya website ko uske original source code ke baghair investigate karna, samajhna aur uski functionality ko apne project mein dobara implement karne mein AI agent ki help lena.

2. Suppose tumne ek website dekhi jisme:
   - Bohat impressive search system hai.
   - Live animations hain.
   - Login aur authentication system hai.
   - Advanced dashboard hai.
   - Data automatically update hota hai.
     Tumhare paas us website ka original source code nahi hai.

3. Ab tumhare paas do options hain:

4. Khud manually investigate karo ke website kaise kaam karti hai.
5. **REA** ki madad se AI agent ko investigation karne do. REA doosre option mein help karta hai.
   - Ye application ke internal structure, available code, functions, strings, API-related evidence aur behavior ko investigate karta hai.

   - Important: REA original source code recover karne ya poori website ko automatically clone karne ka claim nahi karta. Ye evidence ki basis par software ki functionality samajhne mein help karta hai.

---

# REA ka complete setup — Windows + website analysis

Official repository: [morluto/rea — GitHub](https://github.com/morluto/rea?utm_source=chatgpt.com)

Tumhara goal ye hai:

1. Apne Windows computer par REA install karna.
2. AI coding agent ke saath connect karna.
3. Chrome browser connect karna.
4. Kisi website ko investigate karna.
5. Us website ke frontend, JavaScript, API aur interactive behavior ko samajhna.
6. Investigation ke basis par apni PHP + MySQL website banana.

Important: Website analysis ke liye tumhein Ghidra, Hopper ya IDA install karne ki zaroorat nahi. Ye native binary analysis ke tools hain. REA ka website analysis Chrome-family browser se hota hai.&#x20;

## 1. Required software

1. **Node.js**
2. **Google Chrome**
3. **Target website inspection**
4. **Cursor** / **Claude Code** / **Opencode**

### Node.js install karo

1. [Node.js official download](https://nodejs.org/en/download?utm_source=chatgpt.com) open karo.
2. REA-supported version install karo:
   - Node.js 22.23.4+
   - Node.js 24.22.1+
   - Node.js 26.12.1+
3. Windows installer run karo.
4. Default installation options rehne do.
5. CMD open karo.

## 2. REA install

1. Ab CMD ya PowerShell open karo.
2. Ab official setup command run karo:

```cmd
npx rea-agents setup
```

Official installation command Ye command REA ka setup wizard start karegi.

Wizard mein:

1. Available AI agents detect honge.
2. Apna installed agent select karo.
3. Proposed MCP configuration review karo.
4. Workflow instructions aur agent integration approve karo.
5. Setup complete hone do.

Setup existing configuration ka backup bhi banata hai. Apne agent ko setup ke baad completely close karke restart karna.

## 3. REA installation verify karo

Ab apne terminal mein:

```
npx -y rea-agents@latest doctor
```

Ye diagnostic check karega ke required configuration aur dependencies theek hain ya nahi.

Uske baad REA CLI commands dekhne ke liye:

```
npx -y rea-agents@latest --help
```

Agar regular CLI installation chahte ho:

```
npm install --global rea-agents
```

Phir:

```
rea --help
```

Dono methods mein se ek use karna sufficient hai.&#x20;

## 4. Chrome ko REA ke saath connect karo

Ab sabse important step: Chrome ko debugging mode mein launch karna hai.

Chrome normal mode mein open rehne ke bajaye ek separate profile use karenge. Isse tumhare personal browser sessions alag rahenge.

### Windows par Chrome launch karne ka tareeqa

PowerShell open karo aur ye command paste karo:

```
$chrome = "$env:ProgramFiles\Google\Chrome\Application\chrome.exe"

if (!(Test-Path $chrome)) {
    $chrome = "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe"
}

& $chrome `
  --remote-debugging-port=9222 `
  --user-data-dir="$env:LOCALAPPDATA\REA-Chrome-Profile" `
  "https://example.com"
```

`https://example.com` ko apni target website ke URL se replace karna.

[Google Chrome is upgrading video recording on Windows 11 with better quality, low size](https://images.openai.com/static-rsc-4/i10ARROmS-IBkG8-8Vmb-ATUWfgi_gIxZ479Jv8mtOUufWYPMEzcBf8oawel4VNc9EjQzGBRkyadk_We4toZjDfmky845BzXyw3QU-Z2cdjASr1DaYjHW1TMe9CMH4tudX0X1BVHPGxgT65H7AWJO6xQ7g3tlguOqRzgmaFHSZk?purpose=inline)

[windowslatest.com](https://www.windowslatest.com/2024/12/22/google-chrome-is-upgrading-video-recording-on-windows-11-with-better-quality-low-size/?utm_source=chatgpt.com)

Is command mein:

| Parameter                    | Kaam                                    |
| ---------------------------- | --------------------------------------- |
| `remote-debugging-port=9222` | REA ko Chrome se connect karne deta hai |
| `user-data-dir`              | Separate Chrome profile banata hai      |
| Website URL                  | Target website open karta hai           |

Security: Debugging port sirf apne computer ke loopback interface par accessible rakho. Is Chrome profile mein personal email, banking ya private accounts login mat karna. Investigation ke baad Chrome close kar do.

Chrome 136 se default browser profile par remote-debugging flags ignore ho sakte hain, isliye separate profile important hai.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com&sz=32)

GitHub

## 5. Check karo Chrome connection successful hai ya nahi

Ab ek doosra PowerShell terminal open karo.

Pehle ye command run karo:

```
Invoke-RestMethod http://127.0.0.1:9222/json/version
```

Agar Chrome properly start hua hai to browser version aur WebSocket information return honi chahiye.

Ab REA se browser tabs discover karo:

```
rea list-browser-targets http://127.0.0.1:9222 --json
```

Expected output ka simplified example:

```
{
  "targets": [
    {
      "id": "YOUR_TARGET_ID",
      "type": "page",
      "url": "https://example.com"
    }
  ]
}
```

Apne actual output se `id` copy karna. Ye har browser session mein change ho sakti hai.

Connection test passed

&#x20;ka matlab hoga ke REA tumhare Chrome browser ke page targets discover kar pa raha hai.

Official guide: [REA Browser Observation Documentation](https://github.com/morluto/rea/blob/main/docs/guides/web/browser-observation.md?utm_source=chatgpt.com).

## 6. Ab website ka actual analysis karo

Maan lo tumne Chrome mein `https://example.com` open ki hai.

### A. Page structure inspect karo

```
rea inspect-web-page http://127.0.0.1:9222 YOUR_TARGET_ID --json
```

Ye inspect kar sakta hai:

- DOM structure
- Accessibility nodes
- JavaScript scripts
- Page resources
- Network request metadata
- Console metadata
- Workers
- WebSocket frame sizes
- Selected storage information, agar explicitly request karo

### B. JavaScript bundles analyze karo

```
rea analyze-web-bundle http://127.0.0.1:9222 YOUR_TARGET_ID --json
```

Iska result tumhein ye samajhne mein help karega:

- JavaScript modules.
- Imports aur chunk relationships.
- Possible API endpoint references.
- Route candidates.
- Vendor libraries.
- Available source maps.

Ye static analysis hai: is operation mein JavaScript bundle ko execute nahi kiya jata.

### C. Website ke interactions observe karo

```
rea observe-web-session http://127.0.0.1:9222 YOUR_TARGET_ID --observation-ms 15000 --json
```

Command run karne ke baad Chrome mein khud website use karo:

1. Search bar mein text enter karo.
2. Search button press karo.
3. Filters change karo.
4. Different pages par navigate karo.
5. Dropdowns open karo.

REA selected observation window mein navigation aur lifecycle evidence collect karega.

Important: Ye passive observation hai. Ye command khud tumhare liye clicks perform nahi karti.

### D. Website screenshot capture karo

```
rea capture-web-screenshot http://127.0.0.1:9222 YOUR_TARGET_ID --json
```

Ye current visible viewport ka screenshot capture karega.

[Herramientas para desarrolladores de Chrome  |  Chrome DevTools  |  Chrome for Developers](https://images.openai.com/static-rsc-4/AugUhhuxyLd4NbcIGxx_pqjcVB9I-fNIwcHesliC1sU4oSK1t-lG1HNBRn7W0XepVDjT7thk7BG1v4x7_oqVdY0Ja3cKyxPcxUEsRKRpN-lIiIUTkPBRh8f42ewdecgzA-UaKaa2oYYuf1l-irZv7T-EdNjzjWFtPCiwmOeQN1M?purpose=inline)

[developer.chrome.com](https://developer.chrome.com/docs/devtools?hl=es-419&utm_source=chatgpt.com)

Ye chaar operations tumhari initial website investigation ke liye kaafi hain.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com&sz=32)

GitHub

## 7. AI agent ko REA MCP se connect karo

Abhi tak tumne REA ko terminal se use karne ka tareeqa seekha. Lekin REA ka sabse powerful use AI agent ke saath hai.

MCP ka matlab Model Context Protocol hai. Iske through Cursor ya doosra AI agent REA ke tools directly call kar sakta hai.

### Recommended: Cursor

[Setting Up MCP Servers for Your AI Agent Stack (2026) | Bytewaves](https://images.openai.com/static-rsc-4/wl_j7r_rl6lNd93nge0o_EFZ3vRnhyXeSeoC35WRId_hMbVR8gn-xCFqUo3_gswDPBikml-kQIazkVnQYLWeJg3rfTNJn0WjQ6GNXpgUmluaoJSvBSKvKqzlWsMFh5tuJZX4b1raTh--p2Z75jdxh4pmDFsnbMJcSEM7uxGnKJU?purpose=inline)

[bytewaves.news](https://bytewaves.news/tutorials/setting-up-mcp-servers-ai-agent-stack-2026/?utm_source=chatgpt.com)

Agar Cursor installed hai:

1\. PowerShell mein run karo:

```
npx rea-agents setup
```

2. Setup mein Cursor select karo.
3. Configuration changes review karo.
4. Approval do.
5. Cursor completely close karo.
6. Cursor dobara open karo.

Agar tumne pehle hi Cursor select kiya hai, dobara setup karne ki zaroorat nahi.

### MCP connection verify karo

Cursor mein apne project ko open karo aur Agent mode mein ye prompt do:

```
Check whether REA MCP server is connected.

List the available REA tools.

Do not perform any website analysis yet.

Tell me whether the connection is working.
```

Agar connection successful hai, agent available REA tools identify kar sakega.

Agar tools available nahi hain:

```
rea doctor --json
```

Run karo aur diagnostic output check karo.

Official setup documentation: [REA Agent and MCP configuration](https://github.com/morluto/rea/blob/main/docs/getting-started/installation.md?utm_source=chatgpt.com).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com&sz=32)

GitHub+1

# 8. Kisi complete website ki reverse engineering kaise karni hai?

Ab practical example karte hain.

Maan lo tum kisi website ko analyze karna chahte ho:

`https://example.com`

Tum Cursor Agent mein neeche diya gaya prompt use kar sakte ho.

Prompt 1 — Complete website investigation

&#x20;Copy

```
Use REA to investigate this website:

https://example.com

Perform a structured investigation.

STAGE 1:
Inspect website structure, DOM,
accessibility tree, resources,
scripts and screenshots.

STAGE 2:
Analyze JavaScript bundles,
modules, imports, routes,
source maps and API candidates.

STAGE 3:
Investigate network metadata
and observe user interactions.

STAGE 4:
Investigate search, navigation,
filters, dropdowns, animations
and responsive behavior.

STAGE 5:
Create a detailed technical report.

Include:
- Findings
- Supporting evidence
- Confidence levels
- Unknowns and limitations

Do not invent backend details.
Do not collect credentials.
Do not modify the target website.
Do not write code until the report
is complete.
```

AI agent ko pehle investigation report banani chahiye.

## 9. Investigation report mein kya hona chahiye?

Ye structure expect karo:

| Section              | Kya information milegi?                  |
| -------------------- | ---------------------------------------- |
| Website architecture | Pages aur structure                      |
| Frontend             | HTML, CSS, JavaScript                    |
| Components           | Header, footer, cards, modals            |
| Animations           | Observable animation behavior            |
| API                  | Available endpoints aur request metadata |
| Search               | Search aur filtering behavior            |
| Navigation           | Routing aur page transitions             |
| Responsive design    | Different viewport behavior              |
| Limitations          | Jo cheezein determine nahi ho sakin      |

Yaad rakho: browser se backend ka private source code ya database schema automatically nahi milta.

## 10. Ab apni website develop karwao

Jab investigation complete ho jaye to second prompt use karo.

Prompt 2 — Build similar functionality

&#x20;Copy

```
Using the completed REA investigation
report, build an original implementation.

Tech stack:
- PHP 8+
- MySQL
- HTML5
- CSS3
- JavaScript

Requirements:
1. Recreate observable layouts.
2. Implement similar animations.
3. Build search and filtering.
4. Create PHP backend endpoints.
5. Design MySQL database.
6. Use secure PDO queries.
7. Keep code modular.
8. Test all functionality.

Use the investigation report as evidence.
Do not copy proprietary assets or branding.
Ask before destructive project changes.
```

# 11. Common problems aur solutions

| Problem                    | Solution                                                   |
| -------------------------- | ---------------------------------------------------------- |
| `node is not recognized`   | Node.js PATH check karo                                    |
| `rea is not recognized`    | Global installation karo ya `npx` use karo                 |
| `endpoint_unreachable`     | Chrome debugging port check karo                           |
| Target ID missing          | `list-browser-targets` dobara run karo                     |
| Cursor mein MCP missing    | Cursor restart aur `rea doctor`                            |
| Bundle analysis fail       | Scripts aur source-map availability check karo             |
| Website ka backend unknown | Browser evidence se backend implementation assume mat karo |

# 12. Tumhare liye final checklist

REA setup progress

# 0/12

Node.js supported version install

npm version verify

Google Chrome install

AI coding agent install

REA setup command run

AI agent mein MCP connection verify

Dedicated Chrome debugging profile launch

Browser target ID discover

Website structure inspect

JavaScript bundle analyze

Interactions observe

Investigation report generate

## Ab practical installation shuru karte hain

Meri advice hai ke ek saath saari commands run mat karna. Pehle Node.js aur REA install karke verify karte hain.

Mujhe ye do cheezein batao:

1. Tum Cursor use karte ho ya VS Code?
2. Tumhare computer mein Node.js already installed hai ya abhi install karna hai?

In dono ke mutabiq main tumhein exact commands dunga. Hum pehle MCP connection successful karenge, phir tumhari pehli target website analyze karenge.

Official references:

- [Original REA GitHub repository](https://github.com/morluto/rea?utm_source=chatgpt.com)
- [Installation documentation](https://github.com/morluto/rea/blob/main/docs/getting-started/installation.md?utm_source=chatgpt.com)
- [Browser observation documentation](https://github.com/morluto/rea/blob/main/docs/guides/web/browser-observation.md?utm_source=chatgpt.com)
