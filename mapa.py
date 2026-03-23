import folium
from folium.features import DivIcon

mapa = folium.Map(
    location=[-24.8426, -54.3331],
    zoom_start=18,
    tiles="cartodbpositron"
)

# ================= QUIOSQUES =================

with open("quiosques.txt") as arquivo_q:
    for linha in arquivo_q:
        linha = linha.strip()
        if linha == "":
            continue

        dados = linha.split(",")

        numero = int(dados[0])
        lat = float(dados[1])
        lon = float(dados[2])
        status = dados[3]

        cor = "blue" if status == "alugado" else "green"

        folium.Marker(
            location=[lat, lon],
            popup=f"Quiosque {numero} - {status}",
            icon=DivIcon(html=f"""
                <div style="
                    font-size:14px;
                    color:white;
                    background:{cor};
                    border-radius:50%;
                    width:30px;
                    height:30px;
                    text-align:center;
                    line-height:30px;
                    font-weight:bold;">
                    {numero}
                </div>
            """)
        ).add_to(mapa)

# ================= SALÕES =================

with open("saloes.txt") as arquivo_s:
    for linha in arquivo_s:
        linha = linha.strip()
        if linha == "":
            continue

        dados = linha.split(",")

        numero = dados[0]

        coords = [
            [float(dados[1]), float(dados[2])],
            [float(dados[3]), float(dados[4])],
            [float(dados[5]), float(dados[6])],
            [float(dados[7]), float(dados[8])]
        ]

        status = dados[9]
        cor = "red" if status == "reservado" else "green"

        folium.Polygon(
            locations=coords,
            color=cor,
            fill=True,
            fill_color=cor,
            fill_opacity=0.4,
            popup=f"Salão {numero} - {status}"
        ).add_to(mapa)

# ================= BANHEIROS =================

with open("banheiros.txt") as arquivo_b:
    for linha in arquivo_b:
        linha = linha.strip()
        if linha == "":
            continue

        dados = linha.split(",")

        numero = dados[0]

        lat1 = float(dados[1])
        lon1 = float(dados[2])
        lat2 = float(dados[5])
        lon2 = float(dados[6])

        centro_lat = (lat1 + lat2) / 2
        centro_lon = (lon1 + lon2) / 2

        coords = [
            [float(dados[1]), float(dados[2])],
            [float(dados[3]), float(dados[4])],
            [float(dados[5]), float(dados[6])],
            [float(dados[7]), float(dados[8])]
        ]

        folium.Polygon(
            locations=coords,
            color="yellow",
            fill=True,
            fill_color="yellow",
            fill_opacity=0.7,
            popup=f"Banheiro {numero}"
        ).add_to(mapa)

        folium.Marker(
            location=[centro_lat, centro_lon],
            icon=DivIcon(html="""
                <div style="
                    font-size:18px;
                    text-align:center;">
                    🚻
                </div>
            """)
        ).add_to(mapa)

# ================= FINAL =================

mapa.save("mapa_completo.html")

print("Mapa criado com sucesso")