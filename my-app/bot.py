import os
import discord
from decouple import config
from discord.ext import commands
import requests
from predict import *
from PIL import Image

# local
# bot_token = os.getenv('TOKEN')

# heroku
bot_token = config('TOKEN')

# client = discord.Client()
client = commands.Bot("$")

# eventos
@client.event
async def on_ready():
    print('Logado, {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$teste'):
      await message.channel.send('testando 1,2,3...')
      return

    await client.process_commands(message)

# comandos
@client.command(name="oi")
async def send_hello(ctx):
    response = 'Olá, ' + ctx.author.name 
    await ctx.channel.send(response)

@client.command(name="integrantes")
async def send_integrantes(ctx):
    response = 'Integrantes: \n Lucas da Silva dos Santos \n Rafael Nascimento Lourenço' 
    await ctx.channel.send(response)

@client.command(name="racas")
async def send_racas(ctx):
    response = ''
    for index, raca in enumerate(racas):
      response += f'{index + 1} - {raca}\n' 
    await ctx.channel.send(response)

@client.command(name="graficos-old")
async def send_grafico(ctx):
    await ctx.channel.send(content="```Gráficos do modelo antigo:```")
    await ctx.channel.send(content="```Acurácia por época do ultimo treinamentos:```", file=discord.File('atual_epochs_accuracy_old.png'))
    await ctx.channel.send(content="```Perda por época do ultimo treinamentos:```", file=discord.File('atual_epochs_loss_old.png'))
    
    await ctx.channel.send(content="```Acurácia por época de todos os treinamentos:```", file=discord.File('longo_epochs_accuracy_old.png'))
    await ctx.channel.send(content="```Perda por época de todos os treinamentos:```", file=discord.File('longo_epochs_loss_old.png'))

@client.command(name="graficos")
async def send_grafico_modelo_2(ctx):
    await ctx.channel.send(content="```Acurácia por época do ultimo treinamentos:```", file=discord.File('atual_epochs_accuracy.png'))
    await ctx.channel.send(content="```Perda por época do ultimo treinamentos:```", file=discord.File('atual_epochs_loss.png'))
    
    await ctx.channel.send(content="```Acurácia por época de todos os treinamentos:```", file=discord.File('longo_epochs_accuracy.png'))
    await ctx.channel.send(content="```Perda por época de todos os treinamentos:```", file=discord.File('longo_epochs_loss.png'))


@client.command(name="predicao")
async def send_predicao(ctx):
    if ctx.message.attachments:
        imagem_url = ctx.message.attachments[0].url        
        response = requests.get(imagem_url)
        file = open("sample_image.png", "wb")
        file.write(response.content)
        file.close()
        
        converter_imagem('sample_image.png')
        
        resposta_unica = predict_img('sample_image.png')
        resposta = f'```Predição da imagem: {resposta_unica}```' 
    else:
        mesnagem_recebida = ctx.message.content.lower()
        url = mesnagem_recebida[9:].strip()
        if url.startswith('http'):
            imagem_url = url
            response = requests.get(imagem_url, stream = True)
            file = open("sample_image.png", "wb")
            file.write(response.content)
            file.close()
            
            converter_imagem('sample_image.png')
            
            resposta_unica = predict_img('sample_image.png')
            resposta = f'```Predição da imagem: {resposta_unica}```'
        else:
            resposta = 'Por favor envie uma imagem no corpo da mensagem'
    await ctx.channel.send(resposta)



client.run(bot_token)
