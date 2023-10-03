import streamlit as st
from helper import utils

utils.load_sidebar()

"""
### Powershell to use specific DNS server for specific domain

```
Add-DnsClientNrptRule -Namespace ".example.local" -NameServers "10.0.0.1"
```
"""
