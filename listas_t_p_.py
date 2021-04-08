from tkinter import *
from tkinter import ttk#para trabajar con treeview

global count
count=0

global count_2
count_2=0

#aniadir un producto a la tabla
def add_record():
    global count

    if(check_if_is_a_number_list()==True):#si ingresamos los datos correctamente
        
        if(count%2==0):
            #como no tenemos que asignarle un padre dejamos asi
            my_tree.insert(parent='',index='end',iid=count,text="",values=(name_En.get(),amount_En.get(),price_En.get()),tags="evenrow")#index end=agrego los elementos al final
        else:
            my_tree.insert(parent='',index='end',iid=count,text="",values=(name_En.get(),amount_En.get(),price_En.get()),tags="oddrow")#index end=agrego los elementos al final

        count+=1
    #limpio los entry
        name_En.delete(0,END)
        amount_En.delete(0,END)
        price_En.delete(0,END)

#remover todo los elementos 
def remove_all__record():
    for i in my_tree.get_children():#recordemos todos los hijos de la treview
        my_tree.delete(i)#y los eliminamos
    name_En.delete(0,END)
    amount_En.delete(0,END)
    price_En.delete(0,END)


#remover un elemento
def remove_one__record():
    x=my_tree.selection()[0]#[0]=cuando selecciomos muchos nos elimina el ultimo
    my_tree.delete(x)
    name_En.delete(0,END)
    amount_En.delete(0,END)
    price_En.delete(0,END)

    
#remover elementos seleccionados
def remove_many__record():
    x=my_tree.selection()
    for i in x:
        my_tree.delete(i)
    name_En.delete(0,END)
    amount_En.delete(0,END)
    price_En.delete(0,END)


#seleccionar una fila
def select_record():
    name_En.delete(0,END)
    amount_En.delete(0,END)
    price_En.delete(0,END)
    #Grab record number
    selected=my_tree.focus()
    #grab record values
    values=my_tree.item(selected,'values')
   # temp_label.config(text=values)#el values[0]=nombre producto o columna 1
    #muestro los datos en los entry
    name_En.insert(0,values[0])
    amount_En.insert(0,values[1])
    price_En.insert(0,values[2])

#Actualizar un elemento
def update_record():
    #Grab record number
    selected=my_tree.focus()
    #save data
    if(check_if_is_a_number_list()==True):
        my_tree.item(selected,text='',values=(name_En.get(),amount_En.get(),price_En.get()))
        name_En.delete(0,END)
        amount_En.delete(0,END)
        price_En.delete(0,END)


def clicker(e):
    select_record()


def up():#nos acercamos hacia el 0
    rows=my_tree.selection()
    for row in rows:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)-1)#me muevo de fila en fila

def down():#nos alejamos del 0
    rows=my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)#me muevo de fila en fila

#limitar la cantidad de caracteres para ingresar
def limit_entry(var,max_char):
    value = var.get()#tomo el valor
    limit=int(max_char)#paso max_char a int
    #si el tamañoo de value es mayor al del limite
    #limitamos la cantidad de caracteres    
    if len(value) > limit: var.set(value[:limit])

#verificar si una variable es un int o float segun corresponda
def check_if_is_a_number_list():
    try:
        int(amount_En.get())
        float(price_En.get())
        warning.config(text="")
        return True
    except ValueError:
        warning.config(text="only you can write number try again")
        return False


#---FUNCIONES PARA LA TABLA DE TAREAS-#
#aniadir una tarea a la tabla
def add_record_2():
    global count_2
    
    if(check_if_is_a_number_task()==True):
        if(count_2%2==0):
            #como no tenemos que asignarle un padre dejamos asi
            my_tree_2.insert(parent='',index='end',iid=count_2,text="",values=(day_En.get(),month_En.get(),task_En.get(),priority_En.get()),tags="eddrow")#index end=agrego los elementos al final
        else:
            my_tree_2.insert(parent='',index='end',iid=count_2,text="",values=(day_En.get(),month_En.get(),task_En.get(),priority_En.get()),tags="ivenrow")#index end=agrego los elementos al final

        count_2+=1
    #limpio los entry
        day_En.delete(0,END)
        month_En.delete(0,END)
        task_En.delete(0,END)
        priority_En.delete(0,END)

