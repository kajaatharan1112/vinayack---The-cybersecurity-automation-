# Safe Practical Lab Setup (Windows + Kali Linux + Virtual Networking)

## Purpose
Learn with data you control. A university learning project is not authorization to scan nearby strangers, monitor other students, or run malware.

## Recommended topology (ASCII)

```text
                    YOUR PC / Host OS
                    |          |
             VM-A Linux    VM-B Windows/Linux
                 |            |
                 +-- Host-only/Internal virtual switch --+
                                  |
                         Optional lab router VM
                                  |
                       NO unauthorized external scan
```

### Safety choices
- **Host-only/internal network** keeps VM traffic from office/public Wi-Fi. VM NAT outbound connectivity can be used for package updates only where necessary; separate test networks from production.
- Make snapshots before changes; disable shared folders/clipboard for higher-risk exercises.
- Prefer **synthetic logs and harmless sample PCAPs**; don't execute unknown malware binaries.
- Never collect student or colleague browsing history, credentials, cookies, or packet contents without informed permission and organizational authorization.

## Known-safe observation commands

### Windows PowerShell (local device)
```powershell
ipconfig /all
route print
Get-NetTCPConnection | Select-Object -First 20
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
tracert example.com
Get-FileHash -Algorithm SHA256 .\your_own_file.txt
```
`Get-FileHash` requires the example file to exist; commands and output differ by OS/permissions/network policy.

### Linux (local device)
```bash
ip -br addr
ip route
ss -tuln
getent hosts example.com
ping -c 4 127.0.0.1
curl -I https://example.com
sha256sum your_own_file.txt
```

### Local HTTP test — only your own loopback
```bash
mkdir -p ~/network-lab
cd ~/network-lab
printf 'hello network lab\n' > index.html
python3 -m http.server 8000 --bind 127.0.0.1
```
In another terminal:
```bash
curl -v http://127.0.0.1:8000/
```
Then Ctrl+C to stop the server. This demonstrates socket, HTTP, response headers, and application data without reaching another host.

## Evidence notebook template
```text
Goal:
Ownership / authorization:
Date & timezone:
Topology and IP plan:
Prediction:
Command / method:
Observed output:
Alternative explanation:
Impact and rollback:
What I learned:
```

## Important modern caveats
- Remote host may filter ICMP; traceroute stars don't prove failure.
- `netstat`/`ss` listener data is **local**, not evidence you can access a remote service.
- Encryption prevents passive reading of modern web application content from ordinary packet metadata.
- A publicly visible IP or domain is not consent to actively audit or surveil it.
