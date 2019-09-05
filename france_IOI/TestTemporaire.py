#=========================================================================================
# #=========================================================================================
# # La grande fête
# #=========================================================================================
# Un espion était présent à la grande fête organisée la semaine dernière par le gouverneur. 
# Bien qu'on n'ait pas pu l'identifier, on a réussi à intercepter son rapport et à estimer
#  en fonction de ce qu'il a pu voir, à quelle période il a été présent. Sachant pour 
#  chaque invité sa date d'arrivée et de départ, on aimerait interroger tous les suspects
#   potentiels. Vous souhaitez savoir combien de suspects il faudra interroger.
# 
# Ce que doit faire votre programme :
# On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un 
# certain nombre d'invités d'une fête. Écrivez un programme qui détermine combien d'invités
#  ont été présents à un moment de la période étudiée.
# 
# Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de
#  la période étudiée. L'entier suivant, nbInvites, est le nombre total d'invités. Pour
#   chaque invité, votre programme doit ensuite lire deux entiers : sa date d'arrivée et
#    de départ. Un invité est suspect si la période à laquelle il a été présent intersecte
#     la période étudiée. Votre programme doit afficher le nombre d'invités suspects.
# 
# Exemple
# entrée :
# 
# 8
# 12
# 5

# 4
# 7

# 2
# 11

# 3
# 6

# 1
# 8

# 14
# 19
# sortie :
# 
# 2
#=========================================================================================
import random
#=========================================================================================
# liste = [8, 12, 5]
#=========================================================================================
liste = [random.randint(2, 30) for offsetPremiereColonne in range(3)]
while not(liste[0]<=liste[1]):
     liste = [random.randint(2, 30) for offsetPremiereColonne in range(3)]     
#=========================================================================================
# print(" liste" , liste)
#=========================================================================================
#=========================================================================================
# debut=int(input())
# fin=int(input())
# nbInvite=int(input())
#=========================================================================================
somme = 0 

debut = liste[0]
fin = liste[1] 

nbInvite = liste[2]
j = 0
for i in range(nbInvite):
    #=====================================================================================
    # arrive=int(input())
    # depart=int(input())
    #=====================================================================================
    #=====================================================================================
    # print("i ", i)
    #=====================================================================================
    #=====================================================================================
    # liste2 = [4, 7, 2, 11, 3, 6, 1, 8, 14, 19]
    #=====================================================================================
    liste2  = [random.randint( 1, 31) for offsetPremiereColonne in range(nbInvite * 2)]
    #=====================================================================================
    # while not(liste2[j]<=liste2[j+1]):
    #     liste2  = [random.randint( 1, 31) for offsetPremiereColonne in range(nbInvite * 2)]
    #=====================================================================================
    #=====================================================================================
    # print(" liste2" , liste2)
    #=====================================================================================
    j=i
    arrive = liste2[j]
    depart = liste2[j + 1]
    j = j + 2
    #=====================================================================================
    # j=j+3
    #=====================================================================================
    print("debut ", debut, " fin ", fin, " arrive ", arrive, " depart ", depart)
    if ((debut <= arrive <= fin) or (debut <= depart <= fin)):
    #=====================================================================================
    # if not((arrive>=debut and arrive<= fin) or (depart>=debut  and depart<= fin)):
    #=====================================================================================
    #=====================================================================================
    # if not((debut <= arrive and fin >= arrive) or (debut <= depart and fin >= depart)):
    #=====================================================================================
        
    #=====================================================================================
    # if not(arrive>=debut and depart <= fin):
    #=====================================================================================
    #=====================================================================================
    # if not((fin <= arrive)or (depart <= debut)):
    #=====================================================================================
        somme = somme + 1
        print("somme", somme)
print(somme)
            
#=========================================================================================
# version a soumettre   
#=========================================================================================
#=========================================================================================
# debut=int(input())
# fin=int(input())
# nbInvite=int(input())
# somme=0 
# 
# for i in range(nbInvite):
#     arrive=int(input())
#     depart=int(input())
#     if not(debut<=arrive and fin>=arrive) or (debut<=depart and fin>=depart):
#         somme=somme+1
# print(somme)
#=========================================================================================
