# Importando as bibliotecas necessárias
from PIL import Image
import requests
from io import BytesIO
import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
from geopy.distance import geodesic

## Funções

# Função para carregar os dados
@st.cache_data

def load_data():
    data = pd.read_csv('planilha-rs.csv')
    return data

# Função para criar o mapa
def create_map(data):
    view_state = pdk.ViewState(
        latitude=data['LATITUDE'].mean(),
        longitude=data['LONGITUDE'].mean(),
        zoom=10,
        pitch=0
    )

    tooltip = {
        "html": "<b>Nome:</b> {NOME_DO_LOCAL}<br/>"
                "<b>Endereço:</b> {ENDERECO}<br/>"
                "<b>Cidade:</b> {CIDADE}<br/>"
                "<b>WhatsApp:</b> {WHATSAPP}<br/>"
                "<b>Itens Disponíveis:</b> {ITENS_DISPONIVEIS}<br/>"
                "<b>Itens em Falta:</b> {ITENS_EM_FALTA}",
        "style": {
            "backgroundColor": "steelblue",
            "color": "white"
        }
    }

    layer = pdk.Layer(
        "ScatterplotLayer",
        data,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=100,
        radius_min_pixels=5,
        radius_max_pixels=60,
        line_width_min_pixels=1,
        get_position='[LONGITUDE, LATITUDE]',
        get_fill_color=[180, 0, 200, 140],
        get_line_color=[0, 0, 0]
    )

    map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/streets-v11',
        tooltip=tooltip
    )
    return map


