from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

sniff(timeout=10, prn=process_packet)
