import subprocess

def find_subdomains(domain):
    print(f"[+] Discovering subdomains for {domain}")
    try:
        result = subprocess.check_output(["subfinder", "-d", domain])
        subdomains = result.decode().splitlines()
        print(f"[+] Found {len(subdomains)} subdomains")
        return subdomains
    except Exception as e:
        print(f"[-] Error: {e}")
        return []
