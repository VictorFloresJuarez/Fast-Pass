from replit import db
import requests


class LinkLol:
  # Object builder
  def __init__(self, cadenaIntroducida):
    self._cadenaIntroducida = cadenaIntroducida


  # Function that processes user input to generate the link. 
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

  # Function that processes the generated link to make it correct
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


  # Function that prepares the final message to be sent with the link
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
Mira la cuenta de LoL que encontré:
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

# This function gets the lowest price
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


# This function gets the highest price
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