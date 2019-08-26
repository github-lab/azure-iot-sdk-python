# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509Thumbprint(Model):
    """X509Thumbprint.

    :param primary_thumbprint:
    :type primary_thumbprint: str
    :param secondary_thumbprint:
    :type secondary_thumbprint: str
    """

    _attribute_map = {
        "primary_thumbprint": {"key": "primaryThumbprint", "type": "str"},
        "secondary_thumbprint": {"key": "secondaryThumbprint", "type": "str"},
    }

    def __init__(self, primary_thumbprint=None, secondary_thumbprint=None):
        super(X509Thumbprint, self).__init__()
        self.primary_thumbprint = primary_thumbprint
        self.secondary_thumbprint = secondary_thumbprint
