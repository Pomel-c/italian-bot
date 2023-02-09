
# FUNCIONES DEL BOT DEL CONSULADO

def write(i, msg):
    ## Escribo el intentoro en el archivo
    num_file = open(".\Textos\intento.txt", "w") 
    num = repr(i)
    num_file.write(num)
    num_file.close()
    
    ## Escribo el Log del momento
    log_file = open(".\Textos\log.txt", "a") 
    data = repr(msg)
    log_file.write(data + '\n')
    log_file.close()


def read(i):
    if i == 'intento':
        f = open(".\Textos\intento.txt", "r")
        nums = f.readlines()
        return nums[0]
    else:
        with open('.\Textos\datos.txt') as file:
            reader = file.readlines()
            dato = reader[i].strip('\n')
            return(dato)
    
    



# FUNCIONES DEL BOT DE TELEGRAM
def wrt_nuevo(id_nuevo):
    ## Escribo nuevo integrante en la lists
    id_nuevo = id_nuevo
    path = ".\Textos\id_lista.txt"
    id_file = open(path, "a") 
    ide = repr(id_nuevo)
    id_file.write(ide)
    id_file.write('\n')
    id_file.close()



def wrt_list(id_list):
    ## Escribo nuevo integrante en la lists
    id_list = id_list
    # acomodar funcion
    with open(r'.\Textos\id_lista.txt', 'w') as fp:
        for item in id_list:
            # write each item on a new line
            fp.write("%s\n" % item)
    fp.close()



def rde_list():
    names = []
    with open(r'.\Textos\id_lista.txt', 'r') as fp:
        for line in fp:
            x = line[:-1]
            names.append(x)
    return names


def api():
    with open('.\Textos\datos.txt') as file:
        reader = file.readlines()
        api = reader[2].strip('\n')
    return api
    