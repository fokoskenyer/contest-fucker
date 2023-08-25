import os,random,time
import pyautogui
import pyperclip
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def chooseLastName():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    text_file_path = os.path.join(script_dir, 'name.txt')

    with open(text_file_path, 'r') as file:
        names_list = file.read().splitlines()

    randomName = random.choice(names_list)
    return randomName

def chooseFirstName():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    text_file_path = os.path.join(script_dir, 'firstName.txt')

    with open(text_file_path, 'r') as file:
        names_list = file.read().splitlines()

    randomFirstName = random.choice(names_list)
    return randomFirstName




def getNewAlias():

    newName = chooseFirstName() + " " + chooseLastName()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    email_file_path = os.path.join(script_directory, 'email.txt')

    with open(email_file_path, 'r') as file:
        emails = file.read().splitlines()

    if len(emails) == 0:
        print("No emails remaining")
        newEmail = None  # No email available
    else:
        selected_email = random.choice(emails)
        emails.remove(selected_email)

        with open(email_file_path, 'w') as file:
            file.write('\n'.join(emails))

        newEmail = selected_email

    return newName, newEmail




def main():
    while True:
        try:

            # Start browser and loaAudrye Philomenad the initial site
            browser = webdriver.Firefox()
            time.sleep(random.uniform(0,3))
            browser.get("https://wn.nr/WrZ9sGH")
            time.sleep(random.uniform(0,3))

            # Check if the correct site is loaded
            assert "Major Geeks" in browser.title


            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            browser.execute_script("""var otherLabel = document.querySelector("input[value='Other']").parentNode; otherLabel.click();""")
            time.sleep(1.5)
            browser.execute_script("""var continueButton = document.querySelector('button[ng-click="saveEntryDetails(entry_method)"]');if (continueButton) {continueButton.setAttribute('id', 'custom_temp_id');}""")
            browser.find_element(By.ID, "custom_temp_id").click()
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(2)

            newName,newEmail = getNewAlias()
    
            #name
            pyautogui.moveTo(643,850)
            pyautogui.leftClick()
            pyautogui.typewrite(newName)

            time.sleep(random.uniform(0,2))

            #email
            pyautogui.moveTo(643,900)
            pyautogui.leftClick()
            pyautogui.write(newEmail)
            pyperclip.copy("@")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.write("gmail.com")

            time.sleep(random.uniform(0,2))

            #day
            pyautogui.moveTo(545,945)
            pyautogui.leftClick()
            day = str(random.randint(1,30))
            pyautogui.typewrite(day)

            time.sleep(random.uniform(0,2))

            #month
            pyautogui.moveTo(600,945)
            pyautogui.leftClick()
            month = str(random.randint(1,12))
            pyautogui.typewrite(month)

            time.sleep(random.uniform(0,2))

            #year
            pyautogui.moveTo(675,945)
            pyautogui.leftClick()
            year = str(random.randint(1998,2004))
            pyautogui.typewrite(year)

            time.sleep(2.5)
    
            pyautogui.moveTo(600,1050)
            pyautogui.leftClick()

            time.sleep(3.5)
            browser.quit()

        except KeyboardInterrupt:
            ("exited")


if __name__ == '__main__':
    main()