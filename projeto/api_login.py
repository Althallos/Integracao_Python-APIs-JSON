from twilio.rest import Client

#   API que necessita uma conta no site

#           Mandar SMS
account_sid = 'SID da conta'

token = 'Seu token de autenticação'

remetente = 'Número twilio'
destino = 'Seu token de autenticação'

cliente = Client(account_sid, token)

message = cliente.messages.create(
        from_ = remetente, 
        to = destino,
        body = ''Hello, World!\n'
        'Hello, World!\n'
        'Hello, World!''
        )
print(message.sid)