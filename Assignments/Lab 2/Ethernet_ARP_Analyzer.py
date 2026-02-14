/**
 * File: Ethernet_ARP_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: October 6, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * This script serves as a technical companion to Lab 02: Ethernet and ARP. 
 * It explores the structure of Ethernet frames at the Data Link Layer (Layer 2) 
 * and the mechanism of the Address Resolution Protocol (ARP) for mapping 
 * IP addresses to physical MAC addresses.
 */

import uuid
import binascii

class NetworkingArchive:
    """
    A collection of utilities to illustrate Layer 2 concepts.
    """

    @staticmethod
    def get_local_mac():
        """
        Retrieves the 48-bit Ethernet address (MAC) of the local machine.
        This corresponds to Question 1 of the lab report.
        """
        mac_int = uuid.getnode()
        mac_hex = ':'.join(['{:02x}'.format((mac_int >> i) & 0xff) for i in range(0, 48, 8)][::-1])
        return mac_hex

    @staticmethod
    def analyze_frame_header(frame_type_hex):
        """
        Identifies the upper-layer protocol based on the 2-byte EtherType field.
        As seen in Questions 3 and 14 of the report.
        """
        protocols = {
            "0x0800": "Internet Protocol version 4 (IPv4)",
            "0x0806": "Address Resolution Protocol (ARP)",
            "0x86dd": "Internet Protocol version 6 (IPv6)"
        }
        return protocols.get(frame_type_hex, "Unknown Protocol")

    @staticmethod
    def calculate_payload_offset(include_preamble=True):
        """
        Illustrates the byte-offset analysis for application data within a frame.
        Mirroring the calculation in Question 4/8 of the report.
        """
        ethernet_header = 14  # Destination (6) + Source (6) + Type (2)
        ip_header = 20        # Standard IPv4 header
        tcp_header = 32       # As observed in the specific trace file
        
        total_offset = ethernet_header + ip_header + tcp_header
        
        print("-" * 50)
        print("LAYER-BY-LAYER BYTE OFFSET ANALYSIS")
        print("-" * 50)
        print(f"| Ethernet Header: {ethernet_header} bytes")
        print(f"| IP Header:       {ip_header} bytes")
        print(f"| TCP Header:      {tcp_header} bytes")
        print(f"| Total Overhead:  {total_offset} bytes")
        
        if include_preamble:
            # Physical layer usually handles the 8-byte preamble, 
            # but some tools report offsets relative to it.
            print(f"| Relative to Preamble (-2 bytes): {total_offset - 2} bytes")
        print("-" * 50)

def main():
    print("="*70)
    print("SCHOLARLY ANALYSIS: ETHERNET & ADDRESS RESOLUTION PROTOCOL (ARP)")
    print("="*70)

    analyzer = NetworkingArchive()

    # 1. MAC Address Discovery
    local_mac = analyzer.get_local_mac()
    print(f"[!] Local 48-bit Ethernet Address: {local_mac}")

    # 2. Protocol Identification (EtherType)
    print("\n[+] Identifying Frame Types (EtherType):")
    for etype in ["0x0800", "0x0806"]:
        print(f"    - Type {etype}: {analyzer.analyze_frame_header(etype)}")

    # 3. Payload Depth Calculation
    print("\n[+] Application Data Positioning:")
    analyzer.calculate_payload_offset()

    # 4. Critical Networking Insight
    print("\n" + "="*70)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*70)
    print("ARP operates at the 'seam' between Layer 2 and Layer 3. While IP")
    print("addresses govern logical routing across networks, Ethernet addresses")
    print("are required for delivery within a localized segment (broadcast domain).")
    print("Note that an ARP Request is broadcast (FF:FF:FF:FF:FF:FF) because the")
    print("sender doesn't yet know 'who' owns the target IP, whereas the ARP")
    print("Reply is unicast directly back to the solicitor.")
    print("="*70)

if __name__ == "__main__":
    main()
