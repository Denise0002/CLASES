from rich import print
from rich.markdown import Markdown
edad=20
respuesta="es mayor de edad" if edad>17 else "es menor de edad"
texto="""
   # parrafo
   ```bash
   git commmit -m "titulo" -m "cuerpo del commit 
   #commentario 
   ```
   *lista 
   *lista
   *lista
   > informacion valiosa
   {}
""".format(respuesta)
#edad=17
#respuesta="[bold green] es mayor de edad" if edad>17 else "[italic underline purple]es menor de edad"

mostrar_mark=Markdown(texto)
print(mostrar_mark)