#remover todo los elementos 
def remove_all__record_2():
    for i in my_tree_2.get_children():#recordemos todos los hijos de la treview
        my_tree_2.delete(i)#y los eliminamos
    
    day_En.delete(0,END)
    month_En.delete(0,END)
    task_En.delete(0,END)
    priority_En.delete(0,END)


#remover un elemento
def remove_one__record_2():
    x=my_tree_2.selection()[0]#[0]=cuando selecciomos muchos que nos elimine el ultimo
    my_tree_2.delete(x)
    day_En.delete(0,END)
    month_En.delete(0,END)
    task_En.delete(0,END)
    priority_En.delete(0,END)

    
#remover elementos seleccionados
def remove_many__record_2():
    x=my_tree_2.selection()#[0]=cuando selecciomos muchos que nos elimine el ultimo
    for i in x:
        my_tree_2.delete(i)
    day_En.delete(0,END)
    month_En.delete(0,END)
    task_En.delete(0,END)
    priority_En.delete(0,END)
    

#seleccionar una fila
def select_record_2():
    day_En_select.delete(0,END)
    month_En_select.delete(0,END)
    task_En_select.delete(0,END)
    priority_En_select.delete(0,END)
    #Grab record number
    selected=my_tree_2.focus()
    #grab record values
    values=my_tree_2.item(selected,'values')
   # temp_label.config(text=values)#el values[0]=nombre producto o columna 1
    #output to entry boxes
    day_En_select.insert(0,values[0])
    month_En_select.insert(0,values[1])
    task_En_select.insert(0,values[2])
    priority_En_select.insert(0,values[3])


#Actualizar un elemento
def update_record_2():
    #Grab record number
    selected=my_tree_2.focus()
    #save data
    if(check_if_is_a_number_task_selected()==True):
        my_tree_2.item(selected,text='',values=(day_En_select.get(),month_En_select.get(),task_En_select.get(),priority_En_select.get()))
        day_En_select.delete(0,END)
        month_En_select.delete(0,END)
        task_En_select.delete(0,END)
        priority_En_select.delete(0,END)


def clicker_2(e):
    select_record_2()


#verificar si las variables son del tipo int 
def check_if_is_a_number_task():
    try:
        int(day_En.get())
        int(month_En.get())
        int(priority_En.get())
        warning.config(text="")
        return True
    except ValueError:
        warning.config(text="only you can write number try again")
        return False

#verificar si las variables que pertenecen a los entry para modificar son del tipo int 
def check_if_is_a_number_task_selected():
    try:
        int(day_En_select.get())
        int(month_En_select.get())
        int(priority_En_select.get())
        warning.config(text="")
        return True
    except ValueError:
        warning.config(text="only you can write number try again")
        return False



root=Tk()
root.title("Your Lists")
root.geometry("800x900")


my_notebook=ttk.Notebook(root)
my_notebook.pack()

maxChar=Label(root,text="You can write 15 characters or less",font=("",8))
maxChar.pack()

warning=Label(root,text="",font=("",8))
warning.pack()
#frames para separar cada tabla
new_frame_1=Frame(root)
new_frame_2=Frame(root)
#Frame de la primera tabla
tree_frame=Frame(new_frame_1)#para utilizar la barra de scroll en este frame
tree_frame.pack(pady=20)
#Frame de la segunda tabla
tree_frame_2=Frame(new_frame_2)#para utilizar la barra de scroll en este frame
tree_frame_2.pack(pady=20)

#Añado cada frame a un tab
my_notebook.add(new_frame_1,text="Your List of Products")
my_notebook.add(new_frame_2,text="Your Tasks")

#variables
#--lista de productos--#
nameValue = StringVar()
nameValue.trace('w',lambda *args: limit_entry(nameValue,15))

amountValue = StringVar()
amountValue.trace('w',lambda *args: limit_entry(amountValue,15))

priceValue = StringVar()
priceValue.trace('w',lambda *args: limit_entry(priceValue,15))
#--lista de tareas--#
dayValue = StringVar()
dayValue.trace('w',lambda *args: limit_entry(dayValue,2))

