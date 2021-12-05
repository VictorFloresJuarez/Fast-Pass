from replit import db
import requests

class ProcesoDeLlenadoApex:
  # Object builder
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass

  # This function sets the platform
  def setPlataforma(self, entradaUsuario):
    plataformasCoD = db['plataformasApex']
    self._keyPlataforma = comprobarArgumentosPlataforma(entradaUsuario)
    self._keyPlataforma = plataformasCoD[self._keyPlataforma]

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
    r = requests.get('https://www.eldorado.gg/apex-legends-accounts/a/33-0-0', self._params)
    self._linkIngresado = r.url
  
  # This function processes the link
  def procesarLinkApex(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilLinkApex'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilLinkApex'], '=')
  
  # Function that prepares the final message to be sent with the link
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de Apex que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar

# This function checks the introduced platform
def comprobarArgumentosPlataforma(cadenaIntroducida):
  plataformasPosiblesCOD = db['plataformasApex']
  for keyPlataforma in plataformasPosiblesCOD:
    if keyPlataforma in cadenaIntroducida:
      return keyPlataforma