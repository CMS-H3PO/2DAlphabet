from HHH_base_singleChannel import *
from argparse import ArgumentParser
import os


if __name__ == '__main__':
    # usage example
    Description = "Example: %(prog)s -y 2017"

    # input parameters
    parser = ArgumentParser(description=Description)

    parser.add_argument("-y", "--year", dest="year",
                        help="Data taking year(s) (e.g. 2017, Run2)",
                        required=True,
                        metavar="YEAR")

    (options, args) = parser.parse_known_args()






    #all signal datasets
    sigNames = [
          "XToYHTo6B_MX-1300_MY-250", "XToYHTo6B_MX-1300_MY-300", "XToYHTo6B_MX-1300_MY-350", "XToYHTo6B_MX-1300_MY-400", "XToYHTo6B_MX-1300_MY-450", "XToYHTo6B_MX-1300_MY-500",
          "XToYHTo6B_MX-1400_MY-250", "XToYHTo6B_MX-1400_MY-300", "XToYHTo6B_MX-1400_MY-350", "XToYHTo6B_MX-1400_MY-400", "XToYHTo6B_MX-1400_MY-450", "XToYHTo6B_MX-1400_MY-500",
          "XToYHTo6B_MX-1500_MY-250", "XToYHTo6B_MX-1500_MY-300", "XToYHTo6B_MX-1500_MY-350", "XToYHTo6B_MX-1500_MY-400", "XToYHTo6B_MX-1500_MY-450", "XToYHTo6B_MX-1500_MY-500",
          "XToYHTo6B_MX-1600_MY-250", "XToYHTo6B_MX-1600_MY-300", "XToYHTo6B_MX-1600_MY-350", "XToYHTo6B_MX-1600_MY-400", "XToYHTo6B_MX-1600_MY-450", "XToYHTo6B_MX-1600_MY-500",
          "XToYHTo6B_MX-1700_MY-250", "XToYHTo6B_MX-1700_MY-300", "XToYHTo6B_MX-1700_MY-350", "XToYHTo6B_MX-1700_MY-400", "XToYHTo6B_MX-1700_MY-450", "XToYHTo6B_MX-1700_MY-500",
          "XToYHTo6B_MX-1800_MY-250", "XToYHTo6B_MX-1800_MY-300", "XToYHTo6B_MX-1800_MY-350", "XToYHTo6B_MX-1800_MY-400", "XToYHTo6B_MX-1800_MY-450", "XToYHTo6B_MX-1800_MY-500",
          "XToYHTo6B_MX-1900_MY-250", "XToYHTo6B_MX-1900_MY-300", "XToYHTo6B_MX-1900_MY-350", "XToYHTo6B_MX-1900_MY-400", "XToYHTo6B_MX-1900_MY-450", "XToYHTo6B_MX-1900_MY-500",
          "XToYHTo6B_MX-2000_MY-250", "XToYHTo6B_MX-2000_MY-300", "XToYHTo6B_MX-2000_MY-350", "XToYHTo6B_MX-2000_MY-400", "XToYHTo6B_MX-2000_MY-450", "XToYHTo6B_MX-2000_MY-500", "XToYHTo6B_MX-2000_MY-600",
          "XToYHTo6B_MX-2200_MY-250", "XToYHTo6B_MX-2200_MY-300", "XToYHTo6B_MX-2200_MY-350", "XToYHTo6B_MX-2200_MY-400", "XToYHTo6B_MX-2200_MY-450", "XToYHTo6B_MX-2200_MY-500", "XToYHTo6B_MX-2200_MY-600",
          "XToYHTo6B_MX-2400_MY-250", "XToYHTo6B_MX-2400_MY-300", "XToYHTo6B_MX-2400_MY-350", "XToYHTo6B_MX-2400_MY-400", "XToYHTo6B_MX-2400_MY-450", "XToYHTo6B_MX-2400_MY-500", "XToYHTo6B_MX-2400_MY-600",
          "XToYHTo6B_MX-2500_MY-250", "XToYHTo6B_MX-2500_MY-300", "XToYHTo6B_MX-2500_MY-350", "XToYHTo6B_MX-2500_MY-400", "XToYHTo6B_MX-2500_MY-450", "XToYHTo6B_MX-2500_MY-500", "XToYHTo6B_MX-2500_MY-600", "XToYHTo6B_MX-2500_MY-700",
          "XToYHTo6B_MX-2600_MY-250", "XToYHTo6B_MX-2600_MY-300", "XToYHTo6B_MX-2600_MY-350", "XToYHTo6B_MX-2600_MY-400", "XToYHTo6B_MX-2600_MY-450", "XToYHTo6B_MX-2600_MY-500", "XToYHTo6B_MX-2600_MY-600", "XToYHTo6B_MX-2600_MY-700", "XToYHTo6B_MX-2600_MY-800",
          "XToYHTo6B_MX-2800_MY-250", "XToYHTo6B_MX-2800_MY-300", "XToYHTo6B_MX-2800_MY-350", "XToYHTo6B_MX-2800_MY-400", "XToYHTo6B_MX-2800_MY-450", "XToYHTo6B_MX-2800_MY-500", "XToYHTo6B_MX-2800_MY-600", "XToYHTo6B_MX-2800_MY-700", "XToYHTo6B_MX-2800_MY-800",
          "XToYHTo6B_MX-3000_MY-250", "XToYHTo6B_MX-3000_MY-300", "XToYHTo6B_MX-3000_MY-350", "XToYHTo6B_MX-3000_MY-400", "XToYHTo6B_MX-3000_MY-450", "XToYHTo6B_MX-3000_MY-500", "XToYHTo6B_MX-3000_MY-600", "XToYHTo6B_MX-3000_MY-700", "XToYHTo6B_MX-3000_MY-800",
          "XToYHTo6B_MX-3500_MY-250", "XToYHTo6B_MX-3500_MY-300", "XToYHTo6B_MX-3500_MY-350", "XToYHTo6B_MX-3500_MY-400", "XToYHTo6B_MX-3500_MY-450", "XToYHTo6B_MX-3500_MY-500", "XToYHTo6B_MX-3500_MY-600", "XToYHTo6B_MX-3500_MY-700", "XToYHTo6B_MX-3500_MY-800",
          "XToYHTo6B_MX-4000_MY-250", "XToYHTo6B_MX-4000_MY-300", "XToYHTo6B_MX-4000_MY-350", "XToYHTo6B_MX-4000_MY-400", "XToYHTo6B_MX-4000_MY-450", "XToYHTo6B_MX-4000_MY-500", "XToYHTo6B_MX-4000_MY-600", "XToYHTo6B_MX-4000_MY-700", "XToYHTo6B_MX-4000_MY-800", "XToYHTo6B_MX-4000_MY-900"
    ]

    r_Min = -1
    r_Max = 1
    strat = 1



