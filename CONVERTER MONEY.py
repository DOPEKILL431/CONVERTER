#CONVERTER EURO TO FCFA
#CONVERTER FCFA TO EURO


print ("If you want to convert from FCFA to EURO type 1")
print ("If you want to convert from EURO to FCFA type 2")

coef_fcfa_to_euro=655.957
n=int(input("saisir 1 ou 2: "))

if n==1:
      montant_convert=int(input("Saisir le montant à convertir en euro : "))
      result_convert=montant_convert/coef_fcfa_to_euro
      print (montant_convert,"FCFA =",result_convert,"€")

if n==2:
      montant_convert=int(input("Saisir le montant à convertir en FCFA : "))
      result_convert=montant_convert*coef_fcfa_to_euro
      print(montant_convert,"€ =",result_convert,"FCFA")



