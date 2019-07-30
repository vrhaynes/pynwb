from hdmf.utils import docval, call_docval_func, popargs
from . import register_class, CORE_NAMESPACE
from .core import NWBContainer


@register_class('Device', CORE_NAMESPACE)
class Device(NWBContainer):
    """
    """

    __nwbfields__ = ('description',)

    @docval({'name': 'name', 'type': str, 'doc': 'the name of this device'},
            {'name': 'description', 'type': str, 'doc': 'Description of this processing module',
             'default': 'no description provided'},
            {'name': 'parent', 'type': 'NWBContainer',
             'doc': 'The parent NWBContainer for this NWBContainer', 'default': None})
    def __init__(self, **kwargs):
        d = popargs('description', kwargs)
        call_docval_func(super(Device, self).__init__, kwargs)
        self.description = d
