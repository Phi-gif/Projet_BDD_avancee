#!/bin/env python3

import asyncio

async def handle(reader, writer):
    data = await reader.read(100)
    #print('session ouverte') 
    print(f"réception de : {data.decode()}") 
    
    response = "Je suis le serveur et voici ma reponse"
    writer.write(response.encode()) 
    await writer.drain() 
    print(f"envoi de : {response}")
    #print('fin de session')

    writer.close()

#Serveur
async def main(addr,port):
    server = await asyncio.start_server(handle,addr,port) 

    async with server:
        await server.serve_forever()

if __name__ == '__main__':

    serveur = asyncio.run(main("127.0.0.1",1234))
    