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



#official_samples = [
 # (1300, 250), (1300, 300), (1300, 350), (1300, 400), (1300, 450), (1300, 500),
  #(1400, 250), (1400, 300), (1400, 350), (1400, 400), (1400, 450), (1400, 500),
#  (1500, 250), (1500, 300), (1500, 350), (1500, 400), (1500, 450), (1500, 500),
 # (1600, 250), (1600, 300), (1600, 350), (1600, 400), (1600, 450), (1600, 500),
  #(1700, 250), (1700, 300), (1700, 350), (1700, 400), (1700, 450), (1700, 500),
#  (1800, 250), (1800, 300), (1800, 350), (1800, 400), (1800, 450), (1800, 500),
 # (1900, 250), (1900, 300), (1900, 350), (1900, 400), (1900, 450), (1900, 500),
  #(2000, 250), (2000, 300), (2000, 350), (2000, 400), (2000, 450), (2000, 500), (2000, 600),
#  (2200, 250), (2200, 300), (2200, 350), (2200, 400), (2200, 450), (2200, 500), (2200, 600),
 # (2400, 250), (2400, 300), (2400, 350), (2400, 400), (2400, 450), (2400, 500), (2400, 600),
  #(2500, 250), (2500, 300), (2500, 350), (2500, 400), (2500, 450), (2500, 500), (2500, 600), (2500, 700),
#  (2600, 250), (2600, 300), (2600, 350), (2600, 400), (2600, 450), (2600, 500), (2600, 600), (2600, 700), (2600, 800),
 # (2800, 250), (2800, 300), (2800, 350), (2800, 400), (2800, 450), (2800, 500), (2800, 600), (2800, 700), (2800, 800),
  #(3000, 250), (3000, 300), (3000, 350), (3000, 400), (3000, 450), (3000, 500), (3000, 600), (3000, 700), (3000, 800),
#  (3500, 250), (3500, 300), (3500, 350), (3500, 400), (3500, 450), (3500, 500), (3500, 600), (3500, 700), (3500, 800),
 # (4000, 250), (4000, 300), (4000, 350), (4000, 400), (4000, 450), (4000, 500), (4000, 600), (4000, 700), (4000, 800), (4000, 900)
#]




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
    r_Max = 5
    strat = 1


    sigNames = ["XToYHTo6B_MX-4000_MY-350"]

    r_Min = -1
    r_Max = 2
    strat = 1




    bestOrder = {"{}_boosted_SR_pass_toy_multiSignal".format(options.year):"1"}
    for working_area in ["{}_boosted_SR_pass_toy_multiSignal".format(options.year)]:

        jsonConfig   = 'configs/HHH/{0}.json'.format(working_area)

        #test_make(working_area,jsonConfig) # this line can be commented out when reprocessing a subset of signal samples if signal cross sections have not been modified
        polyOrder = bestOrder[working_area]

        for sig in sigNames:
            print("\nProcessing {0}...\n".format(sig))

            test_fit(working_area,polyOrder,sigName=sig,strategy=strat, rMin=r_Min, rMax=r_Max)
            
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

