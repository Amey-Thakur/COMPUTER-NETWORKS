/**
 * File: WiFi_Protocol_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: October 20, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * This script serves as a technical companion to Lab 03: Wireless Fidelity (Wi-Fi).
 * It explores the characteristics of 802.11 wireless frames, specifically 
 * Beacon Frames used for network advertisement and the management of 
 * Service Set Identifiers (SSIDs).
 */

import time

class WiFiManagementArchive:
    """
    A collection of utilities to illustrate 802.11 Link-Layer concepts.
    """

    def __init__(self):
        # Data derived from the Lab 3 trace analysis
        self.access_points = {
            "30 Munroe St": {
                "mac": "00:16:b6:f7:1d:51",
                "beacon_interval": 0.1024,  # Seconds
                "supported_rates": [1, 2, 5.5, 11], # Mbps
                "extended_rates": [6, 9, 12, 18, 24, 36, 48, 54] # Mbps
            },
            "linksys12": {
                "mac": "00:14:bf:cf:d1:b6", # Example derived from trace context
                "beacon_interval": 0.1024
            }
        }

    def simulate_beacon_broadcast(self, ssid):
        """
        Simulates the periodic broadcast of a Beacon frame.
        Reflects Question 2 and 6 of the lab report.
        """
        if ssid in self.access_points:
            ap = self.access_points[ssid]
            print(f"\n[+] Emulating Beacon Frame for SSID: '{ssid}'")
            print(f"    - Source MAC (BSSID): {ap['mac']}")
            print(f"    - Beacon Interval: {ap['beacon_interval']} seconds (102.4ms)")
            
            if "supported_rates" in ap:
                print(f"    - Primary Rates:  {ap['supported_rates']} Mbps")
                print(f"    - Extended Rates: {ap['extended_rates']} Mbps")
        else:
            print(f"[!] SSID '{ssid}' not found in the local radio environment.")

    @staticmethod
    def explain_80211_addressing():
        """
        Explains the triple-addressing scheme used in 802.11 frames.
        As explored in Question 7 and 8 of the report.
        """
        print("\n" + "-"*60)
        print("TECHNICAL INSIGHT: 802.11 TRIPLE-ADDRESSING")
        print("-"*60)
        print("Unlike Ethernet (2 addresses), 802.11 often uses 3 MAC fields:")
        print("1. Receiver Address: The immediate next hop (e.g., the AP).")
        print("2. Transmitter Address: The station sending the frame.")
        print("3. BSSID: The identification of the wireless service set.")
        print("-"*60)

def main():
    print("="*70)
    print("SCHOLARLY ANALYSIS: IEEE 802.11 WIRELESS FIDELITY (WI-FI)")
    print("="*70)

    analyzer = WiFiManagementArchive()

    # 1. Simulate Beaconing for the primary AP mentioned in the report
    analyzer.simulate_beacon_broadcast("30 Munroe St")
    
    # 2. Simulate for the secondary AP
    analyzer.simulate_beacon_broadcast("linksys12")

    # 3. Explain the complex addressing observed in Wireshark
    analyzer.explain_80211_addressing()

    # 4. Scholarly Insight
    print("\n" + "="*70)
    print("SCHOLARLY INSIGHT & NETWORKING TIP")
    print("="*70)
    print("In 802.11, the management of the shared medium relies on 'Beacons'")
    print("which allow stations to discover and synchronize with Access Points.")
    print("The 102.4ms interval is a standard 'Time Unit' (TU) in wireless")
    print("networking, ensuring that power-saving stations know exactly when")
    print("to wake up to listen for buffered traffic indications (TIM).")
    print("="*70)

if __name__ == "__main__":
    main()
