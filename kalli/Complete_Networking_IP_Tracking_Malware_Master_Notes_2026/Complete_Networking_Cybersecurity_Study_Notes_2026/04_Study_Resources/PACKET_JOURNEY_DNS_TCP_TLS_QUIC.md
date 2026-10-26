# Deep walkthrough: What REALLY Happens When You Open a Website?

Assume laptop opens `https://example.com`. Paths and ordering depend on browser caching, preconnect, HTTP/3, DoH, IPv4/IPv6.

```text
Laptop/browser
  | ① DNS resolver / cache (A, AAAA, maybe HTTPS/SVCB)
  | ② Destination selected (IPv4/IPv6), route check (local vs gateway)
  | ③ Neighbor discovery (ARP for IPv4; NDP for IPv6) toward next hop
  | ④ Ethernet/Wi-Fi → switch/AP → router → ISP → Internet/CDN
  | ⑤ TCP SYN→SYN/ACK→ACK + TLS1.3, OR QUIC/TLS1.3 over UDP
  | ⑥ HTTP request inside encrypted secure transport
  | ⑦ Reverse path response, streaming/chunking/caching/rendering
Browser renders page; JS loads more API/images independently
```

## Stage 1 — DNS
The browser might use OS cache, secure DNS resolver, and parallel A/AAAA/HTTPS queries. A DNS answer is a mapping hint, **not** absolute ownership or proof of user intent. CDN routing may return different addresses to different clients.

## Stage 2 — Local forwarding decision
OS checks destination against local subnet. For off-subnet IP, OS sends Ethernet/Wi-Fi frame to **default gateway MAC**, not the remote site's MAC. Router changes L2 framing on each hop. IP addresses usually remain but NAT may translate addresses/ports.

## Stage 3 — Connection & TLS
Classic HTTPS/1.1 or HTTP/2: TCP handshake, then TLS. HTTP/3: QUIC uses UDP and integrated TLS 1.3. Browser verifies server certificate identity. Shared CDN IP may host many domains.

## Stage 4 — What a packet capture actually shows
Packets may show IPs, ports, TCP flags, timing, bytes; modern HTTPS contents are encrypted. DNS may also be encrypted and ECH may hide parts of ClientHello, subject to deployment. **Do not assume packet capture reveals pages or passwords.**

## Stage 5 — User-visible failures and proof
| Browser symptom | First hypotheses | Next safe check |
|---|---|---|
| Name not resolved | DNS or resolver failure | Resolve-DnsName / nslookup |
| Timeout | route, ACL, dropped packets or server unresponsive | local route, gateway, owned firewall logs |
| Connection refused | remote/local listener absent or reset | service state on owned server |
| Certificate warning | bad trust, expiry, clock, hostname mismatch | certificate/clock details |
| HTTP 401/403 | application auth/policy | authorized application logs |
| HTTP 500/503 | application/dependency overload/error | server health and traces |
| Very slow | latency, loss, cache miss, server performance | break down DNS/connect/TLS/TTFB |

## Modern protocols
- **QUIC RFC 9000** includes streams and migration support.
- **HTTP/3 RFC 9114** maps HTTP semantics to QUIC.
- **DNS SVCB / HTTPS RFC 9460** publishes service endpoint/parameter hints.

## Exam challenge
Draw the flow, specify which components see plaintext application content, and explain why remote IP does not identify the user.
