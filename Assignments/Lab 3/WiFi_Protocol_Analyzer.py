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
 * Evaluates IEEE 802.11 wireless frame structures, specifically focusing 
 * on management frames and network discovery mechanisms. Includes 
 * simulations for beaconing intervals, data rate advertisements, and
 * the unique triple-addressing scheme used in 802.11 environments.
 */

import time

class WiFiManagementArchive:
    """
    A collection of utilities to illustrate 802.11 Link-Layer concepts.
    """

    def __init__(self):
        # Radio environment configuration for analyzed access points
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
        Generates a simulation of the periodic BSSID advertisement cycle.
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
        Technical breakdown of the address fields within 802.11 MAC headers.
        """
        print("\n" + "-"*60)
        print("TECHNICAL INSIGHT: 802.11 TRIPLE-ADDRESSING")
        print("-"*60)
        print("Unlike Ethernet (2 addresses), 802.11 often uses 3 MAC fields:")
        print("1. Receiver Address: The immediate next hop (e.g., the AP).")
        print("2. Transmitter Address: The station sending the frame.")
        print("3. BSSID: The identification of the wireless service set.")
        print("-"*60)

    @staticmethod
    def display_scholarly_responses():
        """
        Displays analyzed wireless networking parameters and BSSID data.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: Primary SSID": "30 Munroe St",
            "Q1: Primary BSSID": "00:16:b6:f7:1d:51",
            "Q2: Beacon Interval": "102.4 ms (0.1024s)",
            "Q3: Max Data Rate": "54 Mbps",
            "Q7: Triple-Addressing": "Receiver, Transmitter, BSSID"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def main():
    print("="*70)
    print("SCHOLARLY ANALYSIS: IEEE 802.11 WIRELESS FIDELITY (WI-FI)")
    print("="*70)

    analyzer = WiFiManagementArchive()

    # 0. Scholarly Responses
    analyzer.display_scholarly_responses()

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
