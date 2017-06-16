#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
from socket import socket,error
import hashlib
import Tkinter
import MySQLdb
from Tkinter import *
import tkMessageBox
import time
from datetime import datetime

# Compatibilidad con Python 3

class Servidor(Tkinter.Frame):

    def __init__(self, parent):

        Tkinter.Frame.__init__(self, parent)

        self.parent=parent
        self.initialize_user_interface()

        self.host = '127.0.0.1'
        self.name = 'supermercado'
        self.user = 'root'
        self.password = ''
        self.usuario = ''
        self.conn = None
        self.conn = MySQLdb.connect(host=self.host,
                                    user=self.user,
                                    passwd=self.password,
                                    db=self.name)

        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        MySQL server credentials
        """
        #self.login = Tkinter.Tk()
        self.frame = Frame(self.parent)
        self.parent.title("Supermercado Python Tkinter")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")

        self.label_user=Tkinter.Label(self.parent,text="Usuario: ",anchor=Tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_password=Tkinter.Label(self.parent,text="Clave:", anchor=Tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")

        self.label_user.grid(row=0,column=0,sticky=Tkinter.E+Tkinter.W)
        self.label_password.grid(row=1,column=0, sticky=Tkinter.E+Tkinter.W)

        self.dbuser=Tkinter.Entry(self.parent)
        self.dbpassword=Tkinter.Entry(self.parent,show="*")

        self.dbuser.grid(row=0,column=1,sticky=Tkinter.E+Tkinter.W)
        self.dbpassword.grid(row=1,column=1,sticky=Tkinter.E+Tkinter.W)

        self.connectb=Tkinter.Button(self.parent,text="Ingresar",font="Helvetica 10 bold",command=self.dbconnexion)
        #self.cancelb=Tkinter.Button(self.parent,text="Cancelar",command=self.parent.quit,font="Helvetica 10 bold")

        self.connectb.grid(row=2,column=1,sticky=Tkinter.W)
        #self.cancelb.grid(row=2,column=2)

    def dbconnexion(self):

        self.usuario = self.dbuser.get()
        clave = self.dbpassword.get()
        p = hashlib.new('md5', clave)
        passw = p.hexdigest()

        sql = "SELECT * FROM (usuarios AS U INNER JOIN tipo_usuario AS TU ON U.tipo_user = TU.id) WHERE email = '" + self.usuario + "' AND pass='" + passw + "'"
        # print sql
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        # print result
        if result:
            intento = 'ok'
            hoy = time.strftime("%Y%m%d")
            hora = time.strftime("%H:%M:%S")
            #ip = socket.gethostbyname(socket.gethostname())

            sqlcon = 'INSERT INTO logs (fecha_ingreso,usuario,intentos,ip,hora_ingreso) VALUES ("%s","%s","%s","%s","%s")' % (
            hoy, self.usuario, intento, '', hora)
            self.cursor.execute(sqlcon)

            for registro in result:
                datos = registro[4]
        else:
            datos = 0

            intento = 'Fallo'
            hoy = time.strftime("%Y%m%d")
            hora = time.strftime("%H:%M:%S")
            #ip = socket.gethostbyname(socket.gethostname())

            sqlcon = 'INSERT INTO logs (fecha_ingreso,usuario,intentos,ip,hora_ingreso) VALUES ("%s","%s","%s","%s","%s")' % (
                hoy, self.usuario, intento, '', hora)
            self.cursor.execute(sqlcon)

        print datos

        #if self.dbuser.get()=="admin" and  self.dbpassword.get()=="admin":
        if datos == 1: # Si es Administrador
            self.parent.destroy()
            self.MenuAdmin('admin')

        elif datos == 2: # Si es cliente
            self.parent.destroy()
            self.MenuCliente()

        else:
            self.initialize_user_interface()

    def MenuAdmin(self, master):

        self.admin = Tk()
        self.menu = Menu(self.admin)
        self.admin.config(menu=self.menu)
        self.admin.geometry("500x500+0+0")
        self.alertas = Menu(self.menu)
        self.menu.add_cascade(label="Alertas", menu=self.alertas)
        self.alertas.add_command(label="Productos con Stock Mínimo", command=self.alertas_Productos)

        self.inventario = Menu(self.menu)
        self.menu.add_cascade(label="Inventario", menu=self.inventario)
        self.inventario.add_command(label="Ver Listado de Productos", command=self.Listar_Productos)
        self.inventario.add_command(label="Agregar Nuevos Productos", command=self.Crear_Productos)
        self.inventario.add_command(label="Actualizar Productos", command=self.Act_Productos)

        self.ventas = Menu(self.menu)
        self.menu.add_cascade(label="Ventas", menu=self.ventas)
        self.ventas.add_command(label="Ver Listado de Facturas", command=self.Listar_Facturas)
        self.ventas.add_command(label="Ver Detalle de las Facturas", command=self.Listar_Det_Facturas)
        self.ventas.add_command(label="Ver Total de Ventas del Día", command=self.Total_Ventas)

        self.usuarios = Menu(self.menu)
        self.menu.add_cascade(label="Usuarios", menu=self.usuarios)
        self.usuarios.add_command(label="Ver Listado de Usuarios", command=self.Listar_Usuarios)
        self.usuarios.add_command(label="Ver Listado de Usuarios con Puntos", command=self.Listar_Usuarios_Puntos)

        self.salir = Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=self.salir)
        self.salir.add_command(label="Cerrar Sesión", command=self.cierra_admin)

    def cierra_admin(self):
        self.admin.destroy()

    def alertas_Productos(self):

        self.alert = Tk()
        self.alert.wm_title("Productos con Stock Mínimo")
        self.alert.grid_rowconfigure(0, weight=1)
        self.alert.grid_columnconfigure(0, weight=1)

        sql = "SELECT * FROM productos where stock < stock_minimo"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()

        self.S = Scrollbar(self.alert)
        self.T = Text(self.alert, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command = self.T.yview)
        self.T.config(yscrollcommand = self.S.set)

        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No Hay alerta de productos minimos'

        self.T.insert(END, "ID - Producto - Descripción - Valor Unit - Stock - Stock Mínimo")
        self.T.insert(END, "\n")
        for i in self.datos:
            self.T.insert(END, i)
            self.T.insert(END, "\n")

        mainloop()

    def Listar_Usuarios(self):

        self.listaru = Tk()
        self.listaru.wm_title("Listado de Usuarios")
        self.listaru.grid_rowconfigure(0, weight=1)
        self.listaru.grid_columnconfigure(0, weight=1)

        sql = "SELECT email,nombre,tipo FROM (usuarios AS U INNER JOIN tipo_usuario AS TU ON U.tipo_user = TU.id)"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()

        self.S = Scrollbar(self.listaru)
        self.T = Text(self.listaru, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command = self.T.yview)
        self.T.config(yscrollcommand = self.S.set)

        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No Hay Usuarios Creados'

        self.T.insert(END, "Email (Usuario) - Nombre - Tipo")
        self.T.insert(END, "\n")
        for i in self.datos:
            self.T.insert(END, i)
            self.T.insert(END, "\n")

        mainloop()

    def Listar_Usuarios_Puntos(self):

        self.listarupts = Tk()
        self.listarupts.wm_title("Listado de Usuarios con Puntos")
        self.listarupts.grid_rowconfigure(0, weight=1)
        self.listarupts.grid_columnconfigure(0, weight=1)

        sql = "SELECT nombre, puntos FROM usuarios where puntos > 0"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()

        self.S = Scrollbar(self.listarupts)
        self.T = Text(self.listarupts, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command = self.T.yview)
        self.T.config(yscrollcommand = self.S.set)

        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No hay Usuarios con Puntos'

        self.T.insert(END, "Nombre - Puntos")
        self.T.insert(END, "\n")
        for i in self.datos:
            self.T.insert(END, i)
            self.T.insert(END, "\n")

        mainloop()

    def Listar_Productos(self):

        self.listarp = Tk()
        self.listarp.wm_title("Listado de Productos")
        self.listarp.grid_rowconfigure(0, weight=1)
        self.listarp.grid_columnconfigure(0, weight=1)

        sql = "SELECT * FROM productos"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()

        self.S = Scrollbar(self.listarp)
        self.T = Text(self.listarp, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command = self.T.yview)
        self.T.config(yscrollcommand = self.S.set)

        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No Hay alerta de productos minimos'

        self.T.insert(END, "ID - Producto - Descripción - Valor Unit - Stock - Stock Mínimo")
        self.T.insert(END, "\n")
        for i in self.datos:
            self.T.insert(END, i)
            self.T.insert(END, "\n")

        mainloop()

    def Crear_Productos(self):

        self.crearp = Tk()
        self.crearp.wm_title("Actualizar Productos")
        self.crearp.grid_rowconfigure(0, weight=1)
        self.crearp.grid_columnconfigure(0, weight=1)

        self.label_prod = Tkinter.Label(self.crearp, text="Producto: ", anchor=Tkinter.W, background="dark slate gray",
                                        foreground="white", font="Helvetica 8  bold")
        self.label_desc = Tkinter.Label(self.crearp, text="Descripción:", anchor=Tkinter.W,
                                        background="dark slate gray",
                                        foreground="white", font="Helvetica 8  bold")
        self.label_valor = Tkinter.Label(self.crearp, text="Valor:", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")
        self.label_stockmin = Tkinter.Label(self.crearp, text="Stock Mínimo:", anchor=Tkinter.W,
                                            background="dark slate gray",
                                            foreground="white", font="Helvetica 8  bold")
        self.label_stock = Tkinter.Label(self.crearp, text="Stock:", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")

        self.label_prod.grid(row=0, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_desc.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_valor.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_stockmin.grid(row=3, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_stock.grid(row=4, column=0, sticky=Tkinter.E + Tkinter.W)

        self.txtprod = Tkinter.Entry(self.crearp)
        self.txtdesc = Tkinter.Entry(self.crearp)
        self.txtvlr = Tkinter.Entry(self.crearp)
        self.txtsmin = Tkinter.Entry(self.crearp)
        self.txtstck = Tkinter.Entry(self.crearp)

        self.txtprod.grid(row=0, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtdesc.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtvlr.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtsmin.grid(row=3, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtstck.grid(row=4, column=1, sticky=Tkinter.E + Tkinter.W)

        self.connectb = Tkinter.Button(self.crearp, text="Registrar", font="Helvetica 10 bold", command=self.GuardarP)
        # self.cancelb=Tkinter.Button(self.parent,text="Cancelar",command=self.parent.quit,font="Helvetica 10 bold")

        self.connectb.grid(row=5, column=1, sticky=Tkinter.W)
        # self.cancelb.grid(row=2,column=2)

    def GuardarP(self):

        prod = self.txtprod.get()
        desc = self.txtdesc.get()
        valor = self.txtvlr.get()
        stockmin = self.txtsmin.get()
        stock = self.txtstck.get()

        if prod == '' or desc == '' or valor == '' or stockmin == '' or stock == '':
            tkMessageBox.showerror("error", "Diligencie Todos los Campos")
            self.txtprod.delete(0, END)
        else:
            sql = 'INSERT INTO productos (producto,descripcion,val_unit,stock,stock_minimo) VALUES ("%s","%s","%s","%s","%s")' % (
            prod, desc, valor, stock, stockmin)
            self.cursor.execute(sql)
            self.conn.commit()

            if sql:
                tkMessageBox.showinfo("Información", "Productos Registrado")
                self.txtprod.delete(0, END)
                self.txtdesc.delete(0, END)
                self.txtvlr.delete(0, END)
                self.txtsmin.delete(0, END)
                self.txtstck.delete(0, END)
                self.txtprod.delete(0, END)
                self.crearp.destroy()
            else:
                tkMessageBox.showerror("error", "Error al guardar el Producto")

    def Act_Productos(self):

        #self.Listar_Productos()

        self.actp = Tk()
        self.actp.wm_title("Registrar Productos")
        self.actp.grid_rowconfigure(0, weight=1)
        self.actp.grid_columnconfigure(0, weight=1)

        self.label_codid = Tkinter.Label(self.actp, text="ID Producto a Modificar: ", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")
        self.label_prod = Tkinter.Label(self.actp, text="Producto: ", anchor=Tkinter.W, background="dark slate gray",
                                        foreground="white", font="Helvetica 8  bold")
        self.label_desc = Tkinter.Label(self.actp, text="Descripción:", anchor=Tkinter.W,
                                        background="dark slate gray",
                                        foreground="white", font="Helvetica 8  bold")
        self.label_valor = Tkinter.Label(self.actp, text="Valor:", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")
        self.label_stockmin = Tkinter.Label(self.actp, text="Stock Mínimo:", anchor=Tkinter.W,
                                            background="dark slate gray",
                                            foreground="white", font="Helvetica 8  bold")
        self.label_stock = Tkinter.Label(self.actp, text="Stock:", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")

        self.label_codid.grid(row=0, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_prod.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_desc.grid(row=2, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_valor.grid(row=3, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_stockmin.grid(row=4, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_stock.grid(row=5, column=0, sticky=Tkinter.E + Tkinter.W)

        self.txtcodid = Tkinter.Entry(self.actp)
        self.txtprod = Tkinter.Entry(self.actp)
        self.txtdesc = Tkinter.Entry(self.actp)
        self.txtvlr = Tkinter.Entry(self.actp)
        self.txtsmin = Tkinter.Entry(self.actp)
        self.txtstck = Tkinter.Entry(self.actp)

        self.txtcodid.grid(row=0, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtprod.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtdesc.grid(row=2, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtvlr.grid(row=3, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtsmin.grid(row=4, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtstck.grid(row=5, column=1, sticky=Tkinter.E + Tkinter.W)

        self.connectb = Tkinter.Button(self.actp, text="Registrar", font="Helvetica 10 bold", command=self.ActuaP)
        # self.cancelb=Tkinter.Button(self.parent,text="Cancelar",command=self.parent.quit,font="Helvetica 10 bold")

        self.connectb.grid(row=6, column=1, sticky=Tkinter.W)
        # self.cancelb.grid(row=2,column=2)

    def ActuaP(self):

        idprod = self.txtcodid.get()
        prod = self.txtprod.get()
        desc = self.txtdesc.get()
        valor = self.txtvlr.get()
        stockmin = self.txtsmin.get()
        stock = self.txtstck.get()

        if idprod == '' or prod == '' or desc == '' or valor == '' or stockmin == '' or stock == '':
            tkMessageBox.showerror("error", "Diligencie Todos los Campos")
            self.txtprod.delete(0, END)
        else:
            sql = "UPDATE productos SET producto='%s',descripcion='%s',val_unit='%s',stock='%s',stock_minimo='%s' WHERE id = %i" % (
            prod, desc, valor, stock, stockmin, int(idprod))
            self.cursor.execute(sql)
            self.conn.commit()

            if sql:
                tkMessageBox.showinfo("Información", "Producto Actualizado")
                self.txtcodid.delete(0, END) #Limpiar Cajas de Texto
                self.txtprod.delete(0, END)
                self.txtdesc.delete(0, END)
                self.txtvlr.delete(0, END)
                self.txtsmin.delete(0, END)
                self.txtstck.delete(0, END)
                self.txtprod.delete(0, END)
                self.actp.destroy()
            else:
                tkMessageBox.showerror("error", "Error al Actualizar el Producto")

    def Listar_Facturas_cte(self):

        self.listarf = Tk()
        self.listarf.wm_title("Listado de Facturas")
        self.listarf.grid_rowconfigure(0, weight=1)
        self.listarf.grid_columnconfigure(0, weight=1)

        consulta = 'SELECT id_fatura,fecha_factura,total FROM factura where user = "' + self.usuario +'"'
        self.cursor.execute(consulta)
        self.result = self.cursor.fetchall()

        self.S = Scrollbar(self.listarf)
        self.T = Text(self.listarf, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command = self.T.yview)
        self.T.config(yscrollcommand = self.S.set)

        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No hay Facturas Creadas'

        self.T.insert(END, "ID - Fecha Creación  - Total")
        self.T.insert(END, "\n")
        for i in self.datos:
            self.T.insert(END, i)
            self.T.insert(END, "\n")

        mainloop()

    def Listar_Facturas(self):

        self.listarf = Tk()
        self.listarf.wm_title("Listado de Facturas")
        self.listarf.grid_rowconfigure(0, weight=1)
        self.listarf.grid_columnconfigure(0, weight=1)

        consulta = 'SELECT f.id_fatura,f.fecha_factura,u.nombre,f.total FROM factura as f INNER JOIN usuarios as u ON f.user = u.email'
        self.cursor.execute(consulta)
        self.result = self.cursor.fetchall()

        self.S = Scrollbar(self.listarf)
        self.T = Text(self.listarf, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command = self.T.yview)
        self.T.config(yscrollcommand = self.S.set)

        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No hay Facturas Creadas'

        self.T.insert(END, "ID - Fecha Creación - Nombre - Total")
        self.T.insert(END, "\n")
        for i in self.datos:
            self.T.insert(END, i)
            self.T.insert(END, "\n")

        mainloop()

    def Listar_Det_Facturas(self):

        self.listardetf = Tk()
        self.listardetf.wm_title("Detalle de Facturas")
        self.listardetf.grid_rowconfigure(0, weight=1)
        self.listardetf.grid_columnconfigure(0, weight=1)
        self.listardetf.geometry("200x70+800+0")

        self.label_idfact = Tkinter.Label(self.listardetf, text="ID Factura:", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")

        self.label_idfact.grid(row=0, column=0, sticky=Tkinter.E + Tkinter.W)

        self.txtid = Tkinter.Entry(self.listardetf)

        self.txtid.grid(row=0, column=1, sticky=Tkinter.E + Tkinter.W)

        self.connectb = Tkinter.Button(self.listardetf, text="Consultar", font="Helvetica 10 bold", command=self.Consultar_DetF)
        # self.cancelb=Tkinter.Button(self.parent,text="Cancelar",command=self.parent.quit,font="Helvetica 10 bold")

        self.connectb.grid(row=1, column=1, sticky=Tkinter.W)

    def Consultar_DetF(self):

        idfact = self.txtid.get()

        self.listardetallefact = Tk()
        self.listardetallefact.wm_title("Listado de Facturas")
        self.listardetallefact.grid_rowconfigure(0, weight=1)
        self.listardetallefact.grid_columnconfigure(0, weight=1)

        self.S = Scrollbar(self.listardetallefact)
        self.T = Text(self.listardetallefact, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)

        if idfact == '':
            tkMessageBox.showerror("error", "Diligencie Todos los Campos")

        else:
            sql = "SELECT p.producto, p.descripcion, df.cantidad, p.val_unit, df.valor FROM (detalle_factura as df INNER JOIN productos as p ON df.id_producto = p.id) WHERE df.id_factura=%i" % (int(idfact))
            #print sql
            self.cursor.execute(sql)
            self.result = self.cursor.fetchall()

            if self.result:
                # self.i = 0
                self.datos = self.result

                self.T.insert(END, "Producto - Descripción - Cantidad - Vlr Unit - Valor Total")
                self.T.insert(END, "\n")
                for i in self.datos:
                    self.T.insert(END, i)
                    self.T.insert(END, "\n")
            else:
                #self.datos = 'No hay Facturas Creadas'
                #self.T.insert(END, self.datos)
                tkMessageBox.showerror("error", "Numero de factura no existe")
            mainloop()

    def Total_Ventas(self):

        self.totvent = Tk()
        self.totvent.wm_title("Total de Ventas Diarias")
        self.totvent.grid_rowconfigure(0, weight=1)
        self.totvent.grid_columnconfigure(0, weight=1)

        self.label_fecha = Tkinter.Label(self.totvent, text="Fecha (AAAA-MM-DD)", anchor=Tkinter.W,
                                          background="dark slate gray",
                                          foreground="white", font="Helvetica 8  bold")

        self.label_fecha.grid(row=0, column=0, sticky=Tkinter.E + Tkinter.W)

        self.txtfecha = Tkinter.Entry(self.totvent)

        self.txtfecha.grid(row=0, column=1, sticky=Tkinter.E + Tkinter.W)

        self.buscar = Tkinter.Button(self.totvent, text="Consultar", font="Helvetica 10 bold",
                                       command=self.Consultar_Ventas)

        self.buscar.grid(row=1, column=1, sticky=Tkinter.W)

    def Consultar_Ventas(self):

        fecha = self.txtfecha.get()

        self.conventas = Tk()
        self.conventas.wm_title("Listado de Facturas")
        self.conventas.grid_rowconfigure(0, weight=1)
        self.conventas.grid_columnconfigure(0, weight=1)

        self.S = Scrollbar(self.conventas)
        self.T = Text(self.conventas, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)

        if fecha == '':
            tkMessageBox.showerror("error", "Diligencie Todos los Campos")

        else:
            sql = "SELECT SUM(total) as Total FROM `factura` WHERE `fecha_factura` LIKE '%"+fecha+"%'"
            #print sql
            self.cursor.execute(sql)
            self.result = self.cursor.fetchall()

            if self.result:
                # self.i = 0
                self.datos = self.result

                self.T.insert(END, "Total Ventas del Día")
                self.T.insert(END, "\n")
                for i in self.datos:
                    self.T.insert(END, i)
                    self.T.insert(END, "\n")
            else:
                self.datos = 'No hay Ventas en esta Fecha'
                self.T.insert(END, self.datos)

            mainloop()



    def Comprar_Productos(self):
        self.compra = Tk()
        self.compra.wm_title("Comprar Productos")
        self.compra.geometry("200x70+800+0")
        self.compra.grid_rowconfigure(0, weight=1)
        self.compra.grid_columnconfigure(0, weight=1)

        self.label_codid = Tkinter.Label(self.compra, text="ID Producto: ", anchor=Tkinter.W,
                                         background="dark slate gray",
                                         foreground="white", font="Helvetica 8  bold")
        self.label_prod = Tkinter.Label(self.compra, text="cantidad: ", anchor=Tkinter.W, background="dark slate gray",
                                        foreground="white", font="Helvetica 8  bold")


        self.label_codid.grid(row=0, column=0, sticky=Tkinter.E + Tkinter.W)
        self.label_prod.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)


        self.txtcodid = Tkinter.Entry(self.compra)
        self.txtcant = Tkinter.Entry(self.compra)

        self.txtcodid.grid(row=0, column=1, sticky=Tkinter.E + Tkinter.W)
        self.txtcant.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)


        self.connectb = Tkinter.Button(self.compra, text="Comprar", font="Helvetica 10 bold", command=self.GrabaComp)
        # self.cancelb=Tkinter.Button(self.parent,text="Cancelar",command=self.parent.quit,font="Helvetica 10 bold")

        self.connectb.grid(row=6, column=1, sticky=Tkinter.W)
        # self.cancelb.grid(row=2,column=2)

    def GrabaComp(self):
        hoy = time.strftime("%Y-%m-%d %H:%M:%S")
        idprod = self.txtcodid.get()
        cant = self.txtcant.get()
        if idprod == '' or  cant== '':
            tkMessageBox.showerror("error", " Debe diligenciar todos los campos")


        else:
            sql = "SELECT * FROM productos WHERE id= %i" % (int(idprod))
            self.cursor.execute(sql)
            self.conn.commit()
            self.result = self.cursor.fetchall()
            if self.result:
                for regi in self.result:
                    cantidad = (regi[4])
                    val_unit = int(regi[3])

                if (int(cant) > int(cantidad)):
                    tkMessageBox.showerror("error", 'No hay suficiente existencia')
                    self.txtcant.delete(0, END)
                else:

                    valpagar = int(val_unit) * int(cant)
                    sqlprod = 'INSERT INTO detalle_compra_temp (id_producto,cantidad,valor,user,fecha_registro) VALUES ("%s","%s","%s","%s","%s")' % (
                        idprod, cant, valpagar, self.usuario, hoy)
                    result = self.cursor.execute(sqlprod)
                    self.conn.commit()

                    if result:
                        nuevo_tot = int(cantidad) - int(cant)
                        sqlprod = "UPDATE productos SET stock='%s' WHERE id = %i" % (nuevo_tot, int(idprod))
                        result = self.cursor.execute(sqlprod)
                        self.conn.commit()

                        tkMessageBox.showinfo("Información", "Producto agregado")
                        self.txtcodid.delete(0, END)  # Limpiar Cajas de Texto
                        self.txtcant.delete(0, END)
                        #self.compra.destroy()
            else:
                tkMessageBox.showerror("error", "Producto no existe")
                self.txtcodid.delete(0, END)

    def Genera_factura(self):

        hoy = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = "SELECT sum(valor) as total FROM detalle_compra_temp WHERE user='" + self.usuario + "'"
        self.cursor.execute(sql)
        self.conn.commit()
        self.resultado = self.cursor.fetchall()
        if (self.resultado):
            for regi in self.resultado:
                total = regi[0]

            print total
            if total > 0:
                sqlprod = 'INSERT INTO factura (user,total,fecha_factura) VALUES ("%s","%s","%s")' % (self.usuario, int(total), hoy)
                self.cursor.execute(sqlprod)
                self.conn.commit()

                querynf = "SELECT MAX( id_fatura ) FROM factura"
                self.cursor.execute(querynf)
                self.conn.commit()

                self.result3 = self.cursor.fetchall()

                for resu in self.result3:
                    idfact = resu[0]

                query2 = "insert into detalle_factura (id_producto,cantidad,valor,user,fecha_registro,id_factura) select id_producto,cantidad,valor,user,fecha_registro,%i " % (
                int(idfact)) + " from detalle_compra_temp where user='" + self.usuario + "'"
                self.cursor.execute(query2)
                self.conn.commit()
                #result4 = run_query(query2)
                tkMessageBox.showinfo("Información","Factura Generada")
                deltemp = "delete from  detalle_compra_temp where user='%s'" % self.usuario
                #delresp = run_query(deltemp)
                self.cursor.execute(deltemp)
                self.conn.commit()

                selprod = "select * from detalle_factura where id_factura=%i " % int(idfact)
                #runsq = run_query(selprod)
                self.cursor.execute(selprod)
                self.conn.commit()

                self.runsq = self.cursor.fetchall()


                for prod in self.runsq:
                    idprod = prod[1]
                    cant = prod[2]
                    seldp = "select * from productos where id= %i" % int(idprod)
                    #runpd = run_query(seldp)
                    self.cursor.execute(seldp)
                    self.conn.commit()

                    self.runpd = self.cursor.fetchall()
                    for dprod in self.runpd:
                        cantold = dprod[4]
                    ncant = int(cantold) - int(cant)
                    actudeta = "update productos set stock= %i where id=%i" % (int(ncant), int(idprod))
                    #runacp = run_query(actudeta)
                    self.cursor.execute(actudeta)
                    self.conn.commit()
            else:
                tkMessageBox.showerror("error", "No hay compras pendientes")
        else:
            tkMessageBox.showerror("error", "No hay compras pendientes")

    def CambiarPuntos(self):

        hoy = time.strftime("%Y%m%d")
        sql = "SELECT puntos FROM usuarios where email='" + self.usuario + "'"
        self.cursor.execute(sql)
        self.conn.commit()
        #resultado = run_query(sql)
        self.resultado = self.cursor.fetchall()
        if self.resultado:
            for resp in self.resultado:
                puntos = resp[0]

                if puntos == 0:
                    tkMessageBox.showerror("error",'Usted no tiene puntos para cambiar')
                else:
                    self.redime = Tk()
                    self.redime.wm_title("Cambiar Puntos")
                    self.redime.geometry("250x150+800+0")
                    self.lista_premios=Listbox(self.redime)

                    sql = "SELECT * FROM premios WHERE 1"
                    self.cursor.execute(sql)
                    self.result = self.cursor.fetchall()
                    self.lista_premios.insert(END,str('ID - Premio - Ptos requeridos'))
                    for premi in self.result:
                        idprem = premi[0]
                        premio = premi[1]
                        ptos = premi[2]
                        #print premio
                        self.lista_premios.insert(END,str(idprem )+str(' - ')+str(premio)+str(' - ')+str(ptos))
                        #self.lista_premios.insert(END, ' - ')
                        #self.lista_premios.insert(END, premio)
                        #self.lista_premios.insert(END, ' - ')
                        #self.lista_premios.insert(END, ptos)



                    self.redime.grid_rowconfigure(0, weight=1)
                    self.redime.grid_columnconfigure(0, weight=1)
                    self.label_codid = Tkinter.Label(self.redime, text="ID Producto: ", anchor=Tkinter.W,
                                                     background="dark slate gray",
                                                     foreground="white", font="Helvetica 8  bold")
                    self.label_codid.grid(row=5, column=0, sticky=Tkinter.E + Tkinter.W)
                    self.txtcodidpre = Tkinter.Entry(self.redime)
                    self.txtcodidpre.grid(row=5, column=1, sticky=Tkinter.E + Tkinter.W)
                    self.connectb = Tkinter.Button(self.redime, text="Redimir", font="Helvetica 10 bold",
                                                   command=self.Grabaptos)
                    self.lista_premios.grid(row=0, column=0, sticky=Tkinter.W)
                    self.connectb.grid(row=7, column=1, sticky=Tkinter.W)

    def ListaPremios(self):
        hoy = time.strftime("%Y%m%d")
        sql = "SELECT puntos FROM usuarios where email='" + self.usuario + "'"
        self.cursor.execute(sql)
        self.conn.commit()
        # resultado = run_query(sql)
        self.resultado = self.cursor.fetchall()
        if self.resultado:
            for resp in self.resultado:
                puntos = resp[0]

                if puntos == 0:
                    tkMessageBox.showerror("error", 'Usted no tiene puntos para cambiar')
                else:
                    self.listarupts = Tk()
                    self.listarupts.wm_title("Listado de premios")
                    self.listarupts.grid_rowconfigure(0, weight=1)
                    self.listarupts.grid_columnconfigure(0, weight=1)

                    sql = "SELECT * FROM premios WHERE 1"
                    self.cursor.execute(sql)
                    self.result = self.cursor.fetchall()

                    self.label_codid = Tkinter.Label(self.listarupts, text="ID Producto: ", anchor=Tkinter.W,
                                                     background="dark slate gray",
                                                     foreground="white", font="Helvetica 8  bold")
                    self.label_prod = Tkinter.Label(self.listarupts, text="cantidad: ", anchor=Tkinter.W,
                                                    background="dark slate gray",
                                                    foreground="white", font="Helvetica 8  bold")

                    self.S = Scrollbar(self.listarupts)
                    self.T = Text(self.listarupts, height=10, width=80)
                    self.S.pack(side=RIGHT, fill=Y)
                    self.T.pack(side=LEFT, fill=Y)
                    self.S.config(command=self.T.yview)
                    self.T.config(yscrollcommand=self.S.set)

                    if self.result:
                        # self.i = 0
                        self.datos = self.result

                    else:
                        self.datos = 'No hay Premios por Puntos'

                    self.T.insert(END, "ID - Premio - Puntos - Puede Cambiar")
                    self.T.insert(END, "\n")

                    for premi in self.datos:
                        idprem = premi[0]
                        premio = premi[1]
                        ptos = premi[2]
                        self.T.insert(END, idprem)
                        self.T.insert(END, " - ")
                        self.T.insert(END, premio)
                        self.T.insert(END, " - ")
                        self.T.insert(END, ptos)

                        if puntos < ptos:
                            Cambiar = 'NO'
                        else:
                            Cambiar = 'SI'
                        self.T.insert(END, " - ")
                        self.T.insert(END, Cambiar)
                        self.T.insert(END, "\n")

                    mainloop()


    def Grabaptos(self):
        hoy = time.strftime("%Y%m%d")
        sql = "SELECT puntos FROM usuarios where email='" + self.usuario + "'"
        self.cursor.execute(sql)
        self.conn.commit()
        # resultado = run_query(sql)
        self.resultado = self.cursor.fetchall()
        if self.resultado:
            for resp in self.resultado:
                puntos = resp[0]

                if puntos == 0:
                    tkMessageBox.showerror("error", 'Usted no tiene puntos para cambiar')
                else:
                    idprod = self.txtcodidpre.get()
                    sqlP = "SELECT * FROM premios WHERE id= %i" % int(idprod)
                    #result = run_query(sqlP)
                    self.cursor.execute(sqlP)
                    self.conn.commit()
                    self.resultado = self.cursor.fetchall()
                    if self.resultado:
                        for resp in self.resultado:
                            puntosTot = resp[2]
                            producto = resp[1]

                        if puntosTot > puntos:
                            tkMessageBox.showerror("error",
                                                   "Usted no puede Cambiar los puntos por este premio, los puntos no son suficientes")
                            self.txtcodidpre.delete(0, END)
                        else:
                            TotPuntos = int(puntos) - int(puntosTot)
                            sqli = 'INSERT INTO premios_cambiados(idpremio,user,fecha) VALUES ("%s","%s","%s")' % (
                                idprod, self.usuario, hoy)
                            self.cursor.execute(sqli)
                            self.conn.commit()
                            actpuntos = "update usuarios set puntos='%s' where email='%s'" % (int(TotPuntos), self.usuario)
                            self.cursor.execute(actpuntos)
                            self.conn.commit()
                            tkMessageBox.showinfo("Información","Puntos redimidos por premio " + str(producto))
                            self.redime.destroy()
                    else:
                        tkMessageBox.showerror("error", "El código del premio no existe")
                        self.txtcodidpre.delete(0, END)

    def Listaptos(self):
        self.listarupts = Tk()
        self.listarupts.wm_title("Listado de Puntos")
        self.listarupts.grid_rowconfigure(0, weight=1)
        self.listarupts.grid_columnconfigure(0, weight=1)

        self.S = Scrollbar(self.listarupts)
        self.T = Text(self.listarupts, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        sql = "SELECT puntos FROM usuarios where email='" + self.usuario + "'"
        self.cursor.execute(sql)
        self.conn.commit()
        # resultado = run_query(sql)
        self.result = self.cursor.fetchall()
        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.datos = 'No Tiene Puntos'

        self.T.insert(END, "Puntos")
        self.T.insert(END, "\n")

        for premi in self.datos:
            ptos = premi[0]
            self.T.insert(END, ptos)
            self.T.insert(END, "\n")
        mainloop()

    def Factpendientes(self):

        self.listarupts = Tk()
        self.listarupts.wm_title("Listado de Facturas pendientes por pagar")
        self.listarupts.grid_rowconfigure(0, weight=1)
        self.listarupts.grid_columnconfigure(0, weight=1)

        self.S = Scrollbar(self.listarupts)
        self.T = Text(self.listarupts, height=10, width=80)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        sql = "SELECT * FROM factura where user='" + self.usuario + "'  and estado='sin_pagar'"
        self.cursor.execute(sql)
        self.conn.commit()
        # resultado = run_query(sql)
        self.result = self.cursor.fetchall()
        if self.result:
            # self.i = 0
            self.datos = self.result

        else:
            self.T.insert(END, 'No Hay facturas pendientes por pagar')
            self.T.insert(END, "\n")

        self.T.insert(END, "ID - Valor - Fecha Factura")
        self.T.insert(END, "\n")

        if self.result:
            for premi in self.datos:
                idf = premi[0]
                valorf = int(premi[2])
                fechaf = premi[3]

                self.T.insert(END, idf)
                self.T.insert(END, " - ")
                self.T.insert(END, valorf)
                self.T.insert(END, " - ")
                self.T.insert(END, fechaf)
                self.T.insert(END, "\n")
        mainloop()

    def Pagafact(self):

        hoy = time.strftime("%Y%m%d")
        sql = "SELECT * FROM factura where user='" + self.usuario + "'  and estado='sin_pagar'"
        self.cursor.execute(sql)
        self.conn.commit()
        #resultado = run_query(sql)
        self.resultado = self.cursor.fetchall()
        if self.resultado:
            self.pagafact = Tk()
            self.pagafact.wm_title("Pagar Facturas")
            self.pagafact.geometry("230x70+800+0")
            self.pagafact.grid_rowconfigure(0, weight=1)
            self.pagafact.grid_columnconfigure(0, weight=1)

            self.label_codfact = Tkinter.Label(self.pagafact, text="ID Factura: ", anchor=Tkinter.W,
                                             background="dark slate gray",
                                             foreground="white", font="Helvetica 8  bold")
            self.label_efe = Tkinter.Label(self.pagafact, text="Efectivo: ", anchor=Tkinter.W,
                                            background="dark slate gray",
                                            foreground="white", font="Helvetica 8  bold")

            self.label_codfact.grid(row=0, column=0, sticky=Tkinter.E + Tkinter.W)
            self.label_efe.grid(row=1, column=0, sticky=Tkinter.E + Tkinter.W)

            self.txtcodfact = Tkinter.Entry(self.pagafact)
            self.txtefe = Tkinter.Entry(self.pagafact)

            self.txtcodfact.grid(row=0, column=1, sticky=Tkinter.E + Tkinter.W)
            self.txtefe.grid(row=1, column=1, sticky=Tkinter.E + Tkinter.W)

            self.connectb = Tkinter.Button(self.pagafact, text="Pagar", font="Helvetica 10 bold",
                                           command=self.Grabafact)
            # self.cancelb=Tkinter.Button(self.parent,text="Cancelar",command=self.parent.quit,font="Helvetica 10 bold")

            self.connectb.grid(row=6, column=1, sticky=Tkinter.W)
            # self.cancelb.grid(row=2,column=2)

        else:
            tkMessageBox.showerror("error", 'No tiene facturas pendientes por pagar')

    def Grabafact(self):
        nfact = self.txtcodfact.get()
        efect = self.txtefe.get()

        if nfact == '' or efect == '':
            tkMessageBox.showerror("error", "Diligencie Todos los Campos")
        else:

            resfact = "select * from factura where id_fatura= %i" % (int(nfact))
            #resfa = run_query(resfact)
            self.cursor.execute(resfact)
            self.conn.commit()
            # resultado = run_query(sql)
            self.resfa = self.cursor.fetchall()

            if self.resfa:
                for regif in self.resfa:
                    apagar = regif[2]
                if int(efect) < int(apagar):
                    tkMessageBox.showerror("error", " pago incompleto -- falta efectivo ")
                else:
                    sql = "SELECT puntos FROM usuarios where email='" + self.usuario + "'"
                    #resultado = run_query(sql)
                    self.cursor.execute(sql)
                    self.conn.commit()
                    self.resultado = self.cursor.fetchall()
                    if self.resultado:
                        for resp in self.resultado:
                            puntos = resp[0]
                        ptos = (int(apagar) / 1000) + int(puntos)
                        upda = "update usuarios set puntos=%s where email='%s'" % (int(ptos), self.usuario)
                        #run_query(upda)
                        self.cursor.execute(upda)
                        self.conn.commit()

                        upda = "update factura set estado='liquidado' where id_fatura='%s'" % (nfact)
                        #run_query(upda)
                        self.cursor.execute(upda)
                        self.conn.commit()
                        vueltas = int(efect) - int(apagar)
                        if vueltas > 0:
                            tkMessageBox.showinfo("Información","Factura liquidada, devolucion : " + str(vueltas))
                        else:
                            tkMessageBox.showinfo("Información","Factura liquidada")

                        self.txtefe.delete(0, END)
                        self.txtcodfact.delete(0, END)
                        self.pagafact.destroy()
            else:
                tkMessageBox.showerror("error", " Id de  Factura no existe")
                self.txtcodfact.delete(0, END)

    def MenuCliente(self):

        self.cliente = Tk()
        self.cliente.geometry("500x500+0+0")
        self.menu = Menu(self.cliente)
        self.cliente.config(menu=self.menu)

        self.mercado = Menu(self.menu)
        self.menu.add_cascade(label="Hacer Mercado", menu=self.mercado)
        self.mercado.add_command(label="Ver Listado de Productos",command=self.Listar_Productos)
        self.mercado.add_command(label="Comprar Productos", command=self.Comprar_Productos)
        self.mercado.add_separator()
        self.mercado.add_command(label="Generar Factura", command=self.Genera_factura)
        self.mercado.add_command(label="Facturas pendientes x pago", command=self.Factpendientes)
        self.mercado.add_command(label="Pagar", command=self.Pagafact)



        self.puntos = Menu(self.menu)
        self.menu.add_cascade(label="Puntos", menu=self.puntos)
        self.puntos.add_command(label="Ver Puntos", command=self.Listaptos)
        self.puntos.add_command(label="Listado de premios Por Puntos", command=self.ListaPremios)
        self.puntos.add_command(label="Cambiar Puntos Por Puntos", command=self.CambiarPuntos)

        self.facturas = Menu(self.menu)
        self.menu.add_cascade(label="Facturas", menu=self.facturas)
        self.facturas.add_command(label="Ver Listado de Facturas", command=self.Listar_Facturas_cte)
        self.facturas.add_command(label="Detalle de las Facturas", command=self.Listar_Det_Facturas)

        self.salir = Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=self.salir)
        self.salir.add_command(label="Cerrar Sesión", command=self.cierra_cliente)

    def cerrar_sesion(self):
        exit()

    def cierra_cliente(self):
        self.cliente.destroy()

    def item_insertion_window(self):
        self.new_window=Tkinter.Toplevel(self)
        self.new_window.wm_title("Add my favorite stars")
        self.new_window.grid_rowconfigure(0, weight=1)
        self.new_window.grid_columnconfigure(0, weight=1)

        self.exitb=Tkinter.Button(self.new_window,text="Exit",command=self.new_window.quit)
        self.submitb=Tkinter.Button(self.new_window,text="Submit",command=self.increment_db)
        self.exitb.grid(row=8,column=1)
        self.submitb.grid(row=8,column=0,sticky=Tkinter.W)

        self.v=IntVar()
        self.tvstars=[('YOWERI KAGUTA MUSEVENI', 1), ('KIIZA BESIGYE', 2),
                      ('AMAAMA JOHN MBABAZI ', 3), ('KARUNGI SHARON', 4),
                      ('BYAMUKAMA OSCAR', 5), ('MATILDA MOREEN', 6),
                      ('DUNCANS', 7)]
        self.i=0
        for self.txt, star in self.tvstars:
            self.i=self.i+1
            self.rb=Tkinter.Radiobutton(self.new_window,text=self.txt,variable=self.v,value=star)
            self.rb.grid(row=self.i,column=0,sticky=Tkinter.W)


    def which_artist(self,radiob):
        self.artists = {
                        1:"YOWERI KAGUTA MUSEVENI",
                        2:"KIIZA BESIGYE",
                        3:"AMAAMA JOHN MBABAZI",
                        4:"KARUNGI SHARON",
                        5:"BYAMUKAMA OSCAR",
                        6:"MATILDA MOREEN",
                        7:"DUNCANS",
        }
        return self.artists.get(radiob,"Unknown")

    def increment_db(self):

        #print self.v.get()
        self.chosenartist = self.which_artist(self.v.get())
        print self.chosenartist

        self.config = {
                  'user': 'root',
                  'passwd': '',
                  'host': '127.0.0.1',
                  'db': 'supermercado',
        }

        try:

            self.connecttodb = MySQLdb.connect(**self.config)

        except MySQLdb.Error:

            print"Error de Conexión"

        self.cursor=self.connecttodb.cursor()

        self.cursor.execute("""INSERT INTO mystars(starname) VALUES(%s)""",self.chosenartist)

        self.connecttodb.commit()
        self.connecttodb.close()

try:
    raw_input
except NameError:
    raw_input = input


def main():
    s = socket()
    s.connect(("localhost", 35000))


    while True:
        output_data = raw_input("Desea Ingresar al Supermercado (S/N):  ")

        if output_data == 's' or output_data == 'S':

            try:
                s.send(output_data)
            except TypeError:
                s.send(bytes(output_data, "utf-8"))

            # Recibir respuesta.
            input_data = s.recv(1024)
            if input_data == '1':
                # En Python 3 recv() retorna los datos leídos
                # como un vector de bytes. Convertir a una cadena
                # en caso de ser necesario.
                print(input_data.decode("utf-8") if
                      isinstance(input_data, bytes) else input_data)

                root = Tk()
                app = Servidor(root)
                root.mainloop()
            else:
                print "Terminando Conexión"
                exit()


if __name__=="__main__":
    main()