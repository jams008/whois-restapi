from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from ipwhois import IPWhois
import whois, dns.resolver

app = FastAPI(title='WHOIS Domain')
v1 = FastAPI(title='API VERSION 1')

@app.get("/")
def hello():
    return {"SALALA LALA"}

# redirect url 
@app.get("/api", response_class=RedirectResponse, status_code=301)
async def redirect_url():
    return "/api/v1/"

# api v1 
@v1.get("/")
async def index():
    return {"API V1 WHOIS DOMAIN"}

@v1.get("/domain/{domain}")
async def domain(domain: str):
    data = whois.whois(domain)
    return data

@v1.get("/doamin/{domain}/expired")
async def expired(domain: str):
    data = whois.whois(domain)
    return data.expiration_date

@v1.get("/domain/{domain}/nameserver")
async def nameserver(domain: str):
    data = whois.whois(domain)
    return data.name_servers

@v1.get("/ip/{ip}")
async def ip(ip: str):
    data = IPWhois(ip)
    result = data.lookup_rdap(depth=1)
    return result

@v1.get("/dns/{domain}/{type_dns}")
async def dns_lookup(domain: str, type_dns: str):
    try:
        data = dns.resolver.query(domain, type_dns)
        results = []
        for result in data:
            results.append(result.to_text())
        return {'typedns_'+type_dns: results }
    except dns.resolver.NoAnswer:
        return {'Type dns '+ type_dns +' yang anda cari tidak ada'}
        

app.mount("/api/v1", v1)
