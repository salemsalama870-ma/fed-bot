import os, time, feedparser, requests

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

FEEDS = [
    "https://www.federalreserve.gov/feeds/speeches.xml",
    "https://www.chicagofed.org/rss/speeches",
    "https://www.newyorkfed.org/rss/speeches",
]
seen = set()

def send(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})

def check():
    for u in FEEDS:
        f = feedparser.parse(u)
        for e in f.entries:
            if e.link not in seen:
                seen.add(e.link)
                send(f"🚨 <b>FED SPEECH</b>\n\n<b>{e.title}</b>\n\n{e.get('summary','')[:400]}\n\n🔗 {e.link}")

send("✅ البوت اشتغل - هبعتلك أي كلام جديد من الفيدرالي")
while True:
    try: check()
    except Exception as ex: print(ex)
    time.sleep(60)
