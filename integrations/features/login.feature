# enconding: utf-8

Feature: Criar conta

  Scenario: Acesso a tela de login
    Given que entro no site
    Then devo visualizar a tela de login

  Scenario: Fazer cadastro na plataforma
    Given que clico no botão de signup
    When insiro os dados para o cadastro e clico em login
    Then devo ser direcionado para a tela principal

  Scenario: Login com email incorreta
    Given que entro no site
    Then devo visualizar a tela de login
    When preencho as informações de login com o email incorreto
    Then devo visualizar uma notificação de email ou senha incorreta

  Scenario: Login com senha incorreta
    Given que entro no site
    Then devo visualizar a tela de login
    When preencho as informações de login com a senha incorreta
    Then devo visualizar uma notificação de email ou senha incorreta

  Scenario: Esqueci a senha
    Given que estou na tela de login
    When clico em "Forgot your password?"
    When insiro o email e aperto a tecla "enter"
    Then devo ver a mensagem "sent to registered email"

  Scenario: Acesso a conta
    Given que estou na tela de login
    When preencho os dados
    Then devo ser direcionado para a tela inicial

  Scenario: Logout
    Given que estou na tela de login
    When preencho os dados
    Then devo ser direcionado para a tela inicial
    When clico em logout
    Then devo ver uma mensagem de logout e ser desconectado da conta