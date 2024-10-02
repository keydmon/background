
#? vitacora --------------------------------------------------------------------------------------------------
#promema: eliminar el fonde de imagenes, generandome un png 
# tengo una capeta input y una output donde saldra el resultado y las originales me las dejara en otra carpeta
# la salida sera una carpeta que tenga el la fecha actual de la generacion de la imagen 
# version 1.0
# desarrollador keydmon


#?librerias -------------------------------------------------------------------------------------------------
# interaccion con el sistema operativo
import os
#manejo de fechas importamos el metodo date time de la libreria datetime
from datetime import datetime
#libreria que nos ayudara a eliminar el fondo se llama rembg - descargamos desde pip
#importamos el metodo que se encarga de remover imagenes que se llama remove
from rembg import remove

#?clase ----------------------------------------------------------------------------------------------------

class BackgroundRemove:
    #definimos el metodo constructor para mas adelante crear instancias de la misma
    def __init__(self,input_folder,output_folder):
        #definimos variables de instancia  
        self.input_folder = input_folder
        self.output_folder = output_folder
    #ahora hay que definir los metodos para solucionar el problema
    #! se definen los metodos propios del programa con un _ al inicio, esto hace saber que el usuaruio no podra
    #interactuar directamente con ellos
    
    #* 1. procesar la imagen, o alistarla - este proceso podra interactuar el usuario
    def process_img(self):
        # lo primero es saber la fecha actual con los resultados de las variables
        # llamamos la libreria y el metodo now pa que nos de la fecha actual y utilizamos el metodo strftime para 
        # para que retorne la fecha como string y en un orden deseado
        today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # ahora viene la logica de la creacion de la carpeta, definimos la variable
        #Se utiliza la función os.path.join() para concatenar el nombre del directorio de salida 
        # (self.output_folder) con la fecha y hora formateadas (today). Esto creará una ruta de acceso 
        # completa al directorio donde se almacenarán los archivos procesados.
        # es decir el nombre completo pa crear la carpeta 
        #el join toma uno o varios componens de la ruta y los vuelve uno solo 
        processed_folder = os.path.join(self.output_folder,today)
        #el join toma uno o varios componens de la ruta y los vuelve uno solo 
        # con la funcion makedirs, creamos el directorio especificado por la variable de arriba 
        #con la condicional que si existe no me genere conflicto
        os.makedirs(processed_folder,exist_ok=True)

         #a continuacion vamos crear la funcion que me va a reconocer las imagenes
         # primero creamos un ciclo for que se itere en todos los elementos que se enceuntran en una carpeta
         # en este caso la carpeta es la input folder que es entrada
         #el list dir va a contarlistar todo tipo de archivos, etnonces creamos una condicional para que seolo sean img


        for filename in os.listdir(self.input_folder):
            # la condicion es que si finaliza en por eso el .enswith va a iterar por todos los archivos pero  
            # rectifica si son imagenes y si si, que proceda con la logica.
            if filename.endswith(('.png','.jpg','.jpeg')):
               #la funcion path permite trabajar con rutas de archivos y directorios
               #creamos las rutas del archivo a verificar
               # se crea un input pat con el folder que pasa el usuario mas el nombre del archivo
               input_path = os.path.join(self.input_folder,filename)
               # y el archivo a modificar con la ruta de la carpeta final mas el nombre del archivo
               output_path = os.path.join ( processed_folder,filename)
               #! por ultimo pasamos a eliminar el back ground
               # para acceder a un metodo de mi misma clase le digo apuntese a usted misom y use su propio metodo 
               #* remove_backgraund
               # pasamos las atributos de las rutas de los elementos a procesar
               self._remove_backgraund(input_path,output_path )

               #* _move_original
               #las rutas de inicio y la de final
               self._move_original(input_path,processed_folder)

        
    #* 2. remover el background  - es un proceso interno del progarma
    # para remover el backgroud que necesitamos ?  asi es 
    # la ruta original y la ruta donde vamos a guardar 
   
    def _remove_backgraund(self,input_p,output_p ):
        #vamos a hacer un conext manager
        #el context manager permite que se ejecuten tareas antes y depues de de la ejecucion de un bloque de codigo
        # se inicializa con el with  y garantiza que las operaciones de inicializacion y limpieza se ejecuten bien 
        # el r es permiso de lectura y el w de escritura y como son elementos binarios (las imagenes) se agreba la b
        with open(input_p,'rb') as inp, open (output_p,'wb') as outp:
           #inportamos la funcion remove de la libreria, le pasamos la imagen que el context manager esta manejando inp
           # . read para que lea los binarios que contiene la imagen, y lo guarde en la variable que sera de tipo binario
           background_output = remove(inp.read())
           # y esto lo que va a a hacer es ya escribirme la imagen como binaria con el path que le defini
           outp.write(background_output)
           #ya aqui removimos el background, lo que sigue es mover los archivos



    #* 3.  mover las imagenes a original donde se van las imagenes que ingresamos - es un proceso interno del programa
    # lo primero es definir las rutas, primero definir la de origen
    # dentro de la carpeta de salida va a haber una subcarpeta que se llama orginales que es donde van las img originals
    #
    def _move_original(self,input_p,dest_p ):
        #creamos la variable que va a contener el path (ruta) de la carpeta oroginals
        #que vamos a unir? en este caso el path de la carpeta procesada con el de la nueva de origin
        original_folder= os.path.join(dest_p,'originals')
        #aqui creamos la carpeta 
        os.makedirs(original_folder,exist_ok=True)
        # ahora toca moverlos, tenemos ya el path de origen creado arriba pero falta el de destino 
        # y definir el nombre del archivo para ahcer el movimiento de las imagenes
        filename=os.path.basename(input_p) 
        # extraemos el nombre de la imagen de nuestro input que yo le estoy pasando
        # por ultimo creo el nuevo path donde iria nuestra imagen
        new_path= os.path.join(original_folder,filename)
        # y por ultimo se renombra el archivo con el nuevo nombre de origen 
        os.rename(input_p,new_path)

#? ----- programa para remover background de una imagen ---------------------------------------------

# aca solo falta crear la porcion de cigo que va a ejecutarla
# == se lee equals


if __name__  == '__main__':
#esta funcion sirve para Por lo tanto, se utiliza comúnmente para incluir el código que deseas que se 
#ejecute solo cuando el archivo se ejecute directamente y no cuando se importe como un módulo en otro programa.
    input_folder = 'input'
    output_folder = 'output'
    remover = BackgroundRemove(input_folder,output_folder)
    remover.process_img()

        

