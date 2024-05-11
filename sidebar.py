## Importando utils
from utils import *

# Adicionar uma imagem ao sidebar
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Bandeira_do_Rio_Grande_do_Sul.svg/1200px-Bandeira_do_Rio_Grande_do_Sul.svg.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
st.sidebar.image(img, caption='Ajude o Rio Grande do Sul', use_column_width=True)

# Adicionar informações de contato e links úteis
st.sidebar.header('Informações:')
st.sidebar.write('Telefone de Emergência: 193 (Bombeiros), 190 (Polícia), 192 (Ambulância)')
st.sidebar.write('Saiba como ajudar, visite o [Instagram do projeto](https://www.instagram.com/sosrs_ajuda/)')

# Link para o projeto no GitHub
st.sidebar.markdown('**Projeto SOS RS no GitHub:** [Clique aqui](https://github.com/SOS-RS)')
