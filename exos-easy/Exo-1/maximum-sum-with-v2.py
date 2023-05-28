
#* Ce code définit une fonction sum_two qui prend en argument une liste de nombres nums et une valeur cible target qui par défaut est égale à 9. La fonction utilise un dictionnaire dico pour stocker les nombres de la liste nums et leur index correspondant.

#* Ensuite, la fonction parcourt la liste nums à l'aide d'une boucle for, et pour chaque élément nums[i], elle vérifie si la différence entre la valeur cible target et nums[i] est présente dans le dictionnaire dico. Si c'est le cas, cela signifie que la somme de deux nombres de la liste nums est égale à la valeur cible target, et la fonction renvoie un tableau contenant les indices de ces deux nombres. Sinon, la fonction ajoute nums[i] au dictionnaire dico avec son index correspondant.

#* En résumé, cette fonction cherche à trouver les indices de deux nombres dans une liste qui, lorsqu'ils sont ajoutés, donnent une valeur cible donnée.

#! La complexité de ce code est linéaire, c'est-à-dire O(n), où n est la longueur de la liste nums. Cela est dû au fait que la boucle for parcourt chaque élément de la liste une seule fois, et chaque opération effectuée à l'intérieur de la boucle a une complexité constante. En utilisant un dictionnaire pour stocker les nombres de la liste et leur index correspondant, la recherche de la différence entre la valeur cible et chaque nombre se fait en temps constant, ce qui donne une complexité totale de O(n).
nums = [1, -2, 3, 10, -4, 7, -5, 2]

def sum_two(nums, target = 9):
    dico = {}
    for i in range(len(nums)):
        if target - nums[i] in dico:
    
            return [dico[target-nums[i]], i]
        else:
            dico[nums[i]] = i
    

print(sum_two(nums, target = 9))