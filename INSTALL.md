```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_14
cd CMSSW_10_6_14/src
cmsenv
git clone git@github.com:CMS-H3PO/2DAlphabet.git/
git clone --branch 102x https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
curl -s https://raw.githubusercontent.com/mroguljic/CombineHarvester/master/CombineTools/scripts/sparse-checkout-ssh.sh | bash
scram b clean; scram b -j 10
cmsenv
cd 2DAlphabet
git checkout H3PO
cd ..
scram b -j4


python -m virtualenv twoD-env
source twoD-env/bin/activate
cd 2DAlphabet
python setup.py develop
```
