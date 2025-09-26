# 2) Détecter les utilisateurs “à risque” (règles métier simples)
# Problème. Équipe CRM : repérer les comptes à relancer.
# Règles métier : taux de “skip” > 30% et taux d’écoute < 100 min par jour OU sur les comptes gratuits, aucune écoute offline + écoute de pub > 20 par semaine

from spotify import dataset

user_at_risk = 0
liste_user_at_risk = []

for record in dataset:
    if ((float(record ["skip_rate"]) > 0.3 and float(record ["listening_time"]) < 100)) or ((record ["subscription_type"] == "Free" and record ["offline_listening"] == "0" and float(record ["ads_listened_per_week"]) > 20)):
        user_at_risk = user_at_risk + 1
        liste_user_at_risk.append(record ["user_id"])

print(f"Vous devez relancer {user_at_risk} personnes.")
print(liste_user_at_risk)