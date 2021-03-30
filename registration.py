from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
import pdb
import time

url = "https://firstclass.uslugi.mosreg.ru/summerform"
#url = "https://firstclass.uslugi.mosreg.ru/transfer"
transfer_title = "Выбор образовательной организации, из которой осуществляется перевод"

girl = ' Женский '
boy = ' Мужской '

rus = ' Свидетельство о рождении '
alien = ' Свидетельство о рождении иностранного образца '
birth_doc_path = "/home/mike/test.png"

child_surname = "Тестовый"
child_name = "Ученик"
child_patronym = "Батькович"
child_gender = girl
child_birth_date = "01.02.2015"
child_birth_place = "Россия, г. Челябинск"

doc_type = rus
doc_serial =  "II-АБ"
doc_number = "123456"
doc_date = "01.02.2015"
doc_depart_name = "Каким-то ЗАГСом"

region_name = " Одинцовский Район "
city_name = " Одинцово Город "
street_name = " Белорусская Улица "
house_number = " 13 Дом "
flat_number = "10"

municipal_name = ' Городской округ Одинцовский '
school_name = ' МБОУ Одинцовская лингвистическая гимназия '

mother = " Мать "
father = " Отец "
parent_gender = " Мужской"
parent = father
snils = "18533659198"
#snils = "11963152861"

def select_list(by, selector, search):
    if search == "":
        return
    field = chrome.find_element(by, selector)
    field.location_once_scrolled_into_view

    field.click()
    chrome.find_element(By.XPATH, "//span[text() = '%s']" % search).click()

def check_transfer_form():
    correct = False
    while correct == False:
        try:
            chrome.find_element(By.XPATH, "//div[@group-title = 'Выбор образовательной организации, из которой осуществляется перевод']")
            print("Incorrect form!")
            pdb.set_trace()
            chrome.refresh()
            keep()
        except NoSuchElementException:
            print("Correct form!")
            correct = True

# keep agree
def keep():
    try:
        check = chrome.find_element(By.TAG_NAME, "app-ui-checkbox")
        check.location_once_scrolled_into_view
        check.click()
    # go to child info page
        chrome.find_element(By.ID, "next-button").click()
    except Exception:
        print("eror when keep agree")
        pdb.set_trace()


def gender(selector, g):
    try:
        value = chrome.find_element(By.XPATH, selector)
        pdb.set_trace()
        if g in value.text:
            return
        else:
            select_list(By.XPATH, selector, g)
    except Exception:
        print("eror when set Gender")
        pdb.set_trace()

# set personal info
def personal_info(who):
    if who == 'c':
        id_last_name = "id_childLastName"
        last_name = child_surname
        id_name = "id_childFirstName"
        name = child_name
        id_patronym = "id_childMiddleName"
        patronym = child_patronym
        xpath_gender = "//div[@data-name='childGender']"
        gender = " Мужской "
        id_birth_date = "id_childBirthDate"
        birth_date = child_birth_date
    elif who == 'p':
        id_last_name = "id_parentLastName"
        id_name = "id_parentFirstName"
        id_patronym = "id_parentMiddleName"
        xpath_gender = "//div[@data-name='parentType']"
        gender = " Отец "
        id_birth_date = "id_parentBirthDate"
        birth_date = parent_birth_date
    else:
        print("error type when set personal info")
        pdb.set_trace()
        return

    try:
        chrome.find_element(By.ID, id_last_name).send_keys(last_name)
    except Exception:
        print("eror when set LastName")
        pdb.set_trace()

    try:
        chrome.find_element(By.ID, id_name).send_keys(name)
    except Exception:
        print("eror when set Name")
        pdb.set_trace()

    try:
        chrome.find_element(By.ID, id_patronym).send_keys(patronym)
    except Exception:
        print("eror when set Patronim")
        pdb.set_trace()

    gender(xpath_gender, gender)

    # set birthdate
    try:
        chrome.find_element(By.ID, id_birth_date).send_keys(birth_date)
    except Exception:
        print("eror when set Birthdate")
        pdb.set_trace()

    if who == 'c':
        # set birth place
        try:
            chrome.find_element(By.ID, "id_childBirthPlace").send_keys(birth_place)
        except Exception:
            print("eror when set BirthPlace")
            pdb.set_trace()   
    else:
        gender("//div[@data-name='parentGender']", parent_gender)
        try:
            chrome.find_element(By.ID, "id_parentSnils").send_keys(snils)
        except Exception:
            print("eror when set SNILS")
            pdb.set_trace()

