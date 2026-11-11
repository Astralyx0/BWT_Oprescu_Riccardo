
'''
BWT - Burrow Wheeler
parte da BANANA

step 1:
si aggiunge $ alla fine, e si calcolano tutte le permutazioni delle lettere spostando l'ultima parola al inizio

1. B A N A N A $ (Stringa originale)
2. $ B A N A N A (L'ultimo carattere $ passa davanti)
3. A $ B A N A N (L'ultimo carattere A passa davanti)
4. N A $ B A N A (L'ultimo carattere N passa davanti)
5. A N A $ B A N (L'ultimo carattere A passa davanti)
6. N A N A $ B A (L'ultimo carattere N passa davanti)
7. A N A N A $ B (L'ultimo carattere A passa davanti)


step2:
ordine lessicografico

1) $BANANA
2) A$BANAN
3) ANA$BAN


step 3:
il risultato è la parola che si forma con l'ultima lettera delle righe della matrice step2

___________________

In fine fare relazione spiegando funzionamento, applicazione e implementazione dell'algoritmo in un pdf

'''

#parte 2 : socket

import socket as skt
with skt.socket(skt.AF_INET, skt.SOCK_STREAM) as bwt:
    LO = "127.0.0.1"
    PORT = 5050

    bwt.bind((LO, PORT))

    bwt.listen(5)

    with bwt.accept()[0] as connessione: 
        while True :
            dati = connessione.recv(1024)



            #Step 1 - problem: Come trasformare una frase in una lista di caratteri 



            frase = dati.decode()

            if frase == "password":
                break
            
            caratteri = list(frase)    

            '''
            list(str) builds a new list using items obtained by iterating over the input iterable. 
            A string is an iterable -- iterating over it yields a single character at each iteration step.
            '''
            caratteri.append("$"); #intuibile


            #step 2 - permutare la frase spostando ultimo carattere in prima posizione

            mat = [caratteri.copy()]

            for n in range(0, len(frase)):

                    tmp = caratteri.pop(-1)
                    caratteri.insert(0,tmp) #n=0 : $BANANA
                    #print(caratteri)

                    mat.append(caratteri.copy())  #siccome python usa pointer a valori e non istanze


            #print()       
            #print()  
            #for n in mat:
            #    print(n)




            #step 3 - Sorting the matrix in "ordine lessicografico" (non mi ricordo la parola in english)

            for i in range(len(mat)):
                for j in range(len(mat) - 1 - i):     #bubble sort

                    if mat[j] > mat[j + 1]:

                        mat[j], mat[j + 1] = mat[j + 1], mat[j]


            #print()       
            #print()

            # aprofitto della stampa della matrice per prendere l'ultimo elemento di ogni lista (riga) e inserirlo in un altra lista
            bwtStep3 = []

            for n in mat:
                #print(n)
                bwtStep3.append(n[-1])

            #print()       
            #print()
            #print(bwtStep3) #Risultato finale restituito come lista


            connessione.sendall(str(bwtStep3).encode())



