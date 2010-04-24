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
		self.c.Print("PlotsLumi/%s.png" % p)		
### For area normalization
#		self.c.Print("PlotsArea/%s.png" % p)
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

def draw(mc, data, xTit, yTit, title, category, left, blind):
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

	f1 = 1.2
        stack = ROOT.THStack( "b-tag stack", title )

        #Stacking order b first, then charm, then light
	stack.Add(mc[1]) #light
	stack.Add(mc[0]) #no info
	stack.Add(mc[2]) #charm
	stack.Add(mc[3]) #bottom

        data.SetMaximum( max(data.GetMaximum(), mc[4].GetMaximum()) * f1)
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
        data.SetMaximum( max(data.GetMaximum(), mc[4].GetMaximum()) * f2)
        data.SetMinimum( 0.2 )

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
	hratio.GetYaxis().SetRangeUser(0., 3.)
	
	hratio.Draw("e")

	ratio = 'ratio_'+title
	c.Print(ratio)

#################################

def main(args, left, blind):

	mc = ROOT.TFile.Open("mc.root")
	data = ROOT.TFile.Open("data.root")

	histo = args[0]
	## TCHP
	if histo[0] == 'T' and histo[1] == 'P' and histo[2] == '0':
		if args[1] == 'loosePF':		
			histo = histo[3:] + "_looseTrackCountingHighPurPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseTrackCountingHighPurPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':		
			histo = histo[3:] + "_standardTrackCountingHighPurPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardTrackCountingHighPurPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':		
			histo = histo[3:] + "_looseTrackCountingHighPurCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseTrackCountingHighPurCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardTrackCountingHighPurCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardTrackCountingHighPurCaloBJetTags_GLOBAL"

	## TCHE
	elif histo[0] == 'T' and histo[1] == 'E' and histo[2] == '0':		
		if args[1] == 'loosePF':		
			histo = histo[3:] + "_looseTrackCountingHighEffPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseTrackCountingHighEffPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':		
			histo = histo[3:] + "_standardTrackCountingHighEffPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardTrackCountingHighEffPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':		
			histo = histo[3:] + "_looseTrackCountingHighEffCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseTrackCountingHighEffCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardTrackCountingHighEffCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardTrackCountingHighEffCaloBJetTags_GLOBAL"

	## Jet prob
	elif histo[0] == 'J' and histo[1] == 'P' and histo[2] == '0':
		if args[1] == 'loosePF':		
			histo = histo[3:] + "_looseJetProbabilityPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseJetProbabilityPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':		
			histo = histo[3:] + "_standardJetProbabilityPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardJetProbabilityPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':		
			histo = histo[3:] + "_looseJetProbabilityCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseJetProbabilityCaloBJetTags_GLOBAL"
		else :
			histo = histo[3:] + "_standardJetProbabilityCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardJetProbabilityCaloBJetTags_GLOBAL"		       

	## Jet B prob
	elif histo[0] == 'J' and histo[1] == 'B' and histo[2] == '0':
		if args[1] == 'loosePF':		
			histo = histo[3:] + "_looseJetBProbabilityPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseJetBProbabilityPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':		
			histo = histo[3:] + "_standardJetBProbabilityPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardJetBProbabilityPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':		
			histo = histo[3:] + "_looseJetBProbabilityCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseJetBProbabilityCaloBJetTags_GLOBAL"
		else :
			histo = histo[3:] + "_standardJetBProbabilityCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardJetBProbabilityCaloBJetTags_GLOBAL"	       

	## SSV High Eff (>=2 tracks)
	elif histo[0] == 'S' and histo[1] == 'E' and histo[2] == '0':		
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSimpleSecondaryVertexPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSimpleSecondaryVertexPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSimpleSecondaryVertexPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSimpleSecondaryVertexPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSimpleSecondaryVertexCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSimpleSecondaryVertexCaloBJetTags_GLOBAL"
		else :
			histo = histo[3:] + "_standardSimpleSecondaryVertexCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSimpleSecondaryVertexCaloBJetTags_GLOBAL"

	## SSV High Purity (>=3 tracks)
	elif histo[0] == 'S' and histo[1] == 'P' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSimpleSecondaryVertexHighPurPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSimpleSecondaryVertexHighPurPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSimpleSecondaryVertexHighPurPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSimpleSecondaryVertexHighPurPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSimpleSecondaryVertexHighPurCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSimpleSecondaryVertexHighPurCaloBJetTags_GLOBAL"
		else :
			histo = histo[3:] + "_standardSimpleSecondaryVertexHighPurCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSimpleSecondaryVertexHighPurCaloBJetTags_GLOBAL"

	## CSV
	elif histo[0] == 'C' and histo[1] == 'S' and histo[2] == '0':
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseCombinedSecondaryVertexPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseCombinedSecondaryVertexPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardCombinedSecondaryVertexPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardCombinedSecondaryVertexPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseCombinedSecondaryVertexCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseCombinedSecondaryVertexCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardCombinedSecondaryVertexCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardCombinedSecondaryVertexCaloBJetTags_GLOBAL"

	## CSV MVA
	elif histo[0] == 'C' and histo[1] == 'M' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseCombinedSecondaryVertexMVAPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseCombinedSecondaryVertexMVAPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardCombinedSecondaryVertexMVAPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardCombinedSecondaryVertexMVAPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseCombinedSecondaryVertexMVACaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseCombinedSecondaryVertexMVACaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardCombinedSecondaryVertexMVACaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardCombinedSecondaryVertexMVACaloBJetTags_GLOBAL"

	## SoftMuonByIP3d
	elif histo[0] == 'M' and histo[1] == 'I' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSoftMuonByIP3dPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftMuonByIP3dPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSoftMuonByIP3dPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftMuonByIP3dPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSoftMuonByIP3dCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftMuonByIP3dCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardSoftMuonByIP3dCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftMuonByIP3dCaloBJetTags_GLOBAL"

	## SoftMuonByPt
	elif histo[0] == 'M' and histo[1] == 'P' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSoftMuonByPtPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftMuonByPtPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSoftMuonByPtPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftMuonByPtPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSoftMuonByPtCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftMuonByPtCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardSoftMuonByPtCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftMuonByPtCaloBJetTags_GLOBAL"

	## SoftMuon
	elif histo[0] == 'M' and histo[1] == 'U' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSoftMuonPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftMuonPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSoftMuonPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftMuonPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSoftMuonCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftMuonCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardSoftMuonCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftMuonCaloBJetTags_GLOBAL"

	## SoftElectronByIP3d
	elif histo[0] == 'E' and histo[1] == 'I' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSoftElectronByIP3dPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftElectronByIP3dPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSoftElectronByIP3dPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftElectronByIP3dPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSoftElectronByIP3dCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftElectronByIP3dCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardSoftElectronByIP3dCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftElectronByIP3dCaloBJetTags_GLOBAL"

	## SoftElectronByPt
	elif histo[0] == 'E' and histo[1] == 'P' and histo[2] == '0':			
		if args[1] == 'loosePF':
			histo = histo[3:] + "_looseSoftElectronByPtPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftElectronByPtPFBJetTags_GLOBAL"
		elif args[1] == 'standardPF':
			histo = histo[3:] + "_standardSoftElectronByPtPFBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftElectronByPtPFBJetTags_GLOBAL"
		elif args[1] == 'looseCalo':
			histo = histo[3:] + "_looseSoftElectronByPtCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_looseSoftElectronByPtCaloBJetTags_GLOBAL"
		else:
			histo = histo[3:] + "_standardSoftElectronByPtCaloBJetTags_GLOBAL"
			pfx = "DQMData/Run 1/Btag/Run summary/JetTag_standardSoftElectronByPtCaloBJetTags_GLOBAL"

	else :
		pfx = "!!Nothing to draw!!"
		print "Nothing to draw"
		

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
#	for i in range(5):
#		print "Scaling mc", i
#		mc[i].Scale(mc[-1].Integral()/mc[4].Integral())

#### Scale MC to data lumi ...Data/MC ratio
## Data lumi = 199.58 ub-1 and MC lumi = 157.12 ub-1
	scale = 1.27
	for i in range(5):
		mc[i].Scale(1.27)
##################

#	if len(args) > 3:
#		mc[4].GetXaxis().SetRangeUser(float(args[4]), float(args[5]))
#		mc[-1].GetXaxis().SetRangeUser(float(args[4]), float(args[5]))
#		rebin(mc, tmpl)

	for i, j in enumerate(mc):
		j.SetTitle("")
#		format(j, i)

	newTitle = args[0]+"_"+args[1]

	draw(mc[:-1], mc[-1], args[2], args[3], newTitle, args[1], left, blind)

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
