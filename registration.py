from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
import pdb

url = "https://firstclass.uslugi.mosreg.ru/summerform"

girl = 'Жен'
boy = 'Муж'

rus = 'Свидетельство о рождении'
alien = 'Свидетельство о рождении иностранного образца'

child_surname = "Тестовый"
child_name = "Ученик"
child_patronym = "Батькович"
child_gender = girl
birth_date = "01.02.2015"
birth_place = "Россия, г. Челябинск"

doc_type = alien
doc_serial =  "II-АБ"
doc_number = "123456"
doc_date = "01.02.2015"
doc_depart_name = "Каким-то ЗАГСом"

region_name = "Ленинский Район"
city_name = "Жуковский Город"
street_name = "Безымянный Проезд"
house_number = "1a"

chrome = webdriver.Chrome()
chrome.get(url)

# keep agree
def keep_agree():
    check = chrome.find_element(By.TAG_NAME, "app-ui-checkbox")
    check.location_once_scrolled_into_view
    #check.execute_script('arguments[0].scrollIntoView(true);', check)
    check.click()
    # go to child info page
    chrome.find_element(By.ID, "next-button").click()

def gender(g):
    value = chrome.find_element(By.XPATH, "//div[@data-name='childGender']")
    if g in value.text:
        return
    elif g == boy:
        #chrome.find_element(By.XPATH, "//mat-select[@required_id = 'id_childGender']").click()
        value.click()
        chrome.find_element(By.ID, "mat-option-1").click()
    elif g == girl:
        #chrome.find_element(By.XPATH, "//mat-select[@required_id = 'id_childGender']").click()
        value.click()
        chrome.find_element(By.ID, "mat-option-2").click()

# set personal info
def personal_info():
    last_name = chrome.find_element(By.ID, "id_childLastName")
    last_name.send_keys(child_surname)

    name = chrome.find_element(By.ID, "id_childFirstName")
    name.send_keys(child_name)

    patronym = chrome.find_element(By.ID, "id_childMiddleName")
    patronym.send_keys(child_patronym)

    gender(child_gender)

    # set birthdate
    birthdate = chrome.find_element(By.ID, "id_childBirthDate")
    birthdate.send_keys(birth_date)

    # set birth place
    birthplace = chrome.find_element(By.ID, "id_childBirthPlace")
    birthplace.send_keys(birth_place)

def birth_document_type():
    value = chrome.find_element(By.XPATH, "//div[@data-name='childDocType']")
    value.location_once_scrolled_into_view
    #pdb.set_trace()
    if doc_type in value.text:
        return
    elif doc_type == rus:
        value.click()
        chrome.find_element(By.ID, "mat-option-4").click()
    elif doc_type == alien:
        value.click()
        chrome.find_element(By.ID, "mat-option-5").click()

def upload_birth():
    birth = chrome.find_element(By.ID, "id_childDocBirth")
    birth.location_once_scrolled_into_view
    birth.send_keys("/home/mike/test.png")

def birth():
    birth_document_type()

    serial = chrome.find_element(By.ID, "id_childDocSeries")
    serial.send_keys(doc_serial)

    number = chrome.find_element(By.ID, "id_childDocNumber")
    number.send_keys(doc_number)

    date = chrome.find_element(By.ID, "id_childDocDateObtain")
    date.send_keys(doc_date)

    depart_name = chrome.find_element(By.ID, "id_childDocSource")
    depart_name.send_keys(doc_depart_name)

    upload_birth()    

def select_list(field_id, search_id, search):
    if search == "":
        return
    field = chrome.find_element_by_id(field_id)
    field.location_once_scrolled_into_view
    field.click()
    search_str = chrome.find_element_by_id(search_id)
    search_str.send_keys(search)
    wait = WebDriverWait(chrome, 3)
    element = wait.until(EC.element_to_be_clickable((By.ID,search_id)))
    element.send_keys(Keys.ENTER)

def region():
    select_list("id_district", "mat-input-7", region_name)

def city():
    select_list("id_city", "mat-input-9", city_name)

def street():
    select_list("id_street", "mat-input-13", street_name)

def house():
    select_list("id_house", "mat-input-17", house_number)

keep_agree()
personal_info()
birth()
region()
city()
street()
house()
pdb.set_trace()
chrome.close()