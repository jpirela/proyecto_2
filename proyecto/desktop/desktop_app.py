import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import sqlite3

cx = sqlite3.connect("app.db")
cu = cx.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS llave (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT)")
cx.commit()
cu.execute("CREATE TABLE IF NOT EXISTS texto (id INTEGER PRIMARY KEY AUTOINCREMENT, texto_inicial TEXT, texto_resultante TEXT, key_id INTEGER)")
cx.commit()

class applicacion:
    def __init__(self):
        self.glade_file = "Proyecto_1_Gabriel_Cabrera.glade"
        self.text_e = ""
        self.text_r = ""
        self.text_k = ""
        self.max_text_length = 250
        self.max_key_length = 50

        ctr = self.generar_lista(32, 47)
        num = self.generar_lista(48, 57)
        op = self.generar_lista(58, 64)
        abecedario_mayus = self.generar_lista(65, 90)
        abecedario = self.generar_lista(97, 122)
        ls = self.generar_lista(123, 126)
        self.listas = [ctr, num, op, abecedario_mayus, abecedario, ls]

        self.builder = Gtk.Builder()
        self.cargar_glade()
    
    def cargar_glade(self):
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("main_window")

        self.Text_entry = self.builder.get_object("Text_entry")
        self.Text_entry.set_text(self.text_e)

        self.key = self.builder.get_object("Key")
        self.key.set_text(self.text_k)

        self.Text_result = self.builder.get_object("Text_result")
        self.Text_result.set_label(self.text_r)

        self.button = self.builder.get_object("encode")
        self.button2 = self.builder.get_object("decode")

        self.window.connect("destroy", self.on_window_destroy)
        self.button.connect("clicked", self.on_button_clicked)
        self.button2.connect("clicked", self.on_button2_clicked)

        self.window.show_all()
    
    def recargar(self):
        self.window.hide()
        self.cargar_glade()

    def on_button_clicked(self, button):
        self.text_r = self.operacion(o=0)
        self.recargar()
    
    def on_button2_clicked(self, button2):
        self.text_r = self.operacion(o=1)
        self.recargar()
    
    def on_window_destroy(window, data=None):
        Gtk.main_quit()
        

    def operacion(self, o):
        resultado = []
        self.text_e = self.Text_entry.get_text()
        self.text_k = self.key.get_text()
        text_length = self.longitud(self.text_e)
        key_length = self.longitud(self.text_k)
        if text_length == 0 and key_length == 0:
            return "Ambos la entrada de texto y la llave estan vacias"
        if text_length == 0:
            return "La entrada de texto no tiene contenido"
        if key_length == 0:
            return "La llave esta vacia"
        if text_length > self.max_text_length and key_length > self.max_key_length:
            return "Ambos textos en la entrada de texto y en la llave son muy largos"
        if text_length > self.max_text_length:
            return "El texto en la entrada de texto es muy largo"
        if key_length > self.max_key_length:
            return "El texto en la llave es muy largo"
        salir = 0
        i = 0
        lims_llave = len(self.text_k) - 1
        lim_llave = self.limite(0, lims_llave)
        for caracter in self.text_e:
            caracter_num = ord(caracter)
            i = self.i_plus(i, lims_llave, lim_llave)
            llave = self.num_llave(self.text_k, i)
            if o == 1:
                llave = -llave
            for lista in self.listas:
                salir = self.l_op(resultado, caracter_num, lista, llave)
                if salir == 1:
                    i = i + 1
                    break
            else:
                resultado.append(caracter)
        resultado = "".join(resultado)
        self.save_key(self.text_k)
        self.save_text(self.text_e, self.text_r, self.text_k)
        return resultado

    def l_op(self, resultado, caracter_num, lista, llave):
        lim_inferior = self.limite_inferior(lista)
        lim_superior = self.limite_superior(lista)
        if (caracter_num >= lim_inferior and caracter_num <= lim_superior):
            caracter_num = caracter_num + llave
            caracter_num = self.verificar(caracter_num, lim_inferior, lim_superior)
            resultado.append(caracter_num)
            return 1
        return 0



    def num_llave(self, llave_list, i):
        return ord(llave_list[i])

    def i_plus(self, i, lims_llave, lim_llave):
        if i >= lims_llave:
            return i - lim_llave
        return i



    def verificar(self, caracter, limete_inferior, limite_superior):
        lim = self.limite(limete_inferior, limite_superior)
        while (caracter < limete_inferior or caracter > limite_superior):
            if caracter < limete_inferior:
                caracter = caracter + lim
            elif caracter > limite_superior:
                caracter = caracter - lim
        return chr(caracter)



    def limite_inferior(self, lista):
        return ord(lista[0])

    def limite_superior(self, lista):
        return ord(lista[(len(lista)-1)])

    def limite(self, limite_inferior, limite_superior):
        return (limite_superior - limite_inferior + 1)
    
    def longitud(self, text):
        return len(text)

    def save_key(self, llave):
        cu.execute("SELECT COUNT(*) FROM llave WHERE key = ?", [llave])
        existe = cu.fetchone()[0]
        if existe > 0:
            return
        cu.execute("INSERT INTO llave (key) VALUES (?)", [llave])
        cx.commit()
    
    def save_text(self, text_e, text_r, llave):
        cu.execute("SELECT id FROM llave WHERE key = ?", [llave])
        id_key = cu.fetchone()[0]
        cu.execute("SELECT COUNT(*) FROM texto WHERE texto_inicial = ? and texto_resultante = ? and key_id = ?", (text_e, text_r, id_key))
        existe = cu.fetchone()[0]
        if existe > 0:
            return
        cu.execute("INSERT INTO texto (texto_inicial, texto_resultante, key_id) VALUES (?, ?, ?)", (text_e, text_r, id_key))
        cx.commit()


    def generar_lista(self, limite_inferior, limite_superior):
        lista = []
        limite_superior += 1
        for i in range(limite_superior):
            if i < limite_inferior:
                pass
            else:
                character = chr(i)
                lista.append(character)
        return lista

if __name__ == "__main__":
    app = applicacion()
    Gtk.main()
cx.close()