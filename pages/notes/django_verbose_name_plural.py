import streamlit as st
from helper import utils

utils.load_sidebar()

"""
### Query for a model's "verbose_name_plural"
```
In [4]: PeeringRole._meta.verbose_name_plural
Out[4]: 'BGP Peering Roles'
```
"""
