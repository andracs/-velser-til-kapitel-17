# Python-eksempler fra bogen "Linux basics for hackers", kapitel 17

Ordlisten er fra [dette link](https://github.com/berzerk0/Probable-Wordlists/blob/master/Real-Passwords/Top12Thousand-probable-v2.txt), fra artiklen __["Her er de 12.000 mest brugte passwords: Se om dit også er på listen"](https://www.computerworld.dk/art/244437/her-er-de-12-000-mest-brugte-passwords-se-om-dit-ogsaa-er-paa-listen)__

## Demoserver
Vi brugere denne server til vores forsøg:

```
18.195.65.114
```

:warning: **OBS!** András skal tænde for serveren for at øvelserne virker. 

## Prompt engineering

Her er et eksempel på "prompt engineering": Jeg har stillet Chat GPT (https://chat.openai.com/chat) følgende spørgsmål i chatprompten:

__"Please write a port scanner in python, which scans 18.195.65.114."__

Chat GPT har hjulpet mig til at finde frem til nednestående kode, sam ganske rigtigt gennemfører opgaven. Den har endda skrevet gode kommentarer også.

Vi kan godt videreudvikle denne "boilerplate"-kode, så det lever op til vores behov.

Kan du finde eksempler på, hvordan "prompt engineering" kan hjælpe din programmeringshverdag? 

__!!!! OBS !!!!!__ Chat GPT (lige som Stackoverflow) kan også give forkerte resultater. 
Så du skal ikke stole på resultaterne, men i stedet bør du forholde dig kritisk til dem.  

```
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
    scan_port(port)`

```

# Rìgtige besvarelser

```
Port 21 er VSftpd
Port 22 er SSH 
Port 25 er Zealandbanner
Port 80 er Apache Webserver
Port 111 er NFS
Port 180 er Zealandbanner
Port 554 er Zealandbanner
Port 1723 er Zealandbanner
Port 1781 er Zealandbanner
Port 3306 er MySQL
Port 8788 er Zealandbanner
```

## Noter 
Noget af det har jeg hentet fra https://github.com/IammyselfYBX/Linux_Basics_for_Hackers

Se også https://github.com/gregmalcolm/python_koans
