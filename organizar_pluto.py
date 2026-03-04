origem = "pluto_br.m3u8"
saida = "pluto_br_final.m3u8"

with open(saida, "w", encoding="utf-8") as out:
    with open(origem, "r", encoding="utf-8") as f:
        for linha in f:

            # Se for URL de stream, adicionar parâmetro
            if linha.startswith("http"):
                if "deviceDNT=" not in linha:
                    if "?" in linha:
                        linha = linha.strip() + "&deviceDNT=0\n"
                    else:
                        linha = linha.strip() + "?deviceDNT=0\n"

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
                nome = partes[1].strip()

                if nome.lower().startswith("pluto tv"):
                    nome = nome[8:].strip()

                nome = nome.upper()

                linha = linha.split(",")[0] + ", " + nome + "\n"

            out.write(linha)

print("Pluto organizada com sucesso!")
