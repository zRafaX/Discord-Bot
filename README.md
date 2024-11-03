# Discord Bot em Python

Este é um bot para Discord feito em Python. Ele utiliza a biblioteca `discord.py` para facilitar a criação e organização de comandos. A estrutura é organizada em *cogs*, o que permite que novos comandos e funcionalidades sejam adicionados facilmente.

## Estrutura do Projeto

- **main.py**: Arquivo principal que inicia o bot e carrega as *cogs*.
- **requirements.txt**: Lista de dependências necessárias para rodar o bot.
- **cogs/comandos.py**: Arquivo onde ficam os comandos do bot organizados como uma *cog*.

## Pré-requisitos

1. **Python 3.8 ou superior**: Certifique-se de que o Python está instalado no sistema.
2. **Biblioteca `discord.py`**: O bot utiliza `discord.py` para interação com a API do Discord.

```bash
pip install -r requirements.txt

python main.py
