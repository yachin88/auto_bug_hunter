from discovery import find_subdomains
from vulnerability import run_vuln_scans
from ai_analysis import analyze
from report import generate_report

def main():
    url = input("Enter the target URL: ")

    print("[*] Finding subdomains...")
    subdomains = find_subdomains(url)

    print("[*] Running vulnerability scans...")
    vuln_results = run_vuln_scans(subdomains)

    print("[*] Analyzing results with AI...")
    analysis = analyze(vuln_results)

    print("[*] Generating report...")
    generate_report(url, vuln_results, analysis)

    print("[✓] Scan complete!")

if __name__ == "__main__":
    main()
