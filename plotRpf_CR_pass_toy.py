import ROOT

# variable ranges
x_min = 1000.
x_max = 4500.
y_min = 200.
y_max = 4500.

# polynomials
class Pol_1:
    def __call__(self, arr, par):
        # variable transformations to [0,1] range
        x = (arr[0]-x_min)/(x_max-x_min)
        y = (arr[1]-y_min)/(y_max-y_min)
        
        return 0.01*(par[0]+par[1]*x+par[2]*y)


class Pol_2:
    def __call__(self, arr, par):
        # variable transformations to [0,1] range
        x = (arr[0]-x_min)/(x_max-x_min)
        y = (arr[1]-y_min)/(y_max-y_min)
        
        return 0.01*(par[0]+par[1]*x+par[2]*y+par[3]*x*y+par[4]*x**2+par[5]*y**2)


# fail-to-pass transfer functions
# boosted (best order)
p_b = Pol_2()
rpf_boosted_VR = ROOT.TF2("rpf_boosted_VR;m_{jjj} [GeV];m_{jj} [GeV]",p_b,x_min,x_max,y_min,y_max,6)
rpf_boosted_VR.SetParameter(0,7.1254600356)
rpf_boosted_VR.SetParameter(1,-6.1952111515)
rpf_boosted_VR.SetParameter(2,1.6876169623)
rpf_boosted_VR.SetParameter(3,0.0562667290)
rpf_boosted_VR.SetParameter(4,4.5156972016)
rpf_boosted_VR.SetParameter(5,-3.2904181798)

# semiboosted (best order)
p_sb = Pol_1()
rpf_semiboosted_VR = ROOT.TF2("rpf_semiboosted_VR;m_{jjj} [GeV];m_{jj} [GeV]",p_sb,x_min,x_max,y_min,y_max,3)
rpf_semiboosted_VR.SetParameter(0,4.5827847421)
rpf_semiboosted_VR.SetParameter(1,-2.5909056630)
rpf_semiboosted_VR.SetParameter(2,-0.0564180778)


if __name__ == '__main__':
    # to run in the batch mode (to prevent canvases from popping up)
    ROOT.gROOT.SetBatch()

    # tweak margins
    #ROOT.gStyle.SetPadTopMargin(0.10);
    #ROOT.gStyle.SetPadBottomMargin(0.10);
    #ROOT.gStyle.SetPadLeftMargin(0.10);
    ROOT.gStyle.SetPadRightMargin(0.15);

    # tweak axis title offsets
    ROOT.gStyle.SetTitleOffset(1.45, "Y")

    c = ROOT.TCanvas("c", "",1000,800)
    c.cd()
    
    rpf_boosted_VR.Draw("colz")

    c.SaveAs("rpf_boosted_VR_pass_toy.png")

    rpf_semiboosted_VR.Draw("colz")

    c.SaveAs("rpf_semiboosted_VR_pass_toy.png")