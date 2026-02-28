# 📱 Instagram Reels Exporter — Android App

## How to Get the APK on Your Phone

### Step 1 — Upload to GitHub (Free)

1. Go to **[github.com](https://github.com)** → Sign up (free)
2. Click **"New repository"** → name it `instagram-reels-exporter` → click **Create**
3. Open PowerShell in `c:\Users\thakk\Downloads\instagram Project` and run:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/instagram-reels-exporter.git
git push -u origin main
```

### Step 2 — GitHub Builds the APK Automatically

- After push, go to your repo on GitHub
- Click **Actions** tab → you'll see the build running
- Wait **~20 minutes** for the build to finish ☕
- Click the finished build → scroll down → **Download InstagramReelsExporter-APK**
- You get a `.apk` file

### Step 3 — Install on Your OnePlus 11R

1. Transfer the `.apk` to your phone (WhatsApp to yourself, or Google Drive)
2. On your phone: **Settings → Additional Settings → Developer Options → Install via USB** — or just open the file in **Files** app
3. If asked "Allow from unknown sources" → tap **Allow**
4. Tap **Install** → Done ✅

---

## How the App Works

### First Time Login:
1. Open app → you'll see a **sessionid** field
2. On Chrome (PC or phone), open **instagram.com** (logged in)
3. Press **F12** → **Application** → **Cookies** → `instagram.com` → copy `sessionid` value
4. Paste into the app → tap **Save & Continue**
5. Your login is saved — **you never need to paste it again**

### Fetching Reels:
- Enter username (e.g. `bannedscenes`)
- Pick date range in IST
- Tap **Fetch Reels**
- Tap **Download Excel** → saved to your phone's **Downloads** folder

---

## Session Expires?

Instagram sessions last several months. When it expires, open the app → tap **Change Login** → paste the new sessionid.
