from pathlib import Path
def get_files():
    archivos=[]
    ruta = Path(r'C:\Users\AdminHP\Desktop\Practica')
    for elemento in ruta.iterdir(): #.iterdir() te da la lista de archivos y sus propiedades
        if elemento.is_file():
            archivos.append(elemento)
    return archivos


def rename_files():
    ArchivosRenamed= []
    archivos=get_files()
    for index, archivo in enumerate(archivos, start=0):
        nuevoarchivo=archivo.rename(archivo.with_stem("papas_"+ str(index)))#cambia nombre pero conserva extension para cambiar extension es en vez de stem es name
        ArchivosRenamed.append(nuevoarchivo)
    return ArchivosRenamed

def main():
    archivos= get_files()
    for archivo in archivos:
        print (archivo.name)
        
    archivos=rename_files()
    for archivo in archivos:
        print(archivo.name)
        
    

if __name__ == "__main__":
    main()