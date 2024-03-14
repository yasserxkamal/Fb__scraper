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



# from selenium import webdriver
# import bs4
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Replace 'path/to/chromedriver' with the path to your ChromeDriver executable
# driver = webdriver.Chrome()

# # Open the webpage
# driver.get("https://mbasic.facebook.com/")

# # Wait for the button to be clickable
# button_xpath = "//button[@type='submit' and @name='accept_only_essential' and @value='0' and contains(@class, 'bs')]"
# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

# # Click on the button
# button.click()
# # Wait for the input field to be present




# wait = WebDriverWait(driver, 10)
# input_field_id = "m_login_email"
# email_input = wait.until(EC.presence_of_element_located((By.ID, input_field_id)))
# password_input_name = "pass"
# Password = wait.until(EC.presence_of_element_located((By.NAME, password_input_name)))

# # Remplir l'élément avec le texte "yasser.kamal"
# email_input.send_keys("+212697291403")
# Password.send_keys("yasserkamal1234")

# # Wait for the submit button to be present
# submit_button_xpath = "//input[@type='submit' and @value='Se connecter' and @name='login' and contains(@class, 'bh')]"
# submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))

# # Click on the submit button
# submit_button.click()

# # Wait for the submit button to be present
# submit_button_xpath = "//input[@type='submit' and @value='OK' and contains(@class, 'bo') and contains(@class, 'bp') and contains(@class, 'bq') and contains(@class, 'br') and contains(@class, 'bs')]"
# submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))

# # Click on the submit button
# submit_button.click()


# # Wait for the input field to be present
# input_field_name = "query"
# input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, input_field_name)))

# # Type the desired text into the input field
# input_field.send_keys("#Pizza")
# # Press Enter to perform the search (optional)
# input_field.send_keys(Keys.RETURN)



# post_content_list = []

# # Find all <p> tags within the specified class
# for i in range(10):
#     # Get page source after search
#     html = driver.page_source
#     # Parse HTML
#     soup = bs4.BeautifulSoup(html, 'html.parser')


#     # Find all <article> tags
#     articles = soup.find_all('article')

    
#     # Extract content from each post
#     for article in articles:
#         # Find all <p> tags within the article
#         paragraphs = article.find_all('p')
#         post_content = ''
#         # Extract text content from each <p> tag and concatenate it with line breaks
#         for p in paragraphs:
#             post_content += '\n'.join(p.stripped_strings) + '\n'
#         post_content_list.append(post_content.strip())  # Add the post content to the list



#     # Wait for the button to be visible
#     button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[span='Afficher plus de résultats']"))
#     )

#     # Click the button
#     button.click()


# # Print the list of post content
# print(post_content_list)


# # Get posts  
# posts = soup.find_all('article', class_='bl bm bn')

# for post in posts:
  
#    content = post.find('div', class_='bx')
#    print(content)
# Create a list to store the content of each post


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# driver = webdriver.Chrome()
# driver.get('https://www.facebook.com/')

# # Attendre que l'élément soit présent
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='cookie-policy-manage-dialog-accept-button']")))

# # Cliquer sur l'élément
# element.click()

# # Attendre quelques secondes pour visualiser le résultat
# time.sleep(5)

# email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='royal_email']")))
# Password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='royal_pass']")))

# # Remplir l'élément avec le texte "yasser.kamal"
# email_input.send_keys("+212697291403")
# Password.send_keys("yasserkamal1234")

# elementlog = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='royal_login_button']")))
# # Cliquer sur l'élément
# elementlog.click()

# # Wait for the search input field to be present
# search_input_xpath = "//input[@aria-label='Rechercher sur Facebook']"
# search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_input_xpath)))

# # Type a search query into the input field
# search_input.send_keys("AI at Meta")

# # Press Enter to perform the search (optional)
# search_input.send_keys(Keys.RETURN)

# # Wait for the image element to be present
# image_xpath = "//image[contains(@xlink:href, 'https://scontent-cdg4-1.xx.fbcdn.net')]"
# image_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_xpath)))

# # Click on the image element
# image_element.click()