import numpy as np
from collections import Iterable

from pynwb.core import docval, getargs, popargs
from ..container import NWBContainer

from .timeseries import TimeSeries, _default_conversion, _default_resolution

class OptogeneticSeries(TimeSeries):
    
    @docval({'name': 'name', 'type': str, 'doc': 'The name of this TimeSeries dataset'},
            {'name': 'source', 'type': str, 'doc': ('Name of TimeSeries or Modules that serve as the source for the data '
                                                   'contained here. It can also be the name of a device, for stimulus or '
                                                   'acquisition data')},
            {'name': 'data', 'type': (list, np.ndarray, 'TimeSeries'), 'doc': 'The data this TimeSeries dataset stores. Can also store binary data e.g. image frames'},
            {'name': 'site', 'type': str, 'doc': 'Name of the site description'},
            {'name': 'resolution', 'type': float, 'doc': 'The smallest meaningful difference (in specified unit) between values in data', 'default': _default_resolution},
            # Optional arguments:
            {'name': 'conversion', 'type': float, 'doc': 'Scalar to multiply each element in data to convert it to the specified unit', 'default': _default_conversion},

            ## time related data is optional, but one is required -- this will have to be enforced in the constructor
            {'name': 'timestamps', 'type': (list, np.ndarray, 'TimeSeries'), 'doc': 'Timestamps for samples stored in data', 'default': None},
            {'name': 'starting_time', 'type': float, 'doc': 'The timestamp of the first sample', 'default': None},
            {'name': 'rate', 'type': float, 'doc': 'Sampling rate in Hz', 'default': None},

            {'name': 'comments', 'type': str, 'doc': 'Human-readable comments about this TimeSeries dataset', 'default':None},
            {'name': 'description', 'type': str, 'doc': 'Description of this TimeSeries dataset', 'default':None},
            {'name': 'control', 'type': Iterable, 'doc': 'Numerical labels that apply to each element in data', 'default': None},
            {'name': 'control_description', 'type': Iterable, 'doc': 'Description of each control value', 'default': None},
            {'name': 'parent', 'type': 'NWBContainer', 'doc': 'The parent NWBContainer for this NWBContainer', 'default': None},
    )
    def __init__(self, **kwargs):
        name, source, data = getargs('name', 'source', 'data', kwargs)
        super(OptogeneticSeries, self).__init__(name, source, data, 'watt', **kwargs)
