print("FLICK IL LADRO")
contatore=0
borsa=[]
bag=[]
input("Premi INVIO per iniziare")
print("Ciao!Aiuta Flick a rubare il bottino della banca.")
print()
print("Puoi portare con te tre cose tra")
print("1.Veleno")
print("2.Fumogeno")
print("3.Grimardello")
print("4.Mini drone")
print("5.Pistola")
print("6.Dinamite")
print("7.Coltello")
print("8.Rampino")
print("9.Granata")
print("10.Piantina della banca")
print("11.PC")
print("12.Corda")
cosa1=input("Qual'è la prima cosa che vuoi portare con te?(inserire il numero)")
borsa.append(int(cosa1))
cosa2=input("Qual'è la seconda cosa che vuoi portare con te?(inserire il numero)")
borsa.append(int(cosa2))
cosa3=input("Qual'è la terza cosa che vuoi portare con te?(inserire il numero)")
borsa.append(int(cosa3))
bag=borsa[:]
print("Hai deciso di portare con te le seguenti cose")
if 1 in borsa:
        borsa.remove(1)
        borsa.append("Veleno")
if 2 in borsa:
        borsa.remove(2)
        borsa.append("Fumogeno")
if 3 in borsa:
        borsa.remove(3)
        borsa.append("Grimardello")
if 4 in borsa:
        borsa.remove(4)
        borsa.append("Mini Drone")
if 5 in borsa:
        borsa.remove(5)
        borsa.append("Pistola")
if 6 in borsa:
        borsa.remove(6)
        borsa.append("Dinamite")
if 7 in borsa:
        borsa.remove(7)
        borsa.append("Coltello")
if 8 in borsa:
        borsa.remove(8)
        borsa.append("Rampino")
if 9 in borsa:
        borsa.remove(9)
        borsa.append("Granata")
if 10 in borsa:
        borsa.remove(10)
        borsa.append("Piantina della banca")
if 11 in borsa:
        borsa.remove(11)
        borsa.append("PC")
if 12 in borsa:
        borsa.remove(12)
        borsa.append("Corda")
for x in borsa:
    print(x)
