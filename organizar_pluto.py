import json
import urllib.request

saida = "pluto_br_final.m3u8"

url = "https://service-channels.clusters.pluto.tv/v1/guide?start=0&stop=999&country=BR&deviceType=web&deviceMake=Chrome"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

canais = {}

for item in data["channels"]:
    canais[item["_id"]] = item

with open(saida, "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for canal in canais.values():

        nome = canal["name"].upper()

        if nome.startswith("PLUTO TV"):
            nome = nome[8:].strip()

        grupo = canal.get("category", "PLUTO").upper()
        logo = canal.get("logo", {}).get("path", "")
        canal_id = canal["_id"]

        stream = f"https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/{canal_id}/master.m3u8?deviceDNT=0"

        f.write(f'#EXTINF:-1 tvg-id="{canal_id}" tvg-logo="{logo}" group-title="{grupo}",{nome}\n')
        f.write(stream + "\n")

print("Playlist gerada com sucesso!")
