<h1>Test Technique JobExit</h1>

__OBJECTIF :__ Calculer et afficher une liste contenant les 12 derniers coefficients à appliquer aux différents montants de salaire mensuel d'un salarié afin de ramener ce salaire à un équivalent temps plein.

<h3>Testez le programme avec :</h3>
<code>python3 main.py</code> -> Test avec des valeurs par défauts*
ou
<code>python3 main.py [nom_du_fichier.txt]</code> -> Test avec vos valeurs (voir exemple dans Test.txt)**


<p>
  *: Les valeurs par défauts sont : 
  <code>
  from datetime import date
  periodes_temps_partiel = [( date(2019, 6, 16), date(2019, 12, 21), 0.8, ), ]
  date_entree = date(2017, 1, 1)
  date_sortie = date(2019, 12, 21)
  date_input = date(2019, 12, 28)
  </code> <br />
  **: Le fichier par défauts contient:  <br />
  - Entreprise : <br />
    - ID -> Obligatoire <br />
    - Nom -> Obligatoire <br />
    - Employés : -> Facultatif <br />
      - ID -> Obligatoire <br />
      - Nom -> Obligatoire <br />
      - Date anniversaire -> Obligatoire <br />
      - Date début -> Obligatoire <br />
      - Date fin -> Facultatif <br />
      - Periode et coef temps partiel -> Facultatif <br />
</p>
