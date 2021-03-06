Converting data to NWB
======================

The following are example Jupyter notebooks for converting custom lab data to NWB:

crcns-ret-1: Meister lab retina data
------------------------------------

* **Notebook:** https://github.com/NeurodataWithoutBorders/pynwb/blob/dev/docs/notebooks/convert-crcns-ret-1-meisterlab.ipynb
* **Example:** This example shows:

    * Use of ``UnitTimes``, ``SpikeUnit``, ``ImageSeries``, ``ElectrodeGroup``, ``EpochTimeSeries``, ``Device``
    * Creation and use of custom namespace and extension to extend ``ImageSeries`` to add custom metadata attributes
    * Create external link for ``ImageSeries.data``
    * Read of crcns-ret-1 dataset
    * Convert of the data to NWB
    * Comparison of H5Gate and PyNWB

* **Data:** Convert single-unit neural responses recorded from
  isolated retina from lab mice (Mus Musculus) using
  a 61-electrode array in response to various visual
  stimuli.  Recordings were done by Yifeng Zhang in
  Markus Meister's lab at Harvard University in 2008.
  Further description of the data are available here:
  https://crcns.org/data-sets/retina/ret-1/about-ret-1

* **Data Terms of use** The data used on the notebook and, therefore also the NWB files generated by the notebook are governed
  by the terms-of-use of CRCNS.org described here https://crcns.org/terms .

* **Comparison to NWB 1.0.x`:**

    * **Notebook:** https://github.com/NeurodataWithoutBorders/pynwb/blob/dev/docs/notebooks/convert-crcns-ret-1-meisterlab-compare-nwb-1.0.6.ipynb
    * **Description:** This notebook shows the convert of the same data using the original NWB 1.0.x API to allow for comparison of the
      NWB 1.0.x and NWB 2.x file.


