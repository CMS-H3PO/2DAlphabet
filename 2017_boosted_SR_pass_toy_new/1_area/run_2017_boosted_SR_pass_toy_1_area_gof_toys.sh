#!/bin/bash
echo RUNNING IN DIR: $(pwd)
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /users/ina/CMSSW_14_1_0_pre4
eval `scramv1 runtime -sh`
cd -
echo $*
$*
