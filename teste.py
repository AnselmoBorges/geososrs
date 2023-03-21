def buscaCEP(cep):
    import urllib.request
    import json
    try:
        url = "http://viacep.com.br/ws/%s/json/" % cep
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        dados = json.loads(response.read().decode('utf-8'))
        return dados
    except:
        return False

## mostrar o resultado do cep
cep = '01521000'
resultado = buscaCEP(cep)
print(resultado)