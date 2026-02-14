/**
 * File: DNS_Protocol_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: November 30, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * Analyzes Domain Name System (DNS) protocol interactions and hierarchy.
 * This module simulates nslookup commands for A-Record and NS-Record 
 * resolution, inspects local system DNS configurations (ipconfig), 
 * and evaluates the UDP-based transport layer used for name resolution.
 */

class DNSProtocolArchive:
    """
    Analyzes DNS resolution flows, hierarchy, and transport layer mechanics.
    """

    def __init__(self):
        # Configuration for simulated DNS environment
        self.local_resolvers = ["128.238.29.25", "128.238.29.22", "128.238.29.23"]
        self.default_port = 53
        self.transport_protocol = "UDP (17)"

    def simulate_nslookup_query(self, hostname, server=None, qtype="A"):
        """
        Executes a simulated DNS lookup for the specified hostname and record type.
        """
        query_server = server if server else self.local_resolvers[1]
        print(f"\n[QUERY] nslookup -type={qtype} {hostname} {query_server}")
        print("-" * 75)
        print(f"| Requesting {qtype} record from: {query_server} (Port {self.default_port})")
        
        # Scenario mapping based on manual results
        if hostname == "www.mit.edu":
            print(f"| Response: 18.7.22.83")
        elif hostname == "mit.edu" and qtype == "NS":
            print(f"| Authoritative Servers: bitsy.mit.edu, straub.mit.edu, w20ns.mit.edu")
        elif hostname == "www.aiit.or.kr" and server == "bitsy.mit.edu":
            print(f"| Response (Direct Query): 218.36.94.200")
        else:
            print(f"| Response: [Simulated resolution successful]")
        print("-" * 75)

    def display_system_configuration_audit(self):
        """
        Replicates the local system DNS environment audit.
        """
        print("\n" + "="*75)
        print("LOCAL SYSTEM DNS CONFIGURATION AUDIT")
        print("="*75)
        print(f"| Adaptation Suffix: poly.edu")
        print(f"| IPv4 Interface:   128.238.38.160")
        print(f"| Active Resolvers:")
        for idx, resolver in enumerate(self.local_resolvers, 1):
            print(f"|   {idx}. {resolver}")
        print("="*75)

    @staticmethod
    def display_scholarly_responses():
        """
        Summary of protocol identification and DNS session parameters.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: resolved IP (Asia)": "218.36.94.200 (www.aiit.or.kr)",
            "Q2: Authoritative DNS (EU)": "ns.poly.edu (Example Resolver)",
            "Q4: Transport Protocol": "UDP",
            "Q5: Destination Port": "53",
            "Q7: Query Characteristics": "Type A, Recursive, No Answers",
            "Q8: Response Context": "Contains Resource Records (RRs)",
            "Q10: Resource Retrieval": "No new DNS query (Cached/Persistent)"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*75)
    print("SCHOLARLY ANALYSIS: DOMAIN NAME SYSTEM (DNS)")
    print("="*75)

    analyser = DNSProtocolArchive()

    # 1. Scholarly Findings
    analyser.display_scholarly_responses()

    # 2. Local Configuration Audit
    analyser.display_system_configuration_audit()

    # 3. Simulate Name Resolution Queries
    analyser.simulate_nslookup_query("www.mit.edu")
    analyser.simulate_nslookup_query("mit.edu", qtype="NS")
    analyser.simulate_nslookup_query("www.aiit.or.kr", server="bitsy.mit.edu")

    # 4. Technical Insight
    print("\n" + "="*75)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*75)
    print("DNS caching is essential for reducing global network traffic and")
    print("improving user experience (latency). The 'Time-to-Live' (TTL) field")
    print("in a DNS response dictates how long a local resolver or host should")
    print("cache a record before re-validating it with an authoritative source.")
    print("Tools like 'ipconfig /displaydns' allow inspection of this local cache.")
    print("="*75)

if __name__ == "__main__":
    main()
