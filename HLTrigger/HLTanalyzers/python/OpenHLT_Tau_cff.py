
import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTanalyzers.HLT_FULL_cff import hltEcalRawToRecHitFacility,hltEcalRegionalJetsFEDs,hltEcalRegionalJetsRecHit,HLTDoLocalHcalSequence,hltTowerMakerForJets,hltCaloTowersTau1Regional,hltIconeTau1Regional,hltCaloTowersTau2Regional,hltIconeTau2Regional,hltCaloTowersTau3Regional,hltIconeTau3Regional,hltCaloTowersTau4Regional,hltIconeTau4Regional,hltCaloTowersCentral1Regional,hltIconeCentral1Regional,hltCaloTowersCentral2Regional,hltIconeCentral2Regional,hltCaloTowersCentral3Regional,hltIconeCentral3Regional,hltCaloTowersCentral4Regional,hltIconeCentral4Regional,HLTDoLocalStripSequence

hltTauL1SeedFilter = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet10 OR L1_SingleJet15" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
hltCaloTowersCentral1 = cms.EDProducer("CaloTowerCreatorForTauHLT",
    towers = cms.InputTag("hltTowerMakerForAll"),
    TauId = cms.int32(0),
    TauTrigger = cms.InputTag("hltL1extraParticles","Central"),
    minimumE = cms.double(0.8),
    UseTowersInCone = cms.double(0.8),
    minimumEt = cms.double(0.5)
)
hltCaloTowersCentral2 = cms.EDProducer("CaloTowerCreatorForTauHLT",
    towers = cms.InputTag("hltTowerMakerForAll"),
    TauId = cms.int32(1),
    TauTrigger = cms.InputTag("hltL1extraParticles","Central"),
    minimumE = cms.double(0.8),
    UseTowersInCone = cms.double(0.8),
    minimumEt = cms.double(0.5)
)
hltCaloTowersCentral3 = cms.EDProducer("CaloTowerCreatorForTauHLT",
    towers = cms.InputTag("hltTowerMakerForAll"),
    TauId = cms.int32(2),
    TauTrigger = cms.InputTag("hltL1extraParticles","Central"),
    minimumE = cms.double(0.8),
    UseTowersInCone = cms.double(0.8),
    minimumEt = cms.double(0.5)
)
hltCaloTowersCentral4 = cms.EDProducer("CaloTowerCreatorForTauHLT",
    towers = cms.InputTag("hltTowerMakerForAll"),
    TauId = cms.int32(3),
    TauTrigger = cms.InputTag("hltL1extraParticles","Central"),
    minimumE = cms.double(0.8),
    UseTowersInCone = cms.double(0.8),
    minimumEt = cms.double(0.5)
)
hltIcone2Tau1 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersTau1" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Tau2 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersTau2" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Tau3 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersTau3" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Tau4 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersTau4" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Central1 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersCentral1" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Central2 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersCentral2" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Central3 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersCentral3" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
hltIcone2Central4 = cms.EDProducer( "IterativeConeJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.2 ),
    verbose = cms.untracked.bool( False ),
    jetType = cms.untracked.string( "CaloJet" ),
    src = cms.InputTag( "hltCaloTowersCentral4" ),
    jetPtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    inputEtMin = cms.double( 0.5 ),
    debugLevel = cms.untracked.int32( 0 ),
    alias = cms.untracked.string( "IC5CaloJet" ),
    correctInputToSignalVertex = cms.bool( False ),
    pvCollection = cms.InputTag( "offlinePrimaryVertices" )
)
openhltL2TauJets = cms.EDProducer( "L2TauJetsMerger",
    EtMin = cms.double( 1.0 ),
    JetSrc = cms.VInputTag( 'hltIconeTau1Regional','hltIconeTau2Regional','hltIconeTau3Regional','hltIconeTau4Regional','hltIconeCentral1Regional','hltIconeCentral2Regional','hltIconeCentral3Regional','hltIconeCentral4Regional' )
)
openhltL2TauIsolationProducer = cms.EDProducer( "L2TauNarrowConeIsolationProducer",
    L2TauJetCollection = cms.InputTag( "openhltL2TauJets" ),
    EBRecHits = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    EERecHits = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
                                            CaloTowers = cms.InputTag('hltTowerMakerForAll'),                                       
crystalThresholdEE = cms.double( 0.45 ),
    crystalThresholdEB = cms.double( 0.15 ),
    towerThreshold = cms.double(1.0 ),
    associationRadius = cms.double(0.5 ),

    ECALIsolation = cms.PSet( 
      runAlgorithm = cms.bool( True ),
      innerCone = cms.double( 0.15 ),
      outerCone = cms.double( 0.5 )
    ),
    ECALClustering = cms.PSet( 
      runAlgorithm = cms.bool( True ),
      clusterRadius = cms.double( 0.08 )
    ),
     TowerIsolation = cms.PSet( 
     runAlgorithm = cms.bool( True ),
      innerCone = cms.double( 0.2 ),
      outerCone = cms.double( 0.5 )
    )
)

