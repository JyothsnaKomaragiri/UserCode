// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <DataFormats/Candidate/interface/Candidate.h>
#include <DataFormats/Common/interface/View.h>
#include <iostream>

//#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Math/interface/deltaR.h"

//
// class declaration
//

class TopMCLepJetFilter : public edm::EDFilter {

public:
  explicit TopMCLepJetFilter(const edm::ParameterSet&);
  ~TopMCLepJetFilter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ----------member data ---------------------------
  edm::InputTag truthVector_;
  edm::InputTag jetsVector_;
  std::vector<int> daughterIds_;

  //--- Lepton(ele/mu) pT and eta cuts
  double leptonPt_;
  double leptonEta_;

  //--- GenJet pT and eta cuts
  double genJetPt_;
  double genJetEta_;

  //--- dR cut for overlap removal of leptons from GenJets
  double dRcut_;
  
  //--- Good jet multiplicity
  unsigned int nGoodJets_;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TopMCLepJetFilter::TopMCLepJetFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
  truthVector_          = iConfig.getParameter<edm::InputTag> ("truthVector");
  jetsVector_           = iConfig.getParameter<edm::InputTag> ("jetsVector");
  daughterIds_          = iConfig.getParameter<std::vector<int> >  ("daughterIds");

  leptonPt_             = iConfig.getParameter<double>  ("leptonPt");
  leptonEta_            = iConfig.getParameter<double>  ("leptonEta");

  genJetPt_             = iConfig.getParameter<double>  ("genJetPt");
  genJetEta_            = iConfig.getParameter<double>  ("genJetEta");

  dRcut_                = iConfig.getParameter<double>  ("dRcut");

  nGoodJets_            = iConfig.getParameter<unsigned int>  ("nGoodJets");

}


TopMCLepJetFilter::~TopMCLepJetFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
TopMCLepJetFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;

   Handle<edm::View<reco::Candidate> > truthHandle;
   Handle<edm::View<reco::GenJet > > genjetsHandle;

   iEvent.getByLabel(truthVector_,truthHandle);
   iEvent.getByLabel(jetsVector_,genjetsHandle);

   bool found_lepton = false;
   unsigned int lepID = 0;

   for(edm::View<reco::Candidate>::const_iterator iParticle = truthHandle->begin(); iParticle != truthHandle->end(); iParticle++)
     {
       if(binary_search(daughterIds_.begin(),daughterIds_.end(),abs(iParticle->pdgId()) ) && 
	  iParticle->mother() && abs(iParticle->mother()->pdgId()) == 24 &&
	  iParticle->mother()->mother() && abs(iParticle->mother()->mother()->pdgId()) == 6 &&
	  fabs(iParticle->eta()) < leptonEta_ && iParticle->et() > leptonPt_ ) //kinematic cuts on lepton eta and ET
	 {
	   //cout << "Found One!" << endl;
	   found_lepton = true;
	   break;
	 }
       lepID++;
     }
   if(found_lepton == false)
       return false;

   unsigned int NGoodJets = 0;
   for (edm::View<reco::GenJet>::const_iterator iJet = genjetsHandle->begin(); iJet != genjetsHandle->end(); iJet++) {
     double dr = deltaR(truthHandle->at(lepID).eta(), truthHandle->at(lepID).phi(), iJet->eta(), iJet->phi());
     if (dr < dRcut_)
       continue;
     
     if (iJet->pt() > genJetPt_ && fabs(iJet->eta()) < genJetEta_) {
       NGoodJets++;
     }
   }
   
   //Filter events based on kinematic cuts on leptons, jets and jet multiplicity
   if (found_lepton && NGoodJets >= nGoodJets_) return true;

   return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 
TopMCLepJetFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TopMCLepJetFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(TopMCLepJetFilter);
