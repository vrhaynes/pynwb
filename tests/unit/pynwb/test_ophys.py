import unittest

from pynwb import TimeSeries
from pynwb.ophys import TwoPhotonSeries, RoiResponseSeries, DfOverF, Fluorescence, PlaneSegmentation, ImageSegmentation, OpticalChannel, ImagingPlane, ROI
from pynwb.image import ImageSeries, IndexSeries, ImageMaskSeries, OpticalSeries

import numpy as np


def CreatePlaneSegmentation():
    w, h = 5, 5;
    img_mask = [[0 for x in range(w)] for y in range(h)]
    w, h = 5, 2;
    pix_mask = [[0 for x in range(w)] for y in range(h)]
    pix_mask_weight = [0 for x in range(w)]
    iSS = ImageSeries('test_iS', 'a hypothetical source', list(), 'unit', ['external_file'], [1, 2, 3], 'tiff', timestamps=list())

    roi1 = ROI('roi1', 'roi description1', pix_mask, pix_mask_weight, img_mask, iSS)
    roi2 = ROI('roi2', 'roi description2', pix_mask, pix_mask_weight, img_mask, iSS)
    roi_list = (roi1, roi2)

    oc = OpticalChannel('description', 'emission_lambda')
    ip = ImagingPlane(oc, 'description', 'device', 'excitation_lambda', 'imaging_rate', 'indicator', 'location', (1, 2, 1, 2, 3), 4.0, 'unit', 'reference_frame')

    ps = PlaneSegmentation('name', 'description', roi_list, ip, iSS)
    return ps

class TwoPhotonSeriesConstructor(unittest.TestCase):
    def test_init(self):
        oc = OpticalChannel('description', 'emission_lambda')
        self.assertEqual(oc.description, 'description')
        self.assertEqual(oc.emission_lambda, 'emission_lambda')

        ip = ImagingPlane(oc, 'description', 'device', 'excitation_lambda', 'imaging_rate', 'indicator', 'location', (1, 2, 1, 2, 3), 4.0, 'unit', 'reference_frame')
        self.assertEqual(ip.optical_channel, oc)
        self.assertEqual(ip.device, 'device')
        self.assertEqual(ip.excitation_lambda, 'excitation_lambda')
        self.assertEqual(ip.imaging_rate, 'imaging_rate')
        self.assertEqual(ip.indicator, 'indicator')
        self.assertEqual(ip.location, 'location')
        self.assertEqual(ip.manifold, (1, 2, 1, 2, 3))
        self.assertEqual(ip.conversion, 4.0)
        self.assertEqual(ip.unit, 'unit')
        self.assertEqual(ip.reference_frame, 'reference_frame')

        tPS = TwoPhotonSeries('test_tPS', 'a hypothetical source', list(), 'unit', list(), ip, 1.0, 2.0, ['external_file'], [1, 2, 3], 'tiff', timestamps=list())
        self.assertEqual(tPS.name, 'test_tPS')
        self.assertEqual(tPS.source, 'a hypothetical source')
        self.assertEqual(tPS.unit, 'unit')
        self.assertEqual(tPS.field_of_view, list())
        self.assertEqual(tPS.imaging_plane, ip)
        self.assertEqual(tPS.pmt_gain, 1.0)
        self.assertEqual(tPS.scan_line_rate, 2.0)
        self.assertEqual(tPS.external_file, ['external_file'])
        self.assertEqual(tPS.starting_frame, [1, 2, 3])
        self.assertEqual(tPS.format, 'tiff')
        self.assertEqual(tPS.dimension, [np.nan])

class RoiResponseSeriesConstructor(unittest.TestCase):
    def test_init(self):
        ip = CreatePlaneSegmentation()
        iS = ImageSegmentation('test_iS', ip)

        ts = RoiResponseSeries('test_ts', 'a hypothetical source', list(), 'unit', ['name1'], iS, timestamps=list())
        self.assertEqual(ts.name, 'test_ts')
        self.assertEqual(ts.source, 'a hypothetical source')
        self.assertEqual(ts.unit, 'unit')
        self.assertEqual(ts.roi_names, ['name1'])
        self.assertEqual(ts.segmenttation_interface, iS)

