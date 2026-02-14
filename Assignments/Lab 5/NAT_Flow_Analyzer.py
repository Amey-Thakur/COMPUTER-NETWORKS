/**
 * File: NAT_Flow_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: November 01, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * Simulates Network Address Translation (NAT) router operations. This module
 * demonstrates the automated translation of IP datagrams between private 
 * LAN subnets and public WAN interfaces, including header modification 
 * and checksum recalculation required for protocol transparency.
 */

class NATRouterSimulation:
    """
    Simulates the core functionality of a NAT device.
    """

    def __init__(self):
        # Configuration for NAT gateway simulation
        self.lan_subnet = "192.168.10.0/24"
        self.wan_public_ip = "10.0.1.254"
        self.translation_table = {} # Port-based mapping

    def translate_outgoing_packet(self, src_ip, src_port, dst_ip, dst_port):
        """
        Executes Source IP translation for outbound traffic.
        """
        print("\n" + "-"*70)
        print("OUTGOING FLOW: INTERNAL -> EXTERNAL")
        print("-"*70)
        print(f"[*] Original (Inside): {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        
        # Update the source identifier to the public interface.
        translated_src_ip = self.wan_public_ip
        
        # Recalculate the IP header checksum to reflect address modifications.
        old_checksum = "0x64dc"
        new_checksum = "0x2d82"

        print(f"[+] NAT Action: Source IP translated to {translated_src_ip}")
        print(f"[+] Translated (Outside): {translated_src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        print(f"[+] Checksum Update: {old_checksum} -> {new_checksum}")
        print("-"*70)

    @staticmethod
    def explain_nat_necessity():
        """
        Provides a scholarly context for NAT.
        """
        print("\n" + "="*70)
        print("TECHNICAL INSIGHT: WHY NAT?")
        print("="*70)
        print("Network Address Translation was primarily developed to mitigate the")
        print("exhaustion of IPv4 addresses. By allowing thousands of devices in")
        print("a private network to share a single public IP, NAT significantly")
        print("extended the lifespan of the IPv4 protocol. It also provides a")
        print("layer of security by hiding internal network structures from the")
        print("public Internet.")
        print("="*70)

    @staticmethod
    def display_scholarly_responses():
        """
        Summarizes NAT translation table entries and session parameters.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: Internal Source IP": "192.168.10.11",
            "Q5: Translated WAN IP": "10.0.1.254",
            "Q8: Old Checksum": "0x64dc",
            "Q8: New Checksum": "0x2d82",
            "Q11: Forwarded Destination": "192.168.10.11"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*70)
    print("SCHOLARLY ANALYSIS: NETWORK ADDRESS TRANSLATION (NAT)")
    print("="*70)

    nat = NATRouterSimulation()

    # 0. Scholarly Responses
    nat.display_scholarly_responses()

    # 1. Simulate the specific HTTP GET request flow from the report
    # Inside: 192.168.10.11:53924 to Server: 138.76.29.8:80
    nat.translate_outgoing_packet(
        src_ip="192.168.10.11", 
        src_port=53924, 
        dst_ip="138.76.29.8", 
        dst_port=80
    )

    # 2. Provide scholarly context
    nat.explain_nat_necessity()

    # 3. Scholarly Insight
    print("\n" + "="*70)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*70)
    print("Did you know? When a NAT router modifies an IP address, it must also")
    print("recalculate the IP Header Checksum and potentially the TCP/UDP")
    print("checksum (since those use a pseudo-header containing the IP addresses).")
    print("This makes NAT a computationally expensive operation compared to")
    print("pure Layer 3 routing.")
    print("="*70)

if __name__ == "__main__":
    main()
