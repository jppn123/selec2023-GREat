from .utils import *

class Base(Locators):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 20)
    
    def acessarUrl(self):
        self.driver.get("https://www.organizze.com.br")
        self.driver.maximize_window()
    
    def find(self, elemento):
        sleep(1)
        return self.driver.find_element(*elemento)
    
    def sendKeys(self, elemento, key):
        self.find(elemento).send_keys(*key)
    
    def clickElement(self, elemento):
        self.wait.until(
            lambda  Driver: Driver.find_element(*elemento),
            'não encontrei o elemento'
        ).click()
    
    def waitForUrlBe(self, url, errorText):
        self.wait.until(ec.url_to_be(url), errorText)
        assert self.driver.current_url == url

    def sair(self):
        sleep(3)
        self.driver.quit()
         
class Cadastro(Base):
    def in_page(self):
        assert self.driver.title == "Organizze: Controle as suas finanças pessoais"
        self.clickElement(self.COMECEJABUTTON)
        
    def insertCadastro(self):
        # self.wait.until(ec.url_to_be(self.CADASTROURL), 'não está na pagina de cadastro')
        # assert self.driver.current_url == self.CADASTROURL
        self.wait.until(ec.presence_of_element_located(self.INPUTEMAIL), 'não encontrei o input de email')
        self.sendKeys(self.INPUTEMAIL, self.EMAIL)
        self.sendKeys(self.INPUTSENHA, self.SENHA)
        self.sendKeys(self.INPUTCONFIRMARSENHA, self.SENHA)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        self.clickElement(self.TERMSOFUSEBUTTON)
        self.find(self.FORMSINGUP).submit()
    
    def insertNome(self):
        # self.wait.until(ec.url_to_be(self.BEMVINDOURL), 'não está na pagina de bem vindo')
        # assert self.driver.current_url == self.BEMVINDOURL
        self.wait.until(ec.presence_of_element_located(self.INPUTNAME), 'não encontrei o input de nome')
        self.sendKeys(self.INPUTNAME, self.NOME)
        self.find(self.FORMWELCOME).submit()
        
    def insertMeta(self):
        # self.wait.until(ec.url_to_be(self.OBJECTIVESURL), 'não está na pagina de objetivos')
        # assert self.driver.current_url == self.OBJECTIVESURL
        self.clickElement(self.METABUTTON)
        self.find(self.FORMOBJECTIVES).submit()
    
    def skipIntroducao(self):
        # self.wait.until(ec.url_to_be(self.INTROURL), 'não está na pagina de introdução')
        # assert self.driver.current_url == self.INTROURL
        self.clickElement(self.INTROBUTTON)
        sleep(0.2)
        self.clickElement(self.INTROBUTTON)
        sleep(0.2)
        self.clickElement(self.INTROENDBUTTON)
    
    def inMainPage(self):
        self.wait.until(ec.url_contains('inicio'), 'não está na pagina inicial do usuário')
        assert "inicio" in self.driver.current_url 
    