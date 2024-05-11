## Importando Utils e a Sidebar
from utils import *
from sidebar import *

## Lendo dados da planilha
data = load_data()

# Título e Subtítulo
st.title('SOS RS')
st.markdown('Este é um aplicativo para ajudar a encontrar abrigos e postos de doação no Rio Grande do Sul. Aqui você pode encontrar informações sobre abrigos e postos de doação no Rio Grande do Sul.')

# Exibição dos dados caso necessário
if st.checkbox('Mostrar dados'):
    st.write(data)

# Mapa dos abrigos
st.subheader("Mapa de Abrigos e Postos de Doação")
st.pydeck_chart(create_map(data))

# Medição de distância
st.subheader("Calcular Distância Entre Abrigos")
abrigo1 = st.selectbox('Escolha o primeiro abrigo:', data['NOME_DO_LOCAL'])
abrigo2 = st.selectbox('Escolha o segundo abrigo:', data['NOME_DO_LOCAL'], index=1)
if st.button('Calcular Distância'):
    loc1 = data[data['NOME_DO_LOCAL'] == abrigo1][['LATITUDE', 'LONGITUDE']].iloc[0]
    loc2 = data[data['NOME_DO_LOCAL'] == abrigo2][['LATITUDE', 'LONGITUDE']].iloc[0]
    distance = geodesic(loc1, loc2).km
    st.write(f"A distância entre {abrigo1} e {abrigo2} é de {distance:.2f} km.")

# Filtros e exibição dos dados filtrados
st.subheader("Filtrar Abrigos por Itens Disponíveis ou em Falta")
itens_disp = st.multiselect('Filtrar por Itens Disponíveis:', data['ITENS_DISPONIVEIS'].unique())
itens_falta = st.multiselect('Filtrar por Itens em Falta:', data['ITENS_EM_FALTA'].unique())
if st.button('Aplicar Filtros'):
    filtered_data = data.copy()
    if itens_disp:
        filtered_data = filtered_data[filtered_data['ITENS_DISPONIVEIS'].isin(itens_disp)]
    if itens_falta:
        filtered_data = filtered_data[filtered_data['ITENS_EM_FALTA'].isin(itens_falta)]
    st.write(filtered_data)
    st.pydeck_chart(create_map(filtered_data))

# Gráfico de abrigos por cidade
st.subheader("Quantidade de Abrigos por Cidade")

## Contar abrigos por cidade
abrigo_por_cidade = data['CIDADE'].value_counts().reset_index()
abrigo_por_cidade.columns = ['CIDADE', 'NRO DE ABRIGOS']
fig = px.bar(abrigo_por_cidade, x='CIDADE', y='NRO DE ABRIGOS', title='Quantidade de Abrigos por Cidade')
st.plotly_chart(fig)