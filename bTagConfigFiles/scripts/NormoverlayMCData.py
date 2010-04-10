#!/usr/bin/env python
import sys, os, math, array, ROOT

#For batch mode
ROOT.gROOT.SetBatch(True)

keep = []

canvasIdx = 0

class Canvas:
	def __init__(self):
		global canvasIdx
		canvasIdx += 1
		name = "c%d" % canvasIdx
		self.c = ROOT.TCanvas(name, "", 700, 700)
		ROOT.gPad.UseCurrentStyle()

	def cd(self):
		self.c.cd()

	def Print(self, p):
		self.c.Print("PlotsArea/%s.png" % p)		
#		self.c.Print("PlotsArea/%s.eps" % p)
#		os.system("sed -e 's/0\\.95 0\\.95 0\\.95/1.0 1.0 1.0/g' -i 'PlotsArea/%s.eps'" % p)
#		os.system("epstopdf 'PlotsArea/%s.eps'" % p)

def style():
	global tdrStyle

	ROOT.gROOT.SetStyle("Plain")
	ROOT.gROOT.ForceStyle()

	tdrStyle = ROOT.TStyle()
	tdrStyle.SetFrameBorderMode(0)
	tdrStyle.SetCanvasBorderMode(0)
	tdrStyle.SetPadBorderMode(0)
	tdrStyle.SetPadBorderMode(0)

#	tdrStyle.SetFrameColor(0)
	tdrStyle.SetPadColor(0)
	tdrStyle.SetCanvasColor(0)
	tdrStyle.SetStatColor(0)
	tdrStyle.SetFillColor(0)

	tdrStyle.SetPaperSize(20,26)
#	tdrStyle.SetPadTopMargin(0.08)
#	tdrStyle.SetPadBottomMargin(0.14)
	tdrStyle.SetPadRightMargin(0.04)
	tdrStyle.SetPadLeftMargin(0.16)
#	tdrStyle.SetCanvasDefH(800)
#	tdrStyle.SetCanvasDefW(800)
#	tdrStyle.SetPadGridX(1)
#	tdrStyle.SetPadGridY(1)
	tdrStyle.SetPadTickX(1)
	tdrStyle.SetPadTickY(1)

	tdrStyle.SetTextFont(42) #132
	tdrStyle.SetTextSize(0.09)
	tdrStyle.SetLabelFont(42,"xyz")
	tdrStyle.SetTitleFont(42,"xyz")
	tdrStyle.SetLabelSize(0.045,"xyz") #0.035
	tdrStyle.SetTitleSize(0.045,"xyz")
	tdrStyle.SetTitleOffset(1.5,"y")
    
	tdrStyle.SetTitleX(0.16)
	tdrStyle.SetTitleY(0.93)
	tdrStyle.SetTitleColor(1)
	tdrStyle.SetTitleTextColor(1)
	tdrStyle.SetTitleFillColor(0)
	tdrStyle.SetTitleBorderSize(1)
	tdrStyle.SetTitleFontSize(0.04)
#	tdrStyle.SetPadTopMargin(0.05)
#	tdrStyle.SetPadBottomMargin(0.13)
#	tdrStyle.SetPadLeftMargin(0.14)
#	tdrStyle.SetPadRightMargin(0.02)

	# use bold lines and markers
	tdrStyle.SetMarkerStyle(8)
	tdrStyle.SetHistLineWidth(2)
	tdrStyle.SetLineWidth(1)

	tdrStyle.SetOptTitle(1)
        tdrStyle.SetOptStat(0)

	tdrStyle.cd()

colors = [1, 2, 3, 4, 6, 7, 8, 9, 11]
markers = [20, 21, 22, 23, 24, 25, 26, 27, 28]
styles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def format(h, i, fac = 1.):
	global colors, markers, styles

	h.UseCurrentStyle()
#	if not h.GetSumw2N():
#		h.Sumw2()
#		for j in range(h.GetNbinsX()):
#			v = h.GetBinContent(j + 1) / fac
#			h.SetBinContent(j + 1, v)
#			h.SetBinError(j + 1, math.sqrt(v))

	h.SetFillColor(0)
	h.GetXaxis().SetTitleOffset(0.9)
	h.GetYaxis().SetTitleOffset(1.22)
#	h.SetLineColor(colors[i])
#	h.SetMarkerColor(colors[i])
#	h.SetLineStyle(styles[i])
#	h.SetMarkerStyle(markers[i])
	h.SetStats(0)


def rebin(list, tmpl):
	global keep
	for i in range(len(list)):
		old = list[i]
		new = tmpl.Clone(old.GetName() + "_new")
		keep.append(new)
		for j in range(old.GetNbinsX()):
			new.Fill(old.GetBinCenter(j), old.GetBinContent(j))
		list[i] = new

def draw(mc, data, xTit, yTit, title, left, blind):
	global keep

	c = Canvas()
	keep.append(c)

	mc[4].SetFillColor(ROOT.kYellow) #total
	mc[3].SetFillColor(ROOT.kRed) #bottom
	mc[2].SetFillColor(ROOT.kGreen) #charm
	mc[1].SetFillColor(ROOT.kBlue) # light
	mc[0].SetFillColor(ROOT.kGray) #no info

	data.Sumw2()
	data.SetMarkerSize(1.2)
	data.SetMarkerColor(1)
#	data.SetLineColor(ROOT.kBlue)
#	data.SetMarkerColor(ROOT.kBlue)

	ROOT.gPad.SetLogy(False)
#	ROOT.gPad.SetGridy(True)

