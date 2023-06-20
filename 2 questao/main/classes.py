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

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

    def sair(self):
        sleep(3)
        self.driver.quit()

class TestaPagCadastro(Base):
    def testaFormCadastro(self):
        self.scroll()
        self.clickElement(self.SINGUPBUTTON)
        email = self.find(self.INPUTEMAIL)
        senha = self.find(self.INPUTSENHA)
        confirmSenha = self.find(self.INPUTCONFIRMARSENHA)
        
        email.send_keys('testacont')
        self.scroll()
        self.clickElement(self.SINGUPBUTTON)
        email.send_keys('@gmail.com')
        senha.send_keys('12345678')
        confirmSenha.send_keys('12345678')
        self.scroll()
        self.clickElement(self.SINGUPBUTTON)
        self.clickElement(self.TERMSOFUSEBUTTON)
        email.clear()
        senha.clear()
        confirmSenha.clear()
        self.clickElement(self.TERMSOFUSEBUTTON)
    
    def senhaDiferente(self):
        email = self.find(self.INPUTEMAIL)
        senha = self.find(self.INPUTSENHA)
        confirmSenha = self.find(self.INPUTCONFIRMARSENHA)

        email.send_keys('testacontu@gmail.com')
        senha.send_keys('1234')
        confirmSenha.send_keys('1233')
        self.scroll()
        self.clickElement(self.TERMSOFUSEBUTTON)
        self.clickElement(self.SINGUPBUTTON)
        assert 'Campos de senha estão diferentes.' in self.find(self.WRONGPASSTEXT).text 
        email.clear()
        senha.clear()
        confirmSenha.clear()
        self.clickElement(self.TERMSOFUSEBUTTON)
    
    def testaEmailRepetido(self):
        email = self.find(self.INPUTEMAIL)
        senha = self.find(self.INPUTSENHA)
        confirmSenha = self.find(self.INPUTCONFIRMARSENHA)

        email.send_keys('joao15@gmail.com')
        senha.send_keys('1234')
        confirmSenha.send_keys('1234')
        self.scroll()
        self.clickElement(self.TERMSOFUSEBUTTON)
        self.clickElement(self.SINGUPBUTTON)
        assert 'E-mail já esta em uso.' in self.find(self.WRONGPASSTEXT).text 
        email.clear()
        senha.clear()
        confirmSenha.clear()
        self.clickElement(self.TERMSOFUSEBUTTON)

class Cadastro(TestaPagCadastro):
    def inHomePage(self):
        assert self.driver.title == "Organizze: Controle as suas finanças pessoais"
        self.clickElement(self.COMECEJABUTTON)
        
    def insertCadastro(self, email, senha):
        self.wait.until(ec.presence_of_element_located(self.INPUTEMAIL), 'não encontrei o input de email')
        self.sendKeys(self.INPUTEMAIL, email)
        self.sendKeys(self.INPUTSENHA, senha)
        self.sendKeys(self.INPUTCONFIRMARSENHA, senha)
        self.scroll()
        self.clickElement(self.TERMSOFUSEBUTTON)
        self.clickElement(self.SINGUPBUTTON)
    
    def insertNome(self):
        self.wait.until(ec.presence_of_element_located(self.INPUTNAME), 'não encontrei o input de nome')
        self.sendKeys(self.INPUTNAME, self.NOME)
        self.find(self.FORMWELCOME).submit()
        
    def insertMeta(self):
        self.clickElement(self.METABUTTON)
        self.find(self.FORMOBJECTIVES).submit()
    
    def skipIntroducao(self):
        self.clickElement(self.INTROBUTTON)
        sleep(0.2)
        self.clickElement(self.INTROBUTTON)
        sleep(0.2)
        self.clickElement(self.INTROENDBUTTON)
    
    def inMainPage(self):
        self.wait.until(ec.url_contains('inicio'), 'não está na pagina inicial do usuário')
        assert "inicio" in self.driver.current_url 
    