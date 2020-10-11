#!/bin/env python3

import asyncio
import os.path, time

socket = ("127.0.0.1",1234)
nom_programmeur = "Philippine Renaudin"

async def handle(reader, writer):
    data = await reader.read(100)
    print('session ouverte') 
    print(f"réception de : {data.decode()}") 
    if data.decode() == "où?":
        response = f'{socket}'
    elif data.decode() == "qui?":
        response = nom_programmeur
    elif data.decode() == "quand?":
        response = f'{time.ctime(os.path.getmtime("Q2_serveur.py"))}'
    elif data.decode() =="comment?":
        response = "Voici le code source \n"
        with open('Q2_serveur.py','r') as f:
            for line in f:
                response = response + line
    else : 
        response = "Je n'ai pas compris!"
    writer.write(response.encode()) 
    await writer.drain() 
    print(f"envoi de : {response}")
    print('fin de session')

    writer.close()

#Serveur
async def main(addr,port):
    server = await asyncio.start_server(handle,addr,port) 

    async with server:
        await server.serve_forever()

if __name__ == '__main__':

    serveur = asyncio.run(main("127.0.0.1",1234))
    