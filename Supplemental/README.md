# IP and Subnet Practice Problems - Detailed Solutions


> - **File Name**: `README.md`
> - **Course Repository**: [COMPUTER-NETWORKS](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)
> - **Release Date**: December 06, 2023
> - **License**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

<div align="center">

### Author

| <img src="https://avatars.githubusercontent.com/Amey-Thakur" width="110"/> <br> **[Amey Thakur](https://github.com/Amey-Thakur)** <br><br> [![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) |
| :---: |

</div>

## Description
This document provides comprehensive, step-by-step solutions to the **"IP and Subnet Practice Problems"** supplementary material. It covers IPv4 addressing, subnetting logic, VLSM (Variable Length Subnet Masking), IP datagram analysis, fragmentation, and routing table lookups.

### Technology Stack
- **Domain**: Network Engineering (IPv4/IPv6 Addressing)
- **Tools**: Binary Arithmetic, Subnet Logic

---

## Table of Contents
1.  [Binary to Dotted-Decimal Conversion](#question-1-change-the-following-ip-addresses-from-dotted-decimal-notation-to-binary-notation)
2.  [Dotted-Decimal to Binary Conversion](#question-2-change-the-following-ip-addresses-from-binary-notation-to-dotted-decimal-notation)
3.  [IP Class Identification](#question-3-find-the-class-of-the-following-ip-addresses)
4.  [CIDR Slash Notation](#question-4-write-the-following-masks-in-slash-notation-n)
5.  [Address Block Ranges](#question-5-find-the-range-of-addresses-in-the-following-blocks)
6.  [Subnetting Design (Fixed Length)](#question-6-an-organization-is-granted-the-block-21117180024-create-32-subnets)
7.  [IP Datagram Analysis & Fragmentation](#question-7-ipv4-datagram-analysis)
8.  [ISP Block Distribution (Subnetting)](#question-8-isp-block-161264020-distributed-to-8-organizations)
9.  [Variable Length Subnet Masking (VLSM)](#question-9-variable-length-subnet-formatting-vlsm)
10. [Hex Dump Header Analysis](#question-10-hex-dump-analysis-45000054-00030000-2006)
11. [Route Aggregation (Supernetting)](#question-11-route-aggregation-high-level-supernetting)
12. [Routing Table Lookup (Longest Prefix Match)](#question-12-routing-table-lookup-longest-prefix-match)
13. [IPv6 Address Compression](#question-13-ipv6-compression-shortest-form)

---

## Question 1: Change the following IP addresses from dotted-decimal notation to binary notation.

### Detailed Step-by-Step Analysis

> [!NOTE]
> **Mathematical Principle: Positional Notation**
>
> IPv4 addresses use a **base-2 (binary)** system where each position represents a power of 2. An 8-bit octet is calculated as:
>
> $$ \sum_{i=0}^{7} d_i \times 2^i $$
>
> Where $d_i$ is the bit value (0 or 1) at position $i$.

To convert a decimal octet (0-255) to an 8-bit binary segment, we decompose the number into sums of powers of 2.

| **Bit Position** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Power of 2** | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |

#### A. 114.34.2.8
*   **114** = 64 + 32 + 16 + 2 → `01110010`
*   **34** = 32 + 2 → `00100010`
*   **2** = 2 → `00000010`
*   **8** = 8 → `00001000`

**Result:** `01110010.00100010.00000010.00001000`

#### B. 129.14.6.8
*   **129** = 128 + 1 → `10000001`
*   **14** = 8 + 4 + 2 → `00001110`
*   **6** = 4 + 2 → `00000110`
*   **8** = 8 → `00001000`

**Result:** `10000001.00001110.00000110.00001000`

#### C. 208.34.54.12
*   **208** = 128 + 64 + 16 → `11010000`
*   **34** = 32 + 2 → `00100010`
*   **54** = 32 + 16 + 4 + 2 → `00110110`
*   **12** = 8 + 4 → `00001100`

**Result:** `11010000.00100010.00110110.00001100`

#### D. 238.34.2.1
*   **238** = 128 + 64 + 32 + 8 + 4 + 2 → `11101110`
*   **34** = 32 + 2 → `00100010`
*   **2** = 2 → `00000010`
*   **1** = 1 → `00000001`

**Result:** `11101110.00100010.00000010.00000001`

> [!TIP]
> **Memorization Strategy**
>
> Memorizing the "impostor" values like **128, 192, 224, 240, 248, 252, 254, 255** is crucial for subnetting. These specific sums of contiguous high-order bits appear frequently in subnet masks.

---

## Question 2: Change the following IP addresses from binary notation to dotted-decimal notation.

### Detailed Step-by-Step Analysis
Sum the values of the active bits (where the bit is `1`).

#### A. `01111111.11110000.01100111.01111101`
| Binary | Calculation | Decimal |
| :--- | :--- | :--- |
| `01111111` | 64+32+16+8+4+2+1 | **127** |
| `11110000` | 128+64+32+16 | **240** |
| `01100111` | 64+32+4+2+1 | **103** |
| `01111101` | 64+32+16+8+4+1 | **125** |

**Result:** `127.240.103.125`

#### B. `10101111.11000000.11111000.00011101`
| Binary | Calculation | Decimal |
| :--- | :--- | :--- |
| `10101111` | 128+32+8+4+2+1 | **175** |
| `11000000` | 128+64 | **192** |
| `11111000` | 128+64+32+16+8 | **248** |
| `00011101` | 16+8+4+1 | **29** |

**Result:** `175.192.248.29`

#### C. `11011111.10110000.00011111.01011101`
`11011111` (223) . `10110000` (176) . `00011111` (31) . `01011101` (93)
**Result:** `223.176.31.93`

#### D. `11101111.11110111.11000111.00011101`
`11101111` (239) . `11110111` (247) . `11000111` (199) . `00011101` (29)
**Result:** `239.247.199.29`

> [!TIP]
> **Calculation Shortcut**
>
> When converting high-density binary numbers (lots of 1s), it is often faster to subtract the value of the '0' positions from 255. For example, `11101111` has a 0 at the 16s place, so `255 - 16 = 239`.

---

## Question 3: Find the class of the following IP addresses.

### Detailed Analysis
The class is determined by the specific range of the first octet.

| Class | Range | Leading Bits | Bit Logic |
| :---: | :---: | :--- | :--- |
| **A** | 0 - 127 | `0...` | `00000000` to `01111111` |
| **B** | 128 - 191 | `10...` | `10000000` to `10111111` |
| **C** | 192 - 223 | `110...` | `11000000` to `11011111` |
| **D** | 224 - 239 | `1110...` | `11100000` to `11101111` |

**A. 208.34.54.12** → 208 is in 192-223 → **Class C**
**B. 238.34.2.1** → 238 is in 224-239 → **Class D** (Multicast)
**C. 114.34.2.8** → 114 is in 0-127 → **Class A**
**D. 129.14.6.8** → 129 is in 128-191 → **Class B**

> [!NOTE]
> **Legacy Context**
>
> While Classful addressing is technically obsolete due to **CIDR** (Classless Inter-Domain Routing), understanding it is essential for configuring legacy systems and knowing default subnet masks.

---

## Question 4: Write the following masks in slash notation (/n).

### Detailed Analysis
Count the contiguous "1" bits.

#### Quick Reference Strategy
| Mask | /8 | /16 | /24 | /32 |
| :--- | :---: | :---: | :---: | :---: |
| **Decimal** | 255.0.0.0 | 255.255.0.0 | 255.255.255.0 | 255.255.255.255 |
| **Role** | Class A | Class B | Class C | Host Route |

**A. 255.255.255.0**
`11111111.11111111.11111111.00000000` → 8+8+8 = **/24**

**B. 255.0.0.0**
`11111111.00000000...` → **/8**

**C. 255.255.224.0**
`11111111.11111111.11100000...` → 8+8+3 = **/19**

**D. 255.255.240.0**
`11111111.11111111.11110000...` → 8+8+4 = **/20**

> [!IMPORTANT]
> **Subnetting Mechanics**
>
> Every extra bit in the CIDR prefix **doubles** the number of subnets and **halves** the hosts per subnet. Moving from /19 to /20 splits the network exactly in half.

---

## Question 5: Find the range of addresses in the following blocks.

### Detailed Calculation
Formula: `Block Size = 2^(32 - Prefix)`

#### A. 123.56.77.32/29
*   **Block Size**: 2^(32-29) = 2^3 = **8** addresses.
*   **Boundary**: 32 is a multiple of 8 (0, 8, 16, 24, **32**, 40...).
*   **Range**: `123.56.77.32` to `123.56.77.39`

#### B. 200.17.21.128/27
*   **Block Size**: 2^5 = **32** addresses.
*   **Range**: `200.17.21.128` to `200.17.21.159`

#### C. 17.34.16.0/23
*   **Block Size**: 2^9 = **512** addresses.
*   **Span**: Covers 2 values in the third octet (16, 17).
*   **Range**: `17.34.16.0` to `17.34.17.255`

#### D. 180.34.64.64/30
*   **Block Size**: 2^2 = **4** addresses.
*   **Range**: `180.34.64.64` to `180.34.64.67`

> [!NOTE]
> **Industry Standard**
>
> The **/30** subnet is famously used for Point-to-Point router links because it provides exactly 2 usable IP addresses, maximizing address conservation.

---

## Question 6: An organization is granted the block 211.17.180.0/24. Create 32 subnets.

### Subnetting Design
1.  **Current Prefix**: /24
2.  **Required Subnets**: 32
3.  **Borrowing**: 2^s ≥ 32 → `s = 5` bits.
4.  **New Prefix**: /24 + 5 = **/29**

#### Binary Visualization of Borrowing
The following table visualizes how the subnet mask extends into the host portion.


| Segment | Binary Pattern | Decimal | Note |
| :--- | :--- | :--- | :--- |
| **Original Mask (/24)** | `11111111.11111111.11111111.00000000` | 255.255.255.0 | Default Class C |
| **Borrowed Bits (5)** | `........................11111...` | | 5 bits borrowed |
| **New Mask (/29)** | `11111111.11111111.11111111.11111000` | **255.255.255.248** | Target Subnet Mask |

| Parameter | Calculation | Result |
| :--- | :--- | :--- |
| **New Mask** | /29 (11111000) | **255.255.255.248** |
| **Block Size** | 2^(32-29) = 2^3 | **8** addresses |
| **Usable IPs** | 8 - 2 | **6** hosts/subnet |

#### Subnet 1 (Index 0)
*   **Start**: `211.17.180.0`
*   **End**: `211.17.180.7`

#### Subnet 32 (Index 31)
*   **Offset**: 31 * 8 = 248
*   **Start**: `211.17.180.248`
*   **End**: `211.17.180.255`

> [!TIP]
> **Boundary Check**
>
> Always verify the last subnet ends at the parent block's boundary. Here, both end at `.255`, confirming perfect alignment.

---

## Question 7: IPv4 Datagram Analysis

**Given**: `M=0`, `HLEN=5`, `Total Length=200`, `Offset=200`.

### Analysis

#### Relevant IP Header Fields
Visualizing the placement of the given values:

| Field | Value (Decimal) | Function |
| :--- | :--- | :--- |
| **Total Length** | **200** | Entire packet size (Header + Data) |
| **Identification** | [Unchanged] | Unique ID for reassembly |
| **Flags (M)** | **0** | `More Fragment` bit is OFF (Last Fragment) |
| **Fragment Offset** | **200** | Position of this fragment / 8 |

1.  **Offset Calculation**:
    The offset field is in 8-byte units.
    `True Offset = 200 * 8 = 1600 bytes`
    
    *   **First Byte Number**: **1600**

2.  **Payload Calculation**:
    `Header Size = HLEN(5) * 4 = 20 bytes`
    `Payload = Total(200) - Header(20) = 180 bytes`

3.  **Last Byte Calculation**:
    `Last Byte = First(1600) + Payload(180) - 1 = 1779`
    
    *   **Last Byte Number**: **1779**

4.  **Fragment Type**:
    *   **Offset > 0**: Not the first fragment.
    *   **M = 0**: No more fragments follow.
    *   **Result**: **Last Fragment**.

---

## Question 8: ISP Block 16.12.64.0/20 distributed to 8 organizations.

### Network Design
**ISP Block**: `16.12.64.0/20` (4096 Addresses)
**Requirement**: 8 subblocks of 256 addresses each.

**Allocation**: 256 addresses requires a **/24** mask.

| Org | Subblock | Range |
| :--- | :--- | :--- |
| **1** | `16.12.64.0/24` | 16.12.64.0 - 16.12.64.255 |
| **2** | `16.12.65.0/24` | 16.12.65.0 - 16.12.65.255 |
| **3** | `16.12.66.0/24` | 16.12.66.0 - 16.12.66.255 |
| **4** | `16.12.67.0/24` | 16.12.67.0 - 16.12.67.255 |
| **5** | `16.12.68.0/24` | 16.12.68.0 - 16.12.68.255 |
| **6** | `16.12.69.0/24` | 16.12.69.0 - 16.12.69.255 |
| **7** | `16.12.70.0/24` | 16.12.70.0 - 16.12.70.255 |
| **8** | `16.12.71.0/24` | 16.12.71.0 - 16.12.71.255 |

**Unallocated**: `16.12.72.0` to `16.12.79.255` (2048 addresses remaining).

---

## Question 9: Variable Length Subnet Formatting (VLSM)

**Block**: `80.70.56.0/21` (2048 IPs)

### Allocation Strategy (Largest First)
We must allocate larger blocks first to avoid fragmentation.

| Group | Org | Requirement | Allocated Block | Range | Broadcast Address |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **A** | 1 | 500 Hosts | **80.70.56.0/23** | .56.0 - .57.255 | 80.70.57.255 |
| **A** | 2 | 500 Hosts | **80.70.58.0/23** | .58.0 - .59.255 | 80.70.59.255 |
| | | | *Next Available* | *80.70.60.0* | |
| **B** | 3 | 250 Hosts | **80.70.60.0/24** | .60.0 - .60.255 | 80.70.60.255 |
| **B** | 4 | 250 Hosts | **80.70.61.0/24** | .61.0 - .61.255 | 80.70.61.255 |
| | | | *Next Available* | *80.70.62.0* | |
| **C** | 5 | 50 Hosts | **80.70.62.0/26** | .62.0 - .62.63 | 80.70.62.63 |
| **C** | 6 | 50 Hosts | **80.70.62.64/26** | .62.64 - .62.127 | 80.70.62.127 |
| **C** | 7 | 50 Hosts | **80.70.62.128/26** | .62.128 - .62.191 | 80.70.62.191 |
| | | | *Unallocated* | *80.70.62.192* | |

> [!WARNING]
> **VLSM Rule**
>
> The **"Largest First"** rule in VLSM is mandatory. Assigning small blocks first fractures the address space, making it impossible to fit large blocks later.

---

## Question 10: Hex Dump Analysis: 45000054 00030000 2006...

### Hex Interpretation
`45 00 00 54 00 03 00 00 20 06 ...`

*   **A. Header Size**: `4` (IPv4), `5` (5 words) → **20 bytes**.
*   **B. Options**: Size is exactly 20 bytes → **None**.
*   **C. Data Size**: Length `0054` (84) - Header (20) → **64 bytes**.
*   **D. Fragmentation**: Flags `00`, Offset `00` → **Not Fragmented**.
*   **E. TTL**: `20` (Hex) → **32 Hops**.
*   **F. Protocol**: `06` (Hex) → **TCP**.

#### Common Protocol Numbers
| Decimal | Hex | Protocol |
| :---: | :---: | :--- |
| **1** | `01` | **ICMP** (Ping) |
| **6** | `06` | **TCP** (Reliable) |
| **17** | `11` | **UDP** (Fast) |

---

## Question 11: Route Aggregation (High-Level Supernetting)

**Routes**:
1.  `16.27.24.0/26`
2.  `16.27.24.64/26`
3.  `16.27.24.128/25`

### Aggregation Logic
1.  Combine **1 & 2**: `16.27.24.0` (0-63) + `16.27.24.64` (64-127)
    → **16.27.24.0/25** (0-127)

2.  Combine **Result & 3**: `16.27.24.0/25` (0-127) + `16.27.24.128/25` (128-255)
    → **16.27.24.0/24** (0-255)

**Final Result**: `16.27.24.0/24`

### Binary Alignment Visualization
Aggregating routes requires finding the common high-order bits.

| Route | Binary Pattern (Third Octet) |
| :--- | :--- |
| **.0/26** | `000110`**`00`** |
| **.64/26** | `000110`**`00`** |
| **.128/25** | `000110`**`00`** |
| **Result (/24)** | **`00011000`** (Matches first 24 bits) |

---

## Question 12: Routing Table Lookup (Longest Prefix Match)

**Destination**: `142.150.71.132`

### Binary Prefix Matching Proof
**Destination**: `142.150.71.132` → `10001110.10010110.01000111.10000100`

| Route | Prefix | Destination (Relevant Octet) | Route Prefix (Relevant Octet) | Match? | Length |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **A** | /20 | `...0100 0111...` | `...0100 0000...` | **Yes** | 20 bits |
| **B** | /28 | `...01000111.1000...` | `...01000111.1000...` | **Yes** | **28 bits** |
| **C** | /16 | `...01000111...` | `... (Wildcard) ...` | **Yes** | 16 bits |
| **D** | /30 | `...10000100` | `...100000XX` | No | - |

**Decision**: The longest matching prefix is **/28** (Candidate B).
**Next Hop**: Interface B.

> [!IMPORTANT]
> **Routing Logic**
>
> **Longest Prefix Match** enables hierarchical routing, allowing a specific route (like /28) to override a general default path (like /16).

---

## Question 13: IPv6 Compression (Shortest Form)

### Compression Rules
1.  Drop leading zeros.
2.  Replace one consecutive string of zero blocks with `::`.

**A. 2340:1ABC:119A:A000:0000:0000:0000:0000**
→ `2340:1ABC:119A:A000::`

**B. 0000:00AA:0000:0000:0000:119A:A231**
→ `0:AA::119A:A231` (Compress middle 3 groups)

**C. 2340:0000:0000:0000:0000:119A:A001:0000**
→ `2340::119A:A001:0`

**D. 0000:0000:0000:2340:0000:0000:0000:0000**
→ `::2340:0:0:0:0` (or `0:0:0:2340::`)

> [!CAUTION]
> **Critical Error**
>
> Ambiguity (e.g., `1::1::1`) is fatal in IPv6. The `::` compression symbol can appear **only once** in an address.

---
<div align="center">

[**↑ Back to Top**](#ip-and-subnet-practice-problems---detailed-solutions)

[**← Back to Computer Networks**](https://github.com/Amey-Thakur/COMPUTER-NETWORKS)

</div>

---
<div align="center">

  ### 🎓 [MEng Computer Engineering Repository](https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING)

  **Computer Engineering (M.Eng) - University of Windsor**

  *An archival record of **graduate-level research** and **advanced engineering coursework**.*

</div>
