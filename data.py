""" Data classes"""

class Data_Tier1:
    n = 10
    pourcentage = 0.75
    temps = (5, 10)
    color = "#E57936"

class Data_Tier2:
    n = 20
    liens_t1 = (1, 2)
    liens_t2 = (2, 3)
    temps = (10, 20)
    color = "#3891C1"

class Data_Tier3:
    n = 70
    liens_t2 = 2
    temps = (20, 50)
    color = 'blue'


""" VAL """

data_tier1 = Data_Tier1()
data_tier2 = Data_Tier2()
data_tier3 = Data_Tier3()

couleur = "#EDF9EE"
text_couleur = "#041023"