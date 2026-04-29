import re

def is_valid_domain(domain):
    pattern = r"^[a-zA-Z0-9.-]+$"

    return re.match(pattern, domain)