################################# LINEAR PLOT ################################# 
	c.cd()
	ROOT.gPad.SetLogy(False)
#	ROOT.gPad.SetGridy(True)

	f1 = 1.4
        stack = ROOT.THStack( "b-tag stack", title )

	stack.Add(mc[1])
	stack.Add(mc[0])
	stack.Add(mc[2])
	stack.Add(mc[3])
        stack.SetMaximum( max(data.GetMaximum(), mc[4].GetMaximum()) * f1)
#        stack.SetMinimum( 0 )

	stack.SetTitle("")

	data.SetTitle("")
	data.SetXTitle(xTit)
	data.SetYTitle(yTit)

	data.Draw("E")
	stack.Draw("histsame")
	data.Draw("sameE")

	if left:
		l = ROOT.TLegend(0.22, 0.73, 0.37, 0.88)
	else:
		l = ROOT.TLegend(0.73, 0.73, 0.95, 0.88)
	l.SetFillColor(ROOT.kWhite)
	l.SetMargin(0.12)
        l.SetTextSize(0.035)
	l.SetBorderSize(0)

	keep.append(l)
	l.AddEntry(data, "DATA")
	if not blind:
		l.AddEntry(mc[1], "MC (light)", "f")
		l.AddEntry(mc[2], "MC (charm)", "f")
		l.AddEntry(mc[3], "MC (bottom)", "f")
		l.AddEntry(mc[0], "MC (no info)", "f")
	else :
		l.AddEntry(mc[4], "MC")
	l.Draw()

	c.Print(title)

################################# LOG PLOT ################################# 
	c.cd()
	ROOT.gPad.SetLogy(True)

	f2 = 2.5
        stack.SetMaximum( max(data.GetMaximum(), mc[4].GetMaximum()) * f2)
        stack.SetMinimum( 0.2 )

	data.Draw("E")
	stack.Draw("histsame")
	data.Draw("sameE")

	l.Draw()
	
	newtitle = 'log_'+title
	c.Print(newtitle)

################################# RATIO PLOT ################################# 
	c.cd()
	ROOT.gPad.SetLogy(False)

	hratio = data.Clone()
	hratio.Clear()
	hratio.Divide(data, mc[4], 1., 1.,"B")
	hratio.SetXTitle(xTit)
	hratio.SetYTitle("data/MC ratio")

	#hratio.Sumw2()
	hratio.SetMarkerSize(1.2)
	hratio.SetMarkerColor(4)
	hratio.SetLineWidth(2)

	hratio.Draw("e")

	ratio = 'ratio_'+title
	c.Print(ratio)

#################################

def main(args, left, blind):

	mc = ROOT.TFile.Open("mc.root")
	data = ROOT.TFile.Open("data.root")

	histo = args[0]
	if histo[0] == 'i' and histo[1] == 'p':
		histo = histo[2:] + "_impactParameterTagInfos_GLOBAL"
		pfx = "DQMData/Run 1/Btag/Run summary/TrackIPPlots_impactParameterTagInfos_GLOBAL"
	elif histo[0] == 's' and histo[1] == 'v':
		histo = histo[2:]
		pfx = "DQMData/Run 1/Btag/Run summary/TaggingVariable_combinedSecondaryVertex_GLOBAL"
	elif histo[0] == 'e' and histo[1] == 'l':
		histo = histo[2:] #+ "_softElectronTagInfos_GLOBAL"
		pfx = "DQMData/Run 1/Btag/Run summary/SoftLepton_softElectronTagInfos_GLOBAL"
	else:
		pfx = "DQMData/Run 1/Btag/Run summary/SoftLepton_softMuonTagInfos_GLOBAL"

	print pfx, histo

	mc = [
		mc.Get("%s/%sNI" % (pfx, histo)),
		mc.Get("%s/%sDUSG" % (pfx, histo)),
		mc.Get("%s/%sC" % (pfx, histo)),
		mc.Get("%s/%sB" % (pfx, histo)),
		mc.Get("%s/%sALL" % (pfx, histo))
	]

	mc.append(data.Get("%s/%sALL" % (pfx, histo)))

#### Scale MC to the data area
#### The MC histograms are normalized to the area of the data histograms
	for i in range(5):
#		print "Scaling mc", i
		mc[i].Scale(mc[-1].Integral()/mc[4].Integral())
##################

	if len(args) > 3:
		tmpl = ROOT.TH1F("tmpl", "", int(args[3]), float(args[4]), float(args[5]))
		mc[4].GetXaxis().SetRangeUser(float(args[4]), float(args[5]))
		mc[-1].GetXaxis().SetRangeUser(float(args[4]), float(args[5]))
#		rebin(mc, tmpl)

	for i, j in enumerate(mc):
		j.SetTitle("")
#		format(j, i)

	draw(mc[:-1], mc[-1], args[1], args[2], args[0], left, blind)

if __name__ == '__main__':
	app = ROOT.gApplication
	sh = ROOT.TSignalHandler(ROOT.kSigInterrupt, False)
	sh.Connect("Notified()", "TApplication", app, "Terminate()")
	ROOT.gSystem.AddSignalHandler(sh)
	style()
	s = 1
	run = len(sys.argv) > s and sys.argv[s] == '-r'
	if run: s += 1
	left = len(sys.argv) > s and sys.argv[s] == '-l'
	if left: s += 1
	blind = len(sys.argv) > s and sys.argv[s] == '-t'
	if blind: s += 1
	data = main(sys.argv[s:], left, blind)
	if not run:
		app.Run()
