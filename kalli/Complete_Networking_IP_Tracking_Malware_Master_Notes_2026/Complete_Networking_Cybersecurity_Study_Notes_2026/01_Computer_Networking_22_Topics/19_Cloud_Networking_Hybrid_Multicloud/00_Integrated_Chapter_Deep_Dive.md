# 19 — Integrated Deep-Dive Textbook: Cloud Networking Hybrid Multicloud

## Big Picture: what makes this chapter important?

VPC primitives, private access and distributed networks. Cloud VPC subnets and routes create reachability; identity/IAM and security groups determine authorization; private endpoints can keep provider-service traffic off the public Internet. Kubernetes pods and Services add another logical network layer. Gateway API creates portable ingress/mesh routing intent and Cilium can use eBPF for efficient data-path observability and policy.

## Architecture / Packet Path Diagram

```text
Office --IPsec/BGP--> Cloud VPC: public edge / private API / private DB
                    Kubernetes Pods --Service/Gateway--> clients
```

**Interpretation:** Cloud routes and security groups are independent, and Kubernetes networking has its own overlay/service policies. Private network does not imply IAM security.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Cloud VPC VNet Subnets

**Definition and intuition:** VPC/VNet isolated virtual IP network; subnets and route tables segment cloud resources.

**Mechanism in plain terms:** Cloud fabric maps virtual NICs and routes to gateways and endpoints.

**Industry situation:** Frontend public subnet; API private subnet; DB private subnet.

**Rare/advanced case to study next:** Account boundaries, shared VPC, transit routing, overlapping CIDRs.

**How you prove/disprove your first guess:** Public subnet name alone doesn't give public IP or firewall access.

**Mini exercise:** Design three-tier cloud app IP plan and exposure matrix.

### 2. Cloud Security Groups NACL

**Definition and intuition:** Security groups often stateful instance/ENI policy; network ACL often stateless subnet rules (provider-specific).

**Mechanism in plain terms:** Allow ingress from trusted sources and egress to required deps; ephemeral responses vary by statefulness.

**Industry situation:** Only app security group can connect DB group on port 5432.

**Rare/advanced case to study next:** Identity policies/IAM complement network ACLs; cloud firewalls and inspection layers.

**How you prove/disprove your first guess:** Misplaced 0.0.0.0/0 DB ingress risks exposure; check IPv6 ::/0 too.

**Mini exercise:** Write SG policy for web→API→DB and outbound DNS.

### 3. Hybrid VPN Private Connections

**Definition and intuition:** Site-to-site VPN encrypted overlay; dedicated link private connectivity; route exchange essential.

**Mechanism in plain terms:** IPsec tunnels or carrier circuits join premises CIDRs to cloud VPC.

**Industry situation:** University campus apps reach cloud reporting DB over private VPN.

**Rare/advanced case to study next:** BGP dynamic failover, MTU, overlapping subnets and asymmetric routing.

**How you prove/disprove your first guess:** Private dedicated link often not automatically encrypted; evaluate encryption.

**Mini exercise:** Diagram campus edge → VPN → cloud network → private service.

### 4. Cloud NAT Endpoints and Egress

**Definition and intuition:** Private instances may access external updates via NAT gateway while no inbound Internet path.

**Mechanism in plain terms:** Routes direct public outbound through managed NAT; private endpoints bypass public routing.

**Industry situation:** Database servers update packages while accepting no unsolicited ingress.

**Rare/advanced case to study next:** PrivateLink/service endpoints, per-AZ egress patterns and cost observability.

**How you prove/disprove your first guess:** NAT gateway is not web application firewall; needs SG and logging.

**Mini exercise:** Trace outbound flow private server to patch repository.

### 5. Kubernetes Networking Services CNI

**Definition and intuition:** Pods receive IP, Services abstract replicas, CNI implements connectivity, kube-proxy/eBPF datapath routes.

**Mechanism in plain terms:** Pod-to-Pod, ClusterIP, NodePort/LoadBalancer, NetworkPolicy define flows.

**Industry situation:** Web pod calls API service, API calls DB in private VPC.

**Rare/advanced case to study next:** Dual-stack clusters, topology hints, Gateway API and DNS service discovery.

**How you prove/disprove your first guess:** NetworkPolicy enforcement depends compatible CNI; policy absent may allow all.

**Mini exercise:** Draw pod → service → endpoint pod and DNS discovery.

### 6. Gateway API Service Mesh eBPF

**Definition and intuition:** Gateway API config L4/L7 routes; service mesh provides identity, policy, telemetry across service traffic.

**Mechanism in plain terms:** GatewayClass/Gateway/HTTPRoute assign ingress roles; eBPF can enforce Linux datapath policies.

**Industry situation:** Microservices use mTLS and route 5% users to canary.

**Rare/advanced case to study next:** Cilium/Hubble eBPF, Envoy, sidecar vs ambient patterns, workload identity SPIFFE.

**How you prove/disprove your first guess:** Adding mesh increases operational overhead and does not fix application bugs.

**Mini exercise:** Describe north-south vs east-west and write conceptual HTTPRoute mapping.

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

- [Kubernetes Gateway API Documentation](https://gateway-api.sigs.k8s.io/docs/introduction/)
- [Cilium eBPF Networking and Service Mesh](https://docs.cilium.io/en/stable/network/servicemesh/index.html)
