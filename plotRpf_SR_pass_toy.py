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
p_b = Pol_1()
rpf_boosted_SR = ROOT.TF2("rpf_boosted_SR;m_{jjj} [GeV];m_{jj} [GeV]",p_b,x_min,x_max,y_min,y_max,3)
rpf_boosted_SR.SetParameter(0,6.7721145831)
rpf_boosted_SR.SetParameter(1,-2.6074351906)
rpf_boosted_SR.SetParameter(2,-0.6470441839)

# boosted (toy data order)
p_b_gen = Pol_2()
rpf_boosted_SR_gen = ROOT.TF2("rpf_boosted_SR;m_{jjj} [GeV];m_{jj} [GeV]",p_b_gen,x_min,x_max,y_min,y_max,6)
rpf_boosted_SR_gen.SetParameter(0,6.9307656506)
rpf_boosted_SR_gen.SetParameter(1,-9.8369432147)
rpf_boosted_SR_gen.SetParameter(2,6.2893820120)
rpf_boosted_SR_gen.SetParameter(3,-20.4191583415)
rpf_boosted_SR_gen.SetParameter(4,14.5297129173)
rpf_boosted_SR_gen.SetParameter(5,5.3002377349)

# semiboosted (toy data order)
p_sb_gen = Pol_1()
rpf_semiboosted_SR_gen = ROOT.TF2("rpf_semiboosted_SR;m_{jjj} [GeV];m_{jj} [GeV]",p_sb_gen,x_min,x_max,y_min,y_max,3)
rpf_semiboosted_SR_gen.SetParameter(0,4.8724442514)
rpf_semiboosted_SR_gen.SetParameter(1,-2.2746511445)
rpf_semiboosted_SR_gen.SetParameter(2,-0.9040006014)

# semiboosted (best order)
p_sb = Pol_2()
rpf_semiboosted_SR = ROOT.TF2("rpf_semiboosted_SR;m_{jjj} [GeV];m_{jj} [GeV]",p_sb,x_min,x_max,y_min,y_max,6)
rpf_semiboosted_SR.SetParameter(0,5.2619163438)
rpf_semiboosted_SR.SetParameter(1,-1.9981204934)
rpf_semiboosted_SR.SetParameter(2,-5.2952340986)
rpf_semiboosted_SR.SetParameter(3,-2.8835169697)
rpf_semiboosted_SR.SetParameter(4,-0.0661255946)
rpf_semiboosted_SR.SetParameter(5,10.4284147344)


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
    
    rpf_boosted_SR.Draw("colz")

    c.SaveAs("rpf_boosted_SR_pass_toy.png")

    rpf_boosted_SR_gen.Draw("colz")

    c.SaveAs("rpf_boosted_gen_SR_pass_toy.png")

    rpf_semiboosted_SR.Draw("colz")

    c.SaveAs("rpf_semiboosted_SR_pass_toy.png")
    
    rpf_semiboosted_SR_gen.Draw("colz")

    c.SaveAs("rpf_semiboosted_gen_SR_pass_toy.png")
