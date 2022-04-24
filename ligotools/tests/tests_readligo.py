from ligotools.readligo import loaddata, read_frame
from ligotools.readligo import FileList


def test_FileList():
    files = FileList()
    assert len(files.searchdir('data/')) == 10

def test_loaddata_file_one():
    file = 'data/H-H1_LOSC_4_V2-1135136334-32.hdf5'
    output = loaddata(file, 'H1')
    assert len(output[0]) == len(output[1])
    
def test_loaddata_file_two():
    file = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    output = loaddata(file, 'H1')
    assert len(output[0]) == len(output[1])
    
def test_loaddata_file_three():
    file = 'data/L-L1_LOSC_4_V2-1128678884-32.hdf5'
    output = loaddata(file, 'L1')
    assert len(output[0]) == len(output[1])
