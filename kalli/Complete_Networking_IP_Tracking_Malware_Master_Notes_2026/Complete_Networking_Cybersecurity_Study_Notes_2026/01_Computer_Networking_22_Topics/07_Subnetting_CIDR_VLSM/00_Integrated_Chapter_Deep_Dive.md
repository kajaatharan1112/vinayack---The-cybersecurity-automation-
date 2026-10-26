# 07 — Integrated Deep-Dive Textbook: Subnetting CIDR VLSM

## Big Picture: what makes this chapter important?

Practice /24 to /30 calculations and advanced address allocation. A /26 means six host bits, 64 total IPv4 addresses. To find the network, use a 64-address block: the fourth octet .70 lies in .64-.127. CIDR route aggregation and VLSM are reverse skills: VLSM divides larger prefixes by actual need; aggregation combines aligned adjacent prefixes to reduce routing entries. Never add two discontiguous networks into an aggregate that includes addresses you do not own.

## Architecture / Packet Path Diagram

```text
192.168.20.0/24
  /25: .0-.127 (large)
  /26: .128-.191 (medium)
  /27: .192-.223 (small)
  /27: .224-.255 (reserve)
```

**Interpretation:** VLSM allocations must be aligned by block size; do large host requirements first and leave headroom. IPv6 host planning is different from IPv4.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Binary and Subnet Mask

**Definition and intuition:** Subnet mask ones indicate network bits; IPv4 prefix /24 = 255.255.255.0.

**Mechanism in plain terms:** AND operation IP & mask yields network ID.

**Industry situation:** 192.168.10.42/24 ⇒ network 192.168.10.0.

**Rare/advanced case to study next:** Non-contiguous masks not standard CIDR masks; binary thinking prevents errors.

**How you prove/disprove your first guess:** Do not confuse subnet address with first usable host.

**Mini exercise:** 192.168.10.42 decimal octets to binary and back எழுதவும்.

### 2. CIDR Network Broadcast Hosts

**Definition and intuition:** /26 block=64 addresses; network boundary increments 64; IPv4 broadcast highest address.

**Mechanism in plain terms:** Host bits=32-prefix; address count=2^hostbits; usual usable=total-2 except /31 and /32 special.

**Industry situation:** 192.168.1.70/26 ⇒ network .64, broadcast .127, usable .65-.126.

**Rare/advanced case to study next:** /31 point-to-point RFC3021 uses both addresses; /32 identifies single host.

**How you prove/disprove your first guess:** CIDR math IPv6-இல் broadcast இல்லை; same hosts formula not applied.

**Mini exercise:** Calculate 10.2.4.130/27 network, broadcast, usable count.

### 3. VLSM Address Allocation

**Definition and intuition:** Variable Length Subnet Mask chooses smallest block satisfying host count.

**Mechanism in plain terms:** Sort requirements descending, allocate aligned non-overlapping blocks.

**Industry situation:** 100 hosts need /25, 50 hosts /26, 12 hosts /28.

**Rare/advanced case to study next:** Summarization and future growth reserves important; don't fill every gap today.

**How you prove/disprove your first guess:** Poor VLSM layout leads overlapping prefixes and difficult aggregation.

**Mini exercise:** 192.168.20.0/24-ஐ 90/40/20 hosts-க்கு VLSM ஒதுக்கவும்.

### 4. Supernetting Route Aggregation

**Definition and intuition:** Adjacent networks combine into fewer routing entries when aligned.

**Mechanism in plain terms:** Router forwards longest prefix; aggregates /24s into /22 when contiguous aligned.

**Industry situation:** 10.8.0.0/24...10.8.3.0/24 ⇒ 10.8.0.0/22.

**Rare/advanced case to study next:** BGP route leaks/over-aggregation could blackhole valid destinations.

**How you prove/disprove your first guess:** Summary announce before ownership check risks routing traffic wrong.

**Mini exercise:** Represent 4 /24s as /22 and check boundaries.

### 5. IPv6 Prefix Planning

**Definition and intuition:** IPv6 large address space; /64 usual LAN subnet; /56 home delegation, /48 site patterns, policy varies.

**Mechanism in plain terms:** SLAAC typically depends on /64 for conventional Ethernet LAN.

**Industry situation:** 2001:db8:1234:10::/64 docs example; host bits 64.

**Rare/advanced case to study next:** Don't design IPv6 as IPv4 shortage; prefix hierarchy, security and logging still essential.

**How you prove/disprove your first guess:** IPv6 typo in compressed address can silently route wrong; expand before comparing.

**Mini exercise:** Split 2001:db8:1234::/48 into three /64 sample segments.

### 6. Subnetting Exam Patterns

**Definition and intuition:** Identify prefix, block size, network, first/last host, broadcast, next block.

**Mechanism in plain terms:** Power of two prefix blocks; calculate octet boundary then block increment.

**Industry situation:** /29 = 8 addresses = 6 conventional usable; next block jumps by 8.

**Rare/advanced case to study next:** IPv4 /31 and /32 exceptions; point-to-point design changes answer.

**How you prove/disprove your first guess:** Memorizing class A/B/C is not enough; modern classless routing dominates.

**Mini exercise:** Practice /22 /26 /29 /31 cases; explain steps not just numbers.

## Production-level decision checklist

1. **Boundary:** Which component has ownership of the behavior? Clarify endpoint, device, service and provider.
2. **Baseline:** What is expected when the system works? Record concrete route, protocol, log fields and time.
3. **Observation:** Which evidence supports the suspected cause and what is merely correlation?
4. **Security:** Which minimum privileges, segmented paths, keys and logging are required?
5. **Modern dependency:** What version/hardware/standard/vendor limitations change behavior?
6. **Roll-back plan:** Could a proposed fix break other users? Test in lab first.

## Chapter exam challenge

Explain at least three subtopics using a diagram; then provide one failure that could be misdiagnosed, the correct measurement, a modern industry exception, and an ethically safe lab demonstration.

## Official background

- [RFC 1918 Private IPv4](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 8200 IPv6](https://www.rfc-editor.org/rfc/rfc8200)
