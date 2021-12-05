# Needed imports
import discord
import os
from mantener_activo import keep_alive
from replit import db


from clases.LinkFortnite import LinkFortnite
from clases.LinkLol import LinkLol
from clases.LinkCoD import LinkCoD
from clases.LinkApex import LinkApex
from clases.LinkGtaV import LinkGtaV
from clases.LinkPlayStation import LinkPlayStation
from clases.LinkXbox import LinkXbox

from clasesAsistidas.ProcesoDeLlenadoFortnite import ProcesoDeLlenadoFortnite
from clasesAsistidas.ProcesoDeLlenadoLol import ProcesoDeLlenadoLol
from clasesAsistidas.ProcesoDeLlenadoCoD import ProcesoDeLlenadoCoD
from clasesAsistidas.ProcesoDeLlenadoApex import ProcesoDeLlenadoApex
from clasesAsistidas.ProcesoDeLlenadoGtaV import ProcesoDeLlenadoGtaV
from clasesAsistidas.ProcesoDeLlenadoPlayStation import ProcesoDeLlenadoPlayStation
from clasesAsistidas.ProcesoDeLlenadoXbox import ProcesoDeLlenadoXbox

# Token of our bot
my_secret = os.environ['TOKEN']
client = discord.Client()

# Keys of our database
keys = db.keys()
print(keys)

# Event to know the bot started correctly
@client.event
async def on_ready():
  print('Se ha iniciado el {0.user}'.format(client)) 

# Main event, so the bot can receive messages
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # League of legends command
  if message.content.startswith('!buscar LOL'):
    link = LinkLol(message.content)
    link.procesarCadenaEntrada()
    link.procesarLink()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)
  
  # Fortnite command
  if message.content.startswith('!buscar Fortnite'):
    link = LinkFortnite(message.content)
    link.procesarCadenaEntrada()
    link.procesarLinkFortnite()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)

  # COD command
  if message.content.startswith('!buscar COD'):
    link = LinkCoD(message.content)
    link.procesarEntrada()
    link.procesarLinkCoD()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)
  
  # Apex command
  if message.content.startswith('!buscar Apex'):
    link = LinkApex(message.content)
    link.procesarEntrada()
    link.procesarLinkApex()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)

  # GTAV command
  if message.content.startswith('!buscar GTAV'):
    link = LinkGtaV(message.content)
    link.procesarEntrada()
    link.procesarLinkGtaV()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)

  # PlayStation command
  if message.content.startswith('!buscar PlayStation'):
    link = LinkPlayStation(message.content)
    link.procesarEntrada()
    link.procesarLinkPlayStation()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)

  # Xbox command
  if message.content.startswith('!buscar Xbox'):
    link = LinkXbox(message.content)
    link.procesarEntrada()
    link.procesarLinkPlayStation()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)
  
  # Help command
  if message.content.startswith('!ayuda'):
    mensaje = db['mensajeAyuda']
    await message.channel.send(mensaje) 
  
  # Keywords command
  if message.content.startswith('!palabrasClave'):
    mensaje = db['mensajeClaves']
    await message.channel.send(mensaje)

  # Assisted search process
  if message.content.startswith('!Ayuda con pausas'):
    await message.channel.send(db['buscarConAyudaPrimerMensaje'])
    mensaje = await client.wait_for('message')

    # Assisted search process (Fortnite)
    if (mensaje.content == 'Fortnite'):
      link = ProcesoDeLlenadoFortnite()
      await message.channel.send(db['messUnoFort'])
      await message.channel.send(db['plataformasFortniteAux'])
      mensaje = await client.wait_for('message') 
      link.setPlataforma(mensaje.content)
      await message.channel.send(db['messDosFort'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messTresFort'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messCuatroFort'])
      link.generarLink()
      link.procesarLinkFortnite()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)

    # Assisted search process (COD)
    elif (mensaje.content == 'COD'):
      link = ProcesoDeLlenadoCoD()
      await message.channel.send(db['messUnoFort'])
      await message.channel.send(db['plataformasCodAux'])
      mensaje = await client.wait_for('message') 
      link.setPlataforma(mensaje.content)
      await message.channel.send(db['messDosCod'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messTresCod'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messCuatroCod'])
      link.generarLink()
      link.procesarLinkCoD()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)

    # Assisted search process (Apex)
    elif (mensaje.content == 'Apex'):
      link = ProcesoDeLlenadoApex()
      await message.channel.send(db['messUnoApex'])
      await message.channel.send(db['plataformasApexAux'])
      mensaje = await client.wait_for('message') 
      link.setPlataforma(mensaje.content)
      await message.channel.send(db['messDosApex'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messTresApex'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messCuatroApex'])
      link.generarLink()
      link.procesarLinkApex()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)
    
    # Assisted search process (GTAV)
    elif (mensaje.content == 'GTAV'):
      link = ProcesoDeLlenadoGtaV()
      await message.channel.send(db['messUnoGTAV'])
      await message.channel.send(db['plataformasGTAVAux'])
      mensaje = await client.wait_for('message') 
      link.setPlataforma(mensaje.content)
      await message.channel.send(db['messDosGTAV'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messTresGTAV'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messCuatroGTAV'])
      link.generarLink()
      link.procesarLinkGtaV()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)

    # Assisted search process (PlayStation)
    elif (mensaje.content == 'PlayStation'):
      link = ProcesoDeLlenadoPlayStation()
      await message.channel.send(db['messUnoPlayStation'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messDosPlayStation'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messTresPlayStation'])
      link.generarLink()
      link.procesarLinkPlayStation()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)

    # Assisted search process (Xbox)
    elif (mensaje.content == 'Xbox'):
      link = ProcesoDeLlenadoXbox()
      await message.channel.send(db['messUnoXbox'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messDosXbox'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messTresXbox'])
      link.generarLink()
      link.procesarLinkXbox()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)

    # Assisted search process (League of Legends)
    elif (mensaje.content == 'League of Legends'):
      link = ProcesoDeLlenadoLol()
      await message.channel.send(db['messUnoLoL'])
      await message.channel.send(db['servidoresDisponiblesLoLAux'])
      mensaje = await client.wait_for('message') 
      link.setServidor(mensaje.content)
      await message.channel.send(db['messDosLol'])
      await message.channel.send(db['elosPosiblesLolAux'])
      mensaje = await client.wait_for('message') 
      link.setElo(mensaje.content)
      await message.channel.send(db['messTresLol'])
      mensaje = await client.wait_for('message') 
      link.setPrecioBajo(mensaje.content)
      await message.channel.send(db['messCuatroLol'])
      mensaje = await client.wait_for('message') 
      link.setPrecioAlto(mensaje.content)
      await message.channel.send(db['messCincoLol'])
      link.generarLink()
      link.procesarLinkLol()
      mensajeFinal = link.prepararMensaje()
      embed = discord.Embed(title = mensajeFinal)
      mensajeFinal = await message.channel.send(embed=embed)

    # Assisted search process (game not found)
    else:
      embed = discord.Embed(title = 'No introduciste un juego válido, por favor vuelve a empezar el proceso')
      mensajeFinal = await message.channel.send(embed=embed)


keep_alive()
client.run(my_secret)