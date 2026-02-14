"""
/**
 * File: HTTP_Connectivity_Analyzer.py
 * Author: Amey Thakur
 * GitHub: [Amey-Thakur](https://github.com/Amey-Thakur)
 * Repository: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
 * Session: Fall 2023
 * Release Date: September 19, 2023
 * License: Creative Commons Attribution 4.0 International (CC BY 4.0)
 * 
 * Description:
 * Implementation of an HTTP GET request protocol analyzer. This script
 * demonstrates the automated retrieval of web resources and the 
 * programmatic inspection of HTTP response headers to evaluate 
 * server-side configurations and network transmission characteristics.
 */
"""

import urllib.request
import time

class HTTPProtocolArchive:
    """
    Simulates the archival and analysis of HTTP interactions.
    """

    @staticmethod
    def display_scholarly_responses():
        """
        Displays analyzed protocol metrics and server identification data.
        """
        print("\n" + "="*75)
        print("LABORATORY RESULTS: SCHOLARLY RESPONSES")
        print("="*75)
        responses = {
            "Q1: Observed Protocols": "TCP, HTTP, DNS",
            "Q2: Interaction Latency": "0.0245 seconds",
            "Q3: Server IP Address": "128.119.245.12",
            "Q5: Response Status": "200 OK"
        }
        for q, a in responses.items():
            print(f"{q:<30} : {a}")
        print("="*75)

def analyze_http_request(url):
    """
    Executes a standard HTTP GET request and performs header analysis.
    """
    print("="*70)
    print(f"Scholarly Analysis of HTTP Protocol Interaction")
    print(f"Target URL: {url}")
    print("="*70)
    
    try:
        # Capture the initiation timestamp for RTT calculation.
        start_time = time.time()
        
        # Initialize the network connection and request the remote resource.
        with urllib.request.urlopen(url) as response:
            end_time = time.time()
            latency = end_time - start_time
            
            # Evaluate the HTTP response status.
            status_code = response.getcode()
            print(f"[+] Protocol Status: {status_code} OK")
            print(f"[+] Total Round-Trip Time (Latency): {latency:.4f} seconds")
            
            # Parse and display relevant header metadata.
            print("\n--- Significant HTTP Header Metadata (Server Response) ---")
            headers = response.info()
            
            # The 'Date' header indicates when the server generated the response.
            print(f"| Timestamp: {headers.get('Date', 'Not Provided')}")
            
            # The 'Server' header identifies the backend architecture.
            print(f"| Server Software: {headers.get('Server', 'Not Provided')}")
            
            # The 'Content-Length' specifies the size of the payload in bytes.
            print(f"| Payload Size: {headers.get('Content-Length', 'Not Provided')} bytes")
            
            # The 'Content-Type' defines the media format (HTML in this instance).
            print(f"| Media Format: {headers.get('Content-Type', 'Not Provided')}")
            
            # Read and decode the response body.
            content = response.read().decode('utf-8').strip()
            print("\n--- Retrieved Application Payload ---")
            print(f"> {content}")

            print("\n" + "="*70)
            print("SCHOLARLY INSIGHT & NETWORKING TIP")
            print("="*70)
            print("Note how the latency includes both the propagation delay and the")
            print("processing time at the server. In high-performance networking,")
            print("minimizing header overhead is as critical as raw bandwidth for")
            print("reducing this round-trip time. This script mirrors the visibility")
            print("that Wireshark provides, turning abstract packets into readable data.")
            print("="*70)
            
    except Exception as error:
        print(f"[!] Error during protocol execution: {error}")
        print("Ensure you have an active internet connection to reach the UMass server.")

if __name__ == "__main__":
    # 0. Scholarly Responses
    HTTPProtocolArchive.display_scholarly_responses()

    # The official GAIA server URL used in the University of Windsor Lab sequence
    target_lab_url = "http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html"
    analyze_http_request(target_lab_url)
