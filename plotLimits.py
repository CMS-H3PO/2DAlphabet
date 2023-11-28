import ROOT
import json
import copy
from TwoDAlphabet.ext import CMS_lumi


mass_points = [
  (1200, 300), (1200, 600), (1200, 800), (1200, 1000),
  (1500, 300), (1500, 600), (1500, 800), (1500, 1000), (1500, 1300),
  (2000, 300), (2000, 600), (2000, 900), (2000, 1100), (2000, 1300), (2000, 1600),
  (2500, 300), (2500, 600), (2500, 800), (2500, 1000), (2500, 1300), (2500, 1600), (2500, 1800),
  (3000, 300), (3000, 600), (3000, 800), (3000, 1000), (3000, 1300), (3000, 1600), (3000, 1800), (3000, 2600), (3000, 2800),
  (3500, 300), (3500, 600), (3500, 700), (3500, 1100), (3500, 1300), (3500, 1600), (3500, 2000), (3500, 2500), (3500, 2800),
  (4000, 300), (4000, 600), (4000, 800), (4000, 1000), (4000, 1300), (4000, 1600), (4000, 2000), (4000, 2200), (4000, 2500), (4000, 2800)
]


def makePlot(fit_area, year, config, polyOrder):

    selection = 'boosted'
    if 'semiboosted' in fit_area:
        selection = 'semiboosted'

    gr_limit = copy.deepcopy(ROOT.TGraph2D())
    gr_limit.SetTitle(";m_{X} [GeV];m_{Y} [GeV];95% CL expected upper limit (" + selection + ") [fb]")

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
        #print("limit = {0}".format(limit))
        
        xs_limit = limit * xsec * 1000
        print("xs_limit = {0}".format(xs_limit))
        
        gr_limit.SetPoint(n,mX,mY,xs_limit)
        
        n += 1


    c = ROOT.TCanvas("c", "",1000,900)
    c.cd()

    gr_limit.SetMinimum(0.1) # for now put by hand
    gr_limit.SetMaximum(700) # for now put by hand

    gr_limit.Draw("cont4z")

    CMS_lumi.cmsTextSize = 0.5
    CMS_lumi.cmsTextOffset = 0.8
    CMS_lumi.lumiTextSize = 0.4
    CMS_lumi.CMS_lumi(c, 17, 11)

    c.SetLogz()

    c.SaveAs('2017_{0}_expected_limits_2D.pdf'.format(selection))


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

    year = '2017'

    json_file = open("../H3PO/Analysis/xsecs.json")
    config = json.load(json_file)
    
    makePlot('2017_boosted_SR_pass_toy_multiSignal', year, config, 1)
    makePlot('2017_semiboosted_SR_pass_toy_multiSignal', year, config, 2)
