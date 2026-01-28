"""
@FileName: test.py
@Software: PyCharm

TEST GAN ANOMALY DETECTION
"""

from __future__ import print_function
import json
from sklearn.metrics import confusion_matrix
from options import Options
from lib.data import load_data
from lib.model import FlowGANAnomaly


def test():
    ## PARSE ARGUMENTS
    opt = Options().parse()
    opt.phase = 'test'   
    opt.isTrain = False
    opt.load_weights = True  

    ## LOAD DATA
    train_loader, testload = load_data(opt)

    ## LOAD MODEL
    model = FlowGANAnomaly(opt, train_loader)

    ## RUN TEST
    res = model.test_malware(testload)
    print("=== TEST RESULT ===")
    for k, v in res.items():
        print(f"{k}: {v}")

    print(">> TEST FINISHED")


if __name__ == '__main__':
    test()
