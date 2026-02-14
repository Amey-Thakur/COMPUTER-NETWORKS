"""
/**
 * File: HTTP_Connectivity_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: September 19, 2023
 * License: CC BY 4.0
 * 
 * Description:
 * This script serves as a technical companion to Lab 01: Introduction to Wireshark.
 * It programmatically replicates the HTTP GET request performed during the lab 
 * session to illustrate the interaction between a client (this script) and the 
 * UMass 'gaia' server. By extracting and displaying HTTP headers, it provides 
 * a scholarly look at the metadata exchanged in a standard web communication 
 * cycle, bridging the gap between graphical analysis (Wireshark) and 
 * implementation-level protocol handling.
 */
"""

import urllib.request
import time

def analyze_http_request(url):
    """
    Performs a pedagogical analysis of an HTTP GET request.
    This function mimics the browser behavior observed in the Wireshark capture.
    """
    print("="*70)
    print(f"Pedagogical Analysis of HTTP Protocol Interaction")
    print(f"Target URL: {url}")
    print("="*70)
    
    try:
        # Recording the start time to calculate network latency
        # This mirrors the time-delta analysis performed in the lab report (Question 2)
        start_time = time.time()
        
        # Initializing the HTTP GET request
        # In a Wireshark trace, this corresponds to the 'Hypertext Transfer Protocol' layer
        with urllib.request.urlopen(url) as response:
            end_time = time.time()
            latency = end_time - start_time
            
            # Retrieval of the HTTP Status Code
            # Code 200 signifies a successful 'OK' response from the gaia server
            status_code = response.getcode()
            print(f"[+] Protocol Status: {status_code} OK")
            print(f"[+] Total Round-Trip Time (Latency): {latency:.4f} seconds")
            
            # Scholarly Inspection of HTTP Headers
            # These headers represent the 'Packet Details' observed in the Wireshark GUI
            print("\n--- Significant HTTP Header Metadata (Server Response) ---")
            headers = response.info()
            
            # The 'Date' header indicates when the server generated the response
            print(f"| Timestamp: {headers.get('Date', 'Not Provided')}")
            
            # The 'Server' header identifies the backend architecture
            print(f"| Server Software: {headers.get('Server', 'Not Provided')}")
            
            # The 'Content-Length' specifies the size of the payload in bytes
            print(f"| Payload Size: {headers.get('Content-Length', 'Not Provided')} bytes")
            
            # The 'Content-Type' defines the media format (HTML in this instance)
            print(f"| Media Format: {headers.get('Content-Type', 'Not Provided')}")
            
            # Final Payload Retrieval
            # This is the actual data displayed in the web browser during Step 3 of the lab
            content = response.read().decode('utf-8').strip()
            print("\n--- Retrieved Application Payload ---")
            print(f"> {content}")
            
    except Exception as error:
        print(f"[!] Error during protocol execution: {error}")
        print("Ensure you have an active internet connection to reach the UMass server.")

if __name__ == "__main__":
    # The official GAIA server URL used in the University of Windsor Lab sequence
    target_lab_url = "http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html"
    analyze_http_request(target_lab_url)
