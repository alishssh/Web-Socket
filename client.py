import asyncio
import websockets

async def connect_to_server():
    uri = "ws://localhost:5001"  # The WebSocket server URI

    async with websockets.connect(uri) as websocket:
        print(f"Connected to the server at {uri}.")
        print("Type your message and press Enter to send it.")
        print("Type 'X' to close the connection and exit.")

        try:
            while True:
                message = input()
                if message.lower() == "x":
                    print("Closing the connection.")
                    break

                # Send the message to the server
                await websocket.send(message)

                # Receive the reversed message from the server
                reversed_message = await websocket.recv()
                print(f"Received reversed message: {reversed_message}")

        except Exception as e:
            print(f"An error occurred: {e}")

# Run the client
asyncio.run(connect_to_server())
