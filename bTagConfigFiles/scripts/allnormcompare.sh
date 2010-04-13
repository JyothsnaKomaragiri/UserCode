#!/bin/sh
###############################################################
################# Impact Parameter TagInfo
###############################################################
./NormoverlayMCData.py -r ipdecLen 'Decay length' 'MC Normalized to Data' 25 -0.5 5
./NormoverlayMCData.py -r -l ipjetDist 'Jet distance' 'MC Normalized to Data' 10 -0.15 0.01

./NormoverlayMCData.py -r ipselTrksNbr_2D 'no. of selected tracks for 2D in jet' 'MC Normalized to Data' 20 -0.5 19.5
./NormoverlayMCData.py -r ipselTrksNbr_3D 'no. of selected tracks for 3D in jet' 'MC Normalized to Data' 20 -0.5 19.5

### 2D plots
./NormoverlayMCData.py -r ipip_2D '2D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe_2D '2D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips_2D '2D IP significance' 'MC Normalized to Data' 20 -40 40
./NormoverlayMCData.py -r ipprob_2D '2D IP probability' 'MC Normalized to Data'

./NormoverlayMCData.py -r ipip1_2D '1^{st} track 2D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe1_2D '1^{st} track 2D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips1_2D '1^{st} track 2D IP significance' 'MC Normalized to Data' 20 -40 40

./NormoverlayMCData.py -r ipip2_2D '2^{nd} track 2D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe2_2D '2^{nd} track 2D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips2_2D '2^{nd} track 2D IP significance' 'MC Normalized to Data' 20 -40 40

./NormoverlayMCData.py -r ipip3_2D '3^{rd} track 2D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe3_2D '3^{rd} track 2D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips3_2D '3^{rd} track 2D IP significance' 'MC Normalized to Data' 20 -40 40

### 3D plots
./NormoverlayMCData.py -r ipip_3D '3D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe_3D '3D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips_3D '3D IP significance' 'MC Normalized to Data' 20 -40 40
./NormoverlayMCData.py -r ipprob_3D '3D IP probability' 'MC Normalized to Data'

./NormoverlayMCData.py -r ipip1_3D '1^{st} track 3D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe1_3D '1^{st} track 3D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips1_3D '1^{st} track 3D IP significance' 'MC Normalized to Data' 20 -40 40

./NormoverlayMCData.py -r ipip2_3D '2^{nd} track 3D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe2_3D '2^{nd} track 3D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips2_3D '2^{nd} track 3D IP significance' 'MC Normalized to Data' 20 -40 40

./NormoverlayMCData.py -r ipip3_3D '3^{rd} track 3D IP value' 'MC Normalized to Data' 25 -0.2 0.2
./NormoverlayMCData.py -r ipipe3_3D '3^{rd} track 3D IP error' 'MC Normalized to Data' 25 0 0.05
./NormoverlayMCData.py -r ipips3_3D '3^{rd} track 3D IP significance' 'MC Normalized to Data' 20 -40 40


###############################################################
################# Secondary Vertex TagInfo
###############################################################
./NormoverlayMCData.py -r svjetNSecondaryVertices 'No. of secondary vertices per jet' 'MC Normalized to Data' 9 0.5 7.5
#./NormoverlayMCData.py -r svjetNSecondaryVertices_CAT1 'No. of secondary vertices for CAT1' 'Entries' 10 -0.5 10

./NormoverlayMCData.py -r  svtrackMomentum 'track p [GeV/c]' 'MC Normalized to Data' 10 0 100
./NormoverlayMCData.py -r  svtrackDeltaR '#DeltaR(track, jet axis)' 'MC Normalized to Data' 20 -0.1 0.7

./NormoverlayMCData.py -r svtrackPtRel 'track p_{T}^{rel} [GeV/c]' 'MC Normalized to Data' 10 0 10
./NormoverlayMCData.py -r svtrackEtaRel 'track #eta^{rel}' 'MC Normalized to Data' 10 0 10

./NormoverlayMCData.py -r svtrackPPar 'track parallel momentum [GeV/c]' 'MC Normalized to Data' #10 0 10
./NormoverlayMCData.py -r svtrackPParRatio 'track parallel momentum ratio' 'MC Normalized to Data' 10 0 10
./NormoverlayMCData.py -r svtrackJetDist 'minimum track approach distance to jet axis all jets' 'MC Normalized to Data'
./NormoverlayMCData.py -r svtrackSumJetDeltaR '#DeltaR(track sum, jet axis)' 'MC Normalized to Data' 20 -0.1 0.5

./NormoverlayMCData.py -r svtrackSip2dSig 'signed transverse IP significance' 'MC Normalized to Data' 20 -50 50
./NormoverlayMCData.py -r svtrackSip2dVal 'signed transverse IP [cm]' 'MC Normalized to Data'

