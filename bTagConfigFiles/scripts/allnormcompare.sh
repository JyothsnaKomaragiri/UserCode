#!/bin/sh
#################
for category in `echo "loosePF" "standardPF" "looseCalo" "standardCalo"`
do

###############################################################
################# Secondary Vertex TagInfo
###############################################################
./NormoverlayMCData.py -r svjetNSecondaryVertices ${category} 'No. of secondary vertices per jet' 'MC Normalized to Data' 0.5 4.5

./NormoverlayMCData.py -r  svtrackMomentum ${category} 'track p [GeV/c]' 'MC Normalized to Data' 0 100
./NormoverlayMCData.py -r  svtrackDeltaR ${category} '#DeltaR(track, jet axis)' 'MC Normalized to Data' -0.1 0.7

./NormoverlayMCData.py -r svtrackPtRel ${category} 'track p_{T}^{rel} [GeV/c]' 'MC Normalized to Data' 0 10
./NormoverlayMCData.py -r svtrackEtaRel ${category} 'track #eta^{rel}' 'MC Normalized to Data' 0 10

./NormoverlayMCData.py -r svtrackPPar ${category} 'track parallel momentum [GeV/c]' 'MC Normalized to Data' 0 250
./NormoverlayMCData.py -r -l svtrackPParRatio ${category} 'track parallel momentum ratio' 'MC Normalized to Data' 0 10
./NormoverlayMCData.py -r svtrackJetDist ${category} 'minimum track approach distance to jet axis all jets' 'MC Normalized to Data' -10 0
./NormoverlayMCData.py -r svtrackSumJetDeltaR ${category} '#DeltaR(track sum, jet axis)' 'MC Normalized to Data' -0.1 0.5

./NormoverlayMCData.py -r svtrackSip2dSig ${category} 'signed transverse IP significance' 'MC Normalized to Data' -50 50
./NormoverlayMCData.py -r svtrackSip2dVal ${category} 'signed transverse IP [cm]' 'MC Normalized to Data' -0.3 0.3

./NormoverlayMCData.py -r svtrackSip3dSig ${category} 'signed 3D IP significance' 'MC Normalized to Data' -80 80
./NormoverlayMCData.py -r svtrackSip3dVal ${category} 'signed 3D IP [cm]' 'MC Normalized to Data' -3.1 3.1

./NormoverlayMCData.py -r -l svtrackSip3dSigAboveCharm ${category} 'first track 3D signed IP above charm' 'MC Normalized to Data' -50 50 

./NormoverlayMCData.py -r svflightDistance2dVal_CAT1 ${category} 'transverse flight distance [cm]' 'MC Normalized to Data' 0 2.5
./NormoverlayMCData.py -r svflightDistance2dSig_CAT1 ${category} 'transverse flight distance significance' 'MC Normalized to Data' 0 80

./NormoverlayMCData.py -r svflightDistance3dVal_CAT1 ${category} '3D flight distance [cm]' 'MC Normalized to Data' 0 15
./NormoverlayMCData.py -r svflightDistance3dSig_CAT1 ${category} '3D flight distance significance' 'MC Normalized to Data' 0 80

./NormoverlayMCData.py -r svvertexNTracks_CAT1 ${category} 'no. of tracks at SV' 'MC Normalized to Data' 0.5 11.5
./NormoverlayMCData.py -r svvertexMass_CAT1 ${category} 'vertex mass [GeV/c^{2}]' 'MC Normalized to Data' 0 3.5
./NormoverlayMCData.py -r -l svvertexEnergyRatio_CAT1 ${category} 'fraction of charged jet energy at SV' 'MC Normalized to Data' 0 1
./NormoverlayMCData.py -r svvertexJetDeltaR_CAT1 ${category} '#DeltaR(sv, jet axis)' 'MC Normalized to Data' -0.1 0.7

###############################################################
################# Impact Parameter TagInfo
###############################################################
./NormoverlayMCData.py -r ipdecLen ${category} 'Decay length' 'MC Normalized to Data' -0.5 5
./NormoverlayMCData.py -r -l ipjetDist ${category} 'Jet distance' 'MC Normalized to Data' -0.15 0.01

./NormoverlayMCData.py -r ipselTrksNbr_2D ${category} 'no. of selected tracks for 2D in jet' 'MC Normalized to Data' -0.5 19.5
./NormoverlayMCData.py -r ipselTrksNbr_3D ${category} 'no. of selected tracks for 3D in jet' 'MC Normalized to Data' -0.5 19.5

### 2D plots
./NormoverlayMCData.py -r ipip_2D ${category} '2D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe_2D ${category} '2D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips_2D ${category} '2D IP significance' 'MC Normalized to Data' -40 40
./NormoverlayMCData.py -r ipprob_2D ${category} '2D IP probability' 'MC Normalized to Data' -1.1 1.1

./NormoverlayMCData.py -r ipip1_2D ${category} '1^{st} track 2D IP value' 'MC Normalized to Data' -0.2 0.2

./NormoverlayMCData.py -r ipipe1_2D ${category} '1^{st} track 2D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips1_2D ${category} '1^{st} track 2D IP significance' 'MC Normalized to Data' -40 40

