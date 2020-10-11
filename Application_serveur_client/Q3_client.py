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
    message = ["où?","qui?","quand?"]
    for number in range(161,184):
        for i in message:
            client  = asyncio.run(send(i,f"192.168.123.{number}",1234))