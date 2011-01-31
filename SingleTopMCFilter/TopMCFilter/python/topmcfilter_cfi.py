import FWCore.ParameterSet.Config as cms

topTruthFilter = cms.EDFilter("TopMCLepJetFilter",
                              truthVector = cms.InputTag("genParticles"),
                              jetsVector = cms.InputTag("kt4GenJets"),
                              daughterIds = cms.vint32(11), #PDGID is: 11 for electrons and 13 for muons
                              leptonPt = cms.double(30.),
                              leptonEta = cms.double(2.5),
                              genJetPt = cms.double(30.),
                              genJetEta = cms.double(8.0),
                              dRcut = cms.double(0.3),
                              nGoodJets = cms.uint32(2)
                              )
