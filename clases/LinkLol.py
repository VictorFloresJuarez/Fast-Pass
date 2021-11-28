from replit import db
import requests


class LinkLol:

  def __init__(self, cadenaIntroducida):
    self._cadenaIntroducida = cadenaIntroducida

  def procesarCadenaEntrada(self):
    argumentosElo = db['argumentosElo']
    argumentosServer = db['argumentosServer']
    self._argumentosFinal = db['argumentosFinal']

    paramsUnoPrecio = obtenerPrecioBajo(self._cadenaIntroducida)
    paramsDosPrecio = obtenerPrecioAlto(self._cadenaIntroducida)

    keyElo = comprobarArgumentosElo(self._cadenaIntroducida)
    keyElo = argumentosElo[keyElo]

    keyServer = comprobarArgumentosServer(self._cadenaIntroducida)
    keyServer = argumentosServer[keyServer]

    self._argumentosFinal['params']=[keyElo, keyServer, paramsUnoPrecio, paramsDosPrecio]
    self._params = self._argumentosFinal
    
    r = requests.get('https://www.eldorado.gg/league-of-legends-accounts-for-sale/a/17-1-0/', self._params)
    self._linkIngresado = r.url


  def procesarLink(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilElo'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilElo'], '=')
    for x in range(len(db['parteInutilServidor'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilServidor'], '')
    for x in range(len(db['parteInutilPrecio'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilPrecio'],'')
  

  def getLinkIngresado(self):
    return self._linkIngresado

  def prepararMensaje(self):
    mensaje_para_buscar = f"""
Mira la cuenta de LoL que encontré:
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


def obtenerPrecioBajo(cadenaIntroducida):
  precioBajo = 'precioBajo='
  precioAlto = 'precioAlto='
  indicePrecioBajo = cadenaIntroducida.find(precioBajo)
  indicePrecioAlto = cadenaIntroducida.find(precioAlto)

  cadenaParaArgumentosUno = cadenaIntroducida[indicePrecioBajo+11:indicePrecioAlto-1]
  if (cadenaParaArgumentosUno == ''):
    return ''
  else:
    cadenaFinalBajo = 'lowestPrice='+ cadenaParaArgumentosUno
    return cadenaFinalBajo


def obtenerPrecioAlto(cadenaIntroducida):
  precioAlto = 'precioAlto='
  precioFin = 'finPrecio'
  indicePrecioAlto = cadenaIntroducida.find(precioAlto)
  indicePrecioFin = cadenaIntroducida.find(precioFin)

  cadenaParaArgumentosDos = cadenaIntroducida[indicePrecioAlto+11:indicePrecioFin]
  cadenaFinalAlto = 'highestPrice=' + cadenaParaArgumentosDos

  if (cadenaParaArgumentosDos == ''):
    return ''
  else:
    cadenaFinalAlto = 'highestPrice=' + cadenaParaArgumentosDos
    return cadenaFinalAlto