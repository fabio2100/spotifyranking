from tkinter import *
from tkinter import ttk
import json

def vistaTablaTracks(archivoJson):
  with open(archivoJson,encoding='utf8') as file:
      lista = json.load(file)
  root = Toplevel()
  root.title('Tu ranking Spotify')
  root.geometry("700x300")
  columns = ('#1', '#2', '#3','#4')

  tree = ttk.Treeview(root, columns=columns, show='headings')
  tree.heading('#1', text='')
  tree.heading('#2', text='Canción')
  tree.heading('#3', text='Artista')
  tree.heading('#4',text='Cambio')

  for i in range(len(lista)):
    cancion = lista[i]
    tree.insert('',i,iid=i,text='',values=(str(i+1),cancion['nombre'],cancion['artista'],cancion['cambio']))

  tree.grid(row=0, column=0, sticky='nsew')
  #Scroll bar
  scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  scrollbar.grid(row=0, column=1, sticky='ns')
  root.mainloop()

def vistaTablaArtists(archivoJson):
    with open(archivoJson,encoding='utf8') as file:
      lista = json.load(file)
    root = Toplevel()
    root.title('Tu ranking Spotify')
    root.geometry("700x300")
    columns = ('#1', '#2', '#3')
    img  = PhotoImage(file='upArrow.png')

    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('#1', text='')
    tree.heading('#2', text='Artista')
    tree.heading('#3', text='Cambio')

    for i in range(len(lista)):
      artista = lista[i]
      if artista['cambio']=='Nuevo':
        tree.insert('',i,iid=i,text='',values=(str(i+1),artista['nombre'],artista['cambio']))
      elif int(artista['cambio'])<0:
        tree.insert('',i,iid=i,text='',values=(str(i+1),artista['nombre'],artista['cambio']))
      elif int(artista['cambio'])>0:
        tree.insert('',i,iid=i,text='',values=(str(i+1),artista['nombre'],artista['cambio']))
      else:
        tree.insert('',i,iid=i,text='',values=(str(i+1),artista['nombre'],artista['cambio']))  
    tree.grid(row=0, column=0, sticky='nsew')
    #Scroll bar
    scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    root.mainloop()


