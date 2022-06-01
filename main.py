from packages.engine.mamdani.driver import MamdaniInferenceEnginer as mmdn;
from packages.fis import FIS

if(__name__=='__main__'):
    mmd=mmdn()
    fis=FIS([1,2,3],mmd);
    fis.start();