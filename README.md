# Ventas de Videojuegos

## Instrucciones:

* Deben trabajar en una carpeta que contenga los archivos __games_sales.py__ y __Games_Sales.csv__.
* Al inicio del codigo agregar la siguiente linea:  
``` [Python]
 from games_sales import games,sales
 ```
 * Con esto realizado dispondran de una lista llamada __games__ y un diccionario llamado __sales__ cuya estructura es la siguiente:    
 ``` [Python]
 games =  [(id_juego,nombre,consola,desarrollador,genero,crtica,(año_salida,mes_salida,dia_salida))...]
 sales = {id_juego : (ventas_NA,ventas_PAL,ventas_Japon,ventas_Otros)...}
 ```

* __Importante__: Es posible que algunos valores puedan tomar el valor *None* si es que no se tiene registro de este. Tenga en cuenta esto al momento de usar las estructuras. Los valores que pueden tomar este valor son:
  * La critica del juego
  * La tupla con la fecha de salida
  * Cualquier elemento de la tupla de ventas
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
 * Escriba una funcion que reciba el año de salida, y muestre en pantalla el juego mas vendido de cada genero para ese año, imprimiendo ademas la consola al que pertenece.
 Ejemplo:
  ``` [Python]
 genresTopOne(2000)
 Generos  1999
 -  Role-Playing :  Pokmon Yellow: Special Pikachu Edition  -  GB
 -  Puzzle :  Pong: The Next Level  -  PS
 -  Shooter :  007: Tomorrow Never Dies  -  PS
 -  Misc :  Pokmon Pinball  -  GBC
 -  Fighting :  Super Smash Bros.  -  N64
 -  Sports :  Tony Hawk's Pro Skater  -  PS
 -  Platform :  Donkey Kong 64  -  N64
 -  Strategy :  Warzone 2100  -  PS
 -  Adventure :  Star Wars Episode I: The Phantom Menace  -  PS
 -  Action :  Driver  -  PS
 -  Simulation :  Pokmon Snap  -  N64
 -  Racing :  Gran Turismo 2  -  PS
 ```
 * Cree una funcion que reciba como entrada una consola, e imprima el TOP 10 de juegos mas vendidos para esa consola, mostrando el nombre y el año de lanzamiento del juego.  
 Ejemplo:
  ``` [Python]
 topTenByConsole("SNES")
 - 1   Super Mario World  -  1991
 - 2   Super Mario All-Stars  -  1993
 - 3   Donkey Kong Country  -  1994
 - 4   Super Mario Kart  -  1992
 - 5   Street Fighter II: The World Warrior  -  1992
 - 6   Donkey Kong Country 2: Diddy's Kong Quest  -  1995
 - 7   The Legend of Zelda: A Link to the Past  -  1992
 - 8   Super Mario World 2: Yoshi's Island  -  1995
 - 9   Street Fighter II Turbo  -  1993
 - 10   Donkey Kong Country 3: Dixie Kong's Double Trouble!  -  1996
 ```
 * Programe una funcion que imprima en un formato similar a la funcion anterior, un TOP con las mejores consolas, basado en el promedio de criticas de sus juegos respectivos.
 Ejemplo:
 ``` [Python]
 bestConsole()
 ...
 ```
 
 