monthValue = StringVar()
monthValue.trace('w',lambda *args: limit_entry(monthValue,2))

taskValue = StringVar()
taskValue.trace('w',lambda *args: limit_entry(taskValue,15))

prioValue = StringVar()
prioValue.trace('w',lambda *args: limit_entry(prioValue,4))

#--lista de tareas seleccionas--#
dayValue_select = StringVar()
dayValue_select.trace('w',lambda *args: limit_entry(dayValue_select,2))

monthValue_select = StringVar()
monthValue_select.trace('w',lambda *args: limit_entry(monthValue_select,2))

taskValue_select = StringVar()
taskValue_select.trace('w',lambda *args: limit_entry(taskValue_select,15))

prioValue_select = StringVar()
prioValue_select.trace('w',lambda *args: limit_entry(prioValue_select,4))

#Añado la barra de scroll para la primera tabla
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=LEFT,fill=Y)#FILL X =HORIZONTAL

#Añado la barra de scroll para la segunda tabla
tree_scroll_2=Scrollbar(tree_frame_2)
tree_scroll_2.pack(side=RIGHT,fill=Y)#FILL X =HORIZONTAL

#selectmode=none no selecciona nada 
#browse solo un elemento 
#extended todos los que quieras
#creo las tablas
my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
my_tree.pack(pady=20)

my_tree_2=ttk.Treeview(tree_frame_2,yscrollcommand=tree_scroll_2.set,selectmode="extended")
my_tree_2.pack(pady=20)


#configurar la scroll bar
tree_scroll.config(command=my_tree.yview)
tree_scroll_2.config(command=my_tree_2.yview)
#anadiendo estilos
style=ttk.Style()
#Selecciono un tema
#default 
#alt 
#clam 
#vista
style.theme_use("clam")
#configuro los colores de las tablas
#sin esto no podemos aplicar el color a cada fila
style.configure("Treeview",
    background="white",
    foreground="black",
    rowheight=25,#tamanio de cada opcion
    fieldbackground="white",#espacio que sobra en la table
    font=("",12)
    )
#cambio el color de seleccion
style.map('Treeview',background=[('selected','#FFE58E')])

#Definir nuestras columnas
my_tree['columns']=("Name of Product","Amount","Price")
#Formato de las columnas
my_tree.column("#0", width=0, stretch=NO)#con strech "eliminamos la columna"
my_tree.column("Name of Product",anchor=CENTER,width=160)
my_tree.column("Amount",anchor=CENTER,width=160)
my_tree.column("Price",anchor=CENTER,width=160)

#Creo las cabeceras
my_tree.heading("#0", text="", anchor=CENTER)#SIN ESTA COLUMNA NOS QUEDA MAL ENCAJADO
my_tree.heading("Name of Product",text="Name of Product",anchor=CENTER)
my_tree.heading("Amount",text="Amount",anchor=CENTER)
my_tree.heading("Price",text="Price to unit",anchor=CENTER)

#si tendriamos que pasar de una base de datos a la tabla

'''
Este codigo se utilizo para testear las funcionalidades de la tabla numero 1
data=[
    ["Pizza",4,10],
    ["Hamburguer",4,10],
    ["Donuts",12,2],
    ["Flour",2,3],
    ["Tomato",4,10],
    ["Hot Dogs",14,20],
    ["Met",12,24],
    ["Apples",10,10],
    ["Banana",14,50],
    ["Chocolate",12,2],
    ["Flour",2,3],
    ["Pizza",4,10],
    ["Hamburguer",4,10],
    ["Donuts",12,2],
    ["Flour",2,3],
    ["Pizza",4,10],
    ["Hamburguer",4,10],
    ["Donuts",12,2],
    ["Pizza",4,10],
    ["Hamburguer",4,10],
    ["Donuts",12,2],
    ["Flour",2,3]
]


for record in data:
    if count%2==0:
    #si tenemos un padre-hijo tenemos que completar lo de parent y text
        my_tree.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2]),tags=('evenrow'))#index end=agrego los elementos al final
    else:
        my_tree.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2]),tags=('oddrow'))#index end=agrego los elementos al final

    count+=1

'''
#crear filas con un efecto de "cebra"
my_tree.tag_configure('oddrow',background="white")
my_tree.tag_configure('evenrow',background="lightgreen")

