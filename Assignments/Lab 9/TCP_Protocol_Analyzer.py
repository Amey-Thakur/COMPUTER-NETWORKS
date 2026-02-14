/**
 * File: TCP_Protocol_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: November 21, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * This script serves as a technical companion to Lab 09: Transmission 
 * Control Protocol (TCP). It simulates the Three-Way Handshake, 
 * data segmentation, and Congestion Control mechanisms (Slow Start 
 * and Congestion Avoidance) as captured in the laboratory trace.
 */

class TCPProtocolArchive:
    """
    Analyzes TCP connection management, flow control, and congestion avoidance mechanisms.
    """

    def __init__(self):
        # Configuration parameters from the session capture
        self.host_ip = "192.168.2.95"
        self.host_port = 50533
        self.server_ip = "128.119.245.12" # gaia.cs.umass.edu
        self.server_port = 80
        
        # Captured Sequence Numbers
        self.initial_seq_num = 954047503
        self.synack_seq_num = 1958276926
        
        # Observed Congestion Control Phase Timing
        self.slow_start_start = 2.6
        self.slow_start_end = 2.8
        self.congestion_avoidance_start = 3.2

    def simulate_three_way_handshake(self):
        """
        Replicates the SYN, SYN-ACK, and ACK sequence observed in the trace.
        """
        print("\n" + "="*75)
        print("SIMULATING TCP THREE-WAY HANDSHAKE")
        print("="*75)
        
        # 1. SYN
        print(f"[STEP 1: SYN] Host ({self.host_ip}:{self.host_port}) -> Server ({self.server_ip}:{self.server_port})")
        print(f"    - Flags: [SYN] | Seq: {self.initial_seq_num} | Ack: 0")
        print(f"    - Options: SACK permitted")

        # 2. SYN-ACK
        print(f"\n[STEP 2: SYN-ACK] Server -> Host")
        print(f"    - Flags: [SYN, ACK] | Seq: {self.synack_seq_num} | Ack: {self.initial_seq_num + 1}")
        
        # 3. ACK
        print(f"\n[STEP 3: ACK] Host -> Server")
        print(f"    - Flags: [ACK] | Seq: {self.initial_seq_num + 1} | Ack: {self.synack_seq_num + 1}")
        print("="*75)

    def display_congestion_control_analysis(self):
        """
        Analyzes the phase transitions for TCP Congestion Control protocols.
        """
        print("\n" + "="*75)
        print("TCP CONGESTION CONTROL PHASE ANALYSIS")
        print("="*75)
        print(f"{'Phase':<25} | {'Start (s)':<10} | {'End (s)':<10}")
        print("-" * 75)
        print(f"{'Slow Start Phase':<25} | {self.slow_start_start:<10} | {self.slow_start_end:<10}")
        print(f"{'Congestion Avoidance':<25} | {self.congestion_avoidance_start:<10} | {'Ongoing':<10}")
        print("-" * 75)
        print("Note: Congestion Avoidance was triggered after the rate of")
        print("sequence number growth was adjusted to maintain network stability.")
        print("="*75)

    @staticmethod
    def display_scholarly_responses():
        """
        Summary of technical findings and protocol analysis results.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: Client IP/Port": "192.168.2.95 / 50533",
            "Q2: Server IP/Port": "128.119.245.12 / 80",
            "Q3: SYN Sequence Number": "954047503",
            "Q4: SYN Flag Status": "Set to 1 (SACK permitted)",
            "Q5: SYNACK Seq/Ack": "Seq: 1958276926 | Ack: 954047504",
            "Q6: HTTP POST Seq": "954047504",
            "Q8: Packet Lengths": "684 Bytes (initial), 1492 Bytes (bulk)",
            "Q9: Min Buffer Space": "29200 Bytes (Receiver Window)",
            "Q10: Retransmissions": "Identified as 0 (Monotonic growth)"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*75)
    print("SCHOLARLY ANALYSIS: TRANSMISSION CONTROL PROTOCOL (TCP)")
    print("="*75)

    archive = TCPProtocolArchive()

    # 0. Scholarly Responses
    archive.display_scholarly_responses()

    # 1. Handshake Simulation
    archive.simulate_three_way_handshake()

    # 2. Congestion Control Analysis
    archive.display_congestion_control_analysis()

    # 3. Technical Insight
    print("\n" + "="*75)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*75)
    print("TCP ensures reliable, ordered delivery via 'Positive Acknowledgement")
    print("with Retransmission'. The 1492-byte segments observed in this lab")
    print("align with a standard Ethernet MTU of 1500 bytes (1452 bytes data +")
    print("20 bytes IP + 20 bytes TCP). The lack of retransmissions suggests")
    print("a high-quality link during this specific capture.")
    print("="*75)

if __name__ == "__main__":
    main()
