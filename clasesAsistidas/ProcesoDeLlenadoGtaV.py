from replit import db
import requests

class ProcesoDeLlenadoGtaV:
  # Object builder
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass
    
  # This function sets the platform
  def setPlataforma(self, entradaUsuario):
    plataformasGTAV = db['plataformasGtaV']
    self._keyPlataforma = comprobarArgumentosPlataforma(entradaUsuario)
    self._keyPlataforma = plataformasGTAV[self._keyPlataforma]
  
  # This function sets the lowest price
  def setPrecioBajo(self, precioBajo):
    self._precioBajo = 'lowestPrice='+ precioBajo
  
  # This function sets the highest price 
  def setPrecioAlto(self, precioAlto):
    self._precioAlto = 'highestPrice=' + precioAlto

  # This function generates the link
  def generarLink(self):
    self._argumentosFinal['params']=[self._keyPlataforma, '', self._precioBajo, self._precioAlto]
    self._params = self._argumentosFinal
    r = requests.get('https://www.eldorado.gg/gta-5-modded-accounts/a/25-1-0', self._params)
    self._linkIngresado = r.url
  
  # This function processes the link
  def procesarLinkGtaV(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilLinkGtaV'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilLinkGtaV'], '=')
      
  # Function that prepares the final message to be sent with the link
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de GTAV que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar

# This function checks the introduced platform
def comprobarArgumentosPlataforma(cadenaIntroducida):
  plataformasPosiblesGTAV = db['plataformasGtaV']
  for keyPlataforma in plataformasPosiblesGTAV:
    if keyPlataforma in cadenaIntroducida:
      return keyPlataforma