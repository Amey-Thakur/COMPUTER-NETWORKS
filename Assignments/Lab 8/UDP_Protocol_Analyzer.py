/**
 * File: UDP_Protocol_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: November 14, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * This script serves as a technical companion to Lab 08: User Datagram 
 * Protocol (UDP). It explores the structure of the 8-byte UDP header, 
 * the calculation of payload lengths, and the symmetry of port 
 * assignments in a connectionless transport environment.
 */

class UDPSegmentArchive:
    """
    A collection of utilities to illustrate UDP segmentation and header structures.
    """

    def __init__(self):
        # Data derived from the Lab 08 report analysis
        self.host_ip = "192.168.2.20"
        self.target_ip = "142.251.41.36"
        self.protocol_num_decimal = 17
        self.protocol_num_hex = "0x11"
        self.header_size_bytes = 8

    def simulate_udp_interaction(self):
        """
        Simulates the port swapping observed in request/reply datagrams.
        Reflects Question 7 of the lab report.
        """
        request_src_port = 60124
        request_dst_port = 53 # DNS Query
        
        print("\n" + "="*75)
        print(f"SIMULATING UDP REQUEST/REPLY SYMMETRY")
        print("="*75)
        
        # 1. REQUEST (Outgoing)
        print(f"[PACKET: REQUEST] Host -> DNS Server")
        print(f"    - Source Port: {request_src_port} | Destination Port: {request_dst_port}")
        print(f"    - UDP Length: 62 bytes (Payload) + 8 bytes (Header) = 70 bytes")

        # 2. REPLY (Incoming)
        print(f"\n[PACKET: REPLY] DNS Server -> Host")
        print(f"    - Source Port: {request_dst_port} | Destination Port: {request_src_port}")
        print(f"    - Status: Port values are symmetrically swapped for the return path.")
        print("="*75)

    @staticmethod
    def display_scholarly_responses():
        """
        Prints the specific findings from the Lab 08 report.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: Header Fields": "Source Port, Destination Port, Length, Checksum",
            "Q2: Header Size": "8 Bytes (2 Bytes per field)",
            "Q3: Payload (Length 70)": "62 Bytes (70 - 8)",
            "Q4: Max Payload Size": "65527 Bytes (65535 - 8)",
            "Q5: Max Source Port": "65535 (2^16 - 1)",
            "Q6: IP Protocol Number": "17 (Decimal) / 0x11 (Hex)",
            "Q7: Port Symmetry": "Source/Destination ports swap in replies"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*75)
    print("SCHOLARLY ANALYSIS: USER DATAGRAM PROTOCOL (UDP)")
    print("="*75)

    archive = UDPSegmentArchive()

    # 0. Scholarly Responses
    archive.display_scholarly_responses()

    # 1. UDP Interaction Simulation
    archive.simulate_udp_interaction()

    # 2. Technical Insight
    print("\n" + "="*75)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*75)
    print("UDP is a 'best-effort' connectionless protocol. Unlike TCP, it does")
    print("not maintain state or provide reliability, relying instead on the")
    print("application layer for such features. This minimalism results in very")
    print("low overhead (8 bytes vs 20+ bytes for TCP), making it ideal for")
    print("real-time applications like DNS, VoIP, and streaming.")
    print("="*75)

if __name__ == "__main__":
    main()
