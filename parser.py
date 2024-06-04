def parse_response(response):
    if response:
        versions = []
        for vuln in response:
            for affected in vuln.get('affected', []):
                versions.extend(affected.get('versions', []))
        sorted_versions = sorted(set(versions), key=lambda x: tuple(int(part) if part.isdigit() else part for part in x.split('.')))
        return sorted_versions
    else:
        return None
