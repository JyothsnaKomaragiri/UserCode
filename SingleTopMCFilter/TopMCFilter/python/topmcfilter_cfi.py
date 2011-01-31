import FWCore.ParameterSet.Config as cms

topTruthFilter = cms.EDFilter("TopFilter",
                              truthVector = cms.InputTag("genParticles"),
                              jetsVector = cms.InputTag("kt4GenJets"),
                              daughterIds = cms.vint32(11), #PDGID is: 11 for electrons and 13 for muons
                              leptonPt = cms.untracked.double(30.),
                              leptonEta = cms.untracked.double(2.5),
                              genJetPt = cms.untracked.double(30.),
                              genJetEta = cms.untracked.double(8.0),
                              dRcut = cms.untracked.double(0.3),
                              nGoodJets = cms.untracked.uint(2)
                              )
