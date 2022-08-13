# Test Manual/Automation QA - BEES SAAS

### Fork this repo and follow the instructions bellow for the test 
<BR>

### Business Rules

<br>

We developed a application that will help us to manage our inventory, deposits and items. Feel free to register your account and start using our application.
Take your time to play around on the application's UI and API to get familiar with the system.

For this test you will have to create a test automation project or manual tests cases, try to test as
many scenarios as possible.


<br>
Links:

* Applicattion link - https://test-bees.herokuapp.com
* API Docs - https://test-bees.herokuapp.com/api-docs/index.html 

<BR>

### Technical Requirements for Automation
- Test both UI and API 
- Use page object pattern or relative patterns of your preference.
- Use BDD for any scenario you want to do
- You can choose any programming language, we recommend to you use Python 3.6+,  *BUT IT'S UP TO YOU*
- Please follow code style for your choose language (example: PEP's for python).
- Describe how to run your code in README.MD
- Please generate a report of your tests results

### Technical Requirements for Manual
- Test both UI and API
- Documented all tests cases you created
- For api tests you can use any framework you want, but we recommend to use Postman
- Generate a report with evidences of the tests results

# **Automatização**

Para instalar os pacotes necessários deverá ser feito a instalação do arquivo `pip install -r requirements.txt`
Para os testes será necessário ter o **`edgedriver`** já instalado nas variáveis de ambiente. 
Caso contrario será necessário apontar no arquivo `environment.py` dentro da função  `browser_edge`. Caso queira utilizar outro navegador é 
possível chamando no import o navegador necessário e passando ele como na variável abaixo apontando o caminho do webdriver.
 **[```context.browser = Edge(executable_path=r'E:/DEV/Driver/edgedriver.exe')```]**


#### Os webdrivers podem ser baixados no site abaixo:
- Chrome: https://chromedriver.chromium.org/downloads
- Firefox: https://github.com/mozilla/geckodriver/releases
- Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Existem para vários outros navegadores


### Rodando os testes:
#### Comandos:
- `behave .\integrations\features\ `
