from HHH_base_singleChannel import *
from argparse import ArgumentParser


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

    bestOrder = {"{}_boosted_VR".format(options.year):"1"}
    for working_area in ["{}_boosted_VR".format(options.year)]:

        jsonConfig   = 'configs/HHH/{0}.json'.format(working_area)

        test_make(working_area,jsonConfig)

        for polyOrder in ["2"]:
            if options.year == "2017":
                if polyOrder in ["1", "2", "3"]:
                    test_fit(working_area,polyOrder,strategy=2, rMin=-1, rMax=1)
                else:
                    test_fit(working_area,polyOrder,strategy=1, rMin=-5, rMax=5)
            else:
                test_fit(working_area,polyOrder,strategy=1, rMin=-5, rMax=5)
            test_plot(working_area,polyOrder)


