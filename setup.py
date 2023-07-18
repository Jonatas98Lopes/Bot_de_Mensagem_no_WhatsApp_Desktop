# ESTE ARQUIVO DEVE SER USADO PARA GERAR O EXECUTÁVEL DO PROGRAMA.

import sys
import os
from cx_Freeze import setup, Executable


settings = Executable(
    script='app.py',
    icon='assets\\icone.ico',
)

setup(
    name='Bot de Mensagens no WhatsApp Desktop',
    version='1.0',
    description='Com este software, você pode enviar uma mensagem padrão para vários contatos de forma automatizada.',
    author='Jonatas Lopes de Sousa',
    options= {'build_exe': {
        'include_msvcr': True
    }},
    executables=[settings]
    )