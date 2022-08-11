# enconding: utf-8

  Feature: Items

    Scenario: Lista de items
      Given que estou na tela inicial
      When clico em items no menu superior
      Then devo ser redirecionado para a lista de items

    Scenario: Abrir lista selecionado
      Given que estou na tela de lista
      When clico no botão show this item
      Then devo ser direcionado para os detalhes de item