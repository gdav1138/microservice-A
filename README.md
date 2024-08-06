# microservice-A

Communication Contract:

**Install zmq package and requests package in python**

1. Ensure server.py is running.
2. Send quote request via zeroMQ
    a. server connection must match!
       port: int = 6969
       context = zmq.Context()
    b. request received via socket.send() command on main program
    c. quote grabbed via request.get("http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5")
    d. assign quote to quote_of_the_day variable
3. quote_of_the_day sent back to main program via socket.send_string(quote_of_the_day)

Example Call:

  ZeroMQ setup:
  def server(ip: str = 'localhost', port: int = 6969):
    context = zmq.Context()
    svc_string = "**SERVER**"
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{ip}:{port}")
    print(f"{svc_string}: Connecting to tcp://{ip}:{port}")

  Receive Request:
  message = socket.recv().decode('utf-8')
        print(f"{svc_string}: message from client - {message}")

  Load quote and send:
  response = requests.get("http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5")
        data = response.json()

        quote_of_the_day = data['thought']["quote"]
        socket.send_string(quote_of_the_day)

        ![image](https://github.com/user-attachments/assets/9716057b-0cb8-458a-afeb-61af30e1af70)

