import requests
import socket
import dns.resolver
class IntelligenceEngine:
    def __init__(self, target):
        self.target = target
    def get_ip_info(self, ip):
        try:
            res = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()
            return res if res['status'] == 'success' else None
        except Exception:
            return None
    def get_dns_records(self, domain):
        records = {}
        types = ['A', 'MX', 'NS', 'TXT']
        for r_type in types:
            try:
                answers = dns.resolver.resolve(domain, r_type)
                records[r_type] = [str(rdata) for r in answers for rdata in r.address] if r_type == 'A' else [str(rdata) for rdata in answers]
            except Exception:
                records[r_type] = []
        return records
    def resolve_domain(self, domain):
        try:
            return socket.gethostbyname(domain)
        except Exception:
            return None
