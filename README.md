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
