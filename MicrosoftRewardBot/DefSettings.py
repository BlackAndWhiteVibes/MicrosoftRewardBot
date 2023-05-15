# Cette fonction crée un fichier "path" avec les paramètres de base
def create_settings(path):
    try:
        with open(path, "r"):
            pass
    except:
        with open(path, "w"):
            pass


# Cette fonction sauvegarde un changement de setting
def save_setting(path, name_setting="", new_value=""):
    # Essaye de changer le setting
    try:
        # Garde en mémoire le fichier "path" précédent et cherche le setting
        with open(path, "r") as f:
            ligne = f.readlines()
            for i in range(len(ligne)):
                case = ligne[i]
                if case == str(name_setting) + " :\n":
                    ligne[i + 1] = str(new_value) + "\n"
        # Modifie le fichier "path" avec le setting modifié
        with open(path, "w") as f:
            for i in range(len(ligne)):
                f.write(ligne[i])

    # Si aucun fichier "path" existe, il est alors créé
    except:
        create_settings(path)
        add_setting(path, name_setting, value_setting)


# Crée un nouveau paramètre
def add_setting(path, name_setting, value_setting):
    try:
        with open(path, "a") as f:
            f.write(name_setting + " :\n")
            f.write(value_setting + "\n")
    except:
        pass


# Renvoie la valeur d'un setting
def return_setting(path, name_setting):
    try:
        with open(path, "r") as f:
            ligne = f.readlines()
            for i in range(len(ligne)):
                renvoie = ""
                if ligne[i] == str(name_setting) + " :\n":
                    # permet d'enlever \n du renvoie
                    for y in range(len(ligne[i + 1]) - 1):
                        renvoie += ligne[i + 1][y]
                    return renvoie
    except:
        pass
