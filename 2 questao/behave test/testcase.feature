#language: pt

Funcionalidade: Fazer cadastro no site Organizze

Cenário: Preencher o formulário de cadastro
    Dado que estou na página de cadastro
    Quando inserir meu login/senha e aceitar os termos e enviar
    Então devo ter cadastrado aquela conta e estar em outra página

Cenário: Preencher os requisitos para entrar na página principal
    Dado que devo estar na página de bem vindo
    Quando inserir meu nome e clicar no botão de enviar
    Então devo estar na página de objetivos

    Quando clicar no meu objetivo e clicar no botão de enviar
    Então devo estar na página de introdução

    Quando clicar nos botões de pular
    Então devo estar na página pricipal do usuário