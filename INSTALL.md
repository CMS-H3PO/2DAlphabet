```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_14
cd CMSSW_10_6_14/src
cmsenv
git clone git@github.com:CMS-H3PO/2DAlphabet.git
git clone -b v8.2.1 https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
curl -s https://raw.githubusercontent.com/mroguljic/CombineHarvester/master/CombineTools/scripts/sparse-checkout-ssh.sh | bash
scram b -j 8

python -m virtualenv twoD-env
source twoD-env/bin/activate
cd 2DAlphabet
python setup.py develop
```

After installation, on new shell login:
```
cd CMSSW_10_6_14/src
cmsenv
source twoD-env/bin/activate
```
