# BWT_Oprescu_Riccardo



<h2>BWT - Burrow Wheeler</h2>

parte da BANANA

<h3>step 1:</h3>
si aggiunge $ alla fine, e si calcolano tutte le permutazioni delle lettere spostando l'ultima parola al inizio

1. B A N A N A $ (Stringa originale)
2. $ B A N A N A (L'ultimo carattere $ passa davanti)
3. A $ B A N A N (L'ultimo carattere A passa davanti)
4. N A $ B A N A (L'ultimo carattere N passa davanti)
5. A N A $ B A N (L'ultimo carattere A passa davanti)
6. N A N A $ B A (L'ultimo carattere N passa davanti)
7. A N A N A $ B (L'ultimo carattere A passa davanti)


<h3>step2:</h3>
ordine lessicografico

1) $BANANA
2) A$BANAN
3) ANA$BAN


<h3>step 3:</h3>
il risultato è la parola che si forma con l'ultima lettera delle righe della matrice step2

_______________________________________________________________________________________________


<h2>Parte 2</h2>

 due script "client.py" e "server.py" che utilizzino dei socket TCP per lo scambio di informazioni.
 Il client invia una stringa al server;
 
 il server elabora la trasformata e la restituisce al client.
<code>
```
---
py Client.py 

Inserisci un qualcosa da trasformare...
BANANA 
Reply:  ['A', 'N', 'N', 'B', '$', 'A', 'A']
---
```


</code>
_______________________________________________________________________________________________

In fine fare relazione spiegando funzionamento, applicazione e implementazione dell'algoritmo in un pdf