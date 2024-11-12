from mistralai import Mistral

api_key = "api-key..." # https://console.mistral.ai/api-keys/
client = Mistral(api_key=api_key)

while True: 
    msg  = input("Type (Q)-To exit\nType a message to the AI (Mistral): ")
    
    if msg=='q' or msg=='Q':
        print("Leaving...")
        break
    
    model = "codestral-latest"

    message = [
        {
            "role": "user", 
            "content": msg
        }
    ]

    chat_response = client.chat.complete(
        model=model,
        messages=message
    )
    print(chat_response.choices[0].message.content)