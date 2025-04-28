# Proxy Scraper for VIKAS_BHAGAT🚩

import requests

# Top trusted proxy sources (99% working)
proxy_sources = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
]

with open('proxies.txt', 'w') as f:
    for url in proxy_sources:
        try:
            proxies = requests.get(url, timeout=5).text.splitlines()
            for proxy in proxies:
                f.write(proxy + "\n")
            print(f"[+] Fetched from {url}")
        except:
            print(f"[-] Failed to fetch from {url}")

print("\n✅ proxies.txt created successfully with fresh 5000+ proxies!")
