especes=["CH\u2084","O\u2082","CO\u2082","H\u2082O"]

coefficients=[-1, -2, 1, 2]

etat_init = [3., 20., 0., 0.] #quantités initiales en moles

etat_inter = list(etat_init) #on initialise l'état intermediaire

dksi = 0.0001 #pas

print("====== Etat Initial ======")
for i in range(len(especes)):
    print(especes[i],": {:.3f}".format(etat_inter[i])) #on affiche le résultat avec 3 chiffres après la virgule

x = 0 #avancement initial

while etat_inter[0]>0 and etat_inter[1]>0: #tant qu'il y a des réactifs
    x = x + dksi
    for i in range(len(especes)):
        etat_inter[i] = etat_inter[i] + coefficients[i]*dksi

#recalcul des conditions d'arrêt de la réaction
x = x - dksi
for i in range(len(especes)):
    etat_inter[i] = etat_inter[i] - coefficients[i]*dksi

print("====== Etat Final ======")
for i in range(len(especes)):
    print(especes[i],": {:.3f}".format(etat_inter[i])) #on affiche le résultat avec 3 chiffres après la virgule

print("Avancement final : xf = {:.3f} mol".format(x))
