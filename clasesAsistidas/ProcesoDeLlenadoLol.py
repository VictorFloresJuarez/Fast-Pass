from replit import db
import requests

class ProcesoDeLlenadoLol:

  #Constructor (no recibe nada)
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass
  
  def setServidor(self, entradaUsuario):
    argumentosServer = db['argumentosServer']
    self._keyServer = comprobarArgumentosServer(entradaUsuario)
    self._keyServer = argumentosServer[self._keyServer]

  def setElo(self, entradaUsuario):
    argumentosElo = db['argumentosElo']
    self._keyElo = comprobarArgumentosElo(entradaUsuario)
    self._keyElo = argumentosElo[self._keyElo]

  def setPrecioBajo(self, precioBajo):
    self._precioBajo = 'lowestPrice='+ precioBajo
  
  def setPrecioAlto(self, precioAlto):
    self._precioAlto = 'highestPrice=' + precioAlto
  
  def generarLink(self):
    self._argumentosFinal['params']=[self._keyServer, self._keyElo, self._precioBajo, self._precioAlto]
    self._params = self._argumentosFinal
    r = requests.get('https://www.eldorado.gg/league-of-legends-accounts-for-sale/a/17-1-0/', self._params)
    self._linkIngresado = r.url

  def procesarLinkLol(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilElo'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilElo'], '=')
    for x in range(len(db['parteInutilServidor'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilServidor'], '')
    for x in range(len(db['parteInutilPrecio'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilPrecio'],'')
  
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de League of Legends que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar


def comprobarArgumentosElo(cadenaIntroducida):
  elosPosiblesLol = db['elosPosiblesLol']
  for keyElo in elosPosiblesLol:
    if keyElo in cadenaIntroducida:
      return keyElo

def comprobarArgumentosServer(cadenaIntroducida):
  servidoresPosiblesLol = db['servidoresPosiblesLol']
  for keyServer in servidoresPosiblesLol:
    if keyServer in cadenaIntroducida:
      return keyServer