add_frame=Frame(new_frame_1)
add_frame.pack(pady=20)

#Textos que se encuentras encima de los entry
nl=Label(add_frame,text="Name of Prodruct")
nl.grid(row=0,column=0)

al=Label(add_frame,text="Amount")
al.grid(row=0,column=1)

nl=Label(add_frame,text="Price to unit")
nl.grid(row=0,column=2)

#entrada de datos
name_En=Entry(add_frame,textvariable=nameValue)
name_En.grid(row=1,column=0,padx=5,pady=5)
name_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

amount_En=Entry(add_frame,textvariable=amountValue)
amount_En.grid(row=1,column=1,padx=5,pady=5)
amount_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

price_En=Entry(add_frame,textvariable=priceValue)
price_En.grid(row=1,column=2,padx=5,pady=5)
price_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

#Botones
#aniadir un producto a la tabla
add_but=Button(add_frame,text="Add Record",command=add_record,padx=5,pady=5)
add_but.grid(row=5,column=0,pady=10)
add_but.config(relief=GROOVE,bd=2)
#remover todo los elementos 
remove_all_but=Button(add_frame,text="Remove all Record",command=remove_all__record,padx=5,pady=5)
remove_all_but.grid(row=5,column=2,pady=10)
remove_all_but.config(relief=GROOVE,bd=2)
#remover un elemento
remove_one_but=Button(add_frame,text="Remove one Record",command=remove_one__record,padx=5,pady=5)
remove_one_but.grid(row=6,column=2,pady=10)
remove_one_but.config(relief=GROOVE,bd=2)

#remover elementos seleccionados
remove_many_but=Button(add_frame,text="Remove many Record",command=remove_many__record,padx=5,pady=5)
remove_many_but.grid(row=7,column=2,pady=10)
remove_many_but.config(relief=GROOVE,bd=2)

#Seleccionar un elemento
select_button=Button(add_frame,text="Select record",command=select_record,padx=5,pady=5)
select_button.grid(row=6,column=0,pady=10)
select_button.config(relief=GROOVE,bd=2)
#Actualizar un elemento
save_button=Button(add_frame,text="Save record",command=update_record,padx=5,pady=5)
save_button.grid(row=8,column=2,pady=10)
save_button.config(relief=GROOVE,bd=2)

#moverme hacia arriba
move_up=Button(add_frame,text="Move Up",command=up,padx=5,pady=5)
move_up.grid(row=7,column=0,pady=10)
move_up.config(relief=GROOVE,bd=2)
#moverme hacia abajo
move_down=Button(add_frame,text="Move Down",command=down,padx=5,pady=5)
move_down.grid(row=8,column=0,pady=10)
move_down.config(relief=GROOVE,bd=2)


#------lista de tareas-----------------#
my_tree_2['columns']=("Day","Month","Task","Priority")

#crear filas con un efecto de "cebra"
my_tree_2.tag_configure('eddrow',background="lightcyan")
my_tree_2.tag_configure('ivenrow',background="lightblue")

#Formato de las columnas
my_tree_2.column("#0", width=0, stretch=NO)#con strech "eliminamos la columna"
my_tree_2.column("Day",anchor=CENTER,width=120)
my_tree_2.column("Month",anchor=CENTER,width=120)
my_tree_2.column("Task",anchor=CENTER,width=120)
my_tree_2.column("Priority",anchor=CENTER,width=120)

#Creo las cabeceras
my_tree_2.heading("#0", text="", anchor=CENTER)#SIN ESTA COLUMNA NOS QUEDA MAL ENCAJADO
my_tree_2.heading("Day",text="Day",anchor=CENTER)
my_tree_2.heading("Month",text="Month",anchor=CENTER)
my_tree_2.heading("Task",text="Task",anchor=CENTER)
my_tree_2.heading("Priority",text="Priority",anchor=CENTER)


