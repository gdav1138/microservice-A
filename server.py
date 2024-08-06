import zmq
import requests

## Quote of the day - url "https://quotes.rest/qod?language=en"

def server(ip: str = 'localhost', port: int = 6969):
    context = zmq.Context()
    svc_string = "**SERVER**"
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{ip}:{port}")
    print(f"{svc_string}: Connecting to tcp://{ip}:{port}")

    while True:
        message = socket.recv().decode('utf-8')
        print(f"{svc_string}: message from client - {message}")

        # **** add your server logic here ****
        response = requests.get("http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5")
        data = response.json()

        quote_of_the_day = data['thought']["quote"]
        socket.send_string(quote_of_the_day)
        # **** add your server logic here ^^^^ ****
        # send_message = response.encode('utf-8')
        new_message = f"{svc_string}: sending response to client - '{response}'"
        print(new_message)
        # socket.send(send_message)

if __name__ == '__main__':
    server()
