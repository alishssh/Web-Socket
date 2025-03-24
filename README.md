**Documentation**

Creating a simple web socket where client send some string and server reverse it.

**TechStack**

Backend (Flask)

**ProjectStructure**

/SMTMINTERN/Task7/Web Socket

│           | ├── client.py

│           |├── server.py        

**Step-By-StepImplementation**

**Client.py**

import asyncio

import websockets

async def connect\_to\_server():

    uri ="ws://localhost:5001"  # TheWebSocket server URI

    async withwebsockets.connect(uri) as websocket:

       print(f"Connected to the server at {uri}.")

        print("Type your message and pressEnter to send it.")

        print("Type'X' to close the connection and exit.")

        try:

            while True:

                message= input()

                ifmessage.lower() == "x":

                    print("Closingthe connection.")

                   break

                # Sendthe message to the server

                awaitwebsocket.send(message)

                #Receive the reversed message from the server

               reversed\_message = await websocket.recv()

               print(f"Received reversed message: {reversed\_message}")

        except Exceptionas e:

           print(f"An error occurred: {e}")

**Server.py**

import asyncio

import websockets

async def handle\_connection(websocket, path):  # Ensure 'path' is included

    print(f"Clientconnected from {websocket.remote\_address}")

    try:

        async formessage in websocket:

           print(f"Received message: {message}")

            # Reversethe message

           reversed\_message = message\[::-1\]

            # Send thereversed message back to the client

            awaitwebsocket.send(reversed\_message)

           print(f"Sent reversed message: {reversed\_message}")

    exceptwebsockets.exceptions.ConnectionClosed as e:

       print(f"Client disconnected: {e}")

    except Exception ase:

       print(f"Unexpected server error: {e}")

async def main():

    # Correctly pass thefunction reference

    server = await websockets.serve(handle\_connection,"localhost", 5001)

   print("WebSocket Server running on ws://localhost:5001")

    awaitserver.wait\_closed()

\# Run server with proper event loop handling

if \_\_name\_\_ == "\_\_main\_\_":

    try:

       asyncio.run(main())

    except RuntimeError:

       print("RuntimeError: Closing existing event loop andrestarting.")

        loop =asyncio.new\_event\_loop()

       asyncio.set\_event\_loop(loop)

       loop.run\_until\_complete(main())

**\# Run the client.py and Server.py in a different dedicated terminal**

**Output:**

![Image](https://github.com/user-attachments/assets/78d28229-0a5f-4c81-9b6d-bc29cfe52049)


![image](https://github.com/user-attachments/assets/0e72d6cf-0b0f-42d4-abf5-f7065c2e56e2)


**Conclusion:**

This documentation helps users to understand how a web socket works on client andserver setting or environment.
