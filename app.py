import requests

url = "https://ussuyneumann.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    # mostrar os primeiros 500 caracteres da resposta 
    #print("Retorno:", response.text[:500])
    response_json = response.json()
    dados_restaurante = {}
    for item in response_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print("Ocorreu um problema:", response.status_code)

print(dados_restaurante["McDonald’s"])