add_frame_2=Frame(new_frame_2)
add_frame_2.pack()
#Textos que se encuentras entre los entry

entrada_lb=Label(add_frame_2,text="aqui van los datos para agregar a la tabla")
entrada_lb.grid(row=1,column=0,padx=5,pady=5)

#armo parejas de un texto por ejemplo Day y lo posiciono una columna mas con respecto
# al entry 
day_lb=Label(add_frame_2,text="Day")
day_lb.grid(row=2,column=1,pady=5)

day_En=Entry(add_frame_2,textvariable=dayValue)
day_En.grid(row=2,column=0,padx=5,pady=5)
day_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))


month_lb=Label(add_frame_2,text="Month")
month_lb.grid(row=3,column=1,pady=5)

month_En=Entry(add_frame_2,textvariable=monthValue)
month_En.grid(row=3,column=0,padx=5,pady=5)
month_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))


task_lb=Label(add_frame_2,text="Task")
task_lb.grid(row=4,column=1,pady=5)

task_En=Entry(add_frame_2,textvariable=taskValue)
task_En.grid(row=4,column=0,padx=5,pady=5)
task_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))


priority_lb=Label(add_frame_2,text="Priority")
priority_lb.grid(row=5,column=1,pady=5)

priority_En=Entry(add_frame_2,textvariable=prioValue)
priority_En.grid(row=5,column=0,padx=5,pady=5)
priority_En.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))


entrada_lb=Label(add_frame_2,text="dato seleccionado")
entrada_lb.grid(row=1,column=2,padx=45,pady=5)

#Entry los cuales muestras un elemento seleccionado
#y con los cuales podemos modificar sus valores
day_En_select=Entry(add_frame_2,textvariable=dayValue_select)
day_En_select.grid(row=2,column=2,padx=45,pady=5)
day_En_select.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

month_En_select=Entry(add_frame_2,textvariable=monthValue_select)
month_En_select.grid(row=3,column=2,padx=45,pady=5)
month_En_select.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

task_En_select=Entry(add_frame_2,textvariable=taskValue_select)
task_En_select.grid(row=4,column=2,padx=45,pady=5)
task_En_select.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

priority_En_select=Entry(add_frame_2,textvariable=prioValue_select)
priority_En_select.grid(row=5,column=2,padx=45,pady=5)
priority_En_select.config(relief=GROOVE,bd=2,width=16,font=("aBigDeal",12))

#aniadir un elemento
add_rec=Button(add_frame_2,text="Add Record",command=add_record_2,padx=5,pady=5)
add_rec.grid(row=0,column=0,pady=5)
add_rec.config(relief=GROOVE,bd=2)
#remover todos los elementos
remove_all_rec=Button(add_frame_2,text="Remove All",command=remove_all__record_2,padx=5,pady=5)
remove_all_rec.grid(row=6,column=2,pady=8)
remove_all_rec.config(relief=GROOVE,bd=2)
#remover un elemento
remove_one_rec=Button(add_frame_2,text="Remove one Element",command=remove_one__record_2,padx=5,pady=5)
remove_one_rec.grid(row=6,column=0,pady=8)
remove_one_rec.config(relief=GROOVE,bd=2)
#remover los elementos seleccionados
remove_many_rec=Button(add_frame_2,text="Remove many Element Selected",command=remove_many__record_2,padx=5,pady=5)
remove_many_rec.grid(row=6,column=1,pady=8)
remove_many_rec.config(relief=GROOVE,bd=2)
#guardar cambios
save_rec=Button(add_frame_2,text="Update Record",command=update_record_2,padx=5,pady=5)
save_rec.grid(row=0,column=1,pady=5)
save_rec.config(relief=GROOVE,bd=2)
#seleccionar una fila
select_button=Button(add_frame_2,text="Select record",command=select_record,padx=5,pady=5)
select_button.grid(row=0,column=2,pady=5)
select_button.config(relief=GROOVE,bd=2)

#cuando seleccionamos un elemento con el mouse se selecciona
my_tree.bind("<ButtonRelease-1>",clicker)#cuando soltamos
my_tree_2.bind("<ButtonRelease-1>",clicker_2)#cuando soltamos
root.mainloop()
