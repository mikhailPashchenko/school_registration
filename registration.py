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

rus = ' Свидетельство о рождении '
alien = ' Свидетельство о рождении иностранного образца '

child_surname = "Тестовый"
child_name = "Ученик"
child_patronym = "Батькович"
child_gender = girl
birth_date = "01.02.2015"
birth_place = "Россия, г. Челябинск"

doc_type = rus
doc_serial =  "II-АБ"
doc_number = "123456"
doc_date = "01.02.2015"
doc_depart_name = "Каким-то ЗАГСом"

region_name = ""
city_name = " Жуковский Город "
street_name = " Безымянный Проезд "
house_number = " 1а Дом "
flat_number = "10"

municipal_name = ' Городской округ Одинцовский '
school_name = ' МБОУ Одинцовская лингвистическая гимназия '

chrome = webdriver.Chrome()
chrome.get(url)

# keep agree
def keep_agree():
    check = chrome.find_element(By.TAG_NAME, "app-ui-checkbox")
    check.location_once_scrolled_into_view
    check.click()
    # go to child info page
    chrome.find_element(By.ID, "next-button").click()

def gender(g):
    value = chrome.find_element(By.XPATH, "//div[@data-name='childGender']")
    if g in value.text:
        return
    elif g == boy:
        value.click()
        chrome.find_element(By.ID, "mat-option-1").click()
    elif g == girl:
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

def select_list(by, selector, search):
    if search == "":
        return

    field = chrome.find_element(by, selector)
    field.location_once_scrolled_into_view
    field.click()
    chrome.find_element(By.XPATH, "//span[text() = '%s']" % search).click()

def region():
    select_list(By.ID, "id_district", region_name)

def city():
    select_list(By.ID, "id_city", city_name)

def street():
    select_list(By.ID, "id_street", street_name)

def house():
    select_list(By.ID, "id_house", house_number)

def flat():
    inp = chrome.find_element(By.ID, "id_regFlat")
    inp.send_keys(flat_number)

def municipal():
    select_list(By.XPATH, "//div[@data-name = 'munObr']", municipal_name)
    #field = chrome.find_element(By.XPATH, "//div[@data-name = 'munObr']")
    #field.location_once_scrolled_into_view
    #field.click()
    #chrome.find_element(By.XPATH, "//span[text() = '%s']" % municipal_name).click()

def school():
    field = chrome.find_element(By.XPATH, "//div[@data-name = 'selectedSchools']")
    field.location_once_scrolled_into_view
    field.click()
    chrome.find_element(By.XPATH, "//span[text() = '%s']" % school_name).click()

def year():
    field = chrome.find_element(By.ID, 'id_schoolYear_fake')
    if field.is_enabled():
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys("2021/2022")

def school_data():
    municipal()
    school()
    year()

def submit():
    but = chrome.find_element(By.ID, "next-button")
    if but.is_enabled():
        #but.click()
        print("    Success!     ")
    else:
        pdb.set_trace()

keep_agree()
personal_info()
birth()
region()
city()
street()
house()
flat()
school_data()
submit()
pdb.set_trace()
chrome.close()