# Subnetting — Worked Examples with Answers (beginner → advanced)

## Formula
- IPv4 total addresses = 2^(32 − prefix).
- Conventional usable host count = total − 2, excluding network and broadcast.
- Exceptions: /31 on point-to-point links permits both addresses by RFC 3021; /32 is a host route.
- Increment = 256 − the subnet mask octet where the prefix breaks.

## Example A — 192.168.1.70/26
- /26 mask `255.255.255.192`; block increment = 256−192 = 64.
- Blocks begin `.0`, `.64`, `.128`, `.192`; `.70` falls in `.64–.127`.
- Network = `192.168.1.64`; broadcast = `192.168.1.127`.
- Usable = `192.168.1.65 – 192.168.1.126` (62 addresses).

## Example B — 10.2.4.130/27
- Mask `255.255.255.224`; block increment 32.
- Blocks `.0,.32,.64,.96,.128,.160,.192,.224`.
- `.130` belongs `.128-.159`.
- Network `10.2.4.128`, broadcast `10.2.4.159`, usable `.129-.158` (30).

## Example C — /23 crossing a third/fourth octet boundary
- IP `172.16.9.45/23`; mask `255.255.254.0`.
- Third-octet increment = 2; 9 falls in 8–9.
- Network `172.16.8.0`; broadcast `172.16.9.255`.
- Usable `172.16.8.1` through `172.16.9.254` = 510.

## Example D — VLSM (90 + 40 + 20 clients from a /24)
Start `192.168.20.0/24`:

| Need | Chosen prefix | Network | Usable | Broadcast |
|---|---|---|---|---|
| 90 | /25 (126 usable) | 192.168.20.0/25 | .1–.126 | .127 |
| 40 | /26 (62 usable) | 192.168.20.128/26 | .129–.190 | .191 |
| 20 | /27 (30 usable) | 192.168.20.192/27 | .193–.222 | .223 |
| Reserve | /27 | 192.168.20.224/27 | .225–.254 | .255 |

**Why descending order?** Allocating largest blocks first makes alignment and nonoverlap simpler.

## Example E — Aggregation
`10.8.0.0/24`, `10.8.1.0/24`, `10.8.2.0/24`, `10.8.3.0/24` → `10.8.0.0/22` if all prefixes belong to you and a route aggregate is appropriate.

## Example F — IPv6
`2001:db8:1234::/48` can provide /64 segments such as `2001:db8:1234:1::/64`, `...:2::/64`, `...:3::/64`. IPv6 **does not have broadcast**, and you should not subtract two addresses using IPv4 rules.

## Practice (do without calculator)
1. `192.168.5.99/28`: network/broadcast/usable count?
2. `10.10.11.9/30`: network/broadcast?
3. `172.20.5.1/22`: network/broadcast?

### Answer key
1. Mask 255.255.255.240; increment 16; network `192.168.5.96`, broadcast `.111`, usable `.97-.110` = 14.
2. Increment 4, `.9` in `.8-.11`; network `10.10.11.8`, broadcast `.11`, usable `.9-.10`.
3. Third-octet increment 4; 5 in 4–7; network `172.20.4.0`, broadcast `172.20.7.255`.
