import os

# Cartella con i file XML
XML_DIR = os.path.join(os.path.dirname(__file__), 'xml')


def build_epp_login(user, password):
    """Legge il file login.xml e sostituisce i placeholder"""
    xml_file = os.path.join(XML_DIR, 'login.xml')
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    
    xml_content = xml_content.replace('$$USER$$', user)
    xml_content = xml_content.replace('$$PASSWORD$$', password)
    
    return xml_content


def build_epp_domain_info(domain):
    """Legge il file domain_info.xml e sostituisce i placeholder"""
    xml_file = os.path.join(XML_DIR, 'domain_info.xml')
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    
    xml_content = xml_content.replace('$$DOMAIN$$', domain)
    
    return xml_content


def build_epp_logout():
    """Legge il file logout.xml"""
    xml_file = os.path.join(XML_DIR, 'logout.xml')
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    
    return xml_content


def build_epp_delete_domain(domain):
    """Legge il file delete_domain.xml e sostituisce i placeholder"""
    xml_file = os.path.join(XML_DIR, 'delete_domain.xml')
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    
    xml_content = xml_content.replace('$$DOMAIN$$', domain)
    
    return xml_content
