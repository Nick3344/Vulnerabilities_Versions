import requests

def fetch_vulnerabilities(name):
    ecosystems = ['Debian', 'Ubuntu']
    all_vulnerabilities = []
    url = "https://api.osv.dev/v1/query"

    for ecosystem in ecosystems:
        try:
            response = requests.post(url, json={
                "package": {
                    "name": name,
                    "ecosystem": ecosystem
                }
            })
            response.raise_for_status()
            data = response.json()
            all_vulnerabilities.extend(data.get('vulns', []))
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from osv.dev: {e}")

    return all_vulnerabilities
