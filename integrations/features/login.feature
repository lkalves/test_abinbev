# enconding: utf-8

Feature: Criar conta

  Scenario: Acesso a tela de login
    Given que entro no site
    Then devo visualizar a tela de login

  Scenario: Fazer cadastro na plataforma
    Given que clico no botão de signup
    When insiro os dados para o cadastro e clico em login
    Then devo ser direcionado para a tela principal

  Scenario: Acesso a conta
    Given que estou na tela de login
    When preencho os dados
    Then devo ser direcionado para a tela inicial

