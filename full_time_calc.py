# Fonction qui calcule le nombre de mois entre deux dates
def nb_mois(date1, date2) :
    return (date2.year - date1.year) * 12 + date2.month - date1.month

# Fonction qui calcule si un mois est de 30 ou 31 jours, si la date est au milieu du mois, on calcule le pourcentage de jours
def pourc_mois(date) :
    if (date.day == 30 or date.day == 31) :
        return 0
    else :
        return round((31 - date.day) / 31, 1)

# Fonction qui met à jour la liste des périodes de temps partiel
def put_in_list(coef_list, start_date, end_date, coef, last_coef, last_end, nb) :
    temp = coef

    if (pourc_mois(start_date) != 0) :
        coef = ((1-pourc_mois(start_date)) * last_coef) + (pourc_mois(start_date) * coef)
        last_coef = temp
    else :
        last_coef = coef
    if (start_date > last_end) :
        for i in range(0, nb) :
            if (len(coef_list) >= 12) :
                coef_list.pop(0)
            coef_list.append(round(1/coef, 6))
            coef = last_coef
        return end_date
    else :
        for i in range(0, nb) :
            if (len(coef_list) >= 12) :
                break
            coef_list.insert(round(1/coef, 6))
            coef = last_coef
        return last_end

# Fonction qui calcule les coefficients et qui retourne la liste des 12 coefficients (1/pourcentage travaillé -> ex: 1/0.8)
def calc_coef(periodes_temps_partiel, limit_date, date_sortie):
    coef_list = []
    last_end = limit_date
    last_coef = 1

    if (periodes_temps_partiel == None) :
        return [1 for i in range(0, 12)]
    for part_time in periodes_temps_partiel:
        start = part_time[0]
        end = part_time[1]
        coef = part_time[2]
        if (end == None) :
            end = date_sortie
        if (end < limit_date):
            continue
        if (nb_mois(start, end) < 12) :
            last_end = put_in_list(coef_list, start, end, coef, last_coef, last_end, nb_mois(start, end))
        else :
            coef_list = [round(1/coef, 6) for i in range(0, 12)]
    while (len(coef_list) < 12) :
        if (last_end < date_sortie) :
            for i in range(0, nb_mois(last_end, date_sortie)) :
                coef_list.append(1)
            last_end = date_sortie
        else :
            for i in range(0, 12 - len(coef_list)) :
                coef_list.insert(0, 1)
    return coef_list

# Fonction qui initialise les variables qui vont servir à récupérer les coefficients
def coefficients_equivalent_temps_plein(periodes_temps_partiel, date_entree, date_sortie, date_input) :
    if (date_sortie == None) :
        date_sortie = date_input
    if (pourc_mois(date_sortie) != 0) :
        date_sortie = date_sortie.replace(month = date_sortie.month-1, day = 1)
    limit_date = date_sortie.replace(year = date_sortie.year - 1)
    if (date_entree < limit_date) :
        date_entree = limit_date
    return calc_coef(periodes_temps_partiel, limit_date, date_sortie)