import FWCore.ParameterSet.Config as cms

process = cms.Process("pTbinValidation")

process.load("DQMServices.Components.DQMEnvironment_cfi")

#keep the logging output to a nice level
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("DQMServices.Core.DQM_cfg")

###############
process.source = cms.Source("PoolSource",
			    skipEvents = cms.untracked.uint32(__SKIP_EVENTS__),
			    fileNames = cms.untracked.vstring(__FILE_NAMES__)
			    )

process.maxEvents = cms.untracked.PSet(
	input = cms.untracked.int32(__MAX_EVENTS__)
	)

###############

### Needed for MC truth matching
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.JetMCAlgos.CaloJetsMCFlavour_cfi")

### Standard settings
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

### Use proper Global tag corresponding to the dataset used
process.GlobalTag.globaltag = 'START3X_V26A::All'

### PV filter
process.primaryVertexEventFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"), # tracksSize() > 3 for the older cut
   filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
)


### Jet cleaning for AK5 PF jets
### Use LOOSE PF jet ID
process.goodJetsFilter = cms.EDFilter("PFJetSelector",
	src = cms.InputTag("ak5PFJets"),
#       cut = cms.string("pt > 10.0 && abs(eta) < 2.4"),
        cut = cms.string("pt > 10.0 && abs(eta) < 2.4 && neutralHadronEnergyFraction < 1.0 && neutralEmEnergyFraction < 1.0 && nConstituents > 0 && chargedHadronEnergyFraction > 0.0 && chargedMultiplicity > 0.0 && chargedEmEnergyFraction < 1.0"),
        filter = cms.bool(True)
				      )

### Assciate tracks to AK5 PF jets
process.ak5PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
                                                          jets = cms.InputTag("goodJetsFilter"),
                                                          tracks = cms.InputTag("generalTracks"),
                                                          coneSize = cms.double(0.5)
                                                          )


##########################################################
## For truth matching
##
process.myPartons = cms.EDFilter("PartonSelector",
   withLeptons = cms.bool(False),
   src = cms.InputTag("genParticles")
)

process.ak5PFJetsByRef = cms.EDFilter("JetPartonMatcher",
   jets = cms.InputTag("goodJetsFilter"), ##("ak5PFJets"),
   coneSizeToAssociate = cms.double(0.3),
   partons = cms.InputTag("myPartons")   
)
 
process.ak5PFJetsValAlgo = cms.EDFilter("JetFlavourIdentifier",
   srcByReference = cms.InputTag("ak5PFJetsByRef"),
   physicsDefinition = cms.bool(False)
)
##########################################################
### Load the RecoBTag config file fragment and change few b-tag things
process.load("RecoBTag.Configuration.RecoBTag_cff")

### Feed the new AK5 PF jet track associator to get updated IP TagInfo
process.impactParameterTagInfos.jetTracks = "ak5PFJetTracksAssociatorAtVertex"
process.impactParameterTagInfos.minimumNumberOfHits = 7
process.impactParameterTagInfos.maximumTransverseImpactParameter = 0.2
process.impactParameterTagInfos.minimumTransverseMomentum = 0.0
process.impactParameterTagInfos.maximumChiSquared = 10.0
process.impactParameterTagInfos.useTrackQuality = False
process.impactParameterTagInfos.ghostTrackPriorDeltaR = 0.1

### Loosening the SV cuts
process.secondaryVertexTagInfos.constraint = "PVErrorScaled"
process.secondaryVertexTagInfos.pvErrorScaling = cms.double(2.0)
process.secondaryVertexTagInfos.vertexCuts.v0Filter = cms.PSet(k0sMassWindow = cms.double(0.015))
process.secondaryVertexTagInfos.vertexCuts.maxDeltaRToJetAxis = 1.0
process.secondaryVertexTagInfos.vertexReco.smoothing = cms.bool(True)
process.secondaryVertexTagInfos.trackSelection.maxDistToAxis = 0.1
process.secondaryVertexTagInfos.trackSelection.jetDeltaRMax = 0.5
process.secondaryVertexTagInfos.trackSelection.qualityClass = "tight"

