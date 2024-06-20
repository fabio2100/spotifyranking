import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from datetime import datetime
from tkinter import messagebox
import os
import numpy as np
from vistaDeTabla import *

SPOTIPY_CLIENT_ID='c6a84cfbf6874644b4623305584d051a'
SPOTIPY_CLIENT_SECRET='4f725df0406646d99e19190c4a4d8688'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=scope))

#limite = 50;

#resultados = sp.current_user_top_artists(limite,time_range="long_term")

#artistas = resultados['items']


#print('')
#print('')
#print('Largo plazo')
#artistasLista = {}
#for i in range(len(artistas)):
#    artistaSeparado = artistas[i]
#    print(str(i+1)+'-'+artistaSeparado['name'])
#    artistasLista[str(i+1)] = artistaSeparado['name']
#    
#archivoJson = json.dumps(artistasLista)


#with open('data.json','w') as file:
#  json.dump(archivoJson,file)



def solicitud(plazo='short_term',tipo='tracks',limite=50):
  
  lista = []
  if (tipo=='tracks'):
    resultado = sp.current_user_top_tracks(limite,time_range=plazo)
    tracks = resultado['items']
    for i in range(len(tracks)):
      trackSeparada = tracks[i]
      artista = trackSeparada['artists'][0]['name']
      trackName = trackSeparada['name']
      #print(str(i+1)+'-'+trackName+'---'+artista)
      #lista[str(i+1)] = trackName + '--' + artista
      trackJson = {}
      trackJson['posicion'] = str(i+1)
      trackJson['nombre'] = trackName
      trackJson['artista'] = artista
      lista.append(trackJson)
  elif (tipo=='artists'):
    resultado = sp.current_user_top_artists(limite,time_range=plazo)
    artistas = resultado['items']
    print(tipo,'---',plazo)
    for i in range(len(artistas)):
      artistaSeparado = artistas[i]
      #print(str(i+1)+'-'+artistaSeparado['name'])
      artistaJson = {}
      artistaJson['posicion'] = str(i+1)
      artistaJson['nombre'] = artistaSeparado['name']
      lista.append(artistaJson)
  guardadoInfo(plazo,tipo,lista)
  #Mensaje de diálogo con las listas 
  #messagebox.showinfo(message=lista,title=tipo+'  '+plazo)
    
def comparaListas(listaOld,listaNew,tipo='artists',plazo='short_time'):
  
  listaFnOld = []
  listaExport = []
  for i in range(len(listaOld)):
    listaFnOld.append(listaOld[i]['nombre'])
  for i in range(len(listaNew)):
    aBuscar = listaNew[i]['nombre']
    datoAAgregar = {}
    datoAAgregar['nombre'] = aBuscar
    if tipo == 'tracks':
      datoAAgregar['artista'] = listaNew[i]['artista']
    if aBuscar in listaFnOld:
      posicionVieja=listaFnOld.index(aBuscar)
      cambioEnRanking = posicionVieja - i
      datoAAgregar['cambio'] = cambioEnRanking
    else:
      datoAAgregar['cambio'] = 'Nuevo'

    listaExport.append(datoAAgregar)
  with open('ranking'+str(plazo)+str(tipo)+'.json','w',encoding='utf8') as file:
    json.dump(listaExport,file,indent=2,ensure_ascii=False)
  
  pathRanking = 'ranking'+str(plazo)+str(tipo)+'.json'
  if tipo=='artists':
  
    vistaTablaArtists(pathRanking)
  
  else:
  
    vistaTablaTracks(pathRanking)

  
    

#solicitud('long_term',limite=1)

#Función de guardado de los datos 

def guardadoInfo(plazo,tipo,lista):
  pathArchivoOld = "dataOld"+str(plazo)+str(tipo)+".json"
  pathArchivoNew = 'dataNew'+str(plazo)+str(tipo)+".json"
  pathArchivoIntermedio = 'dataIntermedio'+str(plazo)+str(tipo)+'.json'
  try:
    with open(pathArchivoIntermedio,encoding='utf8') as file:
      dataInter = json.load(file)

    if np.array_equal(dataInter,lista):
      print('NO HAY CAMBIOS DESDE LA ÚLTIMA VEZ DEL RANKING')
    else:
      os.remove(pathArchivoOld)
      os.rename(pathArchivoIntermedio,pathArchivoOld)
      with open(pathArchivoIntermedio,'w',encoding='utf8') as file:
        json.dump(lista,file,indent=2,ensure_ascii=False)
      with open(pathArchivoNew,'w',encoding='utf8') as file:
        json.dump(lista,file,indent=2,ensure_ascii=False)
    
    with open(pathArchivoOld,encoding='utf8') as file:
      listaOld = json.load(file)
    comparaListas(listaOld,dataInter,tipo,plazo)
  except IOError:
    with open('dataNew'+str(plazo)+str(tipo)+'.json','w',encoding='utf8') as file:
      json.dump(lista,file,indent=2,ensure_ascii=False)
    with open('dataOld'+str(plazo)+str(tipo)+'.json','w',encoding='utf8') as file:
      json.dump(lista,file,indent=2,ensure_ascii=False)
    with open(pathArchivoIntermedio,'w',encoding='utf8') as file:
      json.dump(lista,file,indent=2,ensure_ascii=False)
    

    
