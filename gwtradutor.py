import asyncio
from googletrans import Translator

# peguei o def que criei para o pokémon e criei esse mini tradutor

async def tradutor(texto: str):
    async with Translator() as traduzir:
        resultado = await traduzir.translate(texto, dest='pt')
        print(f'\033[34m{resultado.origin} --> {resultado.text}\033[m')

while True:
    texto = input('\033[33mDigite o Texto que quer traduzir: \033[m').strip()
    asyncio.run(tradutor(texto))
    resposta = ' '
    while resposta not in 'sn' or resposta == '':
        resposta = input('\033[35mDeseja Continuar? [S/N]: \033[m').strip().lower()
        if resposta not in 'sn' or resposta == '':
            print('\033[31mErro: Por favor, responda somente com S ou N!\033[m')
    if resposta == 'n':
        break
