import discord
import os
from mantener_activo import keep_alive
from replit import db
from clases.LinkFortnite import LinkFortnite
from clases.LinkLol import LinkLol
from clasesAsistidas.ProcesoDeLlenadoFortnite import ProcesoDeLlenadoFortnite
from clasesAsistidas.ProcesoDeLlenadoLol import ProcesoDeLlenadoLol

my_secret = os.environ['TOKEN']
client = discord.Client()

keys = db.keys()
print(keys)
print(db['mensajeAyuda'])


@client.event
async def on_ready():
  print('Se ha iniciado el {0.user}'.format(client)) 

@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith('!buscar LOL'):
    link = LinkLol(message.content)
    link.procesarCadenaEntrada()
    link.procesarLink()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)
  
  if message.content.startswith('!buscar Fortnite'):
    link = LinkFortnite(message.content)
    link.procesarCadenaEntrada()
    link.procesarLinkFortnite()
    linkListo = link.prepararMensaje()
    await message.channel.send(linkListo)

  if message.content.startswith('!ayuda'):
    mensaje = db['mensajeAyuda']
    await message.channel.send(mensaje) 
  
  if message.content.startswith('!palabrasClave'):
    mensaje = db['mensajeClaves']
    await message.channel.send(mensaje)

  if message.content.startswith('!Ayuda con pausas'):
    await message.channel.send(db['buscarConAyudaPrimerMensaje'])
    mensaje = await client.wait_for('message')
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
      await message.channel.send(mensajeFinal)

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
      await message.channel.send(mensajeFinal)



      
    else:
      await message.channel.send('No introduciste un juego válido, por favor vuelve a empezar el proceso')




keep_alive()
client.run(my_secret)