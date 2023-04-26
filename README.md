# InstaBot.py

O InstaBot.py é um programa que utiliza a biblioteca Selenium para realizar comentários nas últimas publicações de perfis de sua escolha no Instagram.

## Pré-requisitos

- Python 3.x instalado em sua máquina
- Biblioteca Selenium instalada (`pip install selenium`)
- Biblioteca webdriver_manager instalada (`pip install webdriver_manager`)
- Biblioteca pyvirtualdisplay instalada (opcional - necessário apenas para execução em servidor Linux, `pip install pyvirtualdisplay`)

## Como usar

1. Clone o repositório em sua máquina:

```
git clone https://github.com/seuusuario/InstaBot.git
```

2. Acesse a pasta do repositório:

```
cd InstaBot
```

3. Edite o arquivo `instabot.py` e configure as variáveis `comments_text` e `profiles` de acordo com suas preferências. Na variável `comments_text` você deve inserir os comentários que deseja fazer, e na variável `profiles` você deve inserir os perfis que deseja comentar.

4. Na função `main_loop`, insira seu usuário e senha nos parâmetros da função `bot.login()`:

```
bot.login('seu_usuario', 'sua_senha')
```

5. Execute o programa através do comando:

```
python3 instabot.py
```

O programa irá abrir o navegador automaticamente e fazer login em sua conta do Instagram. Em seguida, irá acessar os perfis configurados na variável `profiles` e fazer comentários nas últimas publicações.

## Observações

- O programa utiliza a biblioteca webdriver_manager para gerenciar o driver do navegador. Isso significa que não é necessário baixar e instalar o driver manualmente. O webdriver_manager irá buscar e baixar a versão correta do driver automaticamente de acordo com o navegador instalado em sua máquina.
- É importante lembrar que o Instagram pode bloquear o acesso de contas que realizam atividades suspeitas, como comentar muitas publicações em um curto período de tempo. Use o programa com moderação para evitar problemas com sua conta.
