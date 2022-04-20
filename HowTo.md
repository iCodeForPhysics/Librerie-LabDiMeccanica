<h1>Come usare una libreria.</h1>

1) Creare un file .py
2) Importare la libreria con la dicitura "```import **nome libreria**```"<br>
   Altri modi per importare una libreria:<br>
   ```from **nome libreria** import **nome funzione 1**, ..., **nome funzione x**```<br>
   ```import **nome libreria** as **nome semplificato**```<br>
   Esempio:<br>
   ```
   1  import my_lib_incertezze as inc
   ```
3) Utilizzare la libreria<br>
   In base al modo in cui avete importato la libreria le funzioni vanno chiamate in maniera diversa<br>
   import **nome libreria** -> ```**nome libreria**.**nome funzione**(argomenti)```<br>
   from **nome libreria** import **nome funzione 1** -> ```**nome funzione**(argomenti)```<br>
   import **nome libreria** as **nome semplificato** -> ```**nome semplificato**.**nome funzione**(argomenti)```<br>
   Esempio:<br>
   ```
   1  import my_lib_incertezze as inc
   2  inc.incPropagate(args)
   ```