class DfOverFConstructor(unittest.TestCase):
    def test_init(self):
        ip = CreatePlaneSegmentation()
        iS = ImageSegmentation('test_iS', ip)

        rrs = RoiResponseSeries('test_ts', 'a hypothetical source', list(), 'unit', ['name1'], iS, timestamps=list())

        dof = DfOverF('test_dof', rrs)
        self.assertEqual(dof.source, 'test_dof')
        self.assertEqual(dof.roi_response_series, rrs)

class FluorescenceConstructor(unittest.TestCase):
    def test_init(self):
        ip = CreatePlaneSegmentation()
        iS = ImageSegmentation('test_iS', ip)

        ts = RoiResponseSeries('test_ts', 'a hypothetical source', list(), 'unit', ['name1'], iS, timestamps=list())

        ff = Fluorescence('test_ff', ts)
        self.assertEqual(ff.source, 'test_ff')
        self.assertEqual(ff.roi_response_series, ts)

class ImageSegmentationConstructor(unittest.TestCase):

    def test_init(self):
        w, h = 5, 5;
        img_mask = [[0 for x in range(w)] for y in range(h)]
        w, h = 5, 2;
        pix_mask = [[0 for x in range(w)] for y in range(h)]
        pix_mask_weight = [0 for x in range(w)]
        iSS = ImageSeries('test_iS', 'a hypothetical source', list(), 'unit', ['external_file'], [1, 2, 3], 'tiff', timestamps=list())

        roi1 = ROI('roi1', 'roi description1', pix_mask, pix_mask_weight, img_mask, iSS)
        roi2 = ROI('roi2', 'roi description2', pix_mask, pix_mask_weight, img_mask, iSS)
        roi_list = (roi1, roi2)

        oc = OpticalChannel('description', 'emission_lambda')
        ip = ImagingPlane(oc, 'description', 'device', 'excitation_lambda', 'imaging_rate', 'indicator', 'location', (1, 2, 1, 2, 3), 4.0, 'unit', 'reference_frame')

        ps = PlaneSegmentation('name', 'description', roi_list, ip, iSS)

        iS = ImageSegmentation('test_iS', ps)
        self.assertEqual(iS.source, 'test_iS')
        self.assertEqual(iS.plane_segmentation, ps)

class PlaneSegmentationConstructor(unittest.TestCase):
    def test_init(self):
        w, h = 5, 5;
        img_mask = [[0 for x in range(w)] for y in range(h)]
        w, h = 5, 2;
        pix_mask = [[0 for x in range(w)] for y in range(h)]
        pix_mask_weight = [0 for x in range(w)]
        iSS = ImageSeries('test_iS', 'a hypothetical source', list(), 'unit', ['external_file'], [1, 2, 3], 'tiff', timestamps=list())

        roi1 = ROI('roi1', 'roi description1', pix_mask, pix_mask_weight, img_mask, iSS)
        roi2 = ROI('roi2', 'roi description2', pix_mask, pix_mask_weight, img_mask, iSS)
        roi_list = (roi1, roi2)

        oc = OpticalChannel('description', 'emission_lambda')
        ip = ImagingPlane(oc, 'description', 'device', 'excitation_lambda', 'imaging_rate', 'indicator', 'location', (1, 2, 1, 2, 3), 4.0, 'unit', 'reference_frame')

        iS = PlaneSegmentation('name', 'description', roi_list, ip, iSS)
        self.assertEqual(iS.name, 'name')
        self.assertEqual(iS.description, 'description')
        self.assertEqual(iS.roi_list, roi_list)
        self.assertEqual(iS.imaging_plane, ip)
        self.assertEqual(iS.reference_images, iSS)

if __name__ == '__main__':
    unittest.main()

