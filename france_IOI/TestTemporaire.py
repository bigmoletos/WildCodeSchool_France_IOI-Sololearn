#=========================================================================================
# Département de pédagogie : le « c'est plus, c'est moins »
# Dans une cité commerçante, il est important que les habitants soient forts en calcul 
# mental afin de pouvoir négocier leurs prix et choisir les meilleurs produits sans se 
# faire avoir. Le département de pédagogie de l'université a donc été sollicité afin de 
# mettre au point des exercices stimulants pour les enfants, qui vont les inciter à 
# travailler leur calcul mental.
# 
# Réalisant le potentiel que peut avoir votre robot dans un cadre pédagogique, les 
# chercheurs vous demandent de mettre au point un programme capable de faire jouer de
#  manière automatisée un enfant au jeu du « c'est plus, c'est moins » : l'enfant doit
#   deviner un nombre secret en faisant des propositions, et on lui répond chaque fois 
#   par « c'est plus » ou « c'est moins », jusqu'à ce qu'il ait trouvé le bon nombre.
# 
# L'objectif est bien sûr pour les enfants de trouver le bon nombre le plus rapidement possible !
# 
# Ce que doit faire votre programme :
# Votre programme doit d'abord lire un entier, le nombre que l'enfant devra trouver. Ensuite,
#  il devra lire les propositions du joueur, 
#  et afficher à chaque fois le texte « c'est plus » (l'enfant a proposé un nombre trop petit)
#   ou « c'est moins » (l'enfant a proposé un nombre trop grand) selon les cas, 
#   et recommencer tant que l'enfant n'a pas trouvé le bon nombre.
# 
# À la fin, il faudra afficher le texte « Nombre d'essais nécessaires : »
#  puis, à la ligne en dessous, le nombre d'essais qui ont été nécessaires.
# 
# On vous garantit que l'enfant finira par trouver la bonne valeur !
# 
# Exemples
# Exemple 1
# entrée :
# 5
# 1
# 2
# 3
# 4
# 5
# sortie :
# c'est plus
# c'est plus
# c'est plus
# c'est plus
# Nombre d'essais nécessaires :
# 5
# 
# Exemple 2
# entrée :
# 10
# 5
# 15
# 8
# 12
# 11
# 10
# sortie :
# 
# c'est plus
# c'est moins
# c'est plus
# c'est moins
# c'est moins
# Nombre d'essais nécessaires :
# 6
# 
# Exemple 3
# entrée :
# -50
# -80
# -50
# sortie :
# 
# c'est plus
# Nombre d'essais nécessaires :
# 2
#=========================================================================================
devineLeChiffre=int(input())
chiffreEnfant=0
nbreEssais=0

while (chiffreEnfant!=devineLeChiffre):
    chiffreEnfant=int(input())
    if (chiffreEnfant<devineLeChiffre):
        print("c'est plus")
    elif (chiffreEnfant>devineLeChiffre):
        print("c'est moins")
    nbreEssais+=1       
print( "Nombre d'essais nécessaires :\n" , nbreEssais )
    
    
#=========================================================================================
# correction    
#=========================================================================================
aDeviner = int(input())
proposition = int(input())
nbEssais = 1
while proposition != aDeviner:
   if proposition < aDeviner:
      print("c'est plus")
   if proposition > aDeviner:
      print("c'est moins")
   proposition = int(input())
   nbEssais = nbEssais + 1
print("Nombre d'essais nécessaires : ")
print(nbEssais)




#=========================================================================================
# correction    java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int àDeviner = entrée.nextInt();
      int proposition = àDeviner + 1;
      int nbEssais = 0;
      while (proposition != àDeviner)
      {
         proposition = entrée.nextInt();
         if (proposition < àDeviner)
         {
            System.out.println("c'est plus");
         }
         if (proposition > àDeviner)
         {
            System.out.println("c'est moins");
         }
         nbEssais = nbEssais + 1;
      }
      System.out.println("Nombre d'essais nécessaires : ");
      System.out.println(nbEssais);
   }
}    