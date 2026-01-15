def extract_xml_from_response(response_text):
    """Estrae la parte XML dalla risposta HTTP"""
    if '\r\n\r\n' in response_text:
        return response_text.split('\r\n\r\n', 1)[1]
    return response_text


def extract_dns_info(xml_response):
    """Estrae i record DNS dalla risposta XML"""
    array_dns = []
    
    for line in xml_response.split('\n'):
        line = line.strip()
        if line:
            array_dns.append(line)
    
    return array_dns


def filter_dns_info(array_dns):
    """
    Filtra i dati per ottenere:
    - dns_da_rimuovere: hostName (NS attuali)
    - contatti_tech: contatti tecnici
    """
    dns_da_rimuovere = []
    contatti_tech = []
    
    for record in array_dns:
        # Cerca i record di NS (hostName)
        if '<domain:hostName>' in record:
            # Estrai il nome host
            host_start = record.find('<domain:hostName>') + len('<domain:hostName>')
            host_end = record.find('</domain:hostName>')
            if host_end != -1:
                hostname = record[host_start:host_end]
                dns_da_rimuovere.append(f'<domain:hostAttr><domain:hostName>{hostname}</domain:hostName></domain:hostAttr>')
        
        # Cerca i contatti tecnici
        if '<domain:contact type="tech">' in record:
            contatti_tech.append(record)
    
    return dns_da_rimuovere, contatti_tech