openhltL25TauPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
                                          ClusterCheckPSet = cms.PSet(
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.5 ),
        deltaEtaRegion = cms.double( 0.5 ),
        ptMin = cms.double( 0.9 ),
        originZPos = cms.double( 0.0 ),
        originRadius = cms.double( 0.2 ),
        originHalfLength = cms.double( 0.2 ),
        precise = cms.bool( True ),
        JetSrc = cms.InputTag( 'openhltL2TauJets' ),
        vertexSrc = cms.InputTag( "hltPixelVertices" )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" ),
      maxElement = cms.uint32( 0 )      
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
openhltL25TauCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "openhltL25TauPixelSeeds" ),
    TrajectoryBuilder = cms.string( "hltESPTrajectoryBuilderL3" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" ),
      numberMeasurementsForFit = cms.int32(4)
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
openhltL25TauCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( "openhltL25TauCkfTrackCandidates" ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
openhltL25TauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'openhltL2TauJets' ),
    tracks = cms.InputTag( "openhltL25TauCtfWithMaterialTracks" ),
    coneSize = cms.double( 0.5 )
)
openhltL25TauConeIsolation = cms.EDProducer( "ConeIsolation",
    JetTrackSrc = cms.InputTag( "openhltL25TauJetTracksAssociator" ),
    vertexSrc = cms.InputTag( "hltPixelVertices" ),
    useVertex = cms.bool( True ),
    useBeamSpot = cms.bool( True ),
    BeamSpotProducer = cms.InputTag( "hltOfflineBeamSpot" ),
    MinimumNumberOfPixelHits = cms.int32( 2 ),
    MinimumNumberOfHits = cms.int32( 5 ),
    MaximumTransverseImpactParameter = cms.double( 300.0 ),
    MinimumTransverseMomentum = cms.double( 1.0 ),
    MaximumChiSquared = cms.double( 100.0 ),
    DeltaZetTrackVertex = cms.double( 0.2 ),
    MatchingCone = cms.double( 0.2 ),
    SignalCone = cms.double( 0.15 ),
    IsolationCone = cms.double( 0.5 ),
    MinimumTransverseMomentumInIsolationRing = cms.double( 1.5 ),
    MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
    MaximumNumberOfTracksIsolationRing = cms.int32( 1 ),
    UseFixedSizeCone = cms.bool( True ),
    VariableConeParameter = cms.double( 3.5 ),
    VariableMaxCone = cms.double( 0.17 ),
    VariableMinCone = cms.double( 0.05 )
)
TauOpenHLT = cms.EDProducer("HLTTauProducer",
    L25TrackIsoJets = cms.InputTag("openhltL25TauConeIsolation"),
    L3TrackIsoJets = cms.InputTag("openhltL25TauConeIsolation"),
    SignalCone = cms.double(0.15),
    MatchingCone = cms.double(0.2),
    MinPtTracks = cms.double(1.),
    L2EcalIsoJets = cms.InputTag("openhltL2TauIsolationProducer"),
    IsolationCone = cms.double(0.5)
)

OpenHLTDoCaloSequence = cms.Sequence( hltEcalRawToRecHitFacility + hltEcalRegionalJetsFEDs + hltEcalRegionalJetsRecHit + HLTDoLocalHcalSequence + hltTowerMakerForJets)
OpenHLTCaloTausCreatorSequence = cms.Sequence( OpenHLTDoCaloSequence + hltCaloTowersTau1Regional + hltIconeTau1Regional + hltCaloTowersTau2Regional + hltIconeTau2Regional + hltCaloTowersTau3Regional + hltIconeTau3Regional + hltCaloTowersTau4Regional + hltIconeTau4Regional + hltCaloTowersCentral1Regional + hltIconeCentral1Regional + hltCaloTowersCentral2Regional + hltIconeCentral2Regional + hltCaloTowersCentral3Regional + hltIconeCentral3Regional + hltCaloTowersCentral4Regional + hltIconeCentral4Regional )
OpenHLTL25TauTrackReconstructionSequence = cms.Sequence( HLTDoLocalStripSequence + openhltL25TauPixelSeeds + openhltL25TauCkfTrackCandidates + openhltL25TauCtfWithMaterialTracks )
OpenHLTL25TauTrackIsolation = cms.Sequence( openhltL25TauJetTracksAssociator + openhltL25TauConeIsolation )



#Particle Flow
#Modifying the trajFilter
#trajFilterL3.maxNumberOfHits = cms.int32(100)
#trajFilterL3.minPt = cms.double(0.5)

#HLTRecoJetSequencePrePF = cms.Sequence( HLTDoCaloSequence + hltIterativeCone5CaloJets + hltIterativeCone5CaloJets8 )

