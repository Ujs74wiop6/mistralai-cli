from mistralai import Mistral
from deep_translator import GoogleTranslator

api_key = "api-key..." # https://console.mistral.ai/api-keys/
tradutor_br_en = GoogleTranslator(source= "pt", target= "en")
tradutor_en_br = GoogleTranslator(source= "en", target= "pt")
client = Mistral(api_key=api_key)

while True:
    msg  = input("Digite (Q) - Para sair\nDigite uma mensagem para a IA (Mistral): ")
    
    if msg=='q' or msg=='Q':
        print("Saindo...")
        break
    
    texto = tradutor_br_en.translate(msg)
    model = "codestral-latest"

    message = [
        {
            "role": "user", 
            "content": texto
        }
    ]

    chat_response = client.chat.complete(
        model=model,
        messages=message
    )
    resposta = tradutor_en_br.translate(chat_response.choices[0].message.content)
    print(resposta)