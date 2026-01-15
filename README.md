# EPP Client for NIC.it

Python client for managing .it domains via EPP (Extensible Provisioning Protocol) on NIC.it registry.

## Features

- ✅ EPP login/logout with session management via HTTP/SSL
- ✅ Domain information retrieval
- ✅ DNS nameserver listing
- ✅ Technical contacts extraction
- ✅ Domain deletion (with confirmation)
- ✅ Modular architecture with XML templates
- ✅ Support for NIC.it EPP extensions

## Requirements

- Python 3.6+
- SSL support (built-in)

## Installation

```bash
git clone https://github.com/yourusername/epp-client-nic-it
cd epp-client-nic-it
cp config.example.py config.py
```

Edit `config.py` with your NIC.it EPP credentials:

```python
EPP_HOST = 'epp.nic.it'
EPP_PORT = 443
EPP_USER = 'YOUR_REGISTRAR_ID'
EPP_PASSWORD = 'YOUR_PASSWORD'
```

## Usage

```bash
python3 main.py yourdomain.it
```

The script will:
1. Login to EPP server
2. Retrieve domain information
3. Display nameservers and technical contacts
4. Ask for confirmation to delete the domain
5. Logout from EPP server

## Project Structure

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

## Adding New EPP Commands

1. Create XML template in `xml/` folder with placeholders (e.g., `$$DOMAIN$$`)
2. Add builder function in `epp_builders.py`
3. Use in `main.py` with `client.send_request()`

## Documentation

- [NIC.it EPP Technical Guidelines](https://www.nic.it/sites/default/files/documenti/2024/Linee_Guida_Tecniche_Sincrone_v3_1_last.pdf)

## License

MIT License

## Disclaimer

This is an unofficial client. Use at your own risk. Always test on test domains first.
