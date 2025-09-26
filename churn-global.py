# 1) Mesurer le churn (global + par abonnement)
# Problème. La direction veut connaître le taux d’attrition global et par type d’abonnement.

# from <fichier ou librairie> import <fontion ou classe>
from spotify import dataset

subscribers = 0 # nombre de personnes abonnées à spotify
churners = 0 # nombre de personnes ayant quitté le service
total_users = 0 # nombre total de personnes dans le dataset

churned_free = 0
churned_family = 0
churned_student = 0
churned_premium = 0


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

for record in dataset:
    if record ["subscription_type"]== "Free" and record ["is_churned"] == "1":
        churned_free = churned_free + 1

churn_free_percentage = (churned_free / total_users) * 100
print(f"dont{churn_free_percentage: .2f}% d'abonnements gratuits")

for record in dataset:
    if record ["subscription_type"]== "Family" and record ["is_churned"] == "1":
        churned_family = churned_family + 1

churn_family_percentage = (churned_family / total_users) * 100
print(f"dont{churn_family_percentage: .2f}% d'abonnements famille")

for record in dataset:
    if record ["subscription_type"]== "Student" and record ["is_churned"] == "1":
        churned_student = churned_student + 1

churn_student_percentage = (churned_student / total_users) * 100
print(f"dont{churn_student_percentage: .2f}% d'abonnements étudiants")

for record in dataset:
    if record ["subscription_type"]== "Premium" and record ["is_churned"] == "1":
        churned_premium = churned_premium + 1

churned_premium_percentage = (churned_premium / total_users) * 100
print(f"et{churned_premium_percentage: .2f}% d'abonnement premium.")
