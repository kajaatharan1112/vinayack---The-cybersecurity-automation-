# 19 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Cloud VPC VNet Subnets:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Cloud Security Groups NACL:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Hybrid VPN Private Connections:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Cloud NAT Endpoints and Egress:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Kubernetes Networking Services CNI:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Gateway API Service Mesh eBPF:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Cloud VPC VNet Subnets — Model answer:** VPC/VNet isolated virtual IP network; subnets and route tables segment cloud resources. **Working:** Cloud fabric maps virtual NICs and routes to gateways and endpoints. **Example:** Frontend public subnet; API private subnet; DB private subnet. **Nuance:** Account boundaries, shared VPC, transit routing, overlapping CIDRs. **Avoid:** Public subnet name alone doesn't give public IP or firewall access.

2. **Cloud Security Groups NACL — Model answer:** Security groups often stateful instance/ENI policy; network ACL often stateless subnet rules (provider-specific). **Working:** Allow ingress from trusted sources and egress to required deps; ephemeral responses vary by statefulness. **Example:** Only app security group can connect DB group on port 5432. **Nuance:** Identity policies/IAM complement network ACLs; cloud firewalls and inspection layers. **Avoid:** Misplaced 0.0.0.0/0 DB ingress risks exposure; check IPv6 ::/0 too.

3. **Hybrid VPN Private Connections — Model answer:** Site-to-site VPN encrypted overlay; dedicated link private connectivity; route exchange essential. **Working:** IPsec tunnels or carrier circuits join premises CIDRs to cloud VPC. **Example:** University campus apps reach cloud reporting DB over private VPN. **Nuance:** BGP dynamic failover, MTU, overlapping subnets and asymmetric routing. **Avoid:** Private dedicated link often not automatically encrypted; evaluate encryption.

4. **Cloud NAT Endpoints and Egress — Model answer:** Private instances may access external updates via NAT gateway while no inbound Internet path. **Working:** Routes direct public outbound through managed NAT; private endpoints bypass public routing. **Example:** Database servers update packages while accepting no unsolicited ingress. **Nuance:** PrivateLink/service endpoints, per-AZ egress patterns and cost observability. **Avoid:** NAT gateway is not web application firewall; needs SG and logging.

5. **Kubernetes Networking Services CNI — Model answer:** Pods receive IP, Services abstract replicas, CNI implements connectivity, kube-proxy/eBPF datapath routes. **Working:** Pod-to-Pod, ClusterIP, NodePort/LoadBalancer, NetworkPolicy define flows. **Example:** Web pod calls API service, API calls DB in private VPC. **Nuance:** Dual-stack clusters, topology hints, Gateway API and DNS service discovery. **Avoid:** NetworkPolicy enforcement depends compatible CNI; policy absent may allow all.

6. **Gateway API Service Mesh eBPF — Model answer:** Gateway API config L4/L7 routes; service mesh provides identity, policy, telemetry across service traffic. **Working:** GatewayClass/Gateway/HTTPRoute assign ingress roles; eBPF can enforce Linux datapath policies. **Example:** Microservices use mTLS and route 5% users to canary. **Nuance:** Cilium/Hubble eBPF, Envoy, sidecar vs ambient patterns, workload identity SPIFFE. **Avoid:** Adding mesh increases operational overhead and does not fix application bugs.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
