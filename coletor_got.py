import requests
import json

# URL da API que contém as imagens dos personagens
URL_API = "https://thronesapi.com/api/v2/Characters"

def forjar_banco_de_dados():
    print("Enviando corvos para buscar os dados dos personagens...")
    
    try:
        resposta = requests.get(URL_API)
        resposta.raise_for_status() # Verifica se a requisição deu certo
        
        dados_brutos = resposta.json()
        banco_de_dados = []
        
        # Filtramos apenas o que importa para o nosso front-end
        for personagem in dados_brutos:
            personagem_limpo = {
                "id": personagem["id"],
                "nome": personagem["fullName"],
                "casa": personagem["family"],
                "titulo": personagem["title"],
                "imagem": personagem["imageUrl"]
            }
            banco_de_dados.append(personagem_limpo)
            
        # Salvando tudo em um arquivo JSON local
        with open("personagens_got.json", "w", encoding="utf-8") as arquivo:
            json.dump(banco_de_dados, arquivo, indent=4, ensure_ascii=False)
            
        print(f"Sucesso! {len(banco_de_dados)} personagens foram registrados no meistre (salvos em 'personagens_got.json').")
        print("Agora seu front-end tem dados e imagens para carregar!")

    except requests.exceptions.RequestException as e:
        print(f"A patrulha falhou. Erro na conexão: {e}")

if __name__ == "__main__":
    forjar_banco_de_dados()