./NormoverlayMCData.py -r ipip2_2D ${category} '2^{nd} track 2D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe2_2D ${category} '2^{nd} track 2D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips2_2D ${category} '2^{nd} track 2D IP significance' 'MC Normalized to Data' -40 40

./NormoverlayMCData.py -r ipip3_2D ${category} '3^{rd} track 2D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe3_2D ${category} '3^{rd} track 2D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips3_2D ${category} '3^{rd} track 2D IP significance' 'MC Normalized to Data' -40 40

### 3D plots
./NormoverlayMCData.py -r ipip_3D ${category} '3D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe_3D ${category} '3D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips_3D ${category} '3D IP significance' 'MC Normalized to Data' -40 40
./NormoverlayMCData.py -r ipprob_3D ${category} '3D IP probability' 'MC Normalized to Data' -1.1 1.1

./NormoverlayMCData.py -r ipip1_3D ${category} '1^{st} track 3D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe1_3D ${category} '1^{st} track 3D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips1_3D ${category} '1^{st} track 3D IP significance' 'MC Normalized to Data' -40 40

./NormoverlayMCData.py -r ipip2_3D ${category} '2^{nd} track 3D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe2_3D ${category} '2^{nd} track 3D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips2_3D ${category} '2^{nd} track 3D IP significance' 'MC Normalized to Data' -40 40

./NormoverlayMCData.py -r ipip3_3D ${category} '3^{rd} track 3D IP value' 'MC Normalized to Data' -0.2 0.2
./NormoverlayMCData.py -r ipipe3_3D ${category} '3^{rd} track 3D IP error' 'MC Normalized to Data' 0 0.05
./NormoverlayMCData.py -r ipips3_3D ${category} '3^{rd} track 3D IP significance' 'MC Normalized to Data' -40 40

###############################################################
################# Electron TagInfo
###############################################################
 ./NormoverlayMCData.py -r 'el1st lepton delta R' ${category} '#DeltaR(electron, jet axis)' 'MC Normalized to Data' 0 0.5
 ./NormoverlayMCData.py -r 'el1st lepton energy ratio' ${category}   'Electron p_{T}/Energy^{jet}' 'MC Normalized to Data' 0 1.4
 ./NormoverlayMCData.py -r 'el1st lepton eta rel'    ${category}   'Electron #eta^{rel}' 'MC Normalized to Data' -1 10
 ./NormoverlayMCData.py -r 'el1st lepton p0 par' ${category} 'Electron p_{T}^{rel} in the B rest frame' 'MC Normalized to Data' 0 3
 ./NormoverlayMCData.py -r 'el1st lepton pT rel' ${category} 'Electron p_{T}^{rel} [GeV/C]' 'MC Normalized to Data'  0 3
 ./NormoverlayMCData.py -r 'el1st lepton pT'    ${category} 'Electron p_{T} [GeV/C]'  'MC Normalized to Data' 0 20
 ./NormoverlayMCData.py -r 'el1st lepton parallel energy ratio'   ${category} 'Electron Ppar/Energy^{jet}' 'MC Normalized to Data' 0 1.4
 ./NormoverlayMCData.py -r 'el1st lepton sip2d'	${category} 'Electron signed 2D impact parameter significance' 'MC Normalized to Data' -20 30
 ./NormoverlayMCData.py -r 'el1st lepton sip3d'	${category} 'Electron signed 3D impact parameter significance' 'MC Normalized to Data' -20 30

###############################################################
################# Muon TagInfo
###############################################################
 ./NormoverlayMCData.py -r 'mu1st lepton delta R'	${category} '#DeltaR(muon, jet axis)' 'MC Normalized to Data' 0 0.5
 ./NormoverlayMCData.py -r 'mu1st lepton energy ratio'	${category} 'Muon p_{T}/Energy^{jet}'  'MC Normalized to Data' 0 1.2
 ./NormoverlayMCData.py -r 'mu1st lepton eta rel'	${category} 'Muon #eta^{rel}'   'MC Normalized to Data' -1 10
 ./NormoverlayMCData.py -r 'mu1st lepton p0 par'	${category} 'Muon p_{T}^{rel} in the B rest frame'  'MC Normalized to Data' 0 3
 ./NormoverlayMCData.py -r 'mu1st lepton pT rel'	${category} 'Muon p_{T}^{rel} [GeV/C]'  'MC Normalized to Data' 0 3
 ./NormoverlayMCData.py -r 'mu1st lepton pT'	${category} 'Muon p_{T} [GeV/C]'  'MC Normalized to Data' 0 20
 ./NormoverlayMCData.py -r 'mu1st lepton parallel energy ratio'   ${category} 'Muon Ppar/Energy^{jet}'  'MC Normalized to Data' 0 1.4 
 ./NormoverlayMCData.py -r 'mu1st lepton sip2d'	${category} 'Muon signed 2D impact parameter significance'  'MC Normalized to Data' -20 30
 ./NormoverlayMCData.py -r 'mu1st lepton sip3d'	${category} 'Muon signed 3D impact parameter significance'  'MC Normalized to Data' -20 30

#################
done