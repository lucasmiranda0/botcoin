import discord
import os
import requests
from keep_alive import keep_alive

bitcoinInDolar = requests.get('https://api.coindesk.com/v1/bpi/currentprice/usd.json')
bitcoinJSON = bitcoinInDolar.json()
bitcoinString = str(bitcoinJSON['bpi']['USD']['rate'])
bitcoinString = bitcoinString.split(".", 1)
bitcoinString = bitcoinString[0]
bitcoinString = bitcoinString.replace(',', '')

bitcoinFloat = float(bitcoinString)

dolarToReal = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
dolarJSON = dolarToReal.json()
dolarString = str(dolarJSON['USD']['bid'])

dolarFloat = float(dolarString)

bitcoinReais = dolarFloat * bitcoinFloat

client  = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$bitcoin'):
    await message.channel.send('Preço do bitcoin em reais: {:.0f} R$'.format(bitcoinReais))

  if message.content.startswith('$dolar'):
    await message.channel.send('Preço do dolár: {:.2f} R$'.format(dolarFloat))    

  if message.content.startswith('$bitdolar'):
    await message.channel.send('Preço do bitcoin em dólares: {:.0f} R$'.format(bitcoinFloat))    

  if message.content.startswith('$help'):
    await message.channel.send('Para ver o preço do bitcoin em R$ digite: $bitcoin')
    await message.channel.send('Para ver o preço do dólar digite: $dolar')
    await message.channel.send('Para ver o preço do bitcoin em dólar digite: $bitdolar')

keep_alive()    

client.run(os.getenv('TOKEN'))    