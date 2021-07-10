# Conversor de texto em voz
Um simples conversor texto em voz feito usando a biblioteca pyttsx3 do python.

## Requisitos
Ter o pyttsx3 instalado
```md
pip install pyttsx3
```

## Como usar no Linux
3 maneiras:
  1. Colocar o texto que vai ser lido em `txt.txt`.
  2. alterar a variavel `texto = file.read()` e no lugar de `file.read()` adicionar algum texto.
  3. alterar o caminho do`file = open('./txt.txt', 'r', encoding='utf8')` e no lugar do `'./txt.txt'` colocar o caminho do seu arquivo de texto.

## Como usar no Windows
Além dos passos listados acima alterar o: 
```py
for voice in voices:
    if voice == 'brazil':
        speaker.setProperty('voice', voice.id)
```
Apagar e deixar assim:
```py
speaker.setProperty('voice', voices[2].id)
```
Para ver as vozes do sistema use:
```py
for voice in voices:
    print(voice.id)
```
E ele retornara uma lista com as vozes do sistema Windows. Escolha pela o indece e mude o numero do `voices[2].id`.


