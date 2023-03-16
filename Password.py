# Importation des modules
import string
import hashlib
import json

# Je commence par déclarer ma fonction Password
def Password():
    # Vérifie tant que le mot de passe est invalide, alors la boucle va se répéter...
    while True:
        # Je demande à l'utilisateur d'entrer son mot de passe
        get_password = input("Veuillez entrer votre mot de passe :")

        # Si le mot de passe contient au moins 8 caractères
        if len(get_password) >= 8:
            # Je déclare mes variables, qui serviront à vérifier mes conditions
            uppercase = False
            lowercase = False
            numbers = False
            special_chars = False
            
            for char in get_password: # Pour chaque caractère dans le mot de passe...
                
                if char in string.ascii_uppercase: # Vérifie la présence des lettres en majuscule
                    uppercase = True
                elif char in string.ascii_lowercase: # Vérifie la présence des lettres en minuscule
                    lowercase = True
                elif char.isdigit(): # Vérifie la présence des nombres 
                    numbers = True
                elif char in ['!', '@', '#', '$', '%', '^', '&', '*']: # Vérifie si il y a des caractères spéciaux
                    special_chars = True


            # Si les conditions ne sont pas respectées, alors...
            if not uppercase:
                print("Votre mot de passe doit contenir au moins une majuscule")
            if not lowercase:
                print("Votre mot de passe doit contenir au moins une minuscule")
            if not numbers:
                print("Votre mot de passe doit contenir au moins un nombre")
            if not special_chars:
                print("Votre mot de passe doit contenir au moins un caractère spécial")


            # Enfin si toutes les conditions sont respectées, alors...
            if uppercase and lowercase and numbers and special_chars:
                print("Votre mot de passe est correct")
                return get_password
            else: #Sinon affiche un message d'erreur
                print("Votre mot de passe est incorrect")

        else: # Sinon le mot de passe est trop court
            print("Votre mot de passe est trop court")

# J'appelle ma fonction qui demande un mot de passe, puis qui stocke le résultat dans une variable
user_password = Password()  

# Déclaration de la fonction de cryptage
def cryptage(get_password):
    # Je vais utiliser un algortihme de hashage nommé SHA-256
    # encode() va convertir une string en bytes afin qu'elle puisse être accepté par hashlib.sha()

    hash = hashlib.sha256(get_password.encode('UTF-8')) 
    # Puis la méthode hexdigest va convertir les bytes en une chaîne hexadécimale
    encrypted_password = hash.hexdigest()

    print(encrypted_password) #Enfin affiche moi le mot de passe encrypté

cryptage(user_password) #Enfin J'éxecute ma fonction cryptage qui se charge d'encrypter le mot de passe
            
            

        



    
