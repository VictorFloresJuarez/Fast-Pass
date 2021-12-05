from replit import db
import requests

class ProcesoDeLlenadoCoD:
  # Object builder
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass

  # This function sets the platform
  def setPlataforma(self, entradaUsuario):
    plataformasCoD = db['plataformasCoD']
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
    r = requests.get('https://www.eldorado.gg/call-of-duty-accounts/a/35-0-0', self._params)
    self._linkIngresado = r.url
  
  # This function processes the link
  def procesarLinkCoD(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilLinkCOD'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilLinkCOD'], '=')
      
  # Function that prepares the final message to be sent with the link
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de COD que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar

# This function checks the introduced platform
def comprobarArgumentosPlataforma(cadenaIntroducida):
  plataformasPosiblesCOD = db['plataformasCoD']
  for keyPlataforma in plataformasPosiblesCOD:
    if keyPlataforma in cadenaIntroducida:
      return keyPlataforma