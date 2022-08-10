import requests
import suporte_testes

# testa se o retorno contémn status 200 (lembrando que o response está instalado então a resposta default é sempre 200 e a API não é chamada, na realidade (usado mock em suporte_testes))
def test_status_resposta_api(responses):    
    url = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {"Ocp-Apim-Subscription-Key" : '19a984ff47ec4a20acd1cf0657be1e42'}
    params  = {"mkt": "pt-BR", "q": "", "textDecorations": True, "textFormat": "HTML", "count": 10}
    responses.add(
        responses.GET, 
        url,
        json=suporte_testes.response_dict,
        status=200
    )
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200