while contatore<=1:
    print("Vuoi passare dirattamente alla seconda parte?")
    print("1.Sì")
    print("2.No")
    rispostaj=int(input())
    if rispostaj==1:
        break
    if rispostaj==2:
        print()
    print("Come vuoi entrare nella banca?")
    print("1.Piazza una dinamite(serve la dinamite)")
    print("2.Tenta di entrare attraverso la folla")
    risposta1=input()
    while int(risposta1)>=3:
        print("Perfavore, seleziona una risposta tra le seguenti:")
        print("Come vuoi entrare nella banca?")
        print("1.Piazza una dinamite")
        print("2.Tenta di entrare attraverso la folla")
        risposta1=input()
    if int(risposta1)==1 and 6 in bag:
        print("Sei riuscito a far esplodere il muro e ad entrare")
        print()
        print("Ti hanno sentito alcune guardie")
        print("Cosa vuoi fare?")
        print("1.Scappa tornando indietro prima che le guardie ti prendano")
        print("2.Tenta di uccidere le guardie(serve la pistola)")
        print("3.Avanza con le guardie alle spalle")
        risposta11=input()
        while int(risposta11)>=4:
            print("Perfavore, seleziona una risposta tra le seguenti:")
            print("Ti hanno sentito alcune guardie")
            print("Cosa vuoi fare?")
            print("1.Scappa tornando indietro prima che le gurdie ti prendano")
            print("2.Tenta di uccidere le guardie(serve la pistola)")
            print("3.Avanza con le guardie alle spalle")
            risposta11=input()
        if int(risposta11)==1:
            print("Sei riuscito a scappare tornando indietro")
            print()
            print("Solo che adesso sei al punto di partenza")
            print("HAI PERSO")
            print("Ritenta")
        if int(risposta11)==2 and 5 in bag:
            print("Con fatica sei riucito a uccidere le guardie riparandoti dietro l'angolo")
            print("Peccato che stanno arrivando i rinforzi")
            print()
            print("Cosa vuoi fare?")
            print("1. Corri direttamente verso il caveaux")
            print("2. Travestiti da guardia")
            print("3. Tenta di trovare la tessera per aprire il caveaux")
            print("4. Usa un fumogeno(serve il fumogeno)")
            risposta112=input()
            while int(risposta112)>=5:
                print("Perfavore, seleziona una risposta tra le seguenti:")
                print("Cosa vuoi fare?")
                print("1. Corri direttamente verso il caveaux")
                print("2. Travestiti da guardia")
                print("3. Tenta di trovare la tessera per aprire il caveaux")
                print("4. Usa un fumogeno(serve il fumogeno)")
                risposta112=input()
            if int(risposta112)==1:
                print("Sei davanti al caveaux")
                print()
                print("In che modo vuoi aprirlo?")
                print("1.Tenta password a caso")
                print("2.Hai ancora a disposizione dinamite(serve dinamite)")
                print("3.Hackera la porta(serve il PC)")
                print("4.Cerchi la tessera")
                risposta1121=input()
                while int(risposta1121)>=5:
                    print("Perfavore, seleziona una risposta tra le seguenti:")
                    print("In che modo vuoi aprirlo?")
                    print("1.Tenta password a caso")
                    print("2.Hai ancora a disposizione dinamite(serve dinamite)")
                    print("3.Hackera la porta(serve il PC)")
                    print("4.Cerchi la tessera")
                    risposta1221=input()
                if int(risposta1121)==1:
                    print("La password non è 1234")
                    print("HAI PERSO")
                    print("Ritenta")
                if int(risposta1121)==2 and 6 in bag:
                    print("Anche stavolta ci sei riuscito")
                    print("Entri nel caveaux")
                    break
                if int(risposta1121)==3 and 11 in bag:
                    print("Riesci facilmente ad hackerare la porta")
                    print("Entri nel caveaux")
                    break
                if int(risposta1121)==4:
                    print("Mentre cerchi la tessera apri un armadietto e trovi il direttore che si stava nascondendo")
                    print()
                    print("1.Lo minacci per avere la tessera")
                    print("2.Gli chiedi gentilmente la tessera")
                    risposta11214=input()
                    while int(risposta11214)>=3:
                        print("Perfavore, seleziona una risposta tra le seguenti:")
                        print("1.Lo minacci per avere la tessera")
                        print("2.Gli chiedi gentilmente la tessera")
                        risposta11214=input()
                    if int(risposta11214)==1:
                        print("Il direttore ti consegna immediatamente la tessera")
                        print("Inseguito stordisci il direttore con un calcio")
                        print("E apri senza problemi la porta del caveaux")
                        break
                    if int(risposta11214)==2:
                        print("Mentre parli con gentilezza con il direttore le guardie ti sentono")
                        print("HAI PERSO")
                        print("Ritenta")
            if int(risposta112)==2:
                print("Quando arrivano le altre guardie le informi che il ladro sta scappando ferito")
                print("Senza fretta ti dirigi verso il caveaux")
                print("Arrivando davanti al caveaux scopri che la guardia aveva la tessera per aprire il caveaux proprio nella tasca")
                print("Apri il caveaux")
                break
            if int(risposta112)==3:
                print("Ci hai messo troppo tempo a cercarla")
                print("Le guadie ti puntano il fucile addosso")
                print("HAI PERSO")
                print("Ritenta")
            if int(risposta112)==4 and 2 in bag:
                print("Riesci a scappare usando il fumogeno")
                print()
                print("Per la tua strada trovi una guardia di spalle")
                print("1.Cerchi di aggirarla")
                print("2.La uccidi(serve o la pistola o il coltello")
                print("3.Esegui un calcio volante")
                risposta1124=input()
                while int(risposta1124)>=4:
                    print("Perfavore, seleziona una risposta tra le seguenti:")
                    print("Per la tua strada trovi una guardia di spalle")
                    print("1.Cerchi di aggirarla")
                    print("2.La uccidi(serve o la pistola o il coltello")
                    print("3.Esegui un calcio volante")
                    risposta1124=input()
                if int(risposta1124)==1:
                    print("Sarebbe stato troppo facile")
                    print("HAI PERSO")
                    print("Ritenta")
                if int(risposta1124)==2 and 5 in bag or 7 in bag:
                    print("Uccidi la guardia con freddezza")
                    print()
                    print("Prendi la sua tessera ed entri nel caveaux")
                    break
                if int(risposta1124)==3:
                    print("La guardia cade a terra sorpresa")
                    print()
                    print("Prendi la tessera e apri la porta del caveaux")
        if int(risposta11)==3:
            print("Corri mentre le guardie ti sparano")
            print()
            print("In qualche modo riesci ad evitare i proiettili e ti nascondi nel bagno")
            print("Senti dei passi che si avvicinano al bagno")
            print("1.Prendi il tuo coltello pronto per fare un agguato(serve il coltello)")
            print("2.Aspetti nascondendoti nei gabinetti")
            print("3.Esci dal bagno")
            risposta113=input()
            while int(risposta113)>=4:
                print("Perfavore, seleziona una risposta tra le seguenti:")
                print("Senti dei passi che si avvicinano al bagno")
                print("1.Prendi il tuo coltello pronto per fare un agguato(serve il coltello)")
                print("2.Aspetti nascondendoti nei gabinetti")
                print("3.Esci dal bagno")
            if int(risposta113)==1:
                print("Appena entra la guardia le tagli il collo")
                print()
                print("Uscendo dalla porta vedi che le guardie sono andate a cercare altrove")
                print("Ti dirigi verso il caveaux")
                print("Ad aspettarti davanti alla porta c'è il capo delle guardie con uno scudo antiproiettile")
                print("1.Spari ai suoi piedi(serve la pistola)")
                print("2.Aspetti che si avvicini per usare il coltello")
                print("3.Alzi le mani in alto")
                risposta1131=input()
                while int(risposta1131)>=4:
                    print("Perfavore, seleziona una risposta tra le seguenti:")
                    print("Ad aspettarti davanti alla porta c'è il capo delle guardie con uno scudo antiproiettile")
                    print("1.Spari ai suoi piedi(serve la pistola")
                    print("2.Aspetti che si avvicini per usare il coltello")
                    print("3.Alzi le mani in alto")
                if int(risposta1131)==1 and 5 in bag:
                    print("La guardia cade a terra dolorante")
                    print()
                    print("Entri nel caveaux con la tessera del capo delle guardie")
                    break
                if int(risposta1131)==2:
                    print("Appena la guardia si avvicina estai il coltello")
                    print("Ma la guardia e pronta a respingere l'attacco")
                    print("1.Colpisci dalla parte destra")
                    print("2.Colpisci dalla parte sinistra")
                    risposta11312=input()
                    while int(risposta11312)>=3:
                        print("Perfavore, seleziona una risposta tra le seguenti:")
                        print("Ma la guardia e pronta a respingere l'attacco")
                        print("1.Colpisci dalla parte destra")
                        print("2.Colpisci dalla parte sinistra")
                    if int(risposta11312)==1:
                        print("Hai indovinato, la guardia cade a terra sanguinante")
                        print()
                        print("Prendi la tessera e apri il caveaux")
                        break
                    if int(risposta11312)==2:
                        print("Che sfortuna, la guardia para con lo scudo il tuo colpo e ti stordisce")
                        print("HAI PERSO")
                        print("Ritenta")
                if int(risposta1131)==3:
                    print("La guardia si avvicina")
                    print()
                    print("Appena si trova nel tuo raggio d'azione le dai una testata")
                    print("Ma la guardia non si arrende e parte alla carica")
                    print("1.Para il colpo")
                    print("2.Sgambetto")
                    risposta11313=input()
                    while int(risposta11313)>=3:
                        print("Perfavore, seleziona una risposta tra le seguenti:")
                        print("Ma la guardia non si arrende e parte alla carica")
                        print("1.Para il colpo")
                        print("2.Sgambetto")
                    if int(risposta11313)==1:
                        print("La guardia ti sfonda")
                        print("HAI PERSO")
                    if int(risposta11313)==2:
                        print("La guardia perde l'equilibrio")
                        print("1.Colpo finale")
                        print("2.Aspetta")
                        risposta113132=input()
                        while int(risposta113132)>=3:
                            print("Perfavore, seleziona una risposta tra le seguenti:")
                            print("La guardia perde l'equilibrio")
                            print("1.Colpo finale")
                            print("2.Aspetta")
                        if int(risposta113132)==1:
                            print("Finisci la guardia rubandole la tessera")
                            print("Entri nel caveaux")
                            break
                        if int(risposta113132)==2:
                            print("Mai esitare")
                            print("La guardia tira fuori la pistola e ti centre in testa")
                            print("HAI PERSO")
                            print("Ritenta")
            if int(risposta113)==2:
                print("Nel bagno entra un normalissimo cliente della banca")
                print()
                print("1.Lo uccidi(serve la pistola o il coltello")
                print("2.Lo corrompi")
                risposta1132=input()
                while int(risposta1132)>=3:
                    print("Perfavore, seleziona una risposta tra le seguenti:")
                    print("1.Lo uccidi(serve la pistola o il coltello")
                    print("2.Lo corrompi")
                if int(risposta1132)==1 and 5 in bag or 7 in bag:
                    print("Il cliente urla vedendo il coltello")
                    print("Le guardie ci mettono poco a trovarti")
                    print("HAI PERSO")
                    print("Ritenta")
                if int(risposta1132)==2:
                    print("Il cliente si accontenta di poco e ti lascia passare")
                    print()
                    print("Il cliente ti indica la stanza dove si trovano la tessera")
                    print("Esci dal bagno e senza farti notare nella stanza della tessera")
                    print("Ti avvii verso il caveaux ma vedi i raggi laser che si accendono davanti a te")
                    print("1.Hackerali(serve il pc)")
                    print("2.Tenta di superarli")
                    print("3.Aspetta")
                    risposta13222=input()
                    while int(risposta13222)>=4:
                        print("Perfavore, seleziona una risposta tra le seguenti:")
                        print("1.Hackerali(serve il pc)")
                        print("2.Tenta di superarli")
                        print("3.Aspetta")
                        risposta13222=input()
                    if int(risposta13222)==1 and 11 in bag:
                        print("Riesci a superare il laser ed entrare nel caveaux")
                        break
                    if int(risposta13222)==2:
                        print("Non si sa come ma riesci a suoerare i laser")
                        print("Entri nel caveaux")
                        break
                    if int(risposta13222)==3:
                        print("Mai esitare")
                        print()
                        print("Le guardie arrivano alle tue spalle")
                        print("HAI PERSO")
                        print("Ritenta")
            if int(risposta113)==3:
                print("Non è stata una buona idea")
                print("HAI PERSO")
                print("Ritenta")
    if int(risposta1)==2:
        print("Fingendoti un cliente sei riuscito ad entrare senza destare sospetto")
        print()
        print("Per continuare devi passare per una posta strettamente sorvegliata")
        print("Cosa vuoi fare?")
        print("1. Fingiti uno del personale")
        print("2. Cerca di distrarre le guardie attivando l'allarme antincendio(serve il grimandello)")
        print("3. Sfonda la porta e corri")
        risposta21=input()
        while int(risposta21)>=4:
            print("Perfavore, seleziona una delle risposte seguenti")
            print("Cosa vuoi fare?")
            print("1. Fingiti uno del personale")
            print("2. Cerca di distrarre le guardie")
            print("3. Sfonda la porta e corri")
            risposta21=input()
        if int(risposta21)==1:
            print("Ti fingi uno del personale ma nessuno ti crede")
            print("HAI PERSO")
            print("Ritenta")
        if int(risposta21)==2 and 3 in bag:
            print("Hai attivato l'allarme antincedio e le guardie nella confusione non ti hanno visto passare")  
            print() 
            print("Per entrare nel cavoux hai bisogno della tessera")
            print("Vedi una guardia di spalle che probabilmente ha la tessera nella tasca")
            print("Come agisci?")
            print()
            print("1.Cerchi di prendere la tessera in modo scaltro senza farti notare")
            print("2.Provi a neutralizzare la guardia(serve il drone)")
            print("3.Cerchi un altra opzione")
            risposta212=input()
            while int(risposta212)>=3:
                print("Perfavore, scegli una tra le seguenti risposte")
                print("Come agisci?")
                print("1.Cerchi di prendere la tessera in modo scaltro senza farti notare")
                print("2.Provi a neutralizzare la guardia(serve il drone)")
                print("3.Cerchi un altra opzione")
                risposta212=input()
            if int(risposta212)==1:
                print("La guardia ti ha notato")
                print("HAI PERSO")
                print("Ritenta")
            if int(risposta212)==2 and 4 in bag:
                print("Sei riuscito a neutralizzare la guardia")
                print("Peccato che un altra guardia ti ha visto e si sta avvicinando con la pistola in mano")
                print()
                print("Cosa fai?")
                print("1.Prendi la pistola e la affronti(serve la pistola)")
                print("2.Scappi con la tessera")
                risposta2122=input()
                while int(risposta2122)>=3:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print("Cosa fai?")
                    print("1.Prendi la pistola e la affronti(serve la pistola)")
                    print("2.Scappi con la tessera")
                    risposta2122=input()
                if int(risposta2122)==1 and 5 in bag:
                    print("Hai preso la decisione più rischiosa")
                    print("1.Spari prima tu")
                    print("2.Ti ripari e aspetti che la guardia si avvicini")
                    risposta21221=input()
                    while int(risposta21221)>=3:
                        print("Perfavore, scegli una tra le seguenti risposte")
                        print("1.Spari prima tu")
                        print("2.Ti ripari e aspetti che la guardia si avvicini")
                        risposta21212=input()
                    if int(risposta21221)==1:
                        print("Bel colpo, la guardia si accascia a terra")
                        print("Senza nessuno che ti disturbi prendi la tessera e apri il caveaux")
                        break
                    if int(risposta21221)==2:
                        print("Aspetti che la guardia si avvicini ma appena ti fai vedere la guardia ti fulmina per primo")
                        print("HAI PERSO")
                        print("Ritenta")
                if int(risposta2122)==2:
                    print("Prendi la tessera e scappi ma la guardia inizia a sparare")
                    print()
                    print("1.Tenti di muoverti a zig zag")
                    print("2.Ti abbassi")
                    risposta21222=input()
                    while int(risposta21222)>=3:
                        print("Perfavore, scegli una tra le seguenti risposte")
                        print("1.Tenti di muoverti a zig zag")
                        print("2.Ti abbassi")
                        risposta21112=input()
                    if int(risposta21222)==1:
                        print("Per un certo periodo la tua tecnica funziona ma alla fine la guardia riesce a beccarti")
                        print("HAI PERSO")
                        print("Ritenta")
                    if int(risposta21222)==2:
                        print("La guardia non riesce a beccarti accedi al caveaux con la tessera")
                        break
            if int(risposta212)==3:
                print("Guardandoti intorno hai trovato due opzioni")
                print()
                print("1.Tornare indietro")
                print("2.Andare nell'ufficio del direttore(serve la piantina")
                risposta2123=input()
                while int(risposta2123)>=3:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print("1.Tornare indietro")
                    print("2.Andare nell'ufficio del direttore(serve la piantina")
                    risposta2123=input()
                if int(risposta2123)==1:
                    print("Tornando indietro vieni intravisto da una guardia che ti ordina di fermarti")
                    print()
                    print("1.Fermati")
                    print("2.Scappa")
                    risposta21231=input()
                    while int(risposta21231)>=3:
                        print("Perfavore, scegli una tra le seguenti risposte")
                        print("1.Fermati")
                        print("2.Scappa")
                        risposta21231=input()
                    if int(risposta21231)==1:
                        print("La guardia si avvicina con la pistola che ti punta")
                        print()
                        print("1.Ruba la pistola")
                        print("2.Tenta di abbatterlo")
                        risposta212311=input()
                        while int(risposta212311)>=3:
                            print("Perfavore, scegli una tra le seguenti risposte")
                            print("1.Ruba la pistola")
                            print("2.Tenta di abbatterlo")
                            risposta212311=input()
                        if int(risposta212311)==1:
                            print("Con una mossa scaltra riesci a rubare la pistola e finire la guardia")
                            print()
                            print("Prendi la tessera della guardia e apri il caveaux")
                            break
                        if int(risposta212311)==2:
                            print("La guardia ti anticipa e ti stende")
                            print()
                            print("HAI PERSO")
                            print("Ritenta")
                    if int(risposta21231)==2:
                        print("Scappando ti rifugi in una stanza")
                        print()
                        print("1.Prepari una trappola(serve la corda)")
                        print("2.Preparati ad affrontarla")
                        risposta212312=input()
                        while int(risposta212312)>=3:
                            print("Perfavore, scegli una tra le seguenti risposte")
                            print("1.Prepari una trappola(serve la corda)")
                            print("2.Preparati ad affrontarla")
                            risposta212312=input()
                        if int(risposta212312)==1 and 12 in bag:
                            print("La guardia entra e cade grazie alla tua trappola")
                            print("Prendi la sua tessera e vai ad aprire il caveaux")
                            break
                        if int(risposta212312)==2:
                            print("Come ti posizioni?")
                            print()
                            print("1.Nasconditi")
                            print("2.Aspetti davanti alla porta")
                            risposta2123122=input()
                            while int(risposta2123122)>=3:
                                print("Perfavore, scegli una tra le seguenti risposte")
                                print("1.Nasconditi")
                                print("2.Aspetti davanti alla porta")
                                risposta2123122==input()
                            if int(risposta2123122)==1:
                                print("La guardia entra e ti trova subito subito lasciandoti un buco in fronte")
                                print()
                                print("HAI PERSO")
                                print("Riprova")
                            if int(risposta2123122)==2:
                                print("Sorprendi la guardia sbattendogli la porta addosso facendola svenire")
                                print("Prendi la sua tessera e vai ad aprire il caveaux")
                                break
        if int(risposta21)==3:
            print("Le guardie distratte non ti hanno fermato ma adesso stanno per aprire il fuoco")
            print()
            print("Cosa fai?")
            print("1.Ti fermi e alzi le mani")
            print("2.Usi un fumogeno(serve il fumogeno)")
            risposta213=input()
            while int(risposta213)>=3:
                print("Perfavore, scegli una tra le seguenti risposte")
                print("Cosa fai?")
                print("1.Ti fermi e alzi le mani")
                print("2.Usi un fumogeno(serve il fumogeno)")
                risposta213=input()
            if int(risposta213)==1:
                print("Ti fermi e alzi le mani")
                print()
                print("Le guardie si avvicinano per arrestarti")
                print("Come agisci?")
                print("1.Ti fai arrestare")
                print("2.Aspetti che si avvicinino e cerchi di neutralizzarli")
                risposta2131=input()
                while int(risposta2131)>=3:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print("1.Ti fai arrestare")
                    print("2.Aspetti che si avvicinino e cerchi di neutralizzarli")
                    risposta2131=input()
                if int(risposta2131)==1:
                    print("Le guardie ti arrestano e ti consegnano alla polizia")
                    print("HAI PERSO")
                    print("Ritenta")
                if int(risposta2131)==2:
                    print("Appena si avvicinino tu li fai cascare neutralizzandoli")
                    print()
                    print("Prendi la tessera e apri il caveaux senza problemi")
                    break
            if int(risposta213)==2:
                print("Il tuo fumogeno si rivela essenziale e riesci a rifugiarti in un camera a parte")
                print()
                print("Senti i passi delle guardie che si avvicinano")
                print("Intravedi anche una sedia che ti permetterebbe di salire nei condotti")
                print("Come ti comporti?")
                print("1.Aspetti le guardie pronto a colpire")
                print("2.Ti intrufuli nei condotti")
                risposta2132=input()
                while int(risposta2132)>=3:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print("1.Aspetti le guardie pronto a colpire")
                    print("2.Ti intrufuli nei condotti")
                    risposta2132=input()
                if int(risposta2132)==1:
                    print("Riesci a far fuori la prima guardia")
                    print("Ma la seconda non si fa fregare e ti manda giù con un colpo")
                    print("HAI PERSO")
                    print("Ritenta")
                if int(risposta2132)==2:
                    print("Riesci a fuggire attraverso i condotti")
                    print()
                    print("Attraversando i condotti ti ritrovi esattamente sopra le guardie")
                    print("1.Ti butti sopra di loro")
                    print("2.Continui la tua strada verso il caveaux")
                    risposta21322=input()
                    while int(risposta21322)>=3:
                        print("Perfavore, scegli una tra le seguenti risposte") 
                        print("1.Ti butti sopra di loro")
                        print("2.Continui la tua strada verso il caveaux")
                        risposta21322=input()
                    if int(risposta21322)==1:
                        print("I tuoi anni di addestramento si rivelano essenziali")
                        print("Riesci a mettere KO tutti due")
                        print("Prendi la tessera ed entri senza problemi nel caveaux")
                        break
                    if int(risposta21322)==2:
                        print("Riesci ad arrivare fino al caveux ma ritrovandoti davanti alla porta ti ricordi che non hai nessun modo per entrare")
                        print("Vieni freddato dalla distanza")
                        print("HAI PERSO")
                        print("Ritenta")