######################################################
process.combinedSecondaryVertex.correctVertexMass = False
process.combinedSecondaryVertex.trackPairV0Filter = cms.PSet(k0sMassWindow = cms.double(0.015))
process.combinedSecondaryVertex.pseudoVertexV0Filter = cms.PSet(k0sMassWindow = cms.double(0.015))
process.combinedSecondaryVertex.trackMultiplicityMin = 2
process.combinedSecondaryVertex.trackSelection.maxDistToAxis = 999
process.combinedSecondaryVertex.trackSelection.qualityClass = 'tight'
process.combinedSecondaryVertex.trackSelection.maxDecayLen = 999
process.combinedSecondaryVertex.trackSelection.jetDeltaRMax = 999
process.combinedSecondaryVertex.trackPseudoSelection.maxDistToAxis = 999
process.combinedSecondaryVertex.trackPseudoSelection.qualityClass = 'tight'
process.combinedSecondaryVertex.trackPseudoSelection.maxDecayLen = 999
process.combinedSecondaryVertex.trackPseudoSelection.jetDeltaRMax = 999

######################################################
process.softPFElectrons.BarrelPtCuts                    = cms.vdouble(0.0, 9999.0)
process.softPFElectrons.BarreldRGsfTrackElectronCuts    = cms.vdouble(0.0, 0.005)
process.softPFElectrons.BarrelEemPinRatioCuts           = cms.vdouble(-0.2, 0.2)
process.softPFElectrons.BarrelMVACuts                   = cms.vdouble(-0.4, 1.0)
process.softPFElectrons.BarrelInversedRFirstLastHitCuts = cms.vdouble(0.0, 4.0)
process.softPFElectrons.BarrelRadiusFirstHitCuts        = cms.vdouble(0.0, 5.0)
process.softPFElectrons.BarrelZFirstHitCuts             = cms.vdouble(-20.0, 20.0)
process.softPFElectrons.ForwardPtCuts                     = cms.vdouble(0.0, 9999.0)
process.softPFElectrons.ForwardInverseFBremCuts           = cms.vdouble(1.0, 7.01)
process.softPFElectrons.ForwarddRGsfTrackElectronCuts     = cms.vdouble(0.0, 0.01)
process.softPFElectrons.ForwardRadiusFirstHitCuts         = cms.vdouble(0.0, 6.35)
process.softPFElectrons.ForwardZFirstHitCuts              = cms.vdouble(-50.0, 50.0)
process.softPFElectrons.ForwardMVACuts                    = cms.vdouble(-0.4, 1.0)

process.softElectronTagInfos.jets = cms.InputTag("goodJetsFilter")

######################################################
import RecoBTag.SoftLepton.muonSelection
process.softMuonTagInfos.jets = cms.InputTag("goodJetsFilter")
process.softMuonTagInfos.leptonChi2Cut = 10.0
process.softMuonTagInfos.muonSelection = RecoBTag.SoftLepton.muonSelection.AllTrackerMuons

######################################################
process.load("Validation.RecoB.bTagAnalysis_cfi")

#process.bTagValidation = process.bTagAnalysis.clone()
process.bTagValidation.jetMCSrc = 'ak5PFJetsValAlgo'
process.bTagValidation.allHistograms = True
#process.bTagValidation.finalizePlots = False 
#process.bTagValidation.finalizeOnly = False 
process.bTagValidation.ptRecJetMin = 10.0
process.bTagValidation.ptRanges = cms.vdouble(10.0, 20.0, 40.0, 9999.0)
process.bTagValidation.etaRanges = cms.vdouble(2.4)

######################################################
for i in [0, 1, 2, 3]:
	p = process.bTagValidation.tagConfig[1].parameters.categories[i]
	for j in ['vertexJetDeltaR', 'trackSumJetDeltaR', 'trackDeltaR']:
		if hasattr(p, j):
			getattr(p, j).max = 0.5
	for j in ['trackMomentum']:
		if hasattr(p, j):
			getattr(p, j).nBins = 100
			getattr(p, j).max = 20


