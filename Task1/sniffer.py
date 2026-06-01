from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.inet6 import IPv6


def packet_info(packet):

    print("\n===== Packet Captured =====")

    print(packet.summary())

    # IPv4
    if packet.haslayer(IP):

        print("Version        : IPv4")
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

    # IPv6
    elif packet.haslayer(IPv6):

        print("Version        : IPv6")
        print("Source IP      :", packet[IPv6].src)
        print("Destination IP :", packet[IPv6].dst)

    # Protocols
    if packet.haslayer(TCP):
        print("Protocol       : TCP")

    elif packet.haslayer(UDP):
        print("Protocol       : UDP")

    else:
        print("Protocol       : Other")


# Start sniffing
sniff(prn=packet_info, count=20)
