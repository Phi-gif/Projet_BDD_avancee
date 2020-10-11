#!/bin/env python3
import asyncio

#Client
async def send(message,addr,port):
    reader, writer = await asyncio.open_connection(addr,port)

    print(f'envoi de : {message}')
    writer.write(message.encode()) 

    data = await reader.read(5000) 
    print(f'réception de : {data.decode()}') 

    writer.close()

if __name__ == '__main__':
    message = ["où?","qui?","quand?","comment?","Bonsoir!"]
    for i in message:
        client  = asyncio.run(send(i,"127.0.0.1",1234))