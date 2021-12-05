from replit import db
import requests

class ProcesoDeLlenadoGtaV:
  
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass
    
  def setPlataforma(self, entradaUsuario):
    plataformasGTAV = db['plataformasGtaV']
    self._keyPlataforma = comprobarArgumentosPlataforma(entradaUsuario)
    self._keyPlataforma = plataformasGTAV[self._keyPlataforma]
  
  def setPrecioBajo(self, precioBajo):
    self._precioBajo = 'lowestPrice='+ precioBajo
  
  def setPrecioAlto(self, precioAlto):
    self._precioAlto = 'highestPrice=' + precioAlto

  def generarLink(self):
    self._argumentosFinal['params']=[self._keyPlataforma, '', self._precioBajo, self._precioAlto]
    self._params = self._argumentosFinal
    r = requests.get('https://www.eldorado.gg/gta-5-modded-accounts/a/25-1-0', self._params)
    self._linkIngresado = r.url
  
  def procesarLinkGtaV(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilLinkGtaV'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilLinkGtaV'], '=')
      
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de GTAV que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar

def comprobarArgumentosPlataforma(cadenaIntroducida):
  plataformasPosiblesGTAV = db['plataformasGtaV']
  for keyPlataforma in plataformasPosiblesGTAV:
    if keyPlataforma in cadenaIntroducida:
      return keyPlataforma