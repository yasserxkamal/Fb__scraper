# Importer les modules nécessaires
from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Charger les variables d'environnement depuis le fichier .env
from dotenv import load_dotenv
load_dotenv()

# Récupérer les valeurs des variables d'environnement
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
FB_EMAIL = os.getenv('FB_EMAIL')
FB_PASSWORD = os.getenv('FB_PASSWORD')

# Initialiser le navigateur Chrome avec le chemin du pilote
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

# Ouvrir la page web Facebook
driver.get("https://mbasic.facebook.com/")

# Attendre que le bouton soit cliquable et cliquer dessus
button_xpath = "//button[@type='submit' and @name='accept_only_essential' and @value='0' and contains(@class, 'bs')]"
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
button.click()

# Attendre que les champs de saisie soient présents
wait = WebDriverWait(driver, 10)
input_field_id = "m_login_email"
email_input = wait.until(EC.presence_of_element_located((By.ID, input_field_id)))
password_input_name = "pass"
password_input = wait.until(EC.presence_of_element_located((By.NAME, password_input_name)))

# Remplir les champs avec l'email et le mot de passe
email_input.send_keys(FB_EMAIL)
password_input.send_keys(FB_PASSWORD)

# Attendre que le bouton de soumission soit présent et cliquer dessus
submit_button_xpath = "//input[@type='submit' and @value='Se connecter' and @name='login' and contains(@class, 'bh')]"
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
submit_button.click()

# Attendre que le bouton de confirmation soit présent et cliquer dessus
submit_button_xpath = "//input[@type='submit' and @value='OK' and contains(@class, 'bo') and contains(@class, 'bp') and contains(@class, 'bq') and contains(@class, 'br') and contains(@class, 'bs')]"
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
submit_button.click()

# Attendre que le champ de recherche soit présent
input_field_name = "query"
input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, input_field_name)))

# Effectuer une recherche
search_query = os.getenv('HASHTAG')
input_field.send_keys(search_query)
input_field.send_keys(Keys.RETURN)

post_content_list = []

# Extraire le contenu des 10 premiers résultats de recherche
for i in range(10):
    # Obtenir le code source de la page après la recherche
    html = driver.page_source
    # Analyser le HTML
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Trouver tous les tags <article>
    articles = soup.find_all('article')

    # Extraire le contenu de chaque article
    for article in articles:
        # Trouver tous les tags <p> dans l'article
        paragraphs = article.find_all('p')
        post_content = ''
        # Concaténer le texte de chaque tag <p>
        for p in paragraphs:
            post_content += '\n'.join(p.stripped_strings) + '\n'
        post_content_list.append(post_content.strip())  # Ajouter le contenu de l'article à la liste

    # Attendre que le bouton "Afficher plus de résultats" soit visible et cliquer dessus
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span='Afficher plus de résultats']"))
    )
    button.click()

# Afficher la liste des contenus d'articles
print(post_content_list)
