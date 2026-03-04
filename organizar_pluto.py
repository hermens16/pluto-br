origem = "pluto_br.m3u8"
saida = "pluto_br_final.m3u8"

with open(saida, "w", encoding="utf-8") as out:
    with open(origem, "r", encoding="utf-8") as f:
        for linha in f:

            if linha.startswith("#EXTINF"):

                # Deixar grupo em maiúsculo
                if 'group-title="' in linha:
                    inicio = linha.find('group-title="') + 13
                    fim = linha.find('"', inicio)
                    grupo = linha[inicio:fim]
                    linha = linha.replace(
                        f'group-title="{grupo}"',
                        f'group-title="{grupo.upper()}"'
                    )

                # Processar nome do canal
                partes = linha.split(",")
                nome = partes[1].strip()

                # remover "Pluto TV " do começo
                if nome.lower().startswith("pluto tv"):
                    nome = nome[8:].strip()

                nome = nome.upper()

                linha = linha.split(",")[0] + ", " + nome + "\n"

            out.write(linha)

print("Pluto organizada com sucesso!")
