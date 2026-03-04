import requests

saida = "pluto_br_final.m3u8"

url = "https://api.pluto.tv/v2/channels?start=0&stop=999&country=BR"

response = requests.get(url)
canais = response.json()

with open(saida, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")

    for canal in canais:
        nome = canal["name"].upper()
        grupo = canal.get("category", "PLUTO").upper()
        logo = canal.get("solidLogoPNG", {}).get("path", "")

        stream = f"https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/{canal['_id']}/master.m3u8?deviceDNT=0"

        f.write(
            f'#EXTINF:-1 tvg-id="{canal["_id"]}" tvg-logo="{logo}" group-title="{grupo}",{nome}\n'
        )
        f.write(stream + "\n")

print("Playlist gerada com sucesso!")
