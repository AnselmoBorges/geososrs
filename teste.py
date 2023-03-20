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


buscaCEP('01521000')