'''
Organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo.
Fornito poi il numero di conto, il programma visualizza il saldo oppue un messaggio nel caso in cui il conto non sia presente nella mappa.

'''

Conti_saldi = {
'053432537901':'120000',
'920387184027':'43000',
'820372930281':'3000000',
'040284030020':'450000',
'837129302794':'90847',
'803711274029':'312913840',
'934930273044':'52734957209',
'718204438290':'46383265830',
'126391638452':'66848303',
'381036528402':'58930583',
'047305395082':'2840290',
'948294482109':'649228482',
'857456958772':'6584933821'
}
conto = input("Inserire il numero del conto di cui vuoi visualizzare il saldo.")
if conto in Conti_saldi:
    saldo = Conti_saldi[conto]
    print("Il saldo del conto ", conto," è di ",saldo," euro." )
else:
    print("Il conto fornito non è nella lista.")