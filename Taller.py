import sqlite3 as dbapi
from gi.repository import Gtk

class taller:

    fichero2 = "inicio.glade"
    builder2 = Gtk.Builder()
    builder2.add_from_file(fichero2)
    lnombre = builder2.get_object("lnombre")
    lcontraseña = builder2.get_object("lcontraseña")
    nombre = builder2.get_object("nombre")
    contraseña = builder2.get_object("contraseña")
    lprueba = builder2.get_object("lprueba")
    ventanaEntrada = builder2.get_object("inicio")
    ventanaEntrada.show_all()
    # Conexión con la base de datos, y conectar a la interface
    bd = dbapi.connect("basedatos.dat")
    fichero = "taller.glade"
    print(bd)
    cursor = bd.cursor()
    builder = Gtk.Builder()
    builder.add_from_file(fichero)


    # Método Consultar, imprime los datos de la base por consola
    def on_consultar_clicked(self, control):
        self.cursor.execute("""Select * from taller;""")
        for resultado in self.cursor:
            print("Matricula: " + str(resultado[0]) + ", Vehiculo: " + str(resultado[1]) + ", Kilometros: " + str(
            resultado[2]) + ", Fecha Reparacion: " + str(resultado[3])+ ", Cliente: " + str(
            resultado[4])+ ", CIF o NIF: " + str(resultado[5])+ ", Telefono: " + str(
            resultado[6])+ ", Direccion: " + str(resultado[7]))
       # print(salida);

    # Método Borrar
    def on_borrar_clicked(self, borrar):
        matricula = self.matricula.get_text()
        print("El evento está siendo borrado por código")
        self.cursor.execute("delete from taller where matricula ='" + matricula + "'")
        print("Borrado")
        self.bd.commit()

    # Método Modificar. Modifica a través de la primary Key
    def on_Modificar_clicked(self, modificar):
        vehiculo = self.vehiculo.get_text()
        kilometros = self.kilometros.get_text()
        fecha = self.fecha.get_text()
        cliente = self.cliente.get_text()
        cifnif = self.cifnif.get_text()
        telefono = self.telefono.get_text()
        direccion= self.direccion.get_text()
        matricula = self.matricula.get_text()
        print("Esperando datos")
        self.cursor.execute("update taller set vehiculo ='" + vehiculo + "'"
                                             ",kilometros='" + kilometros + "'"
                                             ",fecha='" + fecha + "'"
                                             ",cliente='" + cliente + "'"
                                             ",cif='" + cifnif +"'"
                                             ",telefono='" + telefono +"'"
                                             ",direccion='" + direccion +"' where matricula='" + matricula + "'")
        print("Modificado")
        self.bd.commit()


    # Método de entrada para poder acceder por usuario y contraseña a la segunda ventana
    def on_Entrada_clicked(self, entrada):
        nombre = self.nombre.get_text();
        contraseña = self.contraseña.get_text();
        if nombre == "taller" and contraseña == "merda":
            self.lprueba.set_text(" %s" % "Peritas estas dentro")
            self.ventana = self.builder.get_object("window1")
            self.ventana.show_all()
            self.ventanaEntrada.hide();
        else:
            self.lprueba.set_text("Prueba otra vez")

    # Método insertar
    def on_insertar_clicked(self, control):
        matricula = self.matricula.get_text()
        vehiculo = self.vehiculo.get_text()
        kilometros = self.kilometros.get_text()
        fecha = self.fecha.get_text()
        cliente = self.cliente.get_text()
        cifnif = self.cifnif.get_text()
        telefono = self.telefono.get_text()
        direccion= self.direccion.get_text()
        print("inserte")
        self.cursor.execute(
            "insert into taller values('" + matricula + "'"
                                     ",'" + vehiculo + "'"
                                     ",'" + kilometros + "'"
                                     ",'" + fecha+"'"
                                     ",'" + cliente + "'"
                                     ",'" + cifnif +"'"
                                     ",'" + telefono +"'"
                                     ",'" + direccion +"')")
        print("Insertado")
        # Siempre se debe hacer un commit al final de cada evento
        self.bd.commit()

    def __init__(self):
        self.ventanaEntrada.show_all();
        # Señales, aquí se declaran los métodos anteriormente comentados, para que al pulsar accedan
        sinais = {"on_insertar_clicked": self.on_insertar_clicked,
                  "on_consultar_clicked": self.on_consultar_clicked,
                  "on_borrar_clicked": self.on_borrar_clicked,
                  "on_Modificar_clicked": self.on_Modificar_clicked,
                  "on_Entrada_clicked": self.on_Entrada_clicked,
                  "on_FiestraPrincipal_destroy": Gtk.main_quit}
        self.builder2.connect_signals(sinais)
        self.builder.connect_signals(sinais)

        self.matricula = self.builder.get_object("matricula")
        self.vehiculo = self.builder.get_object("vehiculo")
        self.kilometros = self.builder.get_object("kilometros")
        self.fecha = self.builder.get_object("fecha")
        self.cliente = self.builder.get_object("cliente")
        self.cifnif = self.builder.get_object("cifnif")
        self.telefono = self.builder.get_object("telefono")
        self.direccion = self.builder.get_object("direccion")

taller()
Gtk.main()
