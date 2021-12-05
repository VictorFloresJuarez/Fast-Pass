from replit import db
import requests

class ProcesoDeLlenadoLol:

  # Object builder
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass
  
  # This function sets the server
  def setServidor(self, entradaUsuario):
    argumentosServer = db['argumentosServer']
    self._keyServer = comprobarArgumentosServer(entradaUsuario)
    self._keyServer = argumentosServer[self._keyServer]

  # This function sets the Elo
  def setElo(self, entradaUsuario):
    argumentosElo = db['argumentosElo']
    self._keyElo = comprobarArgumentosElo(entradaUsuario)
    self._keyElo = argumentosElo[self._keyElo]

  # This function sets the lowest price
  def setPrecioBajo(self, precioBajo):
    self._precioBajo = 'lowestPrice='+ precioBajo

  # This function sets the highest price 
  def setPrecioAlto(self, precioAlto):
    self._precioAlto = 'highestPrice=' + precioAlto

  # This function generates the link
  def generarLink(self):
    self._argumentosFinal['params']=[self._keyServer, self._keyElo, self._precioBajo, self._precioAlto]
    self._params = self._argumentosFinal
    r = requests.get('https://www.eldorado.gg/league-of-legends-accounts-for-sale/a/17-1-0/', self._params)
    self._linkIngresado = r.url

  # This function processes the link
  def procesarLinkLol(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilElo'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilElo'], '=')
    for x in range(len(db['parteInutilServidor'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilServidor'], '')
    for x in range(len(db['parteInutilPrecio'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilPrecio'],'')
  
  # Function that prepares the final message to be sent with the link
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de League of Legends que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar


# This function checks the introduced Elo
def comprobarArgumentosElo(cadenaIntroducida):
  elosPosiblesLol = db['elosPosiblesLol']
  for keyElo in elosPosiblesLol:
    if keyElo in cadenaIntroducida:
      return keyElo

# This function checks the introduced server
def comprobarArgumentosServer(cadenaIntroducida):
  servidoresPosiblesLol = db['servidoresPosiblesLol']
  for keyServer in servidoresPosiblesLol:
    if keyServer in cadenaIntroducida:
      return keyServer