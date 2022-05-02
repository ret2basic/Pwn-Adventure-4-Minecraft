"""
teleport_proxy.py is the prototype proxy of Pwn Adventure 4: Minecraft project. It attempts to implement the teleport hack.

This script is based on https://github.com/barneygale/quarry/blob/master/examples/proxy_hide_chat.py
"""

from twisted.internet import reactor
from quarry.net.proxy import DownstreamFactory, Bridge
import argparse
import sys
import struct
import time
import random
import math

class QuietBridge(Bridge):
    """QuietBridge inherits from quarry.net.proxy.Bridge."""

    entity_id = None
    prev_pos = None
    prev_look = None

    def packet_unhandled(self, buff, direction, name):
        """Handle unhandled packets."""

        if direction == 'downstream':
            self.downstream.send_packet(name, buff.read())
        elif direction == 'upstream':
            print(f"[*][{direction}] {name}")
            self.upstream.send_packet(name, buff.read())
        
    def packet_upstream_player_position(self, buff):
        """"""

        buff.save()
        x, y, z, ground = struct.unpack('>dddB', buff.read())
        print(f"[*] player_position {x} / {y} / {z} | {ground}")
        self.prev_pos = (x, y, z, ground)
        buf = struct.pack('>dddB', x, y, z, ground)
        self.upstream.send_packet('player_position', buf)

    def packet_upstream_player_look(self, buff):
        """"""

        buff.save()
        yaw, pitch, ground = struct.unpack('>ffB', buff.read())
        print(f"[*] player_look {yaw} / {pitch} | {ground}")
        self.prev_look = (yaw, pitch, ground)
        buf = struct.pack('>ffB', yaw, pitch, ground)
        self.upstream.send_packet('player_look', buf)

class QuietDownstreamFactory(DownstreamFactory):
    """"""
    
    bridge_class = QuietBridge
    motd = "pwn4_proxy"

def main(argv):
    """Client -> (port 25565) Proxy (port 12345) -> Server"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--listen-host", default="", help="address to listen on")
    parser.add_argument("-p", "--listen-port", default=25565, type=int, help="The proxy listens on which port")
    parser.add_argument("-b", "--connect-host", default="127.0.0.1", help="address to connect to")
    parser.add_argument("-q", "--connect-port", default=12345, type=int, help="Connect to which port on the server")
    args = parser.parse_args(argv)

    # Create factory
    factory = QuietDownstreamFactory()
    factory.connect_host = args.connect_host
    factory.connect_port = args.connect_port

    # Listen
    factory.listen(args.listen_host, args.listen_port)
    reactor.run()

if __name__ == "__main__":
    main(sys.argv[1:])
