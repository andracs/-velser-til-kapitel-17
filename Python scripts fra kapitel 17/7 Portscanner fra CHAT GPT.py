"""
Her er et eksempel på "prompt engineering".

Jeg har stillet Chat GPT (https://chat.openai.com/chat) følgende spørgsmål i chatprompten:

"Please write a port scanner in python, which scans 18.195.65.114."

Chat GPT har hjulpet mig til at finde frem til følgende kode, sam ganske rigtigt gennemfører opgaven. Den har endda skrevet gode kommentarer også.

Jeg kan godt videreudvikle denne "boilerplate"-kode, så det lever op til min behov.

Kan du finde eksempler på, hvordan "prompt engineering" kan hjælpe din programmeringshverdag?

!!!! OBS !!!!!
Chat GPT (lige som Stackoverflow) kan også give forkerte resultater.
Så du skal ikke stole på resultaterne, men i stedet bør du forholde dig kritisk til dem.
!!!! OBS !!!!!

"""

import socket

target = '18.195.65.114'

def scan_port(port):
    try:
        # Create a new socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout of 1 second to avoid hanging on unresponsive ports
        s.settimeout(1)

        # Attempt to connect to the target on the specified port
        s.connect((target, port))

        # If the connection was successful, print the port number
        print(f'Port {port} is open')

        # Close the socket
        s.close()

    except:
        pass

# Scan ports 1-1000
for port in range(1, 9000):
    scan_port(port)
