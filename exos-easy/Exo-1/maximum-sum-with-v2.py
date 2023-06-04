nums = [1, 7, 5, 2]

def two_sum(nums, target=9):
    num_index = {} # dictionnaire qui associe chaque nombre à son indice
    for index, num in enumerate(nums): # boucle qui parcourt la liste avec enumerate
        complement = target - num # calcul du complément du nombre actuel
        if complement in num_index: # vérification si le complément existe dans le dictionnaire
            return [num_index[complement], index] # renvoi des indices de la paire trouvée
        else:
            num_index[num] = index # ajout du nombre actuel et de son indice au dictionnaire

print(two_sum(nums))
