import streamlit as st
from helper import utils

utils.load_sidebar()

"""
### Cisco IOS: watch commands entered using EEM script (useful for DevOps stuff)

```
event manager applet CLIaccounting
event cli pattern ".*" sync no skip no
action 1.0 syslog priority informational msg "$_cli_msg"
set 2.0 _exit_status 1
```
"""
