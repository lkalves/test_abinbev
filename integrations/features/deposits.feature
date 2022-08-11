# enconding: utf-8

  Feature: Depositos

    Scenario: Lista de depositos
      Given que estou na tela inicial
      When clico em deposits no menu superior
      Then devo ser redirecionado para a lista de depositos

    Scenario: Abrir deposito selecionado
      Given que estou na tela de depositos
      When clico no botão show this deposit
      Then devo ser direcionado para os detalhes do deposito

    Scenario: Editar deposito
      Given que estou na tela de detalhes do deposito
      When clico no botao de edit this deposit e insiro as informações que desejo trocar e clico em update
      Then devo ver a mensagem de Deposit was successfully updated e as informações trocadas

    Scenario: Destroir deposito
      Given que estou na tela de deposito e abro um deposito para destroir
      When clico em destruir deposito
      Then devo ver que o deposito foi excluido