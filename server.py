import asyncio
import websockets

async def handle_connection(websocket, path):  # Ensure 'path' is included
    print(f"Client connected from {websocket.remote_address}")

    try:
        async for message in websocket:
            print(f"Received message: {message}")

            # Reverse the message
            reversed_message = message[::-1]

            # Send the reversed message back to the client
            await websocket.send(reversed_message)
            print(f"Sent reversed message: {reversed_message}")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {e}")

    except Exception as e:
        print(f"Unexpected server error: {e}")

async def main():
    # Correctly pass the function reference
    server = await websockets.serve(handle_connection, "localhost", 5001)

    print("WebSocket Server running on ws://localhost:5001")
    await server.wait_closed()

# Run server with proper event loop handling
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        print("RuntimeError: Closing existing event loop and restarting.")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
