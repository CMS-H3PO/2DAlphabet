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
# boosted
p1 = Pol_1()
rpf_boosted_VR = ROOT.TF2("rpf_boosted_VR;m_{jjj} [GeV];m_{jj} [GeV]",p1,x_min,x_max,y_min,y_max,3)
rpf_boosted_VR.SetParameter(0,6.354246278903588)
rpf_boosted_VR.SetParameter(1,-1.5596348441299028)
rpf_boosted_VR.SetParameter(2,-0.16367639797209677)

# semiboosted
p2 = Pol_2()
rpf_semiboosted_VR = ROOT.TF2("rpf_semiboosted_VR;m_{jjj} [GeV];m_{jj} [GeV]",p2,x_min,x_max,y_min,y_max,6)
rpf_semiboosted_VR.SetParameter(0,5.276590529385103)
rpf_semiboosted_VR.SetParameter(1,-6.354581835388871)
rpf_semiboosted_VR.SetParameter(2,1.0980653307670138)
rpf_semiboosted_VR.SetParameter(3,4.88705909668947)
rpf_semiboosted_VR.SetParameter(4,2.5024077870572796)
rpf_semiboosted_VR.SetParameter(5,-5.606124121805323)


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

    c.SaveAs("rpf_boosted_VR.png")

    rpf_semiboosted_VR.Draw("colzsame")

    c.SaveAs("rpf_semiboosted_VR.png")
