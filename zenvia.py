import requests

url = 'https://api.zenvia.com/v2/channels/sms/messages'

def submitZenvia(contact):
  try:
    json = {
      "from": "dull-taurus",
      "to": f'{contact}',
      "contents": [
        {
          "type": "text",
          "text": "Olá, meu nome é Afrânio Esquerdo Viana e estou participando do processo seletivo do PROGRAMA DE ESTÁGIO TALENT LAB ITACOATIARA (Nível Superior)!"
        }
      ]
    }

    headers = {'X-API-TOKEN':'yFG7OsFhfWciSD_cnlh4YCkBLBvuVWmMVFYq'}

    request = requests.post(url=url, json=json, headers=headers)

    print(request.status_code)
  except Exception as e:
    print(f"Ocorreu o seguinte erro: {e}")

contacts = ["5597991388065","5592988192972","5592993290162"]

for contact in contacts:
  submitZenvia(contact)
