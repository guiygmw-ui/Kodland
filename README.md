# Bot de classificação de aves

Bot do Discord que classifica imagens de aves usando um modelo Keras treinado. O modelo incluído reconhece **pombo** e **pardal**.

## Requisitos

- Python 3.11
- Uma aplicação e um bot criados no [Discord Developer Portal](https://discord.com/developers/applications)
- Acesso à internet para o bot se conectar ao Discord

## Instalação

1. Abra um terminal na pasta do projeto.
2. Instale as dependências listadas no `Pipfile`:

   ```powershell
   pip install pipenv
   pipenv install
   ```

3. No Discord Developer Portal, habilite **Message Content Intent** em **Bot → Privileged Gateway Intents**.
4. Configure o token do bot como variável de ambiente. No PowerShell:

   ```powershell
   $env:DISCORD_TOKEN = "seu-token-do-bot"
   ```

   Não compartilhe nem salve o token no código ou no repositório. Se ele for exposto, redefina-o no Developer Portal.

## Iniciar o bot

No mesmo terminal em que configurou `DISCORD_TOKEN`, execute:

```powershell
pipenv run python bot.py
```

O bot informa no terminal quando estiver conectado. A variável `DISCORD_TOKEN` é obrigatória.

## Comandos

Os comandos usam o prefixo `/` configurado no bot:

| Comando | O que faz |
| --- | --- |
| `/check` | Analisa cada imagem anexada à mensagem e responde com a classe prevista e a confiança. |
| `/hello` | Envia uma mensagem de apresentação. |
| `/heh` | Repete “he” cinco vezes. |

Se não houver imagem em `/check`, o bot pede que o usuário envie uma. Anexos que não forem imagens válidas geram uma mensagem de erro. Quando a confiança da classificação fica abaixo de 60%, o bot informa que não tem certeza.

## Arquivos do projeto

- `bot.py`: comandos, comunicação com o Discord e tratamento de erros.
- `model.py`: preparação da imagem e inferência com Keras.
- `keras_model.h5`: modelo de classificação treinado.
- `labels.txt`: nomes das classes correspondentes às saídas do modelo.
- `Pipfile` e `Pipfile.lock`: dependências e ambiente Python.

O classificador só conhece as classes usadas no treinamento (atualmente, pombo e pardal). O limite de confiança ajuda a sinalizar previsões incertas, mas não substitui um detector de objetos: imagens de objetos irrelevantes ainda podem receber uma dessas classes. A integração com YOLO ou outro detector não faz parte da implementação atual.
