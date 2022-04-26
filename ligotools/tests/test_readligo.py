# from ligotools.readligo import loaddata, read_frame
# from ligotools.readligo import FileList
from ligotools import readligo as rl

def test_FileList():
    files = rl.FileList()
    assert len(files.searchdir('data/')) == 10

def test_loaddata_file_one():
    file = 'data/H-H1_LOSC_4_V2-1135136334-32.hdf5'
    output = rl.loaddata(file, 'H1')
    assert len(output[0]) == len(output[1])
    
def test_loaddata_file_two():
    file = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    output = rl.loaddata(file, 'H1')
    assert len(output[0]) == len(output[1])
    
def test_loaddata_file_three():
    file = 'data/L-L1_LOSC_4_V2-1128678884-32.hdf5'
    output = rl.loaddata(file, 'L1')
    assert len(output[0]) == len(output[1])
