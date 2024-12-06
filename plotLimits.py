import ROOT
import json
import copy
import sys
from TwoDAlphabet.ext import CMS_lumi


mass_points = [
  (1300, 250), (1300, 300), (1300, 350), (1300, 400), (1300, 450), (1300, 500),
  (1400, 250), (1400, 300), (1400, 350), (1400, 400), (1400, 450), (1400, 500),
  (1500, 250), (1500, 300), (1500, 350), (1500, 400), (1500, 450), (1500, 500),
  (1600, 250), (1600, 300), (1600, 350), (1600, 400), (1600, 450), (1600, 500),
  (1700, 250), (1700, 300), (1700, 350), (1700, 400), (1700, 450), (1700, 500),
  (1800, 250), (1800, 300), (1800, 350), (1800, 400), (1800, 450), (1800, 500),
  (1900, 250), (1900, 300), (1900, 350), (1900, 400), (1900, 450), (1900, 500),
  (2000, 250), (2000, 300), (2000, 350), (2000, 400), (2000, 450), (2000, 500), (2000, 600),
  (2200, 250), (2200, 300), (2200, 350), (2200, 400), (2200, 450), (2200, 500), (2200, 600),
  (2400, 250), (2400, 300), (2400, 350), (2400, 400), (2400, 450), (2400, 500), (2400, 600),
  (2500, 250), (2500, 300), (2500, 350), (2500, 400), (2500, 450), (2500, 500), (2500, 600), (2500, 700),
  (2600, 250), (2600, 300), (2600, 350), (2600, 400), (2600, 450), (2600, 500), (2600, 600), (2600, 700), (2600, 800),
  (2800, 250), (2800, 300), (2800, 350), (2800, 400), (2800, 450), (2800, 500), (2800, 600), (2800, 700), (2800, 800),
  (3000, 250), (3000, 300), (3000, 350), (3000, 400), (3000, 450), (3000, 500), (3000, 600), (3000, 700), (3000, 800),
  (3500, 250), (3500, 300), (3500, 350), (3500, 400), (3500, 450), (3500, 500), (3500, 600), (3500, 700), (3500, 800),
  (4000, 250), (4000, 300), (4000, 350), (4000, 400), (4000, 450), (4000, 500), (4000, 600), (4000, 700), (4000, 800), (4000, 900)
]


def makePlot(fit_area, year, config, polyOrder):

    channel = 'boosted'

    gr_limit = copy.deepcopy(ROOT.TGraph2D())
    gr_limit.SetTitle(";m_{X} [GeV];m_{Y} [GeV];95% CL expected upper limit (" + channel + ") [fb]")

    max_xs_limit = 0.
    n = 0
    for (mX, mY) in mass_points:
        sample = 'XToYHTo6B_MX-{0}_MY-{1}'.format(mX, mY)

        print("\nProcessing {0}...".format(sample))

        xsec = config[year][sample]["xsec"]
        #print("xsec = {0}".format(xsec))

        file_path = '{0}/{1}_area_{2}/higgsCombineTest.AsymptoticLimits.mH120.root'.format(fit_area, polyOrder, sample)

        f = ROOT.TFile.Open(file_path)

        t = f.limit
        #for e in t:
            #print(e.quantileExpected, e.limit)
        t.GetEntry(2) # get median expected limit
        limit = t.limit

        xs_limit = limit * xsec * 1000
        if xs_limit == 0.:
            print("WARNING: Limit calculation failed. xs_limit = {0}".format(xs_limit))
            continue
        else:
            print("xs_limit = {0}".format(xs_limit))

        if xs_limit > max_xs_limit:
            max_xs_limit = xs_limit

        gr_limit.SetPoint(n,mX,mY,xs_limit)

        n += 1

    print("\nMaximum xs_limit: {0}\n".format(max_xs_limit))

    c = ROOT.TCanvas("c", "",1000,900)
    c.cd()

    gr_limit.SetMinimum(0.1) # for now put by hand
    gr_limit.SetMaximum(1000) # for now put by hand

    gr_limit.Draw("cont4z")

    CMS_lumi.cmsTextSize = 0.5
    CMS_lumi.cmsTextOffset = 0.8
    CMS_lumi.lumiTextSize = 0.4
    CMS_lumi.CMS_lumi(c, 3, 11)

    c.SetLogz()

    c.SaveAs('{0}_{1}_expected_limits_2D.pdf'.format(year, channel))


if __name__ == '__main__':
    # to run in the batch mode (to prevent canvases from popping up)
    ROOT.gROOT.SetBatch()

    # set plot style
    ROOT.gROOT.SetStyle("Plain")
    ROOT.gStyle.SetPalette(57)

    ROOT.gStyle.SetPadTickX(1)  # to get the tick marks on the opposite side of the frame
    ROOT.gStyle.SetPadTickY(1)  # to get the tick marks on the opposite side of the frame

    # tweak margins
    ROOT.gStyle.SetPadTopMargin(0.1);
    ROOT.gStyle.SetPadBottomMargin(0.1);
    ROOT.gStyle.SetPadLeftMargin(0.12);
    ROOT.gStyle.SetPadRightMargin(0.15);

    # tweak axis title offsets
    ROOT.gStyle.SetTitleOffset(1.5, "Y");
    ROOT.gStyle.SetTitleOffset(1.25, "Z");

    # set nicer fonts
    ROOT.gStyle.SetTitleFont(42, "")
    ROOT.gStyle.SetTitleFont(42, "XYZ")
    ROOT.gStyle.SetLabelFont(42, "XYZ")
    ROOT.gStyle.SetTextFont(42)
    ROOT.gStyle.SetStatFont(42)
    ROOT.gROOT.ForceStyle()

    year = sys.argv[1]

    json_file = open("../H3PO/Analysis/xsecs.json")
    config = json.load(json_file)

    makePlot('{0}_boosted_SR_pass_toy_multiSignal'.format(year), year, config, '1')