#HLTTrackReconstructionForJets = cms.Sequence( hltPFJetPixelSeeds + hltPFJetCkfTrackCandidates + hltPFJetCtfWithMaterialTracks +hltPFJetCkfTrackCandidatesHighPurity )
#HLTPreshowerSequence = cms.Sequence( hltESRawToRecHitFacility + 
#                                     hltEcalRegionalESRestFEDs + 
#                                     hltESRecHitAll 
#                                     )
#HLTParticleFlowSequence = cms.Sequence( HLTPreshowerSequence + hltParticleFlowRecHitECAL + hltParticleFlowRecHitHCAL + hltParticleFlowRecHitPS + hltParticleFlowClusterECAL + hltParticleFlowClusterHCAL + hltParticleFlowClusterHFEM + hltParticleFlowClusterHFHAD + hltParticleFlowClusterPS + hltLightPFTracks + hltParticleFlowBlock + hltParticleFlow )
#HLTPFJetsSequence = cms.Sequence( hltIcone5PFJets )
#HLTPFJetTriggerSequence = cms.Sequence( HLTRecopixelvertexingSequence + HLTTrackReconstructionForJets + HLTParticleFlowSequence + HLTPFJetsSequence )
#HLTPFTauSequence = cms.Sequence( hltPFTauJetTracksAssociator + hltPFTauTagInfo + hltPFTaus)

#Particle Flow
hltPFTaus = cms.EDProducer( "PFRecoTauProducer",
 PFTauTagInfoProducer = cms.InputTag( "hltPFTauTagInfo" ),
 ElectronPreIDProducer = cms.InputTag( "elecpreid" ),
 PVProducer = cms.InputTag( "hltPixelVertices" ),
 Algorithm = cms.string( "ConeBased" ),
 smearedPVsigmaX = cms.double( 0.0015 ),
 smearedPVsigmaY = cms.double( 0.0015 ),
 smearedPVsigmaZ = cms.double( 0.0050 ),
 JetPtMin = cms.double( 0.0 ),
 LeadPFCand_minPt = cms.double( 0.0 ),
 TrackerSignalConeMetric = cms.string( "DR" ),
 TrackerSignalConeSizeFormula = cms.string( "0.2" ),
 TrackerSignalConeSize_min = cms.double( 0.0 ),
 TrackerSignalConeSize_max = cms.double( 0.3 ),
 ECALSignalConeMetric = cms.string( "DR" ),
 ECALSignalConeSizeFormula = cms.string( "0.2" ),
 ECALSignalConeSize_min = cms.double( 0.0 ),
 ECALSignalConeSize_max = cms.double( 0.6 ),
 HCALSignalConeMetric = cms.string( "0.2" ),
 HCALSignalConeSizeFormula = cms.string( "0.10" ),
 HCALSignalConeSize_min = cms.double( 0.0 ),
 HCALSignalConeSize_max = cms.double( 0.6 ),
 TrackerIsolConeMetric = cms.string( "DR" ),
 TrackerIsolConeSizeFormula = cms.string( "0.50" ),
 TrackerIsolConeSize_min = cms.double( 0.0 ),
 TrackerIsolConeSize_max = cms.double( 0.6 ),
 ECALIsolConeMetric = cms.string( "DR" ),
 ECALIsolConeSizeFormula = cms.string( "0.50" ),
 ECALIsolConeSize_min = cms.double( 0.0 ),
 ECALIsolConeSize_max = cms.double( 0.6 ),
 HCALIsolConeMetric = cms.string( "DR" ),
 HCALIsolConeSizeFormula = cms.string( "0.50" ),
 HCALIsolConeSize_min = cms.double( 0.0 ),
 HCALIsolConeSize_max = cms.double( 0.6 ),
 ChargedHadrCand_IsolAnnulus_minNhits = cms.uint32( 0 ),
 EcalStripSumE_deltaPhiOverQ_minValue = cms.double( -0.1 ),
 EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.5 ),
 EcalStripSumE_minClusEnergy = cms.double( 0.1 ),
 EcalStripSumE_deltaEta = cms.double( 0.03 ),
 ElecPreIDLeadTkMatch_maxDR = cms.double( 0.01 ),
 maximumForElectrionPreIDOutput = cms.double( -0.1 ),
 MatchingConeMetric = cms.string( "DR" ),
 MatchingConeSizeFormula = cms.string( "0.15" ),
 MatchingConeSize_min = cms.double( 0.0 ),
 MatchingConeSize_max = cms.double( 0.6 ),
 UseChargedHadrCandLeadChargedHadrCand_tksDZconstraint = cms.bool(True ),
 ChargedHadrCandLeadChargedHadrCand_tksmaxDZ = cms.double( 0.4 ),
 LeadTrack_minPt = cms.double( 0.0 ),
 TrackLeadTrack_maxDZ = cms.double( 0.4 ),
 UseTrackLeadTrackDZconstraint = cms.bool( True ),
 Track_IsolAnnulus_minNhits = cms.uint32( 3 ),
 AddEllipseGammas = cms.bool( False ),
 Rphi = cms.double( 2.0 ),
 MaxEtInEllipse = cms.double( 2.0 ),
 AreaMetric_recoElements_maxabsEta = cms.double( 2.5 ),
 DataType = cms.string( "AOD" )
)

hltPFTausTightCone = hltPFTaus.clone()
hltPFTausTightCone.TrackerSignalConeSizeFormula = cms.string( "0.15" )
hltPFTausTightCone.ECALSignalConeSizeFormula = cms.string( "0.15" )

#HLTPFTauSequence+= hltPFTausTightCone

