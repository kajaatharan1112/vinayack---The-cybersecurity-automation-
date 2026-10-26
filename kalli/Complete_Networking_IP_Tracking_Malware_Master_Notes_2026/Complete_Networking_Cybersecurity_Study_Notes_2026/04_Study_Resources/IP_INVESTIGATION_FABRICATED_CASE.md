# Worked case — Suspicious Remote IP on YOUR API (fabricated log)

This training scenario uses documentation prefix **203.0.113.0/24**, not a real target.

## Evidence
```text
2026-10-26T03:00:01Z src=203.0.113.24  method=POST path=/login status=401 user=test01
2026-10-26T03:00:04Z src=203.0.113.24  method=POST path=/login status=401 user=test01
2026-10-26T03:00:08Z src=203.0.113.24  method=POST path=/login status=401 user=test02
2026-10-26T03:00:12Z src=203.0.113.24  method=GET  path=/help  status=200 user=-
2026-10-26T03:00:15Z src=198.51.100.10 method=GET path=/status status=200 user=-
```

## Question 1: What is proven?
There were three failed authentication requests observed by this **fictional server**, from the same **logged source address** in a 7-second span. The server log has not yet proven who issued the requests or whether they are malicious.

## Question 2: What is NOT proven?
Not the country/city/house, username behind a NAT, remote desktop activity, files accessed on source computer, browser history, or the user's intention.

## Question 3: What extra authorized evidence would help?
- App authentication outcome and account ID, device/session metadata in privacy-approved logs.
- Reverse proxy trust chain: was client IP extracted safely from trusted proxy headers?
- Rate baseline and legitimate integration/job patterns.
- Owned firewall flow/NAT records and synchronized timestamps.
- Threat feeds as **supporting hints**, not verdicts.

## Question 4: A proportionate response
Temporarily enforce rate limits on login endpoint, require phishing-resistant MFA if applicable, notify the on-call owner, preserve short-lived logs, investigate false-positive integrations, and document rollback. Do not publicly accuse a person or scan unknown host.

## Investigation template
| Field | Value |
|---|---|
| Scope | Own API logs only |
| Initial observation | 3 × HTTP 401 / 7 seconds |
| Attribution confidence | Low (source IP is not identity) |
| Alternatives | Human mistake, broken mobile app, automated attacker |
| Next step | Correlate app logs and trusted proxy chain |
| Legal/privacy | Minimize retention/access |
