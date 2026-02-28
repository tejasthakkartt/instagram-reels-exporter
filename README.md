# 📸 Instagram Reels → Excel Exporter

A desktop app to export your Instagram Reels **view counts and links** to a formatted Excel file, filtered by date range.

---

## 📋 Prerequisites

Before running the script, you need:

1. An **Instagram Business or Creator account** (not a Personal account)
2. A **Facebook Page** linked to your Instagram account
3. A **Meta Developer App** with an Access Token

---

## 🔑 Step 1 – Get Your Instagram Access Token

### Create a Meta Developer App
1. Go to [developers.facebook.com](https://developers.facebook.com) and log in
2. Click **My Apps → Create App**
3. Choose **Business** as the app type → Next
4. Fill in the app name and contact email → Create App

### Add Instagram Product
1. On your App Dashboard, click **Add Product**
2. Find **Instagram** and click **Set Up**

### Generate an Access Token
1. In the left sidebar, go to **Instagram → API Setup with Instagram Login** (or use the Graph API Explorer)
2. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
3. Select your App from the dropdown top-right
4. Click **Generate Access Token** and log in
5. Grant the following permissions:
   - `instagram_manage_insights`
   - `instagram_basic`
   - `pages_read_engagement`
6. Copy the **Access Token** shown

### Make It Long-Lived (Recommended)
Short-lived tokens expire in 1 hour. To convert to a 60-day token, call:

```
https://graph.instagram.com/access_token
  ?grant_type=ig_exchange_token
  &client_id=YOUR_APP_ID
  &client_secret=YOUR_APP_SECRET
  &access_token=YOUR_SHORT_LIVED_TOKEN
```

---

## 🔍 Step 2 – Get Your Instagram User ID (Optional)

The app can **auto-detect your user ID** from the token. But if you prefer to get it manually:

```
https://graph.instagram.com/me?fields=id,username&access_token=YOUR_TOKEN
```

The `id` field in the response is your Instagram User ID.

---

## 🚀 Step 3 – Install & Run

### Install dependencies
Open a terminal in this folder and run:

```bash
pip install -r requirements.txt
```

### Run the app
```bash
python instagram_reels_exporter.py
```

---

## 🖥️ How to Use

1. **Paste your Access Token** in the first field
2. **User ID** – leave blank for auto-detection, or paste your numeric user ID
3. **Set your date range** (From / To) in `YYYY-MM-DD` format
4. Click **🔍 Fetch Reels** – the table will populate with results
5. Click **📥 Download Excel** to save the `.xlsx` file

---

## 📊 Output Excel Format

| Reel Link | View Count | Date |
|-----------|------------|------|
| https://www.instagram.com/reel/... | 12,345 | 2024-06-15 10:30 |
| ... | ... | ... |

- **Reel Link** – clickable hyperlink directly to the reel
- **View Count** – total plays/views fetched from the Insights API
- **Date** – when the reel was posted (UTC)

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `API error 400: OAuthException` | Token is invalid or expired. Re-generate it. |
| `API error 403` | Missing permissions. Add `instagram_manage_insights` to your token. |
| View count is 0 for all reels | Your account must be a Business/Creator account for insights access. |
| No reels found | Check your date range includes dates when you posted reels. |

---

## 📁 Project Files

```
instagram Project/
├── instagram_reels_exporter.py   ← Main app (run this)
├── requirements.txt              ← Python dependencies
└── README.md                     ← This file
```
