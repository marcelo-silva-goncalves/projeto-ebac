# Instalando/importando bibliotecas

import os
from getpass import getpass

username = 'marcelo-silva-goncalves' # insira o seu nome de usuário do github
os.environ['GITHUB_USER'] = username

!git config --global user.name "${GITHUB_USER}"

usermail = getpass() #Insira seu email de login no github
os.environ['GITHUB_MAIL'] = usermail

!git config --global user.email '${GITHUB_MAIL}'

usertoken = getpass() #insira seu user token criado para seu projeto
os.environ['GITHUB_TOKEN'] = usertoken