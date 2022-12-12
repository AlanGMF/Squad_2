import os

DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/api/utils')

def get_csv_files() -> list:
    output_dir = f'{DIR}/utils/etl/processed_data/'
    rootDir = output_dir
    #result = {}  # Declaramos el diccionario

    for dirName, subdirList, fileList in os.walk(rootDir):
        filenames = []  # Declaramos la lista en la que se almacenarán los nombres de archivo.
        for fname in fileList:
            filenames.append(output_dir + fname)  # Añadimos el nombre de archivo a la lista
        #result[dirName] = filenames  # y por último seteamos el diccionario (como clave está el directorio y como valor los archivos.
    print(filenames)
get_csv_files()