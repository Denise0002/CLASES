from tkinter import*
from funciones import*
ventana=Tk()

ventana.title("Calculadora")
ventana.geometry("296x265")
ventana.resizable(0,0)
fuente_general=("arial",8,"bold")

i=0
pantalla=Entry(ventana,
               width=22,
               bg="black",#asigna el color de fondo
               fg="white",#asicna el color de letra
               borderwidth=0,#tamaño del borde del cuadro de texto
               font=("arial",18,"bold"))#asignamos el tipo y tamaño de fuente
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)

boton=Button(ventana,text="1",
             width=9,height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general,
             command=lambda:enviar_boton("1",pantalla)).grid(row=1,column=0,padx=1,pady=1)
boton=Button(ventana,text="2",
             width=9,
             height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=1,column=1,padx=1,pady=1)
boton=Button(ventana,text="3",
             width=9,height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=1,column=2,padx=1,pady=1)
boton=Button(ventana,text="4",
             width=9,
             height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=2,column=0,padx=1,pady=1)
boton=Button(ventana,text="5",
             width=9,
             height=3,
             bg="white",
             fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=2,column=1,padx=1,pady=1)
boton=Button(ventana,text="6",
             width=9,height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=2,column=2,padx=1,pady=1)
boton=Button(ventana,text="7",
             width=9,height=3,
             bg="white",
             fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=3,column=0,padx=1,pady=1)
boton=Button(ventana,text="8",
             width=9,height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=3,column=1,padx=1,pady=1)
boton=Button(ventana,text="9",
             width=9,height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=3,column=2,padx=1,pady=1)
boton=Button(ventana,text="0",
             width=9,height=3,
             bg="white",fg="red",
             borderwidth=0,
             cursor="hand2",font=fuente_general).grid(row=4,column=1,padx=1,pady=1)
#bunton igual
boton_igual=Button(ventana,text="=",
                   width=9,
                   height=3,
                   bg="red",
                   fg="white",
                   borderwidth=0,
                   cursor="hand2",font=fuente_general).grid(row=4,column=0,padx=1,pady=1)
boton_punto=Button(ventana,text=".",
                   width=9,
                   height=3,
                   bg="green",
                   fg="white",
                   borderwidth=0,
                   cursor="hand2",font=fuente_general).grid(row=4,column=2,padx=1,pady=1)

# boton de operaciones
boton_mas=Button(ventana,text="+",
                 width=9,height=3,
                 bg="deep sky blue",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",font=fuente_general).grid(row=1,column=3,padx=1,pady=1)
boton_menos=Button(ventana,text="-",
                   width=9,height=3,
                   bg="deep sky blue",
                   fg="white",
                   borderwidth=0,
                   cursor="hand2",font=fuente_general).grid(row=2,column=3,padx=1,pady=1)
boton_por=Button(ventana,text="*",
                 width=9,
                 height=3,
                 bg="deep sky blue",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",font=fuente_general).grid(row=3,column=3,padx=1,pady=1)
boton_division=Button(ventana,text="/",
                      width=9,
                      height=3,
                      bg="deep sky blue",
                      fg="white",
                      borderwidth=0,
                      cursor="hand2",font=fuente_general).grid(row=4,column=3,padx=1,pady=1)

ventana.mainloop()

