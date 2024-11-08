import whois
import re
from utils import validate_domain

def get_whois_data(domain):
    try:
        domain_info = whois.whois(domain)
        return {
            "domain_name": domain_info.domain_name,
            "creation_date": domain_info.creation_date,
            "expiration_date": domain_info.expiration_date,
            "registrar": domain_info.registrar,
            "status": domain_info.status
        }
    except Exception as e:
        return {"error": str(e)}

def analyze_whois_data(domain_data):
    suspicious_patterns = {
        "short_registration_period": lambda creation, expiration: (
            expiration - creation).days < 365 if creation and expiration else False,
        "unusual_registrar": r"(cheap|free|unknown|untrusted)",
        "status_flags": r"(clientHold|serverHold|redemptionPeriod)",
        "domain_name_suspicious_pattern": r"(login|secure|verify|update|pay|account|bank|[0-9]+|[-]{2,})"
    }
    
    # Registration period analysis
    short_reg_period = suspicious_patterns["short_registration_period"](
        domain_data.get("creation_date"), domain_data.get("expiration_date"))
    
    # Registrar analysis
    registrar = domain_data.get("registrar", "").lower() if domain_data.get("registrar") else ""
    registrar_flagged = bool(re.search(suspicious_patterns["unusual_registrar"], registrar))
    
    # Status analysis
    status = " ".join(domain_data.get("status", [])).lower() if domain_data.get("status") else ""
    status_flagged = bool(re.search(suspicious_patterns["status_flags"], status))
    
    # Domain name
    domain_name = domain_data.get("domain_name", "")
    if isinstance(domain_name, list):
        domain_name = domain_name[0]
    domain_name_flagged = bool(re.search(suspicious_patterns["domain_name_suspicious_pattern"], domain_name.lower()))
    
    return {
        "short_registration_period": short_reg_period,
        "registrar_flagged": registrar_flagged,
        "status_flagged": status_flagged,
        "domain_name_flagged": domain_name_flagged
    }