from behave import *
import sys
sys.path.insert(0,"..")
from main.classes import *

bot = Cadastro()
EMAIL = 'jppn3@gmail.com'
SENHA = '12345678'

@given(u'que estou na página de cadastro')
def impl(context):
    bot.acessarUrl()
    bot.inHomePage()
    bot.waitForUrlBe(bot.CADASTROURL, 'não está na página de cadastro')

@when(u'testar os campos do form e depois apaga-los')
def impl(context):
    bot.testaFormCadastro()
    bot.senhaDiferente()
    bot.testaEmailRepetido()

@when(u'inserir meu login/senha e aceitar os termos e enviar')
def impl(context):
    bot.insertCadastro(EMAIL, SENHA)

@then(u'devo ter cadastrado aquela conta e estar em outra página')
def impl(context):
    ...

@given(u'que devo estar na página de bem vindo')
def impl(context):
    bot.waitForUrlBe(bot.BEMVINDOURL, 'não está na página de bem vindo')

@when(u'inserir meu nome e clicar no botão de enviar')
def impl(context):
    bot.insertNome()

@then(u'devo estar na página de objetivos')
def impl(context):
    bot.waitForUrlBe(bot.OBJECTIVESURL, 'não está na página de objetivos')

@when(u'clicar no meu objetivo e clicar no botão de enviar')
def impl(context):
    bot.insertMeta()
    
@then(u'devo estar na página de introdução')
def impl(context):
    bot.waitForUrlBe(bot.INTROURL, 'não está na página de introdução')

@when(u'clicar nos botões de pular')
def impl(context):
    bot.skipIntroducao()

@then(u'devo estar na página pricipal do usuário')
def impl(context):
    bot.inMainPage()
    bot.sair()