./NormoverlayMCData.py -r svtrackSip3dSig 'signed 3D IP significance' 'MC Normalized to Data'  20 -80 80
./NormoverlayMCData.py -r svtrackSip3dVal 'signed 3D IP [cm]' 'MC Normalized to Data'

./NormoverlayMCData.py -r -l svtrackSip3dSigAboveCharm 'first track 3D signed IP above charm' 'MC Normalized to Data' 10 -50 60 #-30.2 20.2

./NormoverlayMCData.py -r svflightDistance2dVal_CAT1 'transverse flight distance [cm]' 'MC Normalized to Data' #25 0 2.5
./NormoverlayMCData.py -r svflightDistance2dSig_CAT1 'transverse flight distance significance' 'MC Normalized to Data' #40 0 60

./NormoverlayMCData.py -r svflightDistance3dSig_CAT1 '3D flight distance significance' 'MC Normalized to Data' #20 0 42
./NormoverlayMCData.py -r svflightDistance3dVal_CAT1 '3D flight distance [cm]' 'MC Normalized to Data' #25 0 10

./NormoverlayMCData.py -r svvertexNTracks_CAT1 'no. of tracks at SV' 'MC Normalized to Data' 9 0.5 9.5
./NormoverlayMCData.py -r svvertexMass_CAT1 'vertex mass [GeV/c^{2}]' 'MC Normalized to Data' 15 0 3
./NormoverlayMCData.py -r -l svvertexEnergyRatio_CAT1 'fraction of charged jet energy at SV' 'MC Normalized to Data' 25 0 1
./NormoverlayMCData.py -r svvertexJetDeltaR_CAT1 '#DeltaR(sv, jet axis)' 'MC Normalized to Data' 20 -0.1 0.7

###############################################################
################# Electron TagInfo
###############################################################
 ./NormoverlayMCData.py -r 'el1st lepton delta R'	'#DeltaR(electron, jet axis)' 'MC Normalized to Data' 20 0 0.5
 ./NormoverlayMCData.py -r 'el1st lepton energy ratio'   'Electron p_{T}/Energy^{jet}' 'MC Normalized to Data' 20 0 1.4
 ./NormoverlayMCData.py -r 'el1st lepton eta rel'	'Electron #eta^{rel}' 'MC Normalized to Data' 20 -1 10
 #./NormoverlayMCData.py -r 'el1st lepton id'	'Electron identification discriminaint' 'MC Normalized to Data'
 ./NormoverlayMCData.py -r 'el1st lepton p0 par'	'Electron p_{T}^{rel} in the B rest frame' 'MC Normalized to Data' 20 0 3
 ./NormoverlayMCData.py -r 'el1st lepton pT rel'	'Electron p_{T}^{rel} [GeV/C]' 'MC Normalized to Data'  20 0 3
 ./NormoverlayMCData.py -r 'el1st lepton pT'	'Electron p_{T} [GeV/C]'  'MC Normalized to Data' 
 ./NormoverlayMCData.py -r 'el1st lepton parallel energy ratio'   'Electron Ppar/Energy^{jet}' 'MC Normalized to Data' 20 0 1.4
 ./NormoverlayMCData.py -r 'el1st lepton sip2d'	'Electron signed 2D impact parameter significance' 'MC Normalized to Data'
 ./NormoverlayMCData.py -r 'el1st lepton sip3d'	'Electron signed 3D impact parameter significance' 'MC Normalized to Data'

###############################################################
################# Muon TagInfo
###############################################################
 ./NormoverlayMCData.py -r  '1st lepton delta R'	'#DeltaR(muon, jet axis)' 'MC Normalized to Data' 20 0 0.5
 ./NormoverlayMCData.py -r  '1st lepton energy ratio'	'Muon p_{T}/Energy^{jet}'  'MC Normalized to Data' 20 0 1.2
 ./NormoverlayMCData.py -r  '1st lepton eta rel'	'Muon #eta^{rel}'   'MC Normalized to Data' 20 -1 10
 #./NormoverlayMCData.py -r '1st lepton id'	'Muon identification discriminaint'  'MC Normalized to Data'
 ./NormoverlayMCData.py -r '1st lepton p0 par'	'Muon p_{T}^{rel} in the B rest frame'  'MC Normalized to Data' 20 0 3
 ./NormoverlayMCData.py -r '1st lepton pT rel'	'Muon p_{T}^{rel} [GeV/C]'  'MC Normalized to Data' 20 0 3
 ./NormoverlayMCData.py -r '1st lepton pT'	'Muon p_{T} [GeV/C]'  'MC Normalized to Data'
 ./NormoverlayMCData.py -r '1st lepton parallel energy ratio'   'Muon Ppar/Energy^{jet}'  'MC Normalized to Data' 20 0 1.4 
 ./NormoverlayMCData.py -r '1st lepton sip2d'	'Muon signed 2D impact parameter significance'  'MC Normalized to Data' 
 ./NormoverlayMCData.py -r '1st lepton sip3d'	'Muon signed 3D impact parameter significance'  'MC Normalized to Data'

