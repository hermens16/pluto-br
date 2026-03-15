origem = "plutotv_br.m3u8"
saida = "pluto_br_final.m3u8"

# grupos que irão virar SÉRIES
series = [
    "JORNADA NAS ESTRELAS",
    "RETRÔ",
    "NOVELAS",
    "REALITY",
    "MTV",
    "ESTILO DE VIDA",
    "SOUTH PARK"
]

# grupos que irão virar DOCUMENTÁRIOS
documentarios = [
    "NATUREZA",
    "CURIOSIDADES",
    "MISTÉRIOS E SOBRENATURAL",
    "INVESTIGAÇÃO"
]

ordem_grupos = [
"ESPORTES",
"FILMES",
"SÉRIES",
"DOCUMENTÁRIOS",
"ANIME & TOKUSATSU",
"INFANTIL",
"MÚSICA",
"NOTÍCIAS",
"VARIEDADES",
"TV ABERTA"
]

with open(origem, "r", encoding="utf-8") as f:
    linhas = f.readlines()

grupos = {}
for g in ordem_grupos:
    grupos[g] = []

i = 0

while i < len(linhas):

    linha = linhas[i]

    if linha.startswith("#EXTINF"):

        grupo = "VARIEDADES"

        if 'group-title="' in linha:
            inicio = linha.find('group-title="') + 13
            fim = linha.find('"', inicio)

            grupo_original = linha[inicio:fim].upper()

            grupo = grupo_original

            if grupo_original in series:
                grupo = "SÉRIES"

            elif grupo_original in documentarios:
                grupo = "DOCUMENTÁRIOS"

            elif grupo_original == "NICKELODEON":
                grupo = "INFANTIL"

            elif grupo_original == "TV BRASILEIRA":
                grupo = "TV ABERTA"

            elif grupo_original == "ANIME & GEEK":
                grupo = "ANIME & TOKUSATSU"

        linha = linha.replace(
            f'group-title="{grupo_original}"',
            f'group-title="{grupo}"'
        )

        partes = linha.split(",")

        if len(partes) > 1:

            nome = partes[1].strip()

            if nome.lower().startswith("pluto tv"):
                nome = nome[8:].strip()

            nome = nome.upper()

            nova_extinf = partes[0] + "," + nome + "\n"

        else:
            nova_extinf = linha

        url = linhas[i+1]

        if grupo not in grupos:
            grupos[grupo] = []

        grupos[grupo].append(nova_extinf)
        grupos[grupo].append(url)

        i += 2
        continue

    i += 1

with open(saida, "w", encoding="utf-8") as out:

    out.write("#EXTM3U\n")

    for grupo in ordem_grupos:

        if grupo in grupos:

            for linha in grupos[grupo]:
                out.write(linha)

print("Playlist Pluto organizada com sucesso!")
