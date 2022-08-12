# enconding: utf-8

  Feature: Items

    Scenario: Lista de items
      Given que estou na tela inicial
      When clico em items no menu superior
      Then devo ser redirecionado para a lista de items

    Scenario: Abrir item selecionado
      Given que estou na tela de items e clico no botão show this item
      Then devo ser direcionado para os detalhes de item

    Scenario: Criar item
      Given que estou na tela de item
      When clico em add item e insiro as informações
      Then devo visualizar o item recém criado

    Scenario: Editar item
      Given que estou na tela de item
      When clico em edit item e insiro as informações para atualizar
      Then ser redirecionado e mostrada a mensagem de sucesso

