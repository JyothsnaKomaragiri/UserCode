import FWCore.ParameterSet.Config as cms

process = cms.Process("EventFilter")

process.load('Configuration/StandardSequences/Services_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.source = cms.Source("PoolSource",
    #inputCommands = cms.untracked.vstring("drop *","keep *_source_*_*"),
    fileNames = cms.untracked.vstring(
    'file:///storage/top/RAW/mc/RelValTTbar_Tauola/CC9D9A51-40C4-DF11-85AD-003048678E80.root',
     )
)

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
#process.genMaker = cms.Path( process.genParticles )

process.topTruthFilter = cms.EDFilter("TopMCLepJetFilter",
                                      truthVector = cms.InputTag("genParticles"),
                                      jetsVector = cms.InputTag("kt4GenJets"),
                                      daughterIds = cms.vint32(11), #PDGID is: 11 for electrons and 13 for muons
                                      leptonPt = cms.untracked.double(30.),
                                      leptonEta = cms.untracked.double(2.5),
                                      genJetPt = cms.untracked.double(30.),
                                      genJetEta = cms.untracked.double(8.0),
                                      dRcut = cms.untracked.double(0.3),
                                      nGoodJets = cms.untracked.uint32(2)
                                     )


process.Out = cms.OutputModule("PoolOutputModule",
                               outputCommands = cms.untracked.vstring('keep *'),
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p') ),
                               fileName = cms.untracked.string('skim04_1Ele_atLeast4Jets.root')
                              )

process.p = cms.Path(process.genParticles * process.topTruthFilter )
process.outpath = cms.EndPath(process.Out)

