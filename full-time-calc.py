from datetime import date, timedelta

periodes_temps_partiel = [    
    (date(2019, 6, 16), #date debut periode temps partiel
    date(2019, 12, 21), #date fin periode temps partiel
    0.8),] #coefficient temps partiel
date_entree = date(2017, 1, 1) #date d'entrée dans l'entreprise
date_sortie = date(2019, 12, 21) #date de sortie de l'entreprise
date_input = date(2019, 12, 28) #date de calcul

# Fonction qui calcule le nombre de jours entre deux dates
def nb_jours(date1, date2) :
    return (date2 - date1).days

# Fonction qui calcule le nombre de mois entre deux dates
def nb_mois(date1, date2) :
    return (date2.year - date1.year) * 12 + date2.month - date1.month

# Fonction qui calcul si un mois est de 30 ou 31 jours, si la date est au milieu du mois, on calcule le pourcentage de jours
def pourc_mois(date) :
    if (date.day == 30 or date.day == 31) :
        return 0
    else :
        return round((31 - date.day) / 31, 1)

# Fonction qui retoure une liste de 12 coefficients de temps de travail pour ramener au temps plein les périodes de temps partiel (1 = temps plein, O.8 = temps partiel à 80%) calcul défini par temps plein = temps plein / temps partiel
def coefficients_equivalent_temps_plein(periodes_temps_partiel, date_entree, date_sortie, date_input) :
    coef = []
    duree_temps_partiel = nb_mois(periodes_temps_partiel[0][0], periodes_temps_partiel[0][1])
    coef_temps_partiel = periodes_temps_partiel[0][2]
    coef_temps_partiel1 = pourc_mois(periodes_temps_partiel[0][0])
    duree_emploi = nb_mois(date_entree, date_sortie)

    if (coef_temps_partiel1 != 0) :
        full = 1 - coef_temps_partiel1
        coef_temps_partiel1 = (full * 1) + (coef_temps_partiel1 * coef_temps_partiel)
    if (duree_emploi < 12) :
        return []
    for i in range (0, 12) :
        if (i < (12 - duree_temps_partiel)) :
            coef.append(1)
        else :
            if (coef_temps_partiel1 != 0) :
                coef.append(1 / coef_temps_partiel1)
                coef_temps_partiel1 = 0
            else :
                coef.append(1 / coef_temps_partiel)
    return coef

def main() :
    coefficients = coefficients_equivalent_temps_plein(periodes_temps_partiel, date_entree, date_sortie, date_input)
    print(coefficients)

if __name__ == "__main__" :
    main()