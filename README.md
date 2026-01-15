# Client EPP per NIC.it

Client Python per la gestione dei domini .it tramite EPP (Extensible Provisioning Protocol) sul registro NIC.it.

## Funzionalità:
- ✅ Login/logout EPP con gestione della sessione via HTTP/SSL
- ✅ Recupero delle informazioni di un dominio
- ✅ Elenco dei nameserver DNS
- ✅ Estrazione dei contatti tecnici
- ✅ Cancellazione del dominio (con richiesta di conferma)
- ✅ Architettura modulare basata su template XML
- ✅ Supporto alle estensioni EPP specifiche di NIC.it

## Requisiti:
- Python 3.6 o superiore
- Supporto SSL (integrato)

## Installazione
```bash
git clone https://github.com/mleasi/epp-client-nic-it
cd epp-client-nic-it
cp config.example.py config.py
```

Modifica il file `config.py` inserendo le credenziali EPP di NIC.it:

```python
EPP_HOST = 'epp.nic.it'
EPP_PORT = 443
EPP_USER = 'TUO_ID_REGISTRAR'
EPP_PASSWORD = 'TUA_PASSWORD'
```

## Utilizzo

```bash
python3 main.py yourdomain.it
```

## Struttura del progetto

```
├── main.py              # Main script
├── epp.py              # EPPClient class
├── epp_builders.py     # XML template builders
├── epp_utils.py        # Parsing utilities
├── config.py           # Configuration (not in repo)
├── config.example.py   # Configuration template
└── xml/                # EPP XML templates
    ├── login.xml
    ├── logout.xml
    ├── domain_info.xml
    └── delete_domain.xml
```

## Aggiungere nuovi comandi EPP

1. Crea un template XML nella cartella `xml/` con i segnaposto (e.g., `$$DOMAIN$$`)
2. Aggiungi la funzione builder in `epp_builders.py`
3. Utilizzala in `main.py` tramite `client.send_request()`

## Documentazione

- [NIC.it EPP Technical Guidelines](https://www.nic.it/sites/default/files/documenti/2024/Linee_Guida_Tecniche_Sincrone_v3_1_last.pdf)
