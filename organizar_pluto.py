import json
import urllib.request

saida = "pluto_br_final.m3u8"

url = "https://api.pluto.tv/v2/channels?start=0&stop=500&country=BR"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://pluto.tv/",
    "Origin": "https://pluto.tv"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

with open(saida, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")

    for canal in data:

        nome = canal["name"].upper()

        if nome.startswith("PLUTO TV"):
            nome = nome[8:].strip()

        grupo = canal.get("category", "PLUTO").upper()
        logo = canal.get("solidLogoPNG", {}).get("path", "")
        canal_id = canal["_id"]

        stream = f"https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/{canal
