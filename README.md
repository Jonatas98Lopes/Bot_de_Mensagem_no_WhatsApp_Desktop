# Bot de Mensagem no WhatsApp Desktop

## Descrição:

O objetivo desse projeto é automatizar o processo de envio de mensagens no aplicativo do WhatsApp para computador. A ideia é que o usuário forneça uma mensagem que deseja enviar, assim como a lista de contatos.

Assista ao vídeo de funcionamento do projeto [clicando aqui!](https://www.linkedin.com/feed/update/urn:li:activity:7086850269812056065/)

***

## Requisitos:

* Ter o Python 3 instalado no seu computador. De preferência, na versão 3.11.

* Ter habilitado a opção **Add to Path** na hora da instalação do Python.

* Possuir o aplicativo do WhatsApp para computador instalado. **NÃO** É O WHATSAPP WEB.

* Possuir um navegador de internet. É bem provável que aplicação funcione em outros navegadores como: Firefox, Microsoft Edge, Opera, Safari, porém, a aplicação foi desenvolvida no Google Chrome, portanto, dê preferência para rodar o programa nele. 

Obs: Para fazer com que a aplicação rode num navegador específico, você deve definir o mesmo como seu navegador padrão. No Windows, por exemplo, você pode alterar isso em **Aplicativos padrão**.

* Possuir uma resolução de tela de **1366 x 766**. É possível alterar essas configurações no seu sistema operacional. No Windows, por exemplo, procure por **Configurações de exibição**.

* Quando for rodar o projeto, feche todos os outros programas e desabilite as notificações no seu sistema operacional.

***

## Algoritmo do Projeto:

* Obter a mensagem a enviar.

* Obter os números dos contatos:.

PARA CADA CONTATO, DEVEMOS FAZER O SEGUINTE:

   * Abrir o navegador.

   * Acessar o site: https://api.whatsapp.com/send?phone=NUMERODOCONTATO

   * Clicar em "Abrir" - O WhatsApp Desktop.
	
   * Selecionar a barra de mensagem.

   * Escrever a mensagem.
	
   * Clicar para enviar a mensagem.

   * Pausar a operação por alguns segundos.

   * Fechar a janela aberta no navegador.

DEPOIS DE ENVIAR A MENSAGEM PARA TODOS OS CONTATOS, DEVEMOS:

* Fechar o WhatsApp Desktop.

* Informar o usuário que o programa foi encerrado.

***

## Como rodar o projeto?

Assim que clonar este código, sugiro que você crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.

### Criando ambiente virtual com Python:

1. Clone o projeto.

2. Estando dentro da pasta do projeto, abra o seu terminal.

CASO ESTEJA NO **WINDOWS**, RODE O COMANDO ABAIXO E AGUARDE A CRIAÇÃO:

```
python -m venv nome_do_ambiente_virtual
```

**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

CASO ESTEJA NO LINUX OU NO MAC, RODE O COMANDO ABAIXO E A AGUARDE A CRIAÇÃO:

```
python3 -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

3. Ative o ambiente virtual através do seu terminal:

NO CASO DO **WINDOWS**, RODE:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

NO CASO DO **LINUX** OU **MAC**, RODE:

```
source nome_do_ambiente_virtual\bin\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

***

### Instalando bibliotecas necessárias:

Feito isso, vamos instalar as bibliotecas necessárias através do arquivo requirements.txt:
No **Windows**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```
No **Linux** ou **MAC**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip3 install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.

**LEMBRE-SE DE FECHAR TODOS PROGRAMAS E DESABILITAR AS NOTIFICAÇÕES ANTES DE RODAR O PROGRAMA!**

***

### Possíveis problemas:

Caso, você tenha uma tela de tamanho diferente, você deve alterar as linhas do arquivo **app.py** que estão sob o seguinte comentário: **# Depende do tamanho da sua tela**.

O projeto foi desenvolvido em ambiente Windows, e, com comandos para pressionar as teclas de um teclado Windows ou Linux possívelmente. Ou seja, é possível que num Mac as teclas não sejam pressionadas corretamente.

***

### Gerando executável:

Caso você queira um executável do projeto. Você deve ter executado as etapas anteriores. - ATÉ A PARTE DE INSTALAR AS BIBLIOTECAS DO ARQUIVOS requirements.txt.

Feito isso, você deve estar com o seu ambiente virtual ativador e abrir o seu terminal na pasta raiz do projeto.

Estando lá, digite o seguinte comando

NO **WINDOWS**:
```
python setup.py build
```

NO **LINUX** OU NO **MAC**:
```
python3 setup.py build
```

Uma pasta **build**, com um arquivo **app** deve ser gerado.
O ARQUIVO **app** será o seu executável.