# Problème. Finance : estimer le MRR de base par plan et par pays (utilisateurs non churnés). Sur base des prix suivants :

# country_list = []
# free_sub_CA = 0
# premium_sub_CA = 0
# family_sub_CA = 0
# student_sub_CA = 0
# mrr_premium_CA = 0
# mrr_family_CA = 0
# mrr_student_CA = 0

# for record in dataset:
#     if record["country"] not in country_list:
#         country_list.append(record ["country"])
        
#     if record["country"] == "CA" and record["is_churned"] == "0":
#         if record["subscription_type"] == "Free":
#             free_sub_CA = free_sub_CA + 1
#         if record["subscription_type"] == "Premium":
#             premium_sub_CA = premium_sub_CA + 1
#         if record["subscription_type"] == "Family":
#             family_sub_CA = family_sub_CA + 1
#         if record["subscription_type"] == "Student":
#             student_sub_CA = student_sub_CA + 1

# mrr_premium_CA = premium_sub_CA * 9.99

# print(mrr_premium_CA)

#########################################################################################################

from spotify import dataset

PRICES = {"Free": 0.0, "Premium": 9.99, "Family": 14.99, "Student": 4.99}
COUNTRY = ['CA', 'DE', 'AU', 'US', 'UK', 'IN', 'FR', 'PK']

def mrr_sub_country(dataset, country, subscription_type):
    sub_country = 0
    for record in dataset:
        if record["is_churned"] == "0":
            if record["country"] == country and record["subscription_type"] == subscription_type:
                sub_country = sub_country + 1

    mrr = sub_country * PRICES[subscription_type]
    return mrr

for country in COUNTRY:
    for sub_type in PRICES.keys():
        print(country, sub_type, mrr_sub_country(dataset, country, sub_type))