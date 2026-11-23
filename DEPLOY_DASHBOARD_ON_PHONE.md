# Asli Streamlit Dashboard phone par kaise dekhein (Cloud link)

Dashboard ke 2 hisse hote hain, ye samajhna zaroori hai:
- **Server:** jo Python chalata hai, data banata / HiveMQ se leta hai.
  Ye phone par nahi chalega — Streamlit bahut bhaari hai, kam RAM wale
  phone par atak jaata hai.
- **Screen:** jo tum browser me dekhte ho. Ye phone par aaram se khulti hai.

Isliye asli dashboard ka **server Cloud par chalega, screen phone par
khulegi.** Tumhe phone par sirf ek link kholna hoga. Ye link free me
Streamlit Community Cloud se banta hai.

## Phone se hi deploy karo (koi laptop nahi chahiye)

### Step 1 — Code GitHub par daalo
1. Phone ke browser ya GitHub app me github.com kholo, login karo.
2. **New repository** banao (naam kuch bhi, jaise `compressor-dashboard`).
3. Is project ke zip ko phone me extract karo, phir GitHub repo me
   **Add file → Upload files** se saari files/folders upload karo.
   Zip file khud upload mat karo — uske andar ki files upload karo.
4. Commit kar do. `.env` file tumhare paas hai hi nahi (sirf
   `.env.example` hai), isliye password GitHub par nahi jayega.

### Step 2 — Streamlit Cloud par app banao
1. Phone ke browser me **share.streamlit.io** kholo, GitHub se login karo.
2. **New app** dabao:
   - Repository: tumhara naya repo select karo
   - Branch: `main`
   - Main file path: `layer2/dashboard_live.py`
3. **Deploy** dabao. Pehli baar 2–3 minute lag sakte hain.

### Step 3 — Pehle bina HiveMQ ke check karo (zaroori)
Deploy hote hi link kholo. Dashboard **simulation mode** me chalega —
readings aur charts dikhenge, har 5th reading me leak bhi aayega.
Agar ye dikh raha hai, to matlab deploy sahi hua hai, dashboard kaam
kar raha hai. Yehi sabse bada proof hai ki dashboard work kar raha hai.

### Step 4 — Asli HiveMQ data chahiye to Secrets daalo
1. Streamlit Cloud me app ke teen dots (⋮) → **Settings → Secrets** kholo.
2. `.streamlit/secrets.toml.example` wala format paste karo, aur asli
   values bharo:
   - Host: HiveMQ console se keenbee cluster ka host
   - Username/Password: HiveMQ console → Access Management →
     MQTT Credentials wale (website ka login password nahi)
3. **Save** karo, phir app ko **Reboot** karo.
4. Ab dashboard HiveMQ se live data dikhayega. Agar publisher nahi chal
   raha, to dashboard simulation mode me hi rahega — ye bhi theek hai,
   dashboard khaali nahi dikhega.

### Step 5 — Phone par aaram se kholo
Link ko phone ke Chrome me kholo, aur chaaho to **Add to Home screen**
kar lo — phir wo app jaisa dikhega, roz link dhoondhna nahi padega.

## Normal baatein (ghabrana nahi)
- Free Cloud app jab der tak use nahi hota, to so jaata hai. Dobara
  kholne par 1–2 minute lagna normal hai.
- Link kisi ko bhi bhej sakte ho — dashboard me koi password nahi hai,
  aur HiveMQ ka password Secrets me chhupa rehta hai, link me nahi dikhta.
- Login wala dashboard chahiye to main file path badal ke
  `layer5/dashboard_login.py` select karo. Usme demo login hai:
  admin / admin123, viewer / viewer123.

## Turant wala option (agar Cloud abhi nahi karna)
`mobile-dashboard.html` ko phone ke Chrome me kholo — yehi dashboard
bina server, bina deploy ke turant dikh jayega. Logic wahi hai, sirf
ye HiveMQ live se nahi judta, simulation dikhata hai.