#    sigNames = ["XToYHTo6B_MX-3500_MY-350", "XToYHTo6B_MX-4000_MY-300"]

 #   r_Min = -1
  #  r_Max = 3
   # strat = 2


#    sigNames = ["XToYHTo6B_MX-2800_MY-350"]

 #   r_Min = -1
  #  r_Max = 5
   # strat = 2


#    sigNames = ["XToYHTo6B_MX-1400_MY-350", "XToYHTo6B_MX-1600_MY-250", "XToYHTo6B_MX-1700_MY-500", "XToYHTo6B_MX-1800_MY-350", "XToYHTo6B_MX-2800_MY-350"]

 #   r_Min = -1
  #  r_Max = 1
   # strat = 2



#    sigNames = ["XToYHTo6B_MX-2800_MY-350", "XToYHTo6B_MX-3000_MY-350", "XToYHTo6B_MX-3500_MY-300", "XToYHTo6B_MX-4000_MY-350"]

 #   r_Min = -1
  #  r_Max = 3
   # strat = 1



    bestOrder = {"{}_boosted_SR_pass_toy_multiSignal".format(options.year):"1"}
    for working_area in ["{}_boosted_SR_pass_toy_multiSignal".format(options.year)]:

        jsonConfig   = 'configs/HHH/{0}.json'.format(working_area)

        test_make(working_area,jsonConfig) # this line can be commented out when reprocessing a subset of signal samples if signal cross sections have not been modified
        polyOrder = bestOrder[working_area]

        for sig in sigNames:
            print("\nProcessing {0}...\n".format(sig))

            test_fit(working_area,polyOrder,sigName=sig,strategy=strat, rMin=r_Min, rMax=r_Max, setParams={'qcd_rpfT_1_par0':'4.38','qcd_rpfT_1_par1':'-4.01','qcd_rpfT_1_par2':'0.10'})
            
            test_limit(working_area,polyOrder,'%s/runConfig.json'%working_area,blind=True,strategy=strat,extra=("--rMin={0} --rMax={1}".format(r_Min, r_Max)))

            fit_area = "{0}/{1}_area".format(working_area,polyOrder)
            sig_area = "{0}_{1}".format(fit_area,sig)
            if os.path.exists(sig_area):
                print("\nSignal area {0} already exists. Removing".format(sig_area))
                os.system("rm -rf {0}".format(sig_area))
            cmd = "mv {0} {1}".format(fit_area,sig_area)
            print("\n" + cmd)
            os.system(cmd)

            print("\nDone processing {0}\n".format(sig))

