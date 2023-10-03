import streamlit as st
from helper import utils

utils.load_sidebar()

"""
### Retrieve secrets via Nautobot's shell_plus

1. Retrieve a secret for a given circuit.
It assumes that a relationship exists between __Circuits__ and __Secrets Groups__.
```
>>> from nautobot.extras.choices import SecretsGroupAccessTypeChoices, SecretsGroupSecretTypeChoices
>>> secret_from_circuit = RelationshipAssociation.objects.get(relationship=Relationship.objects.get(slug="circuit-to-secretsgroup").id, destination_id=Circuit.objects.get(cid='456').id).source.get_secret_value(access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC, secret_type=SecretsGroupSecretTypeChoices.TYPE_USERNAME)
>>> secret_from_circuit
'ath01user'
```
---
2. Retrieve a secret from a given device.
It assumes that a __Secrets Group__ has been assigned to the device.
```
>>> from nautobot.extras.choices import SecretsGroupAccessTypeChoices, SecretsGroupSecretTypeChoices
>>> d = Device.objects.first()
>>> secret_from_device = d.secrets_group.get_secret_value(access_type=SecretsGroupAccessTypeChoices.TYPE_GENERIC, secret_type=SecretsGroupSecretTypeChoices.TYPE_USERNAME)
>>> secret_from_device
'ath01user'
```
"""
