import discord 
from discord.ext import commands 
import os 

intents = discord.Intents.all()
bot = commands.Bot("$", intents=intents)

@bot.event
async def on_ready():
    print("carlinhos chegouu")
 
bot.run(AQUI VAI O SEU TOKEN.)import discord 
from discord.ext import commands 

intents = discord.Intents.all()
bot = commands.Bot("$", intents=intents)

@bot.event
async def on_ready():
    print("carlinhos chegouu")

@bot.command() 
async def projeto(ctx:command.context):
  await ctx.send ("aqui é o projeto escrito em py, objetivo dele e praticamente aprender a mexer com chats bots logica de programação com python,tão quanto aprender a mexer com inteligencia artificial."):

bot.run(AQUI VAI O SEU TOKEN.)

#não eu não irei escrever muito aqui dentro so mais tarde pos estou produzindo o restante em outro lugar e ter que parar pra colocar o projeto aqui e explicar ele todo e demorado demais e eu tenho certeza que nem paciencia pra ler a maioria das pessoas tem 
