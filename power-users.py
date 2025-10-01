# Problème. Produit : cibler les gros utilisateurs pour bêta-tests. 
# Règles métier : + de 200 min d’écoute par jour et + de 50 titres écoutés par jour

from spotify import dataset

power_users = 0
list_user = []

for record in dataset:
    if int(record["listening_time"]) > 200 and int(record["songs_played_per_day"]) > 50:
        power_users = power_users + 1
        list_user.append(record["user_id"])
print(f"Il y a {power_users} utilisateurs éligibles à la bêta-test.")
print(f"Voici les utilisateurs à relancer : {list_user}")