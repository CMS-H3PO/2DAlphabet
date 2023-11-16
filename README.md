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

To calculate expected limits, we first need to generate toy data in the pass category of the signal regions. For this we use the pass-to-fail transfer functions obtained from the control region fits. First we need to extract the fit parameter values which can be done using the following command
```
python printFitParameters.py -i 2017_boosted_CR/1_area/fitDiagnosticsTest.root
python printFitParameters.py -i 2017_semiboosted_CR/2_area/fitDiagnosticsTest.root
```
The printed fit parameter values need to be put into `plotRpf.py` which can be used to plot the transfer functions
```
python plotRpf.py
```
The toy data is generated using the `generateToys.py` script which imports the transfer functions from `plotRpf.py`
```
python generateToys.py -t /STORE/HHH/Histograms/2017/20231019_162502/TTbar_Histograms.root -d /STORE/HHH/Histograms/2017/20231019_162502/JetHT_Histograms.root
```
Two output files are produced, `JetHT_Histograms_VR_pass_toy.root` with the toy data in the pass category of the control regions and `JetHT_Histograms_SR_pass_toy.root` with the toy data in the pass category of the signal regions. These files need to be moved to the same folder with the other histogram files
```
mv JetHT_Histograms_*_pass_toy.root /STORE/HHH/Histograms/2017/20231019_162502/
```
The toy data in the control regions is used in `HHH_boosted_CR_pass_toy.py` and `HHH_semiboosted_CR_pass_toy.py` as a sanity check (closure test) to make sure that the toy data fits converge on parameter values similar to those used in the generation of the toy data. The parameter values can be checked with the following commands
```
python printFitParameters.py -i 2017_boosted_CR_pass_toy/1_area/fitDiagnosticsTest.root
python printFitParameters.py -i 2017_semiboosted_CR_pass_toy/2_area/fitDiagnosticsTest.root
```
after `HHH_boosted_CR_pass_toy.py` and `HHH_semiboosted_CR_pass_toy.py` are run.

To perform the same checks as for the control region fits and calculate expected limits for the benchmark XToYHTo6B_MX-2400_MY-800 case for the boosted selection, run
```
python -u HHH_boosted_SR_pass_toy.py |& tee boosted_SR_pass_toy_`date "+%Y%m%d_%H%M%S"`.log
```
To do the same for the semiboosted selection, run
```
python -u HHH_semiboosted_SR_pass_toy.py |& tee semiboosted_SR_pass_toy_`date "+%Y%m%d_%H%M%S"`.log
```

To calculate expected limits for multiple signal samples for the boosted selection, run
```
python -u HHH_boosted_SR_pass_toy_multiSignal.py |& tee boosted_SR_pass_toy_multiSignal_`date "+%Y%m%d_%H%M%S"`.log
```
To do the same for the semiboosted selection, run
```
python -u HHH_semiboosted_SR_pass_toy_multiSignal.py |& tee semiboosted_SR_pass_toy_multiSignal_`date "+%Y%m%d_%H%M%S"`.log
```
Note that some samples might require special processing with a modified `rMax` value for the limit calculation to converge.

Finally, to produce the expected limit plots, run
```
python plotLimits.py
```