def birth_document_type():
    try:
        value = chrome.find_element(By.XPATH, "//div[@data-name='childDocType']")
        value.location_once_scrolled_into_view
        if doc_type in value.text:
            return
        elif doc_type == rus:
            value.click()
            chrome.find_element(By.ID, "mat-option-4").click()
        elif doc_type == alien:
            value.click()
            chrome.find_element(By.ID, "mat-option-5").click()
    except Exception:
        print("eror when set DocTypeBirth")
        pdb.set_trace()

def upload_birth():
    try:
        birth = chrome.find_element(By.ID, "id_childDocBirth")
        birth.location_once_scrolled_into_view
        birth.send_keys(birth_doc_path)
    except Exception:
        print("eror when upload BirthDoc")
        pdb.set_trace()

def birth():
    birth_document_type()

    try:
        serial = chrome.find_element(By.ID, "id_childDocSeries")
        serial.send_keys(doc_serial)

        number = chrome.find_element(By.ID, "id_childDocNumber")
        number.send_keys(doc_number)

        date = chrome.find_element(By.ID, "id_childDocDateObtain")
        date.send_keys(doc_date)

        depart_name = chrome.find_element(By.ID, "id_childDocSource")
        depart_name.send_keys(doc_depart_name)
    except Exception:
        print("eror when set DocBirth")
        pdb.set_trace()

    upload_birth()    

def region():
    try:
        #select_list(By.ID, "id_district", region_name)
        field = chrome.find_element(By.ID, "id_district")
        field.location_once_scrolled_into_view
        field.click()
        chrome.find_element(By.ID, "mat-input-7").send_keys("Одинцовский")
        time.sleep(1)
        chrome.find_element(By.XPATH, "//span[text() = '%s']" % region_name).click()
    except Exception:
        print("eror when set region")
        pdb.set_trace()

def city():
    try:
        select_list(By.ID, "id_city", city_name)
    except Exception:
        print("eror when set city")
        pdb.set_trace()

def street():
    try:
        select_list(By.ID, "id_street", street_name)
    except Exception:
        print("eror when set street")
        pdb.set_trace()

def house():
    try:
        select_list(By.ID, "id_house", house_number)
    except Exception:
        print("eror when set house")
        pdb.set_trace()

def flat():
    try:
        inp = chrome.find_element(By.ID, "id_regFlat")
        inp.send_keys(flat_number)
    except Exception:
        print("eror when set flat number")
        pdb.set_trace()

def municipal():
    try:
        select_list(By.XPATH, "//div[@data-name = 'munObr']", municipal_name)
    except Exception:
        print("eror when set Municipal place")
        pdb.set_trace()

def school():
    try:
        field = chrome.find_element(By.XPATH, "//div[@data-name = 'selectedSchools']")
        field.location_once_scrolled_into_view
        field.click()
        chrome.find_element(By.XPATH, "//span[text() = '%s']" % school_name).click()
    except Exception:
        print("AHTUNG!!! ERROR WHEN SET SCHOOL!")
        pdb.set_trace()

def year():
    try:
        field = chrome.find_element(By.ID, 'id_schoolYear_fake')
        if field.is_enabled():
            field.send_keys(Keys.CONTROL + "a")
            field.send_keys(Keys.DELETE)
            field.send_keys("2021/2022")
    except Exception:
        print("eror when set year")
        pdb.set_trace()

def school_data():
    municipal()
    school()
    year()

def submit():
    try:
        button = chrome.find_element(By.ID, "next-button")
        if button.is_enabled():
            #button.click()
            print("    Success!     ")
        else:
            pdb.set_trace()
    except Exception:
        print("eror when submit form!")
        pdb.set_trace()

def live():
    region()
    city()
    street()
    house()
    flat() 

def child_form():
    keep()
    check_transfer_form()
    personal_info('c')
    birth()
    region()
    city()
    street()
    house()
    flat()
    school_data()
    submit()

def parent_form():
    personal_info('p')



chrome = webdriver.Chrome()
chrome.set_window_position(0,0)
chrome.set_window_size(700,800)
#pdb.set_trace()
chrome.get(url)
child_form()
pdb.set_trace()
chrome.close()