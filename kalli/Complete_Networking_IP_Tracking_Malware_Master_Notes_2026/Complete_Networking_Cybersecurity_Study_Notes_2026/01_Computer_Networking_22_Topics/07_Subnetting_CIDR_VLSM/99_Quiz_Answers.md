# 07 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Binary and Subnet Mask:** Define, draw its workflow, give a real example and identify one important limitation.

2. **CIDR Network Broadcast Hosts:** Define, draw its workflow, give a real example and identify one important limitation.

3. **VLSM Address Allocation:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Supernetting Route Aggregation:** Define, draw its workflow, give a real example and identify one important limitation.

5. **IPv6 Prefix Planning:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Subnetting Exam Patterns:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Binary and Subnet Mask — Model answer:** Subnet mask ones indicate network bits; IPv4 prefix /24 = 255.255.255.0. **Working:** AND operation IP & mask yields network ID. **Example:** 192.168.10.42/24 ⇒ network 192.168.10.0. **Nuance:** Non-contiguous masks not standard CIDR masks; binary thinking prevents errors. **Avoid:** Do not confuse subnet address with first usable host.

2. **CIDR Network Broadcast Hosts — Model answer:** /26 block=64 addresses; network boundary increments 64; IPv4 broadcast highest address. **Working:** Host bits=32-prefix; address count=2^hostbits; usual usable=total-2 except /31 and /32 special. **Example:** 192.168.1.70/26 ⇒ network .64, broadcast .127, usable .65-.126. **Nuance:** /31 point-to-point RFC3021 uses both addresses; /32 identifies single host. **Avoid:** CIDR math IPv6-இல் broadcast இல்லை; same hosts formula not applied.

3. **VLSM Address Allocation — Model answer:** Variable Length Subnet Mask chooses smallest block satisfying host count. **Working:** Sort requirements descending, allocate aligned non-overlapping blocks. **Example:** 100 hosts need /25, 50 hosts /26, 12 hosts /28. **Nuance:** Summarization and future growth reserves important; don't fill every gap today. **Avoid:** Poor VLSM layout leads overlapping prefixes and difficult aggregation.

4. **Supernetting Route Aggregation — Model answer:** Adjacent networks combine into fewer routing entries when aligned. **Working:** Router forwards longest prefix; aggregates /24s into /22 when contiguous aligned. **Example:** 10.8.0.0/24...10.8.3.0/24 ⇒ 10.8.0.0/22. **Nuance:** BGP route leaks/over-aggregation could blackhole valid destinations. **Avoid:** Summary announce before ownership check risks routing traffic wrong.

5. **IPv6 Prefix Planning — Model answer:** IPv6 large address space; /64 usual LAN subnet; /56 home delegation, /48 site patterns, policy varies. **Working:** SLAAC typically depends on /64 for conventional Ethernet LAN. **Example:** 2001:db8:1234:10::/64 docs example; host bits 64. **Nuance:** Don't design IPv6 as IPv4 shortage; prefix hierarchy, security and logging still essential. **Avoid:** IPv6 typo in compressed address can silently route wrong; expand before comparing.

6. **Subnetting Exam Patterns — Model answer:** Identify prefix, block size, network, first/last host, broadcast, next block. **Working:** Power of two prefix blocks; calculate octet boundary then block increment. **Example:** /29 = 8 addresses = 6 conventional usable; next block jumps by 8. **Nuance:** IPv4 /31 and /32 exceptions; point-to-point design changes answer. **Avoid:** Memorizing class A/B/C is not enough; modern classless routing dominates.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
