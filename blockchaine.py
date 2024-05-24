from hash import hash_char_64
from verif import verifier_integrite
class block:#https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants
    # Attributs de classe
    nom  = ""
    prenom = ""
    age = ""
    id = "maurice" # pour avoir une racine pour le hash
    id_precedent = ""
    # methode pour aficher
    def affiche(self):
        print("ID : ", self.id)
        print("ID_precedent : ", self.id_precedent)
        print("Nom : ", self.nom)
        print("Prénom : ", self.prenom)
        print("Âge : ", self.age)

     

chaine = [] # chaine qui nous sert à stoker cette objet

n= int(input(" Enter le nombre d'ellement à entrer  : ")) 

for i in range(n): # on demande a l'utilisateur de rentrer n block(s)
    obj_i = block()
    obj_i.nom = input(" entrer le nom : ")
    obj_i.prenom = input(" entrer le prenom : ")
    obj_i.age = input(" entrer l'age : ")
    if i == 0 :  # dans le cadre du premier block
        obj_i.id_precedent = ""
        hash = obj_i.nom + obj_i.prenom + obj_i.age + obj_i.id # on concataine tout les ellement du block
        obj_i.id = hash_char_64(hash)# on hash notre concatenation et on fait de ça notre id 
        chaine.append(obj_i)
    else:# dans les autres cas 
        obj_i.id_precedent = str(chaine[i-1].id)
        hash = obj_i.nom + obj_i.prenom + obj_i.age + obj_i.id_precedent ## on concataine tout les ellement du block + le id du block précédent
        obj_i.id = hash_char_64(hash)
        chaine.append(obj_i)

for i in range(n): # on afiche tout les ellement enregister
    print("")
    print ((chaine[i]).affiche())
verifier_integrite(chaine)
