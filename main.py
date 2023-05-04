import openai
import config
import typer
from rich import print
from rich.table import Table

openai.api_key = config.api_key

def main(): 

    print("[bold green]ChatGPT API en Python [/bold green]")

    table = Table("Comando","Description")
    table.add_row("exit","Salir de la aplicacion")

    print(table)

#contexto del asistente

messages=[{"role":"system",
           "content":"eres un asistente muy util."}]

while True:
    content = input ("Hola! soy tu asistente virtual, en que te puedo ayudar hoy?")

    if content == "exit":
        break

    messages.append({"role":"user","content":content})
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",messages= messages)
    
    response_content = response.choices[0].message.content

    messages.append({"role": "assistant", "content": response_content})

    print(response_content)

if __name__ == "__main__":
    typer.run(main)


