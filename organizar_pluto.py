origem = "plutotv_br.m3u8"
saida = "pluto_br_final.m3u8"

with open(origem, "r", encoding="utf-8") as f:
    linhas = f.readlines()

with open(saida, "w", encoding="utf-8") as out:

    for linha in linhas:

        if linha.startswith("#EXTINF"):

            if 'group-title="' in linha:
                inicio = linha.find('group-title="') + 13
                fim = linha.find('"', inicio)
                grupo = linha[inicio:fim]

                linha = linha.replace(
                    f'group-title="{grupo}"',
                    f'group-title="{grupo.upper()}"'
                )

            partes = linha.split(",")

            if len(partes) > 1:
                nome = partes[1].strip()

                if nome.lower().startswith("pluto tv"):
                    nome = nome[8:].strip()

                nome = nome.upper()

                linha = partes[0] + "," + nome + "\n"

        out.write(linha)

print("Playlist organizada com sucesso!")
