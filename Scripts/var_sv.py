
# FUNCIONES DEL BOT DEL CONSULADO

def wrt(i, msg):
    ## Escribo el numero en el archivo
    nume = i
    path = "D:\Documentos\Bot ciudadania\Textos\intento.txt"
    num_file = open(path, "w") 
    num = repr(nume)
    num_file.write(num)
    num_file.close()
    
    ## Escribo el Log del momento
    msg = msg
    path = "D:\Facultad UM\log.txt"
    log_file = open(path, "a") 
    data = repr(msg)
    log_file.write(data)
    log_file.write('\n')
    log_file.close()

def rde():
    ## Leo el numero que esta escrito en el archivo
    path = "D:\Documentos\Bot ciudadania\Textos\intento.txt"
    f = open(path, "r")
    nums = f.readlines()
    nums = [int(i) for i in nums]
    n = nums[0] 
    return n


# FUNCIONES DEL BOT DE TELEGRAM



def wrt_nuevo(id_nuevo):
    ## Escribo nuevo integrante en la lists
    id_nuevo = id_nuevo
    path = "D:\Documentos\Bot ciudadania\Textos\id_lista.txt"
    id_file = open(path, "a") 
    ide = repr(id_nuevo)
    id_file.write(ide)
    id_file.write('\n')
    id_file.close()



def wrt_list(id_list):
    ## Escribo nuevo integrante en la lists
    id_list = id_list
    # acomodar funcion
    with open(r'D:\Documentos\Bot ciudadania\Textos\id_lista.txt', 'w') as fp:
        for item in id_list:
            # write each item on a new line
            fp.write("%s\n" % item)
    fp.close()



def rde_list():
    names = []
    with open(r'D:\Documentos\Bot ciudadania\Textos\id_lista.txt', 'r') as fp:
        for line in fp:
            x = line[:-1]
            names.append(x)
    return names


def api():
    path = "D:\Documentos\Bot ciudadania\Textos\API_KEY.txt"
    f = open(path, "r")
    api = f.readlines()
    api = api[0]
    
    
    return api
    