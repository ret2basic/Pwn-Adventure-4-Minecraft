# Pwn Adventure 4: Minecraft

## Setup

Install JDK 17:

```shell
sudo apt install openjdk-17-jdk
```

Download `paper.jar` at https://papermc.io/downloads. Windows Defender may catch this file as virus but I promise it is a legit file. Configure Paper server:

```shell
java -jar paper-1.18.2-137.jar
```

Agree to the EULA by changing the content of `eula.txt` to `eula=true`. Also, we can modify the `server.properties` file:

```
...
online-mode=false
...
```

Spawn a Minecraft server:

```shell
java -jar paper-1.18.2-317.jar
```

In Minecraft, go to "Multiplayer -> Add Server" and set 127.0.0.1 as Server Address.

## Proxy

Our prototype proxy is named `teleport_proxy.py`, where we are going to attempt a naive teleport hack.

To set up this proxy, first change the server port from 25565 to 12345 since our proxy will be listening on port 25565 and we need two different ports to handle upstream (port 25565) and downstream (port 12345). Edit the port option in `server.properties`:

```
...
server-port=12345
...
```

Spawn a game server:

```shell
java -jar paper-1.18.2-317.jar
```

Be aware that twisted has **SSL problems** on Windows machines. It is an old library and only supports Linux, but there is a way to circumvent this barrier. This issue solved my problem: https://github.com/barneygale/quarry/issues/135.

Install `certifi`:

```shell
pip3 install certifi
```

Start the proxy in **Git Bash**:

```shell
SSL_CERT_FILE="$(python -m certifi)" python3 teleport_proxy.py
```

Then spawn the game client and watch the proxy logging. Moving on to our first hack.

## Teleport (kind of)


