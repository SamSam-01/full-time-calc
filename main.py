from sys import argv
from parse_file import parse, print_entreprise_info, print_entreprises
from full_time_calc import coefficients_equivalent_temps_plein
from datetime import date

periodes_temps_partiel = [    
    (date(2019, 6, 16), #date debut periode temps partiel
    date(2019, 12, 21), #date fin periode temps partiel
    0.8),] #coefficient temps partiel
date_entree = date(2017, 1, 1) #date d'entrée dans l'entreprise
date_sortie = date(2019, 12, 21) #date de sortie de l'entreprise
date_input = date(2019, 12, 28) #date de calcul

def main():
    if (len(argv) < 2):
        coefficients = coefficients_equivalent_temps_plein(periodes_temps_partiel, date_entree, date_sortie, date_input)
        print(coefficients)
    else:
        entreprises = parse(argv[1])
        print_entreprise_info(1)

if __name__ == "__main__":
    main()
