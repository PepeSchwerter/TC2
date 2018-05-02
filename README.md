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
 
