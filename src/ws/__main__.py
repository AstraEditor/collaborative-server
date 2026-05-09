from src.ws import WebSocketServer

def main():
    server = WebSocketServer()
    server.run()

if __name__ == "__main__":
    main()