process.bTagValidation.tagConfig = cms.VPSet(
        cms.PSet(
                process.bTagTrackIPAnalysisBlock,
                type = cms.string("TrackIP"),
                label = cms.InputTag("impactParameterTagInfos")
        ),
        cms.PSet(
                process.bTagCombinedSVAnalysisBlock,
                ipTagInfos = cms.InputTag("impactParameterTagInfos"),
                type = cms.string("GenericMVA"),
                svTagInfos = cms.InputTag("secondaryVertexTagInfos"),
                label = cms.InputTag("combinedSecondaryVertex")
        ),
	############### Disc
        cms.PSet(
            process.bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("trackCountingHighEffBJetTags")
        ), 
        cms.PSet(
            process.bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("trackCountingHighPurBJetTags")
        ), 
        cms.PSet(
            process.bTagProbabilityAnalysisBlock,
            label = cms.InputTag("jetProbabilityBJetTags")
        ), 
        cms.PSet(
            process.bTagBProbabilityAnalysisBlock,
            label = cms.InputTag("jetBProbabilityBJetTags")
        ), 
        cms.PSet(
            process.bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("simpleSecondaryVertexBJetTags")
        ), 
        cms.PSet(
            process.bTagGenericAnalysisBlock,
            label = cms.InputTag("combinedSecondaryVertexBJetTags")
        ), 
        cms.PSet(
            process.bTagGenericAnalysisBlock,
            label = cms.InputTag("combinedSecondaryVertexMVABJetTags")
        ), 
	################### SOFT LEPTON TAGINFOS  and Disc ###################
        cms.PSet(
            process.bTagSoftLeptonByIPAnalysisBlock,
            label = cms.InputTag("softElectronByIP3dBJetTags")
        ), 
        cms.PSet(
            process.bTagSoftLeptonByPtAnalysisBlock,
            label = cms.InputTag("softElectronByPtBJetTags")
        ),
        cms.PSet(
            process.bTagSoftLeptonAnalysisBlock,
            label = cms.InputTag("softMuonBJetTags")
        ),
	cms.PSet(
            process.bTagSoftLeptonByIPAnalysisBlock,
            label = cms.InputTag("softMuonByIP3dBJetTags")
        ), 
        cms.PSet(
            process.bTagSoftLeptonByPtAnalysisBlock,
            label = cms.InputTag("softMuonByPtBJetTags")
        ) ,
        cms.PSet(
            process.bTagSoftLeptonAnalysisBlock,
            type = cms.string("SoftLepton"),
            label = cms.InputTag("softMuonTagInfos")
        ),
        cms.PSet(
            process.bTagSoftLeptonAnalysisBlock,
            type = cms.string("SoftLepton"),
            label = cms.InputTag("softElectronTagInfos")
        )
)

#process.bTagValidation.tagConfig[2].parameters.discriminatorEnd = 10.0
#process.bTagValidation.tagConfig[3].parameters.discriminatorEnd = 10.0

######################################################
### Now put everything in the path in proper sequence
process.p = cms.Path(
	process.primaryVertexEventFilter *
	process.goodJetsFilter *
	process.ak5PFJetTracksAssociatorAtVertex *
	#### Truth Matching
	process.myPartons *
	process.ak5PFJetsByRef *
	process.ak5PFJetsValAlgo * 
	##### IP and SV Tag infos and discriminators
	process.impactParameterTagInfos *
	process.secondaryVertexTagInfos *
	## Disc
	process.trackCountingHighEffBJetTags *
	process.trackCountingHighPurBJetTags *
	process.jetProbabilityBJetTags *
	process.jetBProbabilityBJetTags *
	process.simpleSecondaryVertexBJetTags *
	process.combinedSecondaryVertexBJetTags *
	process.combinedSecondaryVertexMVABJetTags *
	##### Soft lepton tag info and discriminators
	process.softPFElectrons *
	process.softElectronTagInfos *
	process.softMuonTagInfos *
	## Disc
	process.softMuonBJetTags *
	process.softMuonByPtBJetTags *
	process.softMuonByIP3dBJetTags *
	process.softElectronByPtBJetTags *
	process.softElectronByIP3dBJetTags *
	#####
	process.bTagValidation *
	process.dqmSaver
	)

process.dqmEnv.subSystemFolder = 'BTAG'
process.dqmSaver.producer = 'DQM'
process.dqmSaver.workflow = '/POG/BTAG/BJET'
process.dqmSaver.convention = 'Offline'
process.dqmSaver.saveByRun = cms.untracked.int32(-1)
process.dqmSaver.saveAtJobEnd = cms.untracked.bool(True) 
process.dqmSaver.forceRunNumber = cms.untracked.int32(1)
######################################################