while True:
    print("Dopo il difficile percorso ti ritrovi finalmente nel desiderato caveaux")
    print("In tutta fretta prendi due sacchi di denaro")
    print("All'improvviso senti un ferro che si appoggia alla tua testa")
    print("1.Alza le mani")
    print("2.Non abbassare le mani")
    rispostax=int(input())
    while rispostax>=3:
        print("Perfavore, scegli una tra le seguenti risposte")
        print("1.Alza le mani")
        print("2.Non alzare le mani le mani")
        rispostax=int(input())
    if rispostax==1:
        print("Mai arrenderti, vieni colpito e stordito")
        print("HAI PERSO")
        print("Ritenta")
    if rispostax==2:
        print("Non alzi le mani e ti giri facendo cadere l'arma dalle mani del tuo avversario")
        print()
        print("Ti ritrovi davanti un altro ladro per esattezza un'altra ladra")
        print("Ti chiede se vuoi fidarti di lei per scappare")
        print()
        print("1.Ti fidi")
        print("2.Non ti fidi")
        rispostay=int(input())
        if rispostay==1:
            print("Lei ti invita a seguirla, spiegando che la sua banda sta aspettando fuori con una macchina blindata")
            print()
            print("Insieme uscite dal caveaux")
            print("Mentre salite scendete le scale la guardie vi intercettano e aprono il fuoco")
            print("1.Barricatevi")
            print("2.Lancia una granata(serve la granata)")
            print("3.Cercate una via alternativa")
            rispostay1=int(input())
            while rispostay1>=4:
                print("Perfavore, scegli una tra le seguenti risposte")
                print("Mentre salite la guardie vi intercettano e aprono il fuoco")
                print("1.Barricatevi")
                print("2.Lancia una granata(serve la granata)")
                print("3.Scappate(serve il fuomogeno)")
                rispostay1=int(input())
            if rispostay1==1:
                print("Riuscite a mettere un po di mobili per fare una protezione")
                print("L'insieme di mobili non riusicrà a resistere tanto ai colpi")
                print()
                print("Cosa fate?")
                print("1.Usa un fumogeno(serve il fumogeno)")
                print("2.Lascia fare alla ragazza")
                print("3.Tornate indietro")
                rispostay11=int(input())
                while rispostay11>=4:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print()
                    print("Cosa fate?")
                    print("1.Usa un fumogeno(serve il fuogeno)")
                    print("2.Lascia fare alla ragazza")
                    print("3.Tornate indietro")
                if rispostay11==1 and 2 in bag:
                    print("Grazie al fumogeno riuscite a fare il giro dei soldati ed uscire dalla banca")
                    print("Davanti a voi c'è un furgone blindato ad aspettarvi")
                    print()
                    print("Indietreggi ma la ragazza ti spiega che si tratta della sua banda")
                    print("1.Sali sul furgone")
                    print("2.Non salire sul furgone")
                    rispostay111=int(input())
                    if rispostay111==1:
                        print("Sali sul furgone")
                        print()
                        print("Riuscite a fare un bel po' di kilometri e seminare la polizia")
                        print("Man mano che il tempo passa capisci che la banda non vorrà lasciarti andare cosi facilmente")
                        print("Cosa pensi di fare?")
                        print("1.Prova ad buttarti fuori dalla finestra")
                        print("2.Cerca di parlare")
                        rispostay1111=int(input())
                        if rispostay1111==1:
                            print("Rieci ad uscire ma rimani investito")
                            print("HAI PERSO")
                        if rispostay1111==2:
                            print("Inizii a conversare")
                            print()
                            print("1.Avvelena la bibita del guidatore mentre gli altri sono distratti(serve il veleno)")
                            print("2.Racconta una bugia su altri soldi nascosti")
                            rispostay11112=int(input())
                            if rispostay11112==1 and 1 in bag:
                                print("Racconti che ci sono altri soldi presso la tua casa non molto lontana da qui")
                                print("Mentre gli altri stanno discutendo su quetsta ipotesi riesci ad avvelenare la bibita del guidatore")
                                print()
                                print("Mentre vi dirigete la posto l'autista ha un attacco cardiaco e fa sbandare il furgone che si ribalta")
                                print("Fortunatamente non rimani ferito e riesci a scappare con i soldi")
                                print("HAI VINTO")
                                break
                            if rispostay11112==2:
                                print("La banda ci pensa e decide di dirigersi nel posto da te descritto,la tua casa")
                                print("I soldi ovviamente non esistono")
                                print("Ormai hai capito che quelli ti lasciano vivo solo per quei soldi")
                                print()
                                print("Ormai vi state avvicinando")
                                print("1.Chiama la polizia")
                                print("2.Ruba una pistola")
                                risposta111122=int(input())
                                if risposta111122==1:
                                    print("Provi a chiamare la polizia ma vieni beccato")
                                    print("La banda non lo prende bene")
                                    print("HAI PERSO")
                                if risposta111122==2:
                                    print("Riesci abilmente a rubare una pistola")
                                    print()
                                    print("Appena arrivvate sul posto prendi in ostaggio la ragazza con la pistola che hai rubato")
                                    print("Inizii ad allontanarti lentamente")
                                    print("Tutti i suoi compagni tirano fuori le armi")
                                    print("1.Uccidi la ragazza")
                                    print("2.Risparmi la ragazza")
                                    rispostafinale=int(input())
                                    if rispostafinale==1:
                                        print("Uccidi la ragazza")
                                        print("I suoi compagni dalla disperazione si accosciano per terra")
                                        print("Ne approfitti per entrare nel furgone e svignartela")
                                        print("HAI VINTO")
                                        break
                                    if rispostafinale==2:
                                        print("Non hai abbastanza coraggio e risparmi la ragazza pero spari alle ruote bucandole")
                                        print("Venite riconosciuti e non potendo fuggire venite arrestati")
                                        print("HAI PERSO")                        
                    if rispostay111==2:
                        print("Rifiuti di salire")
                        print()
                        print("La ragazza fa uscire la sua banda che ti spoglia dei soldi che hai rubato")
                        print("Ti abbandonano davanti alla banca, la polizia non ci mette niente a raggiungerti")
                        print("HAI PERSO")
                if rispostay11==2:
                    print("Non trovando nessuna soluzione chiedi aiuto alla ragazza")
                    print("Lei inizia a chiamare qualcuno")
                    print()
                    print("In meno di 20 secondi dietro alle spalle delle guardie viene aperto un secondo fuoco")
                    print("Ti spiega che il fuoco di supporto è la sua banda")
                    print("Dopo che tutte le guardie sono state ammazzate uscite dalla banca")
                    print()
                    print("Ad aspettarvi c'è il furgone blindato della banda")
                    print("1.Entri nel furgone")
                    print("2.Non entrare nel furgone")
                    rispostay112=int(input())
                    if rispostay112==1:
                        print("Sali sul furgone") 
                        print()
                        print("Riuscite a fare un bel po' di kilometri e seminare la polizia")
                        print("Man mano che il tempo passa capisci che la banda non vorrà lasciarti andare cosi facilmente")
                        print("Cosa pensi di fare?")
                        print("1.Prova ad buttarti fuori dalla finestra")
                        print("2.Cerca di parlare")
                        rispostay1111=int(input())
                        if rispostay1111==1:
                            print("Rieci ad uscire ma rimani investito")
                            print("HAI PERSO")
                        if rispostay1111==2:
                            print("Inizii a conversare")
                            print()
                            print("1.Avvelena la bibita del guidatore mentre gli altri sono distratti(serve il veleno)")
                            print("2.Racconta una bugia su altri soldi nascosti")
                            rispostay11112=int(input())
                            if rispostay11112==1 and 1 in bag:
                                print("Racconti che ci sono altri soldi presso la tua casa non molto lontana da qui")
                                print("Mentre gli altri stanno discutendo su quetsta ipotesi riesci ad avvelenare la bibita del guidatore")
                                print()
                                print("Mentre vi dirigete la posto l'autista ha un attacco cardiaco e fa sbandare il furgone che si ribalta")
                                print("Fortunatamente non rimani ferito e riesci a scappare con i soldi")
                                print("HAI VINTO")
                                break
                            if rispostay11112==2:
                                print("La banda ci pensa e decide di dirigersi nel posto da te descritto,la tua casa")
                                print("I soldi ovviamente non esistono")
                                print("Ormai hai capito che quelli ti lasciano vivo solo per quei soldi")
                                print()
                                print("Ormai vi state avvicinando")
                                print("1.Chiama la polizia")
                                print("2.Ruba una pistola")
                                risposta111122=int(input())
                                if risposta111122==1:
                                    print("Provi a chiamare la polizia ma vieni beccato")
                                    print("La banda non lo prende bene")
                                    print("HAI PERSO")
                                if risposta111122==2:
                                    print("Riesci abilmente a rubare una pistola")
                                    print()
                                    print("Appena arrivvate sul posto prendi in ostaggio la ragazza con la pistola che hai rubato")
                                    print("Inizii ad allontanarti lentamente")
                                    print("Tutti i suoi compagni tirano fuori le armi")
                                    print("1.Uccidi la ragazza")
                                    print("2.Risparmi la ragazza")
                                    rispostafinale=int(input())
                                    if rispostafinale==1:
                                        print("Uccidi la ragazza")
                                        print("I suoi compagni dalla disperazione si accosciano per terra")
                                        print("Ne approfitti per entrare nel furgone e svignartela")
                                        print("HAI VINTO")
                                        break
                                    if rispostafinale==2:
                                        print("Non hai abbastanza coraggio e risparmi la ragazza pero spari alle ruote bucandole")
                                        print("Venite riconosciuti e non potendo fuggire venite arrestati")
                                        print("HAI PERSO") 
                    if rispostay112==2:
                        print("Rifiuti di salire")
                        print()
                        print("La ragazza ordina alla sua banda di prendere tutti soldi che hai rubato")
                        print("Ti abbandonano davanti alla banca, la polizia non ci mette niente a raggiungerti")
                        print("HAI PERSO")
                if rispostay11==3:
                    print("Tornando indietro vi accorgete di essere circondati dalle guardie")
                    print("HAI PERSO")
            if rispostay1==2 and 9 in bag:
                print("Riesci a uccidere un bel po' di guardie ma crolla il soffitto e rimani ucciso")
                print("HAI PERSO")
            if rispostay1==3:
                print("Riuscite a prendere una strada alternativa uscendo da una vecchia uscita sul retro")
                print()
                print("Li trovate due moto")
                print("La ragazza riesce facilmente ad accendere le moto")
                print("Partite per tentare la fuga")
                print("Subito vi accorgete che qualcosa non va")
                print("Piu avanti scoprite che la zona è stata isolata")
                print("Vi avvicinate al ponte e scoprite che il ponte è bloccato da una barricata di macchine della polizia")
                print()
                print("1.Fai un inversione")
                print("2.Tenta di oltrepassare la barricata in qualche modo")
                print("3.Lancia della dinamite per sfondare la barricata(serve le dinamite)")
                rispostay13=int(input())
                while rispostay13>=4:
                    print("Perfavore, seleziona una tra le risposte seguenti")
                    print("1.Fai un inversione")
                    print("2.Tenta di oltrepassare la barricata in qualche modo")
                    print("3.Lancia della dinamite per sfondare la barricata(serve la dinamite)")
                    rispostay13=int(input())
                if rispostay13==1:
                    print("Tenti di fare l'inversione ma i tiratori scelti della polizia ti bucano le ruote")
                    print("Muori cadendo violentamete dalla moto")
                    print("HAI PERSO")
                if rispostay13==2:
                    print("Accelleri al massimo e in qualche modo riuscite ad oltrepassare la barricata sia tu sia la ragazza")
                    print("Vi allontanate dalla barricata")
                    print()
                    print("Sentite un elicottero alle vostre spalle")
                    print("Come lo seminate?")
                    print("1.Accelerate")
                    print("2.Prendete una strada sterrata")
                    rispostay132=int(input())
                    if rispostay132==1:
                        print("Riuscite a seminare l'elicottero ma alla fine della strada vi aspetta la polizia e questa volta non vi lascia scappaare")
                        print("HAI PERSO")
                    if rispostay132==2:
                        print("Prendendo la strada sterrata riuscite a nacondervi tra gli alberi e seminare l'elicottero")
                        print()
                        print("Dopo circa 2 ore di tragitto la ragazza ti chiede di fermarsi un attimo")
                        print("Sai che non bisognerebbe fidarsi di una come lei")
                        print("1.Accetti e ti fermi")
                        print("2.Scappi")
                        rispostay1321=int(input())
                        if rispostay1321==1:
                            print("Accetti di fermarti")
                            print()
                            print("Guardando bene scopri che la ragazza è ferita gravemente all'addome")
                            print("Cosa fai?")
                            print("1.Scappi")
                            print("2.La aiuti")
                            rispostay13211=int(input())
                            if rispostay13211==1:
                                print("Mentre stai per anartene la ragazza tira fuori la sua pistola e spara un colpo")
                                print("Come reagisci a questa provocazione")
                            if rispostay13211==2:
                                print("Decidi di aiutarla anche perchè sai che lei ha già previsto la tua fuga")
                                print()
                                print("1.La curi con il veleno(serve il veleno)")
                                print("2.Cerchi di ucciderla")
                                print("3.La curi veramente")
                                rispostay132112=int(input())
                                if rispostay132112==1 and 1 in bag:
                                    print("Riesci a versare di nascosto un po di veleno sugli stracci per tamponare la ferita")
                                    print("Lei muore non potendo respirare a causa del veleno")
                                    print("Scappi lasciandola lì")
                                    print("HAI VINTO")
                                    break
                                if rispostay132112==2:
                                    print("Cerchi di ucciderla mettendole la meni al collo")
                                    print("Lei pronta a tutto tira fuori la pistola e fa partire un colpo che ti trapassa")
                                    print("Morite tutti e due dissanguati")
                                    print("HAI PERSO")
                                if rispostay132112:
                                    print("Pian piano riesci a tamponare la ferita e salvarla")
                                    print("Alla fine la ladra resta fedele e vi separate")
                                    print("HAI VINTO")
                                    break
                        if rispostay1321==2:
                            print("La ladra l'aveva previsto")
                            print("Fa esplodere la tua moto con un dispotivo a distanza")
                            print("HAI PERSO")
                if rispostay13==3 and 6 in bag:
                    print("Riuscite a passare attraverso l'esplosione")
                    print("Percorrete molti kilometri per seminare per bene la polizia")
                    print("La ragazza ti chiede di fermarsi un attimo")
                    print("Sai che non bisognerebbe fidarsi di una come lei")
                    print("1.Accetti e ti fermi")
                    print("2.Scappi")
                    rispostay1321=int(input())
                    if rispostay1321==1:
                            print("Accetti di fermarti")
                            print()
                            print("Guardando bene scopri che la ragazza è ferita gravemente all'addome")
                            print("Cosa fai?")
                            print("1.Scappi")
                            print("2.La aiuti")
                            rispostay13211=int(input())
                            if rispostay13211==1:
                                print("Mentre stai per anartene la ragazza tira fuori la sua pistola e spara un colpo")
                                print("Come reagisci a questa provocazione")
                            if rispostay13211==2:
                                print("Decidi di aiutarla anche perchè sai che lei ha già previsto la tua fuga")
                                print()
                                print("1.La curi con il veleno(serve il veleno)")
                                print("2.Cerchi di ucciderla")
                                print("3.La curi veramente")
                                rispostay132112=int(input())
                                if rispostay132112==1 and 1 in bag:
                                    print("Riesci a versare di nascosto un po di veleno sugli stracci per tamponare la ferita")
                                    print("Lei muore non potendo respirare a causa del veleno")
                                    print("Scappi lasciandola lì")
                                    print("HAI VINTO")
                                    break
                                if rispostay132112==2:
                                    print("Cerchi di ucciderla mettendole la meni al collo")
                                    print("Lei pronta a tutto tira fuori la pistola e fa partire un colpo che ti trapassa")
                                    print("Morite tutti e due dissanguati")
                                    print("HAI PERSO")
                                if rispostay132112:
                                    print("Pian piano riesci a tamponare la ferita e salvarla")
                                    print("Alla fine la ladra resta fedele e vi separate")
                                    print("HAI VINTO")
                                    break
                    if rispostay1321==2:
                            print("La ladra l'aveva previsto")
                            print("Fa esplodere la tua moto con un dispotivo a distanza")
                            print("HAI PERSO")
        if rispostay==2:
            print("Non ti fidi")
            print()
            print("Le guardie si avvicinano, ti giri per vedere cosa fa la ladra ma lei è scomparsa")
            print("Esci dal caveaux scappi su per le scale")
            print("Un tuo amico ti sta aspettando con l'elicottero sul tetto")
            print("Cosa fai?")
            print()
            print("1.Continui a scappare")
            print("2.Usa il fumogeno(serve il fumogeno)")
            print("3.Rischia provando a distrarre le guardie")
            rispostay21=int(input())
            while rispostay21>=4:
                print("Perfavore, scegli una tra le seguenti risposte")
                print()
                print("1.Continui a scappare")
                print("2.Usa il fumogeno(serve il fumogeno)")
                print("3.Rischia provando a distrarre le guardie")
                rispostay21=int(input())
            if rispostay21==1:
                print("Riesci a raggiungere il tetto con le guardie alle spalle")
                print("Vedi l'elicottero del tuo amico che ti sta aspettando")
                print()
                print("Cosa vuoi fare?")
                print("1.Continui la tua corsa fino all'elicottero")
                print("2.Lancia la granata verso le guardie o spara colpi di avvertimento(serve la granata o la pistola")
                print("3.Blocca la porta")
                rispostay211=int(input())
                while rispostay211>=4:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print()
                    print("cosa vuoi fare?")
                    print("1.La segui senza che se ne accorga")
                    print("2.Fai la tua strada")
                    rispostay00=int(input())
                if rispostay211==1:
                    print("Le guardie arrivano e ti colpiscono la gamba")
                    print("HAI PERSO")
                if rispostay211==2 and 5 in bag or 9 in bag:
                    print("Con questa mossa riesci a guadagnare tempo")
                    print()
                    print("Accendi l'elicottero e partite")
                    print("Ma qualcosa vi blocca")
                    print("Notate che le guardie sono riuscite ad agganciare una catena dei ferro all'elicottero")
                    print("Cosa fate?")
                    print()
                    print("1.Ti arrendi e fate atterrare l'elicottero")
                    print("2.Usa il mitragliatore dell'elicottero")
                    print("3.Cerca di rompere la catena aumentando la potenza dell'elicottero")
                    rispostay2112=int(input())
                    while rispostay2112>=4:
                        print("Perfavore scegli una tra le seguenti risposte")
                        print("Cosa fate?")
                        print()
                        print("1.Ti arrendi e fate atterrare l'elicottero")
                        print("2.Usa il mitragliatore dell'elicottero")
                        print("3.Cerca di rompere la catena aumentando la potenza dell'elicottero")
                        rispostay2112=int(input())
                    if rispostay2112==1:
                        print("Iniziate a abbassarvi in segno di resa")
                        print()
                        print("Proprio mentre tutte le speranze erano perdute le guardie iniziano a morire una dopo l'altra")
                        print("L'autore del massacro si rivela essere la ladra, la quale slega la catena e sale sull'elicottero")
                        print()
                        print("Cosa fai?")
                        print("1.Non farla salire")
                        print("2.Falla salire")
                        rispostay21121=int(input())
                        if rispostay21121==1:
                            print("La respingi con un calcio")
                            print()
                            print("Una mossa infame ma almeno riesci a fuggire")
                            print("HAI VINTO ma cosa non faresti per i soldi")
                            break
                        if rispostay21121==2:
                            print("Porgi la mano per farla salire")
                            input()
                            print("La ladra sale ma con una mossa acrobatica ti fa cadere e neutralizza il tuo amico prendendo il possesso dell'elicottero")
                            print("Rimani a guardare l'elicottero che si allontana mentre vieni arrestato")
                            print("HAI PERSO")
                    if rispostay2112==2:
                        print("Scegli di usare il mitragliatore ma le guardie capiscano il tuo intento e si riparano dietro il muro")
                        print()
                        print("Vi ritrovate bloccati in mezzo all'aria senza sapere cosa fare")
                        print("Il tiratore scelto delle guardie colpisce il tuo nemico ed iniziate a precipitare schiantandovi")
                        print("HAI PERSO")
                    if rispostay2112==3:
                        print("L'elicottero non riesce a spezzare la catena e surriscaldandosi prende fuoco")
                        print("Precipitate mentre la banconote infuocate volano dappertutto")
                        print("HAI PERSO")
                if rispostay211==3:
                    print("Bloccando la porta riesci a guadagnare tempo e salire sull'elicottero")
                    print("Il tuo amico parte e in meno di un minuto vi ritrovate a volare sopra a città con i soldi")
                    print("Atterrate nel vostro covo")
                    print("Mentre sposti i sacchi dall'elicottero nel furgone il tuo compagno ti atterra con un calcio")
                    print("Mentre sei a terra dolorante il tuo amico tira fuori la pistola dice che il patto è saltato e che tutto il denaro d'ora in poi appartiene a lui")
                    print()
                    print("Cosa fai?")
                    print("1.Lo lasci andare")
                    print("2.Hai da ridire")
                    print("3.Fermalo(serve il drone)")
                    print("4.Tira fuori la pistola(serve la pistola)")
                    rispostay2113=int(input())
                    if rispostay2113==1:
                        print("Lo lasci andare mentre ti lecchi le ferite")
                        print()
                        print("1.Informi la polizia")
                        print("2.Lascia stare")
                        rispostay21131=int(input())
                        if rispostay21131==1:
                            print("La polizia ferma il tuo amico")
                            print("In seguito vieni arrestato anche te")
                            print()
                            print("Scopri che tu e il tuo amico traditore vi ritrovate nella stessa prigione")
                            print("Uccidi il tuo ex amico per vendetta")
                            print("HAI PERSO")
                        if rispostay21131==2:
                            print("Il tuo ex amico fugge e diventa milionario")
                            print("Te riesci a soppravivere come fuggisco senza farti trovare dalla polizia")
                            print("HAI VINTO ma senza ottenere nulla")
                            break
                    if rispostay2113==2:
                        print("Ti rialzi perchè sai che il tuo amico non avrebbe il coraggio di sparare e con un discorso calmo gli fai cambiare idea")
                        print()
                        print("Lo uccidi tu?")
                        print("1.Sì")
                        print("2.No")
                        rispostay21132=int(input())
                        if rispostay21132==1:
                            print("Tu invece non hai pietà per che prova a tradirti e lo uccidi con la sua stessa pistola")
                            print("HAI VINTO però la tua crudeltà non ha limiti")
                            break
                        if rispostay21132==2:
                            print("Insieme vi dividete il denaro")
                            print("HAI VINTO")
                            break
                    if rispostay2113==3 and 4 in bag:
                        print("Mentri sei a terra riesci a comandare il tuo drone e dare una scossa al traditore facendogli perdere i sensi")
                        print("Scappi con i soldi, giorni dopo scoprirai che il tuo ex amico è stato arrestato")
                        print("HAI VINTO")
                        break
                    if rispostay21132==4 and 5 in bag:
                        print("Tiri fuori la pistola e il tuo ex amico spaventato inizia a sparare all'impazzata ferendoti gravemente")
                        print("Muori lentamente dissanguandoti mentre il tuo amico scappa")
                        print("HAI PERSO")
            if rispostay21==2 and 2 in bag:
                print("Riesci a seminare le guardie facilmente")
                print()
                print("Hai la strada spianata per salire sul tetto")
                print("Cosa fai?")
                print("1.Vendicati delle guardie")
                print("2.Vai sul tetto")
                rispostay212=int(input())
                while rispostay212>=3:
                    print("Perfavore, scegli una tra le seguenti risposte")
                    print()
                    print("Cosa fai?")
                    print("1.Vendicati delle guardie")
                    print("2.Vai sul tetto")
                    risposta212=int(input())
                if rispostay212==1:
                    print("Perchè fare questo quando puoi semplicemente scappare")
                    print("Le guardie ti fanno fuori")
                    print("HAI PERSO")
                if rispostay212==2:
                    print("Ti ritrovi sul tetto")
                    print("L'elicottero è lì che ti aspetta con il tuo amico dentro")
                    print("Il tuo amico parte e in meno di un minuto vi ritrovate a volare sopra a città con i soldi")
                    print("Atterrate nel vostro covo")
                    print("Mentre sposti i sacchi dall'elicottero nel furgone il tuo compagno ti atterra con un calcio")
                    print("Mentre sei a terra dolorante il tuo amico tira fuori la pistola dice che il patto è saltato e che tutto il denaro d'ora in poi appartiene a lui")
                    print()
                    print("Cosa fai?")
                    print("1.Lo lasci andare")
                    print("2.Hai da ridire")
                    print("3.Fermalo(serve il drone)")
                    print("4.Tira fuori la pistola(serve la pistola)")
                    rispostay2113=int(input())
                    if rispostay2113==1:
                        print("Lo lasci andare mentre ti lecchi le ferite")
                        print()
                        print("1.Informi la polizia")
                        print("2.Lascia stare")
                        rispostay21131=int(input())
                        if rispostay21131==1:
                            print("La polizia ferma il tuo amico")
                            print("In seguito vieni arrestato anche te")
                            print()
                            print("Scopri che tu e il tuo amico traditore vi ritrovate nella stessa prigione")
                            print("Uccidi il tuo ex amico per vendetta")
                            print("HAI PERSO")
                        if rispostay21131==2:
                            print("Il tuo ex amico fugge e diventa milionario")
                            print("Te riesci a soppravivere come fuggisco senza farti trovare dalla polizia")
                            print("HAI VINTO ma senza ottenere nulla")
                            break
                    if rispostay2113==2:
                        print("Ti rialzi perchè sai che il tuo amico non avrebbe il coraggio di sparare e con un discorso calmo gli fai cambiare idea")
                        print()
                        print("Lo uccidi tu?")
                        print("1.Sì")
                        print("2.No")
                        rispostay21132=int(input())
                        if rispostay21132==1:
                            print("Tu invece non hai pietà per che prova a tradirti e lo uccidi con la sua stessa pistola")
                            print("HAI VINTO però la tua crudeltà non ha limiti")
                            break
                        if rispostay21132==2:
                            print("Insieme vi dividete il denaro")
                            print("HAI VINTO")
                            break
                    if rispostay2113==3 and 4 in bag:
                        print("Mentri sei a terra riesci a comandare il tuo drone e dare una scossa al traditore facendogli perdere i sensi")
                        print("Scappi con i soldi, giorni dopo scoprirai che il tuo ex amico è stato arrestato")
                        print("HAI VINTO")
                        break
                    if rispostay21132==4 and 5 in bag:
                        print("Tiri fuori la pistola e il tuo ex amico spaventato inizia a sparare all'impazzata ferendoti gravemente")
                        print("Muori lentamente dissanguandoti mentre il tuo amico scappa")
                        print("HAI PERSO")
            if rispostay21==3:
                print("Bel tentativo ma le guardie non sono stupide")
                print("HAI PERSO")