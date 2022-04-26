# coding=utf-8
from ligotools.readligo import loaddata,read_frame
from ligotools.readligo import FileList
from ligotools.utils import whitten, reqshift, write_wavfile, plot_helper, plot_one
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

import os
import json

def test_FileList():
    files = FileList()
    assert len(files.searchdir("data/")) == 10
def test_loaddata_file():
    file = "data/H-H1_LOSC_4_V2-1135136334-32.hdf5"
    output = loaddata(file, "H1")
    assert len(output[0]) == len(output[1])
def test_loaddata_output_types():
    file = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    output = loaddata(file, "H1")
    assert isinstance(output[0], np.ndarray)
    assert isinstance(output[1], np.ndarray)
    assert isinstance(output[2], dict)
def test_loaddata_files():
    file_h = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    file_l = "data/L-L1_LOSC_4_V2-1128678884-32.hdf5"
    output_h = loaddata(file, "H1")
    output_l = loaddata(file, "L1")
    assert output_h.shape == output_l.shape

file = "data/H-H1_LOSC_4_V2-1135136334-32.hdf5"
strain_H1, time_H1, chan_dict_H1 = loaddata(file, "H1")
events = json.load(open('data/BBH_events_v3.json',"r"))
event = events['GW150914']
fs = event['fs']  
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = fs*4)
psd_H1 = interp1d(freqs, Pxx_H1)
def test_whitten():
    strain_H1_whiten = whiten(strain_H1,psd_H1,time_H1[1] - time_H1[0])
    assert strain_H1_whiten.shape == strain_H1.shape
def test_write_wavfile():
    strain_H1_whiten = whiten(strain_H1,psd_H1,time_H1[1] - time_H1[0])
    write_wavfile('audio/test.wav', 1, strain_H1_whiten)
    assert os.path.exists("audio/test.wav")
    os.remove("audio/test.wav")
def test_reqshift():
    strain_H1_whiten = whiten(strain_H1,psd_H1,time_H1[1] - time_H1[0])
    test_reqshift = reqshift(strain_H1_whiten)
    assert isinstance(test_reqshift, np.ndarray)
def test_plot_helper():
    det = "L1"
    timemax = 1
    time = np.linspace(2.0, 3.0, num=5)
    SNR = np.sin(time)
    plot_one(det, time, timemax, SNR)
    assert plt.get_fignums() > 0