import json

def generate_report(url, vuln_results, analysis):
    report = {
        "url": url,
        "scan_results": analysis
    }
    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("[+] Report saved as report.json")
