/**
 * File: ICMP_Protocol_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: November 10, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * Explores the Internet Control Message Protocol (ICMP) for network 
 * diagnostics. Implements simulation logic for ICMP Echo Request/Reply 
 * (Ping) cycles and the "Time Exceeded" error feedback mechanisms 
 * utilized for path discovery in traceroute operations.
 */

import random

class ICMPProtocolArchive:
    """
    A collection of utilities to illustrate ICMP transmission and error handling.
    """

    def __init__(self):
        # Default parameters for ICMP analysis
        self.host_ip = "192.168.2.20"
        self.ping_target_ip = "142.251.41.36"      # google.com
        self.traceroute_target_ip = "172.217.1.4"  # google.com (alternate resolved IP)
        self.default_protocol_num = 1              # ICMP Protocol Number

    def simulate_ping_handshake(self):
        """
        Generates a simulation of the Echo Request/Reply handshake.
        """
        identifier = random.randint(0x0100, 0x0200)
        sequence_num = 1
        
        print("\n" + "="*75)
        print(f"SIMULATING ICMP PING HANDSHAKE")
        print("="*75)
        
        # 1. ECHO REQUEST
        print(f"[PACKET 1: REQUEST] Host ({self.host_ip}) -> Target ({self.ping_target_ip})")
        print(f"    - ICMP Type: 8 (Echo Request) | Code: 0")
        print(f"    - Identifier: {hex(identifier)} | Sequence: {sequence_num}")
        print(f"    - Checksum: 0xad5d (Valid)")

        # 2. ECHO REPLY
        print(f"\n[PACKET 2: REPLY] Target ({self.ping_target_ip}) -> Host ({self.host_ip})")
        print(f"    - ICMP Type: 0 (Echo Reply) | Code: 0")
        print(f"    - Identifier: {hex(identifier)} | Sequence: {sequence_num}")
        print(f"    - Checksum: 0x5550 (Valid)")
        print("="*75)

    def simulate_traceroute_error(self, hop_num):
        """
        Replicates ICMP Type 11 error generation for path discovery.
        """
        router_ip = f"10.216.228.{hop_num}"
        print(f"\n[TRACEROUTE HOP {hop_num}] Sending Probe with TTL={hop_num}...")
        print(f"[-] Router ({router_ip}) reports: ICMP Type 11, Code 0 (Time to live exceeded in transit)")
        print(f"    - Payload includes: Original IP Header + First 8 bytes of ICMP payload.")

    @staticmethod
    def display_scholarly_responses():
        """
        Displays analyzed ICMP type/code mappings and diagnostic findings.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: Host IP Address": "192.168.2.20",
            "Q1: Destination IP": "142.251.41.36",
            "Q2: Ping Request Type": "Type 8, Code 0",
            "Q3: Ping Reply Type": "Type 0, Code 0",
            "Q5: Protocol Num (UDP)": "0x11 (17) if it were UDP",
            "Q8: Error vs Reply": "Error (Type 11) vs Reply (Type 0)"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*75)
    print("SCHOLARLY ANALYSIS: INTERNET CONTROL MESSAGE PROTOCOL (ICMP)")
    print("="*75)

    archive = ICMPProtocolArchive()

    # 0. Scholarly Responses
    archive.display_scholarly_responses()

    # 1. Ping Logic
    archive.simulate_ping_handshake()

    # 2. Traceroute Logic
    print("\n[+] Identifying Traceroute Mechanics:")
    archive.simulate_traceroute_error(1)
    archive.simulate_traceroute_error(2)

    # 3. Technical Insight
    print("\n" + "="*75)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*75)
    print("ICMP is the 'diagnostic' tool of the IP suite. While Ping tests")
    print("reachability, Traceroute leverages the error feedback mechanism")
    print("inherent in IP to discover the multi-hop path to a destination.")
    print("Note that Windows uses ICMP Echo Requests for its 'tracert' tool,")
    print("while Unix-like systems often default to UDP probes.")
    print("="*75)

if __name__ == "__main__":
    main()
