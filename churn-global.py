# 1) Mesurer le churn (global + par abonnement)
# Problème. La direction veut connaître le taux d’attrition global et par type d’abonnement.

# from <fichier ou librairie> import <fontion ou classe>
from spotify import dataset

subscribers = 0 # nombre de personnes abonnées à spotify
churners = 0 # nombre de personnes ayant quitté le service
total_users = 0 # nombre total de personnes dans le dataset

# for <élément> in <itérable>:
for record in dataset:
    total_users = total_users + 1
    if record ["is_churned"] == "1":
        churners = churners + 1
    else:
        subscribers = subscribers + 1

churn_percentage = (churners / total_users) * 100

print(f"Le nombre total d'utilisateurs est de {total_users} personnes")
print(f"Il reste {subscribers} abonnés")
print(f"Le nombre total d'utilisateurs s'étant désabonnés est donc de {churn_percentage: .2f}%")
