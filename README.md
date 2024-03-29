# Confiabilidad de la técnica CRC

Este software calcula el código de redundancia cíclica de un mensaje de texto sin saltos de línea. Además, el programa verifica la probabilidad de que ocurra un falso negativo, es decir, de que el descodificador regrese un residuo de cero cuando el mensaje tiene errores.

Matemáticamente, estas probabilidades son bien conocidas, de tal manera que:

1. las ráfagas de errores son detectadas al 100% cuando L ≤ r o
2. son detectadas con probabilidad 1 - (1/2)^(r-1) cuando L = r + 1 o
3. son detectadas con probabilidad 1 - (1/2)^(r) cuando L > r + 1,

donde L es la longitud de la ráfaga y r es el número de bits que integran el código CRC.

## Dependencias

```PowerShell
pip3 install bitarray matplotlib
```

## Pruebas

Para probar la primera propiedad, basta con ejecutar el script crc_test de la siguiente manera:

```PowerShell
python.exe .\main.py .\test.txt 10011 4 0 1000
```

El argumento `test.txt` contiene el texto al que se le calculará el CRC, 10011 es el polinomio generador, el primer 4 corresponde a la longitud del código CRC, mientras que el segundo 4 corresponde al tamaño de la ráfaga de errores. El siguiente entero corresponde a la semilla que se utilizará para inicializar el estado del generador de número pseudoaleatorios. El último entero indica el número de veces que el experimento se va a repetir.

Si se desea comprobar la segunda propiedad, se puede emplear la siguiente configuración, en la que solo se varia el tamaño de la ráfaga a cinco.

```PowerShell
python.exe .\main.py .\test.txt 10011 5 0 1000
```

La tercera propiedad se puede validar modificando el tamaño de la ráfaga a seis.


```PowerShell
python.exe .\main.py .\test.txt 10011 6 0 1000
```
