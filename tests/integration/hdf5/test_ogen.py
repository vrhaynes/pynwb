from pynwb.ogen import OptogeneticSeries, OptogeneticStimulusSite
from pynwb.device import Device
from pynwb.testing import NWBH5IOMixin, AcquisitionH5IOMixin, TestCase


class TestOptogeneticStimulusSiteIO(NWBH5IOMixin, TestCase):

    def setUpContainer(self):
        """ Return the test OptogeneticStimulusSite to read/write """
        self.device = Device(name='dev1')
        return OptogeneticStimulusSite('stim_site', self.device, 'my stim site', 300., 'in the brain')

    def addContainer(self, nwbfile):
        """ Add the test OptogeneticStimulusSite and Device to the given NWBFile """
        nwbfile.add_device(self.device)
        nwbfile.add_ogen_site(self.container)

    def getContainer(self, nwbfile):
        """ Return the test OptogeneticStimulusSite from the given NWBFile """
        return nwbfile.get_ogen_site(self.container.name)


class TestOptogeneticSeriesIO(AcquisitionH5IOMixin, TestCase):

    def setUpContainer(self):
        """ Return the test OptogeneticSeries to read/write """
        self.device = Device(name='dev1')
        self.ogen_stim_site = OptogeneticStimulusSite('stim_site', self.device, 'my stim site', 300., 'in the brain')
        return OptogeneticSeries('stim_series', [1., 2., 3.], self.ogen_stim_site, rate=100.)

    def addContainer(self, nwbfile):
        """
        Add the test OptogeneticSeries as an acquisition and add Device and OptogeneticStimulusSite to the given
        NWBFile
        """
        nwbfile.add_device(self.device)
        nwbfile.add_ogen_site(self.ogen_stim_site)
        nwbfile.add_acquisition(self.container)
