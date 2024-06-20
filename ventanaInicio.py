from tkinter import *
from inicio import *
from functools import partial

#window
tkWindow = Tk()  
tkWindow.geometry('350x150')  
tkWindow.title('Tu ranking de Spotify')
#Partials para validación
validarSolicitudArtistaCorto = partial(solicitud,tipo='artists')
validarSolicitudArtistaMedio = partial(solicitud,plazo='medium_term',tipo='artists')
validarSolicitudArtistaLargo = partial(solicitud,plazo='long_term',tipo='artists')
validarSolicitudTracksCorto = partial(solicitud)
validarSolicitudTracksMedio = partial(solicitud,plazo='medium_term')
validarSolicitudTracksLargo = partial(solicitud,plazo='long_term')
#Labels y buttons
labelsArtistas = Label(tkWindow,text='Artistas').grid(row=0,columnspan=3)
cortoTermino = Button(tkWindow,text='Últimas 4 semanas',command=validarSolicitudArtistaCorto).grid(row=1,column=0,padx=2)
medioTermino = Button(tkWindow,text='Últimas 6 meses',command=validarSolicitudArtistaMedio).grid(row=1,column=1,padx=2)
largoTermino = Button(tkWindow,text='Inicio de los tiempos',command=validarSolicitudArtistaLargo).grid(row=1,column=2,padx=2)
labelsCanciones = Label(tkWindow,text='Canciones').grid(row=2,columnspan=3)
cortoTerminoCanciones = Button(tkWindow,text='Últimas 4 semanas',command=validarSolicitudTracksCorto).grid(row=3,column=0,padx=2)
medioTerminoCanciones = Button(tkWindow,text='Últimas 6 meses',command=validarSolicitudTracksMedio).grid(row=3,column=1,padx=2)
largoTerminoCanciones = Button(tkWindow,text='Inicio de los tiempos',command=validarSolicitudTracksLargo).grid(row=3,column=2,padx=2)

tkWindow.mainloop()