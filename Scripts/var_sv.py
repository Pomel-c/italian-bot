
def wrt(i, msg):
    ## Escribo el numero en el archivo
    nume = i
    path = "D:\Documentos\Bot ciudadania\Textos\sumero.txt"
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
    path = "D:\Documentos\Bot ciudadania\Textos\sumero.txt"
    f = open(path, "r")
    nums = f.readlines()
    nums = [int(i) for i in nums]
    n = nums[0] 
    return n

