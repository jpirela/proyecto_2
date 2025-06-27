#import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk, GLib
#import sqlite3
#cx = sqlite3.connect("test.db")
#cu = cx.cursor()

GLADE_FILE = "Proyecto_1_Gabriel_Cabrera.glade"





#####################################################################################
def encriptar(texto, llave):
    resultado = []
    for caracter in texto:
        for simbolo in ctr:
            if caracter == simbolo:
                caracter = ord(caracter) + llave
                caracter = verificar(caracter, 32, 47)
                resultado.append(caracter)
                break
        else:
            for simbolo in num:
                if caracter == simbolo:
                    caracter = ord(caracter) + llave
                    caracter = verificar(caracter, 48, 57)
                    resultado.append(caracter)
                    break
            else:
                for simbolo in op:
                    if caracter == simbolo:
                        caracter = ord(caracter) + llave
                        caracter = verificar(caracter, 58, 64)
                        resultado.append(caracter)
                        break
                else:
                    for simbolo in abecedario_mayus:
                        if caracter == simbolo:
                            caracter = ord(caracter) + llave
                            caracter = verificar(caracter, 65, 90)
                            resultado.append(caracter)
                            break
                    else:
                        for simbolo in abecedario:
                            if caracter == simbolo:
                                caracter = ord(caracter) + llave
                                caracter = verificar(caracter, 97, 122)
                                resultado.append(caracter)
                                break
                        else:
                            for simbolo in ls:
                                if caracter == simbolo:
                                    caracter = ord(caracter) + llave
                                    caracter = verificar(caracter, 123, 126)
                                    resultado.append(caracter)
                                    break
                            else:
                                resultado.append(caracter)
    resultado = "".join(resultado)
    return resultado
#####################################################################################





def operacion():
    resultado = []
    texto = "funciona muy bien" #text_entry.get_text()
    if texto == "":
        #text_display.set_text("La entrada de texto no tiene contenido")
        return "La entrada de texto no tiene contenido"
    llave_list = "Nanbg" #key.get_text()
    if llave_list == "":
        #text_display.set_text("La llave esta vacia")
        return "La llave esta vacia"
    salir = 0
    i = 0
    lims_llave = len(llave_list) - 1
    lim_llave = limite(0, lims_llave)
    for caracter in texto:
        caracter_num = ord(caracter)
        i = i_plus(i, lims_llave, lim_llave)
        llave = num_llave(llave_list, i)
        for lista in listas:
            salir = l_op(resultado, caracter_num, lista, llave)
            if salir == 1:
                i = i + 1
                break
        else:
            resultado.append(caracter)
    resultado = "".join(resultado)
    #text_display.set_text(resultado)
    return resultado

def l_op(resultado, caracter_num, lista, llave):
    lim_inferior = limite_inferior(lista)
    lim_superior = limite_superior(lista)
    if (caracter_num >= lim_inferior and caracter_num <= lim_superior):
        caracter_num = caracter_num + llave
        caracter_num = verificar(caracter_num, lim_inferior, lim_superior)
        resultado.append(caracter_num)
        return 1
    return 0



def num_llave(llave_list, i):
    return ord(llave_list[i])

def i_plus(i, lims_llave, lim_llave):
    if i >= lims_llave:
        return i - lim_llave
    return i



def verificar(caracter, limete_inferior, limite_superior):
    lim = limite(limete_inferior, limite_superior)
    while (caracter < limete_inferior or caracter > limite_superior):
        if caracter < limete_inferior:
            caracter = caracter + lim
        elif caracter > limite_superior:
            caracter = caracter - lim
    return chr(caracter)



def limite_inferior(lista):
    return ord(lista[0])

def limite_superior(lista):
    return ord(lista[(len(lista)-1)])

def limite(limite_inferior, limite_superior):
    return (limite_superior - limite_inferior + 1)



def generar_lista(limite_inferior, limite_superior):
    lista = []
    limite_superior += 1
    for i in range(limite_superior):
        if i < limite_inferior:
            pass
        else:
            character = chr(i)
            lista.append(character)
    return lista





def ver_num(caracter):
    return ord(caracter)

def ver_chr(num):
    return chr(num)






#def on_window_destroy(window, data=None):
#    Gtk.main_quit()

#def cargar_glade():
#    builder = Gtk.Builder()
#    builder.add_from_file(GLADE_FILE)
#
#
#    window = builder.get_object("main_window")
#
#    text_entry = builder.get_object("Text_entry")
#    key = builder.get_object("Key")
#    text_display = builder.get_object("Text_result")
#    button = builder.get_object("start")
#
#
#    window.connect("destroy", on_window_destroy)
#    button.connect("clicked", on_button_clicked)
#
#    window.show_all()

#def on_button_clicked(button):
#    operacion()


if __name__ == "__main__":
    #texto = "funciona muy bien"
    ctr = generar_lista(32, 47)
    num = generar_lista(48, 57)
    op = generar_lista(58, 64)
    abecedario_mayus = generar_lista(65, 90)
    abecedario = generar_lista(97, 122)
    ls = generar_lista(123, 126)
    listas = [ctr, num, op, abecedario_mayus, abecedario, ls]
    #print(texto)
    print(operacion())
    #print(operacion(texto="z", llave=0))
    #print(limite_inferior(abecedario))
    #print(limite_superior(abecedario))
    #print(ver_num("9"))
    #print(ver_chr(78))
    #texto_encriptado = encriptar(texto, 5)
    #print(texto)
    #print(texto_encriptado)
    #lim = limite(97, 122)
    #print(lim)
    #cargar_glade()
    #Gtk.main()