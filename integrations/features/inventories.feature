# enconding: utf-8

  Feature: Inventories

    Scenario: Abrir lista de inventários
      Given que realizo o login
      When clico em inventaries do menu superior
      Then devo ver a lista de inventários

    Scenario: Criar um inventario
      #Given que realizo o login
       When clico em inventaries do menu superior
       Then devo ver a lista de inventários
       When clico em show this inventory
       Then devo visualizar o inventário

     Scenario: Editar inventario
       Given que realizo o login
       When clico em inventaries do menu superior
       Then devo ver a lista de inventários
       When clico em show this inventory
       Then devo visualizar o inventário
       When clicar em edit this inventory
       When preencho o formulario e clico em edit
       Then devo visualizar a mensagem de que foi editado com sucesso

     Scenario: Apagar inventario
       Given que realizo o login
       When clico em inventaries do menu superior
       Then devo ver a lista de inventários
       When clico em show this inventory
       Then devo visualizar o inventário
       When clico em destroy this inventory
       Then devo visualizar a mensagem de inventário destruido
