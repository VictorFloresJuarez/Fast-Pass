from replit import db
import requests

class ProcesoDeLlenadoPlayStation:
  
  def __init__(self):
    self._argumentosFinal = db['argumentosFinal']
    pass
  
  
  def setPrecioBajo(self, precioBajo):
    self._precioBajo = 'lowestPrice='+ precioBajo
  
  def setPrecioAlto(self, precioAlto):
    self._precioAlto = 'highestPrice=' + precioAlto

  def generarLink(self):
    self._argumentosFinal['params']=['', '', self._precioBajo, self._precioAlto]
    self._params = self._argumentosFinal
    r = requests.get('https://www.eldorado.gg/psn-accounts/a/104-1-0', self._params)
    self._linkIngresado = r.url
  
  def procesarLinkPlayStation(self):
    for x in range(len(db['parteInutilParams'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilParams'], '')
    for x in range(len(db['parteInutilPlayStation'])):
      self._linkIngresado = self._linkIngresado.replace(db['parteInutilPlayStation'], '=')
      
  def prepararMensaje(self):
    mensaje_para_buscar = f"""
 Mira la cuenta de PlayStation que encontré:
 {self._linkIngresado}
 """
    return mensaje_para_buscar

