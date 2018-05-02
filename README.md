# Ventas de Videojuegos

## Instrucciones:

* Deben trabajar en una carpeta que contenga los archivos __games_sales.py__ y __Games_Sales.csv__.
* Al inicio del codigo agregar la siguiente linea:  
``` [Python]
 from games_sales import games,sales
 ```
 * Con esto realizado dispondran de una lista llamada __games__ y un diccionario llamado __sales__ cuya estructura es la siguiente:    
 ``` [Python]
 games = [(id_juego,nombre,consola,desarrollador,genero,crtica,(año_salida,mes_salida,dia_salida)...]
 sales = {id_juego : (ventas_NA,ventas_PAL,ventas_Japon,ventas_Otros)...}
 ```

 * Programe una funcion que reciba como entrada el año 
