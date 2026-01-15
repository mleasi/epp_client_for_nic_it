#!/usr/bin/env python3

import sys
from config import EPP_HOST, EPP_PORT, EPP_USER, EPP_PASSWORD
from epp import EPPClient
from epp_builders import (
    build_epp_login,
    build_epp_domain_info,
    build_epp_logout,
    build_epp_delete_domain
)
from epp_utils import (
    extract_xml_from_response,
    extract_dns_info,
    filter_dns_info
)


def main():
    # Controlla parametri
    if len(sys.argv) < 2:
        print("Uso: main.py NOMEDOMINIO")
        sys.exit(1)
    
    domain = sys.argv[1]
    print(f"Connessione a EPP per dominio: {domain}\n")
    
    # Crea client EPP
    client = EPPClient(EPP_HOST, EPP_PORT)
    
    # --------- FACCIO LOGIN A EPP --------------
    print("[1] Logging in to EPP server...")
    login_xml = build_epp_login(EPP_USER, EPP_PASSWORD)
    login_response = client.send_request(login_xml)
    
    if not client.is_logged_in():
        print("❌ Login failed - no session cookie received")
        print(f"Response: {login_response[:500]}")
        return
    
    print(f"✓ Login successful! Session cookie: {client.session_cookie}\n")
    
    # --------- CHIEDO INFO PER DOMINIO -----------
    print(f"[2] Requesting domain info for {domain}...")
    domain_info_xml = build_epp_domain_info(domain)
    domain_info_response = client.send_request(domain_info_xml)
    
    # Estrai la parte XML
    xml_response = extract_xml_from_response(domain_info_response)
    print("✓ Domain info received\n")
    
    # --------- RACCOLGO I DATI DNS ----------------
    print("[3] Processing DNS records...")
    array_dns = extract_dns_info(xml_response)
    
    print(f"Found {len(array_dns)} lines in response\n")
    
    # Filtra i dati
    dns_da_rimuovere, contatti_tech = filter_dns_info(array_dns)
    
    print("=" * 60)
    print("NAMESERVER ATTUALI (da rimuovere):")
    print("=" * 60)
    for dns in dns_da_rimuovere:
        print(dns)
    
    print("\n" + "=" * 60)
    print("CONTATTI TECNICI:")
    print("=" * 60)
    for contact in contatti_tech:
        print(contact)
    
    # --------- CHIEDO CONFERMA PER ELIMINARE IL DOMINIO -----------
    print("\n" + "=" * 60)
    print("⚠️  ELIMINA DOMINIO")
    print("=" * 60)
    confirm = input(f"Sei sicuro di voler eliminare il dominio '{domain}'? (si/no): ").strip().lower()
    
    if confirm == 'si':
        print(f"\n[4] Deleting domain {domain}...")
        delete_domain_xml = build_epp_delete_domain(domain)
        
        print(f"delete_domain_xml: {delete_domain_xml}\n")
        
        delete_response = client.send_request(delete_domain_xml)
        
        # Estrai la parte XML
        delete_xml_response = extract_xml_from_response(delete_response)
        print("✓ Delete request sent")
        
        print(f"Response: {delete_xml_response}\n")
    else:
        print("Eliminazione annullata.\n")
    
    # --------- FACCIO LOGOUT DA EPP --------------
    print("[5] Logging out...")
    logout_xml = build_epp_logout()
    logout_response = client.send_request(logout_xml)
    print("✓ Logout successful\n")
    
    print("=" * 60)
    print("RIEPILOGO")
    print("=" * 60)
    print(f"Dominio: {domain}")
    print(f"Nameserver trovati: {len(dns_da_rimuovere)}")
    print(f"Contatti tecnici: {len(contatti_tech)}")


if __name__ == "__main__":
    main()
