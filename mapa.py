import folium
from folium.features import DivIcon

mapa = folium.Map(
    location=[-24.8420, -54.3330],
    zoom_start=18,
    tiles="cartodbpositron"
)


# 🔵 QUIOSQUES


arquivo_q = open("quiosques.txt", "r")

for linha in arquivo_q:
    dados = linha.strip().split(",")

    numero = int(dados[0])
    lat = float(dados[1])
    lon = float(dados[2])
    status = dados[3]

    if status == "alugado":
        cor = "blue"
    else:
        cor = "green"

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
                font-weight:bold;
            ">
                {numero}
            </div>
        """)
    ).add_to(mapa)

arquivo_q.close()


# SALÕES


arquivo_s = open("saloes.txt", "r")

for linha in arquivo_s:
    dados = linha.strip().split(",")

    numero = dados[0]

    coords = [
        [float(dados[1]), float(dados[2])],
        [float(dados[3]), float(dados[4])],
        [float(dados[5]), float(dados[6])],
        [float(dados[7]), float(dados[8])]
    ]

    status = dados[9]

    if status == "reservado":
        cor = "red"
    else:
        cor = "green"

    folium.Polygon(
        locations=coords,
        color=cor,
        fill=True,
        fill_color=cor,
        fill_opacity=0.4,
        popup=f"Salão {numero} - {status}"
    ).add_to(mapa)

arquivo_s.close()

# =========================
mapa.save("mapa_completo.html")

print("Mapa completo criado!")