# AlphaHunt Python SDK

# Overview

This is the official Python SDK for [AlphaHunt](https://alphahunt.io). It provides a simple interface for interacting with the AlphaHunt API.

# Installation

```bash
$ pip install 'git+https://github.com/csirtgadgets/alphahunt-sdk-py#egg=alphahunt_sdk'
```

# Basic Usage

## Simple IoC Query
```bash
% alphahunt -q 65.108.93.119 --insights | jq
{
  "last_at": "2024-06-19 22:28:35+00:00",
  "searched_by": [
    {
      "information": "2024-06-19T22:28:35"
    }
  ],
  "score": "medium",
  "metadata": {
    "q": "65.108.93.119",
    "geo": {
      "asn": 24940,
      "asn_desc": "Hetzner Online GmbH",
      "cc": "FI",
      "city": "Helsinki",
      "longitude": 24.9344,
      "latitude": 60.1797,
      "location": [
        24.9344,
        60.1797
      ],
      "timezone": "Europe/Helsinki",
      "region": "Uusimaa"
    },
    "rdata": [],
    "peers": [
      {
        "asn": "6939",
        "prefix": "65.108.0.0/16",
        "cc": "DE",
        "rir": "ripencc",
        "dt": "2001-02-09"
      },
      {
        "asn": "24940",
        "prefix": "65.108.0.0/16",
        "cc": "DE",
        "rir": "ripencc",
        "dt": "2001-02-09"
      }
    ],
    "whois": {
      "domain_name": "appone.cloud",
      "registrar": "Key-Systems, LLC",
      "whois_server": "http://www.key-systems.net",
      "referral_url": null,
      "updated_date": "2023-10-30 13:42:21+00:00",
      "creation_date": "2023-10-02 08:07:41+00:00",
      "expiration_date": "2024-10-02 08:07:41+00:00",
      "name_servers": [
        "ns3.second-ns.de",
        "ns1.your-server.de",
        "ns.second-ns.com"
      ],
      "status": "ok https://icann.org/epp#ok",
      "emails": "info@key-systems.net",
      "dnssec": "unsigned",
      "name": "REDACTED FOR PRIVACY",
      "org": "SACO Software and Consulting GmbH",
      "address": "REDACTED FOR PRIVACY",
      "city": "REDACTED FOR PRIVACY",
      "state": null,
      "registrant_postal_code": "REDACTED FOR PRIVACY",
      "country": "DE"
    }
  },
  "nodes": [
    {
      "id": "65.108.93.119",
      "tags": [
        "botnet_cc",
        "vidar"
      ],
      "provider": "threatfox.abuse.ch",
      "confidence": 100,
      "first_at": "2023-01-02T12:07:38+00:00",
      "last_at": "2023-01-02T12:07:38+00:00",
      "reported_at": "2023-01-02T12:07:38+00:00",
      "descriptions": [
        "Vidar",
        "Indicator that identifies a botnet command&control server (C&C)"
      ],
      "portlist": [],
      "geo": {
        "asn": 24940,
        "asn_desc": "Hetzner Online GmbH",
        "cc": "FI",
        "city": "Helsinki",
        "longitude": 24.9344,
        "latitude": 60.1797,
        "location": [
          24.9344,
          60.1797
        ],
        "timezone": "Europe/Helsinki",
        "region": "Uusimaa"
      },
      "references": [
        "https://threatfox.abuse.ch/ioc/1064362",
        "https://malpedia.caad.fkie.fraunhofer.de/details/win.vidar"
      ]
    },
    {
      "id": "http://65.108.93.119/1929",
      "tags": [
        "botnet_cc",
        "vidar"
      ],
      "provider": "threatfox.abuse.ch",
      "confidence": 100,
      "first_at": "2023-01-02T12:07:39+00:00",
      "last_at": "2023-01-02T12:07:39+00:00",
      "reported_at": "2023-01-02T12:07:39+00:00",
      "descriptions": [
        "Vidar",
        "Indicator that identifies a botnet command&control server (C&C)"
      ],
      "portlist": [],
      "geo": {
        "asn": 24940,
        "asn_desc": "Hetzner Online GmbH",
        "cc": "FI",
        "city": "Helsinki",
        "longitude": 24.9344,
        "latitude": 60.1797,
        "location": [
          24.9344,
          60.1797
        ],
        "timezone": "Europe/Helsinki",
        "region": "Uusimaa"
      },
      "references": [
        "https://threatfox.abuse.ch/ioc/1064363",
        "https://malpedia.caad.fkie.fraunhofer.de/details/win.vidar"
      ]
    },
    {
      "id": "http://65.108.93.119/1375",
      "tags": [
        "botnet_cc",
        "vidar"
      ],
      "provider": "threatfox.abuse.ch",
      "confidence": 100,
      "first_at": "2023-01-02T12:07:43+00:00",
      "last_at": "2023-01-02T12:07:43+00:00",
      "reported_at": "2023-01-02T12:07:43+00:00",
      "descriptions": [
        "Vidar",
        "Indicator that identifies a botnet command&control server (C&C)"
      ],
      "portlist": [],
      "geo": {
        "asn": 24940,
        "asn_desc": "Hetzner Online GmbH",
        "cc": "FI",
        "city": "Helsinki",
        "longitude": 24.9344,
        "latitude": 60.1797,
        "location": [
          24.9344,
          60.1797
        ],
        "timezone": "Europe/Helsinki",
        "region": "Uusimaa"
      },
      "references": [
        "https://threatfox.abuse.ch/ioc/1064369",
        "https://malpedia.caad.fkie.fraunhofer.de/details/win.vidar"
      ]
    },
    {
      "id": "http://65.108.93.119/",
      "tags": [
        "botnet_cc",
        "vidar"
      ],
      "provider": "threatfox.abuse.ch",
      "confidence": 100,
      "first_at": "2023-01-02T12:07:43+00:00",
      "last_at": "2023-01-02T12:07:43+00:00",
      "reported_at": "2023-01-02T12:07:43+00:00",
      "descriptions": [
        "Vidar",
        "Indicator that identifies a botnet command&control server (C&C)"
      ],
      "portlist": [],
      "geo": {
        "asn": 24940,
        "asn_desc": "Hetzner Online GmbH",
        "cc": "FI",
        "city": "Helsinki",
        "longitude": 24.9344,
        "latitude": 60.1797,
        "location": [
          24.9344,
          60.1797
        ],
        "timezone": "Europe/Helsinki",
        "region": "Uusimaa"
      },
      "references": [
        "https://threatfox.abuse.ch/ioc/1064370",
        "https://malpedia.caad.fkie.fraunhofer.de/details/win.vidar"
      ]
    }
  ],
  "related": {},
  "insights": "### Response to the Data\n\n#### Analysis Summary\nThe IP address 65[.]108.93.119 is associated with multiple indicators of compromise (IOCs) related to the Vidar malware, specifically as a botnet command and control (C&C) server. The data provided includes high-confidence reports from threat intelligence sources such as ThreatFox by abuse[.]ch.\n\n#### Key Points:\n1. **Tags**: The tags \"botnet_cc\" and \"vidar\" indicate that this IP is involved in botnet activities, specifically linked to the Vidar malware.\n2. **Score**: The score is marked as \"medium,\" indicating a moderate level of risk.\n3. **Geolocation**: The IP is registered under ASN 24940, Hetzner Online GmbH, located in Helsinki, Finland.\n4. **Recency**: The most recent activity was reported on January 2, 2023, which makes it older than 45 days but still relevant given the nature of botnet C&C servers which can remain active for extended periods.\n\n#### Reasoning:\n- **Botnet C&C Server**: Multiple references confirm that this IP address has been identified as a command and control server for the Vidar botnet.\n- **Confidence Level**: High confidence levels from reputable sources like ThreatFox reinforce the credibility of these findings.\n- **ASN Popularity**: Hetzner Online GmbH (ASN 24940) is a well-known hosting provider but not necessarily indicative of benign activity when associated with specific malicious tags like \"botnet_cc.\"\n\n### Threat Hunting Action Plan\n\n#### Next Steps:\n\n1. **Detection**\n   - Implement network monitoring rules to detect any traffic to or from 65[.]108.93.119.\n   - Use IDS/IPS systems to flag communications involving this IP.\n\n2. **Corrective Actions**\n   - Block all inbound and outbound traffic to/from 65[.]108.93.119 at your firewall or perimeter security devices.\n   - Review logs for any historical connections to this IP address and investigate potentially compromised hosts.\n\n3. **Mitigations**\n   - Apply MITRE ATT&CK techniques such as:\n     - T1071 (Application Layer Protocol): Monitor for unusual application layer protocol usage that may indicate C&C communication.\n     - T1090 (Connection Proxy): Detect use of proxies that could be used by malware for C&C communication.\n\n4. **Incident Response**\n   - If evidence of compromise is found, initiate incident response procedures including containment, eradication, and recovery steps according to your organization's IR plan.\n\n5. **User Awareness**\n   - Educate users about phishing attacks which are common vectors for initial infection by malware like Vidar.\n\n6. **Update Security Measures**\n   - Ensure antivirus/antimalware solutions are up-to-date with signatures capable of detecting Vidar-related threats.\n   - Regularly update software patches across all systems to mitigate vulnerabilities exploited by malware.\n\n### Conclusion\nGiven the medium score and high-confidence indicators linking this IP address to malicious activities related to Vidar botnet operations, immediate action should be taken to monitor and block traffic associated with it while investigating potential compromises within your network infrastructure.\n\nBy following these steps, you can effectively mitigate risks posed by this threat actor and enhance your organization's overall cybersecurity posture.\n\n\n"
}
}
```

## Research Question
```bash
% alphahunt --research "who is apt43?"                                                          
# Research Summary

The task was to perform a deep and technical analysis of the threat actor APT43, with a focus on its activities, tactics, techniques, and procedures (TTPs), and its impact on the technology sector, particularly CRM systems, and its alignment with NIST CSF Tier 2. APT43 is a North Korean cyber espionage group known for its sophisticated cyber operations aimed at supporting the North Korean regime's strategic objectives, including nuclear ambitions and financial gain through cybercrime.

## Assessment Rating

Rating: HIGH

The assessment rating for APT43 is HIGH due to the significant threat it poses to national security, financial stability, and critical infrastructure. APT43's activities are not only sophisticated but also persistent and adaptive, targeting high-value sectors such as government, defense, technology, and financial services. The group's ability to fund its operations through cybercrime, particularly cryptocurrency theft, further amplifies its threat level.

## Findings

1. **Attribution and Mission**: APT43 has been tracked since 2018 and is believed to operate on behalf of North Korea's Reconnaissance General Bureau (RGB). The group's activities align with North Korea's strategic intelligence priorities, including nuclear and geopolitical intelligence gathering.
   
2. **Financial Operations**: APT43 engages in cybercrime to fund its espionage activities. The group steals and launders cryptocurrency to purchase operational infrastructure, reducing financial strain on the North Korean government. They use hash rental and cloud mining services to convert stolen cryptocurrency into clean funds.

3. **Targeting and Tactics**: APT43 targets government, business services, manufacturing, education, research, and think tanks, particularly those focused on geopolitical and nuclear policy. The group uses sophisticated social engineering techniques, including creating spoofed personas and leveraging stolen personally identifiable information (PII) to conduct phishing attacks and register domains.

4. **Collaboration and Adaptability**: APT43 collaborates with other North Korean cyber espionage groups, sharing tools, infrastructure, and tactics. This collaboration enhances their operational capabilities and complicates attribution efforts for defenders.

5. **Malware and Tooling**: APT43 uses a variety of malware families, including PENCILDOWN, ROCKHATCH, and HANGMAN.V2. The group has also been observed using multi-platform malware such as POOLRAT, which targets Windows, Linux, and macOS systems.

6. **Impact on Technology Sector**: APT43's activities pose a significant threat to the technology sector, particularly CRM systems, as they target sensitive information and intellectual property. The group's focus on financial gain through cryptocurrency theft also impacts financial stability and trust in digital financial systems.

...
```

## Available Integrations
```bash
% alphahunt --integrations-available | jq
[
  {
    "name": "abusech_malwarebazaar",
    "description": "AbuseCH Malware Bazaar",
    "url": "https://bazaar.abuse.ch",
    "provides": [
      "md5",
      "sha1",
      "sha256"
    ],
    "requires_token": true,
    "free_tier": true
  },
  {
    "name": "abusech_threatfox",
    "description": "AbuseCH ThreatFox",
    "url": "https://threatfox.abuse.ch",
    "provides": [
      "url",
      "fqdn",
      "md5",
      "sha1",
      "sha256",
      "sha512",
      "ipv4",
      "ipv6"
    ],
    "requires_token": true,
    "free_tier": true
  },
  {
    "name": "abusech_urlhaus",
    "description": "AbuseCH URLhaus",
    "url": "https://urlhaus.abuse.ch",
    "provides": [
      "fqdn",
      "ipv4",
      "ipv6",
      "url"
    ],
    "requires_token": false,
    "free_tier": null
  },
  {
    "name": "blockchain",
    "description": "Blockchain",
    "url": "https://blockchain.com",
    "provides": [
      "btc",
      "bch"
    ],
    "requires_token": false,
    "free_tier": null
  },
...


```

```python
from alphahunt_sdk import integrations_available

for i in integrations_available():
    print(i)
```

## Search

```python

from alphahunt_sdk import search
from pprint import pprint

r = search('evilbit.com')
if r["score"] == "high":
    print("high score")
else:
    print("low score")

pprint(r)
```

## Research

```python
from alphahunt_sdk import research

r = research('who is apt43?')
print(r)
```

## Account

```bash

$ alphahunt --account
$ alphahunt --integrations  # list integrations
$ alphahunt --integration-enable <integration> [--token <token>]  # enable integration
$ alphahunt --integration-disable <integration>  # disable/remove integration
```

```python

from alphahunt_sdk import account, integrations, integration_enable, integration_disable
from pprint import pprint

pprint(account())

pprint(integrations())

integration_enable("urlscanio", "1234")
integration_disable("urlscanio")



```
