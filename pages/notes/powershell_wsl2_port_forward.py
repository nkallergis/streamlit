import streamlit as st
from helper import utils

utils.load_sidebar()

"""
### Expose a WSL2 service to the LAN via PowerShell command

```
netsh interface portproxy add v4tov4 listenport=8000 listenaddress=(192.168.x.x) connectport=8000 connectaddress=$($(wsl hostname -I).Trim())
```
"""
