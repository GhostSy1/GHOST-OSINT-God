import requests
from bs4 import BeautifulSoup
class WebsiteIntelligence:
    def __init__(self, url):
        self.url = url if url.startswith("http") else f"http://{url}"
    def get_tech_stack(self):
        try:
            res = requests.get(self.url, timeout=10)
            headers = res.headers
            soup = BeautifulSoup(res.text, 'html.parser')
            tech = []
            if 'Server' in headers: tech.append(f"Server: {headers['Server']}")
            if 'X-Powered-By' in headers: tech.append(f"Powered-By: {headers['X-Powered-By']}")
            scripts = [s.get('src') for s in soup.find_all('script') if s.get('src')]
            if any('jquery' in s.lower() for s in scripts): tech.append("Library: jQuery")
            if any('react' in s.lower() for s in scripts): tech.append("Framework: React")
            return tech
        except Exception:
            return []
    def get_whois(self, domain):
        try:
            import whois
            return whois.whois(domain)
        except Exception:
            return None
