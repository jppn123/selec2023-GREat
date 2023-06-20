from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class PageBemVindo():
    BEMVINDOURL = 'https://app.organizze.com.br/seja-bem-vindo'
    FORMWELCOME = (By.ID, 'seja-bem-vindo-form')
    INPUTNAME = (By.NAME, 'name')
    
class PageObjectives():
    OBJECTIVESURL = 'https://app.organizze.com.br/meus-objetivos'   
    FORMOBJECTIVES = (By.ID, 'meus-objetivos-form')
    METABUTTON = (By.XPATH, '//div/form/label[2]')
    
class PageIntro():
    INTROURL = 'https://app.organizze.com.br/introducao'
    INTROBUTTON = (By.ID, 'introducao-next-button')
    INTROENDBUTTON = (By.ID, 'introducao-end-button')

class PageCadastro():
    CADASTROURL = 'https://auth.organizze.com.br/cadastro'
    INPUTEMAIL = (By.ID, 'email')
    INPUTSENHA = (By.ID, 'password')
    INPUTCONFIRMARSENHA = (By.ID, 'repeatPassword')
    TERMSOFUSEBUTTON = (By.ID, 'termsOfuse')
    FORMSINGUP = (By.ID, 'signUp')
    SINGUPBUTTON = (By.XPATH, '//section/div/form/button')
    WRONGPASSTEXT = (By.XPATH, '//div/div[3]/span')
    
class Locators(PageBemVindo, PageObjectives, PageIntro, PageCadastro):
    URL = 'https://www.organizze.com.br'
    NOME = 'joão'
    COMECEJABUTTON = (By.XPATH, "//div/div[3]/a[2]")
    
     

    
    
    

