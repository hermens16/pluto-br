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

with open(origem, "r", encoding="utf-8") as f:
    linhas = f.readlines()

with open(saida, "w", encoding="utf-8") as out:

    for linha in linhas:

        if linha.startswith("#EXTINF"):

            if 'group-title="' in linha:
                inicio = linha.find('group-title="') + 13
                fim = linha.find('"', inicio)
                grupo = linha[inicio:fim].upper()

                # regras de agrupamento
                if grupo in series:
                    grupo = "SÉRIES"

                elif grupo in documentarios:
                    grupo = "DOCUMENTÁRIOS"

                elif grupo == "NICKELODEON":
                    grupo = "INFANTIL"

                elif grupo == "TV BRASILEIRA":
                    grupo = "TV ABERTA"

                elif grupo == "ANIME & GEEK":
                    grupo = "ANIME & TOKUSATSU"

                linha = linha.replace(
                    f'group-title="{linha[inicio:fim]}"',
                    f'group-title="{grupo}"'
                )

            partes = linha.split(",")

            if len(partes) > 1:
                nome = partes[1].strip()

                # remove prefixo PLUTO TV
                if nome.lower().startswith("pluto tv"):
                    nome = nome[8:].strip()

                nome = nome.upper()

                linha = partes[0] + "," + nome + "\n"

        out.write(linha)

print("Playlist organizada com sucesso!")
