# Installation (Lorien)

The following steps need to be done only once for the initial installation
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_14
cd CMSSW_10_6_14/src
cmsenv
git clone -b v8.2.1 https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
curl -s https://raw.githubusercontent.com/mroguljic/CombineHarvester/master/CombineTools/scripts/sparse-checkout-ssh.sh | bash
scram b -j 8
cd -

python -m virtualenv twoD-env
source twoD-env/bin/activate
git clone git@github.com:CMS-H3PO/2DAlphabet.git
cd 2DAlphabet
python setup.py develop
```
You now have all the required software installed and the enviroment set up.

To set up environment in a new shell, run the following
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd CMSSW_10_6_14
cmsenv
cd -
source twoD-env/bin/activate
cd 2DAlphabet
```
or alternatively just run
```
source 2DAlphabet/activate_env
cd 2DAlphabet
```

# Running fits

For running fits and making plots for the boosted control region, run
```
python -u HHH_boosted_CR.py |& tee boosted_CR_`date "+%Y%m%d_%H%M%S"`.log
```
To do the same for the semiboosted control region, run
```
python -u HHH_semiboosted_CR.py |& tee semiboosted_CR_`date "+%Y%m%d_%H%M%S"`.log
```
Note that piping output to the `tee` command will both print it to the terminal and save it in a log file. The log file name will contain a timestamp.

To calculate expected limits for the boosted selection, run
```
python -u HHH_boosted_SR.py |& tee boosted_SR_`date "+%Y%m%d_%H%M%S"`.log
```
To do the same for the semiboosted selection, run
```
python -u HHH_semiboosted_SR.py |& tee semiboosted_SR_`date "+%Y%m%d_%H%M%S"`.log
```
