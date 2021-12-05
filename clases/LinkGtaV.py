from replit import db
import requests

class LinkGtaV:
  #Constructor del objeto
  def __init__(self, cadenaIntroducida):
    self._cadenaIntroducida = cadenaIntroducida


  #Función que procesa la entrada del usuario para generar el link
  def procesarEntrada(self):
    argumentosPlataforma = db['plataformasGtaV']
    self._argumentosFinal = db['argumentosFinal']

    paramsUnoPrecio = obtenerPrecioBajo(self._cadenaIntroducida)
    paramsDosPrecio = obtenerPrecioAlto(self._cadenaIntroducida)

    keyPlataforma = comprobarArgumentosPlataforma(self._cadenaIntroducida)
    keyPlataforma = argumentosPlataforma[keyPlataforma]

    self._argumentosFinal['params']=[keyPlataforma, '', paramsUnoPrecio, paramsDosPrecio]
    self._params = self._argumentosFinal
    
    r = requests.get('https://www.eldorado.gg/gta-5-modded-accounts/a/25-1-0', self._params)
    self._linkIngresado = r.url

  def procesarLinkGtaV(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilLinkGtaV'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilLinkGtaV'], '=')

  def prepararMensaje(self):
    mensaje_para_buscar = f"""Mira la cuenta de Gta V que encontré:
    {self._linkIngresado}"""
    return mensaje_para_buscar






def comprobarArgumentosPlataforma(cadenaIntroducida):
    plataformasPosiblesGtaV = db['plataformasGtaV']
    for keyPlataforma in plataformasPosiblesGtaV:
      if keyPlataforma in cadenaIntroducida:
        return keyPlataforma


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