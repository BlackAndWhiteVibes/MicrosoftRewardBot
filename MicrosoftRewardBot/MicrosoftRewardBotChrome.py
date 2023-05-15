from datetime import datetime
import DefSettings

if DefSettings.return_setting("Comptes.txt", "Date de changement") != datetime.now().strftime("%Y-%m-%d") :
    from random import randint
    import time
    import importlib
    import subprocess

    def import_if_not_exists(module_name):
        try:
            importlib.import_module(module_name)
        except ImportError:
            print(f"{module_name} module not found. Installing {module_name}...")
            subprocess.check_call(["pip", "install", module_name])
        
    import_if_not_exists("selenium")

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import logging

    DefSettings.create_settings("Comptes.txt")
    DefSettings.create_settings("Horaire.txt")

    def save_crash(exception_info):
        # Récupére la date et l'heure actuelles
        maintenant = datetime.now()
        with open('crash.log', 'a') as f:
            print(str(exception_info))
            f.write('---- CRASH REPORT ----\n')
            f.write(maintenant.strftime("%Y-%m-%d %H:%M:%S"))
            f.write(str(exception_info))
            f.write('\n\n')


    def recherche_journaliere():
        recherche = "numero: "
        for i in range(40):
            recherche = recherche+str(randint(1,9))
            driver.get('https://www.bing.com/search?q='+recherche)
            print(driver.title)


    def defi_journalier():
        # Ouvrir la page Google
        driver.get('https://rewards.bing.com/')
        try:
            # Attendre que le bouton "Bienvenue dans le programme Microsoft Rewards" soit visible
            button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-glyph glyph-cancel']")))
            # Cliquer sur le bouton
            button.click()
        except:
            pass
        
        # Attendre que le bouton des cookies soit visible
        refuser_button = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_2j0fmugLb1FgYz6KPuB91w']//button[text()='Refuser']")))
        # Cliquer sur le bouton
        refuser_button.click()
        
        print(driver.title)
        #Les quetes quotidienne
        try:
            print("Ouverture des fenêtres des quêtes quotidiennes...")
            for nb_daily_set in range(3):
                time.sleep(3)
                # Attendre que la quête quotidienne soit chargée et cliquable
                daily_set = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'mee-card[ng-if="$ctrl.dailySets[0].length > {nb_daily_set}"]')))
                daily_set_text = daily_set.text
                text = daily_set_text.split('\n')
                print(f"La quête quotidienne {nb_daily_set} rapporte {text[0]} points.")
                print(f"Son titre est {text[1]}.")
                try:
                    # Cliquer sur la quête quotidienne
                    daily_set.click()
                    defi_on_page(1, text[1], driver)
                except:
                    print("Ce defi est soit :")
                    print(" - pas pris en charge par le navigateur actuel (exemple:seulement pris en charge par edge et pas par chrome)")
                    print(" - impossible à effectuer avant d'avoir redemarrer votre ordinateur (bug du navigateur entier)")
                    # Ouvrir la page Google
                    driver.get('https://rewards.bing.com/')
        except:
            save_crash("[[[[Crash des quêtes quotidiennes...]]]]")
            pass
        
        #Les activités quotidienne
        try:
            print("Ouverture des fenêtres des activités quotidiennes...")
            last_defi = False
            while not last_defi:
                try:
                    for nb_daily_activity in range(0,20):
                        daily_activity = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'mee-card[ng-if="$ctrl.cardItems.length > {nb_daily_activity}"]')))
                        last_defi_number = nb_daily_activity
                except:
                    last_defi = True
            print(f"Their is {last_defi_number+1} defi today [With or without point]")
                    
            first_defi_number = 0
            while first_defi_number != last_defi_number:
                try:
                    for nb_daily_activity in range(first_defi_number,last_defi_number+1):
                        # Attendre que l'activite quotidienne soit chargée et cliquable
                        daily_activity = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'mee-card[ng-if="$ctrl.cardItems.length > {nb_daily_activity}"]')))
                        daily_activity_text = daily_activity.text
                        text = daily_activity_text.split('\n')
                        print(f"L'activités quotidienne {nb_daily_activity+1} rapporte {text[0]} points.")
                        print(f"Son titre est {text[1]}.")
                        
                        # Cliquer sur l'activite quotidienne
                        daily_activity.click()
                        defi_on_page(1, text[1], driver)
                    break
                except:
                    first_defi_number += 1
                    driver.get('https://rewards.bing.com/')
            print(f"Activités completed today : {first_defi_number}")
        except:
            save_crash("[[[[Crash des activités quotidiennes...]]]]")
            pass


    def defi_on_page(page_number, title_defi, driver):
        # Basculer vers le nouvel onglet
        driver.switch_to.window(driver.window_handles[page_number])
        try:
            if title_defi == 'Sondage Rewards quotidien':
                preference_resolution(driver)
            if title_defi.find('Quiz') != -1:
                QCM_resolution(driver)
        finally:
            driver.close()
            # Revenir à l'onglet principal
            driver.switch_to.window(main_tab)


    def preference_resolution(driver):
        try:
            # Attendre que le bouton de debut de question de preference est cliquable
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "btoption0")))
            # Cliquer sur le bouton
            time.sleep(1)
            button.click()
            time.sleep(1)
            print("Sondage résolue.")
        except:
            pass
        

    def QCM_resolution(driver):
        try:
            # Attendre que le bouton de debut de QCM est cliquable
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "rqStartQuiz")))
            # Cliquer sur le bouton
            time.sleep(1)
            button.click()
            
            # Recupere le nombre de points récuperable
            box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "rqMCredits")))
            time.sleep(1)
            # Récupére la valeur de l'élément
            points_obtainable = int(box.text)
            points_obtainable = int(points_obtainable/10)
            for number_of_question in range(points_obtainable):
                print(f"Résolution de la question {number_of_question+1} du quizz")
                try:
                    points_obtained_during = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "rqECredits")))
                    number_case = 0
                    points_obtained_start = 0
                    while points_obtained_during != points_obtained_start:
                        # Attendre que le bouton de réponse soit cliquable
                        button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, f"rqAnswerOption{number_case}")))
                        # Cliquer sur le bouton
                        button.click()
                        number_case += 1
                        # Attendre que les points obtenus soient mis à jour
                        points_obtained_start = points_obtained_during
                        points_obtained_during = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "rqECredits")))
                except:
                    pass
            time.sleep(1)
        except:
            pass


    def start_new_driver():
        global driver, main_tab
        print("Demarrage d'une nouvelle fenetre chrome\n")
        PATH = "chromedriver.exe"
        
        # Définir les options pour Chrome en mode headless
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--log-level=3')

        # Créer une instance de webdriver en utilisant les options de Chrome en mode headless
        driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
        driver.maximize_window() # For maximizing window
        
        # Ouvrir une page Google
        driver.get('https://www.google.com/')
        print(driver.title)
        # Récupérer l'identifiant de l'onglet principal
        main_tab = driver.current_window_handle

    
    def SavePoints(email):
        driver.get('https://www.bing.com/')
        # Attendre que l'élément soit présent
        box = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "id_rc")))
        time.sleep(1)
        # Récupérer la valeur de l'élément
        valeur = str(box.get_attribute("textContent"))
        print("nb points = ", valeur)
        # Récupérer la date et l'heure actuelles
        maintenant = datetime.now()
        # Formater la date et l'heure en une chaîne de caractères
        date_heure = maintenant.strftime("%Y-%m-%d %H:%M:%S") + " || " + "Points maintenant: " + valeur
        #Sauvegarde des points gagnés entre le debut et la fin du script dans un fichier
        i = int(DefSettings.return_setting("Comptes.txt", "Changement " + str(email) + " numero"))+1
        DefSettings.add_setting("Horaire.txt", "Changement " + str(email) + " numero " + str(i), date_heure)
        DefSettings.save_setting("Comptes.txt", "Changement " + str(email) + " numero", new_value=i)
        print("Points sauvegardés.")


    def connexion_compte(nb_comptes):
        # Ouvrir la page Microsoft reward
        driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252fmsrewards%252fapi%252fv1%252fenroll%253fpubl%253dBINGIP%2526crea%253dMY00IA%2526pn%253dBINGTRIAL5TO250P201808%2526partnerId%253dBingRewards%2526pred%253dtrue%2526sessionId%253d3E078F06B54C69BD0B809DD5B42D68B8%26sig%3d3E078F06B54C69BD0B809DD5B42D68B8&wp=MBI_SSL&lc=1036&CSRFToken=11c48651-7076-41d6-a705-67b809f51c0b&cobrandid=03c8bbb5-2dff-4721-8261-a4ccff24c81a&lw=1&fl=easi2')
        print(driver.title)
        # Attendre que la barre de recherche soit chargée et la sélectionner
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "loginfmt")))
        # Entrer le mail dans la barre de recherche et envoyer la requête
        search_box.send_keys(str(compte[nb_comptes]))
        search_box.send_keys(Keys.RETURN)
        print("Envoie email...")

        # Attendre que la barre de recherche soit chargée et la sélectionner
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "passwd")))
        # Entrer le mdp dans la barre de recherche et envoyer la requête
        search_box.send_keys(str(compte[nb_comptes+1]))
        print("Ecriture mdp.")
        time.sleep(1)
        # Attendre que la barre de recherche soit chargée et la sélectionner
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "passwd")))
        search_box.submit()
        print("Envoie mdp...")

        # Attendre jusqu'à ce que le bouton soit présent sur la page
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idBtn_Back")))
        # cliquer sur le bouton
        search_box.click()
        print("Refus de rester connecter.")
        try:
            # attendre jusqu'à ce que le bouton soit présent sur la page
            search_box = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "bnp_btn_reject")))
            # cliquer sur le bouton
            search_box.click()
            print("Refus des cookies.")
        except:
            pass
        name_account = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "id_n")))
        # Récupérer la valeur de l'élément
        print("Connecter au compte: " + str(name_account.get_attribute("textContent")))


    def deconnexion_compte():
        # Se déconnecter
        driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com')
        print("Déconnecter.\n")

    

    compte =[]
    # Ouvre le fichier Comptes.txt en mode lecture
    with open('Comptes.txt', 'r') as f:
        # Lit les lignes du fichier
        lignes = f.readlines()

        for i in range(0,len(lignes),8):
            # Extrait l'adresse email et le mot de passe
            email = DefSettings.return_setting("Comptes.txt", "adresse email " + str((6+i)//6))
            mdp = DefSettings.return_setting("Comptes.txt", "mot de passe " + str((6+i)//6))
            compte.append(email)
            compte.append(mdp)

    try:
        for nb_comptes in range(0,len(compte),2):
            start_new_driver()
            connexion_compte(nb_comptes)

            recherche_journaliere()
            defi_journalier()

            SavePoints(str(compte[nb_comptes]))
            with open('horaire.txt', 'a') as f:
                f.write("\n")

            deconnexion_compte()
            print("Supression de la fenetre chrome...\n")
            driver.quit()
            print("Supression effectue.\n")
            
        DefSettings.save_setting("Comptes.txt", "Date de changement", datetime.now().strftime("%Y-%m-%d"))
        
    finally:
        pass
