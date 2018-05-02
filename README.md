# Ventas de Videojuegos

## Instrucciones:

* Deben trabajar en una carpeta que contenga los archivos __games_sales.py__ y __Games_Sales.csv__.
* Al inicio del codigo agregar la siguiente linea:  
``` [Python]
 from games_sales import games,sales
 ```
 * Con esto realizado dispondran de una lista llamada __games__ y un diccionario llamado __sales__ cuya estructura es la siguiente:    
 ``` [Python]
 ga [(id_juego,nombre,consola,desarrollador,genero,crtica,(año_salida,mes_salida,dia_salida))...]
 sales = {id_juego : (ventas_NA,ventas_PAL,ventas_Japon,ventas_Otros)...}
 ```

 * Programe una funcion que pueda recibir como parametro opcional el año de lanzamiento, y devuelva una sub-lista de __games__ cuyo año de lanzamiento sea el ingresado. Si no se ingresa nada devuelve la misma lista.  
 Ejemplo:
 ``` [Python]
 print getByDate(1999)
 > [(5, 'Pong: The Next Level', 'PS', 'Hasbro Interactive', 'Puzzle', None, (1999, 10, 31))
    (59, 'Need for Speed: High Stakes', 'PS', 'Electronic Arts', 'Racing', None, (1999, 3, 1))
    (60, 'Star Wars Episode I Racer', 'N64', 'LucasArts', 'Racing', 8.7, (1999, 5, 19))
    (64, 'Madden NFL 2000', 'PS', 'EA Sports', 'Sports', None, (1999, 7, 31))
    (93, 'Rugrats Studio Tour', 'PS', 'THQ', 'Adventure', None, (1999, 11, 10))...]
 ```
 * Desafio: Programe la misma funcion pero que a la vez reciba el mes y el dia como parametros opcionales.
 * Escriba una funcion que reciba el año de salida, y muestre en pantalla el juego mas vendido de cada genero para ese año.
 Ejemplo:
  ``` [Python]
 genresTopOne(2000)
 Generos  2000
-  Role-Playing :  Pokmon Gold / Silver Version  -  GB
-  Shooter :  Perfect Dark  -  N64
-  Misc :  Crash Bash  -  PS
-  Fighting :  Tekken Tag Tournament  -  PS2
-  Strategy :  Pokmon Stadium  -  N64
-  Platform :  Spyro: Year of the Dragon  -  PS
-  Adventure :  The Legend of Zelda: Majora's Mask  -  N64
-  Action :  Driver 2  -  PS
-  Simulation :  Hey You  Pikachu!  -  N64
-  Sports :  Tony Hawk's Pro Skater 2  -  PS
-  Racing :  Colin McRae Rally  -  PS
 ```
 
