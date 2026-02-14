/**
 * File: IP_Protocol_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: November 07, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * This script serves as a technical companion to Lab 06: Internet Protocol (IP).
 * It simulates the structure of an IPv4 datagram and demonstrates two critical
 * networking concepts analyzed in the lab:
 * 1. TTL (Time-to-Live) decrement during Traceroute operations.
 * 2. IP Fragmentation of large UDP segments (e.g., 3000 bytes).
 */

class IPv4PacketArchive:
    """
    Simulates the archival and analysis of IPv4 datagrams.
    """

    def __init__(self, source_ip="192.168.2.95", destination_ip="128.119.245.12"):
        self.version = 4
        self.header_length = 20 # Standard 20 bytes (Question 4)
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.protocol = "ICMP (1)" # Or UDP (17) depending on context

    def simulate_traceroute_ttl(self, max_hops=3):
        """
        Simulates the incrementing TTL behavior of Traceroute.
        Reflects Questions 2 and 7 of the lab report.
        """
        print("\n" + "-"*75)
        print("SIMULATION: TRACEROUTE TTL MECHANISM")
        print("-"*75)
        for ttl in range(1, max_hops + 1):
            identification = 53000 + ttl # Simulated incrementing ID
            print(f"[Packet {ttl}] Identification: {identification} | TTL: {ttl}")
        print("-"*75)

    def simulate_fragmentation(self, udp_payload_size=3000, mtu=1500):
        """
        Simulates the fragmentation of a large segment into multiple datagrams.
        Reflects Questions 13 to 19 of the lab report.
        """
        print("\n" + "="*75)
        print("SIMULATION: IP FRAGMENTATION (3000-byte UDP Segment)")
        print("="*75)
        
        # Calculation logic derived from lab analysis
        # Total Length = 1500 (MTU)
        # Header = 20
        # Payload per fragment = 1480 (must be multiple of 8)
        
        total_remaining = udp_payload_size
        offset = 0
        frag_count = 1
        identification = 0xfda1 # Identification remains constant across fragments
        
        while total_remaining > 0:
            payload_in_this_frag = min(total_remaining, mtu - self.header_length)
            total_length = payload_in_this_frag + self.header_length
            more_fragments = 1 if (total_remaining > payload_in_this_frag) else 0
            
            print(f"Fragment #{frag_count}:")
            print(f"  - Total Length: {total_length} bytes")
            print(f"  - Identification: {hex(identification)} ({identification})")
            print(f"  - More Fragments (MF) Flag: {more_fragments}")
            print(f"  - Fragment Offset: {offset}")
            
            total_remaining -= payload_in_this_frag
            offset += (payload_in_this_frag // 8) # Offset is in units of 8 bytes
            frag_count += 1
            print("-" * 30)

    @staticmethod
    def provide_scholarly_context():
        """
        Technical insights on the Internet Protocol.
        """
        print("\n" + "="*75)
        print("SCHOLARLY INSIGHT: FRAGMENTATION VS. PMTUD")
        print("="*75)
        print("While IPv4 allows routers to fragment packets, this is often")
        print("avoided in modern networks due to performance overhead. Path MTU")
        print("Discovery (PMTUD) is generally preferred, where the source host")
        print("detects the smallest MTU along the path and adjusts its segment")
        print("size accordingly. In IPv6, routers no longer perform")
        print("fragmentation; it is solely the responsibility of the source node.")
        print("="*75)

    @staticmethod
    def display_scholarly_responses():
        """
        Prints the specific findings from the Lab 06 report.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: IP Address": "192.168.2.95",
            "Q2: Initial TTL": "1",
            "Q3: Protocol": "ICMP (1)",
            "Q4: Header Length": "20 bytes",
            "Q5: Payload Length": "72 bytes",
            "Q6: Path MTU Fragmentation": "3 Fragments (for 3000-byte segment)",
            "Q14: MF Flag (Fragment 1)": "Set (1)",
            "Q15: Offset (Fragment 1)": "0",
            "Q19: MF Flag (Last Fragment)": "Not Set (0)"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*75)
    print("SCHOLARLY ANALYSIS: INTERNET PROTOCOL (IPV4)")
    print("="*75)
    
    analyzer = IPv4PacketArchive()
    
    # 0. Scholarly Responses
    analyzer.display_scholarly_responses()

    # 1. Traceroute TTL Analysis
    analyzer.simulate_traceroute_ttl()
    
    # 2. Fragmentation Simulation
    analyzer.provide_scholarly_context()
    analyzer.simulate_fragmentation()
    
    # 3. Networking Tip
    print("\n" + "-"*75)
    print("NETWORKING TIP: The 'Identification' field is used by the destination")
    print("host to determine which fragments belong to the same original")
    print("datagram, ensuring correct reassembly.")
    print("-" * 75)

if __name__ == "__main__":
    main()
