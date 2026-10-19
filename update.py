import json
from datetime import datetime, timezone
from google_play_scraper import app

APPS = [
  {"name": "Talking Tom Cat", "id": "com.outfit7.talkingtom", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingtom"},
  {"name": "Talking Ben the Dog", "id": "com.outfit7.talkingben", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingben"},
  {"name": "Talking Tom Cat 2", "id": "com.outfit7.talkingtom2free", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingtom2free"},
  {"name": "Talking Pierre the Parrot", "id": "com.outfit7.talkingpierrefree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingpierrefree"},
  {"name": "Talking Tom & Ben News", "id": "com.outfit7.talkingnewsfree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingnewsfree"},
  {"name": "Talking Ginger", "id": "com.outfit7.talkinggingerfree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkinggingerfree"},
  {"name": "Talking Angela", "id": "com.outfit7.talkingangelafree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingangelafree"},
  {"name": "Talking Ginger 2", "id": "com.outfit7.gingersbirthdayfree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.gingersbirthdayfree"},
  {"name": "My Talking Tom", "id": "com.outfit7.mytalkingtomfree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkingtomfree"},
  {"name": "My Talking Angela", "id": "com.outfit7.mytalkingangelafree", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkingangelafree"},
  {"name": "Talking Tom Gold Run", "id": "com.outfit7.talkingtomgoldrun", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingtomgoldrun"},
  {"name": "My Talking Hank: Islands", "id": "com.outfit7.mytalkinghank", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkinghank"},
  {"name": "Talking Tom Candy Run", "id": "com.outfit7.talkingtomcandyrun", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingtomcandyrun"},
  {"name": "My Talking Tom 2", "id": "com.outfit7.mytalkingtom2", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkingtom2"},
  {"name": "Talking Tom Hero Dash", "id": "com.outfit7.herodash", "url": "https://play.google.com/store/apps/details?id=com.outfit7.herodash"},
  {"name": "My Talking Tom Friends", "id": "com.outfit7.mytalkingtomfriends", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkingtomfriends"},
  {"name": "My Talking Angela 2", "id": "com.outfit7.mytalkingangela2", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkingangela2"},
  {"name": "Talking Tom Time Rush", "id": "com.outfit7.talkingtomtimerush", "url": "https://play.google.com/store/apps/details?id=com.outfit7.talkingtomtimerush"},
  {"name": "Talking Tom Friends World", "id": "com.outfit7.ttfworld", "url": "https://play.google.com/store/apps/details?id=com.outfit7.ttfworld"},
  {"name": "My Talking Tom Friends 2", "id": "com.outfit7.mytalkingtomfriends2", "url": "https://play.google.com/store/apps/details?id=com.outfit7.mytalkingtomfriends2"}
]

results = []

for item in APPS:
    try:
        res = app(item["id"], lang="ru", country="us")
        updated_ts = res.get("updated") # Время обновления в секундах (Unix timestamp)
        
        results.append({
            "name": item["name"],
            "id": item["id"],
            "url": item["url"],
            "version": res.get("version") or "Зависит от устройства",
            "updated_ts": updated_ts,
            "icon": res.get("icon", ""),
            "status": "ok"
        })
    except Exception as e:
        results.append({
            "name": item["name"],
            "id": item["id"],
            "url": item["url"],
            "version": "Н/Д",
            "updated_ts": None,
            "icon": "",
            "status": "error"
        })

output = {
    "last_checked": int(datetime.now(timezone.utc).timestamp()),
    "apps": results
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
