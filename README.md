# BWT_Oprescu_Riccardo



<h1>BWT - Burrow Wheeler</h1>

parte da BANANA

<h2>step 1:</h2>
si aggiunge $ alla fine, e si calcolano tutte le permutazioni delle lettere spostando l'ultima parola al inizio

1. B A N A N A $ (Stringa originale)
2. $ B A N A N A (L'ultimo carattere $ passa davanti)
3. A $ B A N A N (L'ultimo carattere A passa davanti)
4. N A $ B A N A (L'ultimo carattere N passa davanti)
5. A N A $ B A N (L'ultimo carattere A passa davanti)
6. N A N A $ B A (L'ultimo carattere N passa davanti)
7. A N A N A $ B (L'ultimo carattere A passa davanti)


<h2>step2:</h2>
ordine lessicografico

1) $BANANA
2) A$BANAN
3) ANA$BAN


<h1>step 3:</h1>
il risultato è la parola che si forma con l'ultima lettera delle righe della matrice step2

_______________________________________________________________________________________________--

In fine fare relazione spiegando funzionamento, applicazione e implementazione dell'algoritmo in un pdf