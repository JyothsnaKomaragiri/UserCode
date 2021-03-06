#define TSelectorMultiDraw_cxx
// The class definition in TSelectorMultiDraw.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.

// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// Root > T->Process("TSelectorMultiDraw.C")
// Root > T->Process("TSelectorMultiDraw.C","some options")
// Root > T->Process("TSelectorMultiDraw.C+")
//

#include "TSelectorMultiDraw.h"
#include "TrackSelector.h"
#include "MuonSelector.h"
#include <TH2.h>
#include <TStyle.h>
#include "informationTrackCuts.h"
#include "informationMuonCuts.h"

using namespace std;

void TSelectorMultiDraw::Begin(TTree * tree)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();
 
   for(int i=0; i<nSelectors; i++)        fArrSelectors[i]->Begin(tree);  
   for(int j=0; j<nTrackSelectors; j++)   fArrTrackSelectors[j]->Begin(tree);
   for(int j=0; j<nMuonSelectors; j++)    fArrMuonSelectors[j]->Begin(tree);

}

void TSelectorMultiDraw::SlaveBegin(TTree * tree)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

}

Bool_t TSelectorMultiDraw::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // It can be passed to either TSelectorMultiDraw::GetEntry() or TBranch::GetEntry()
   // to read either all or the required parts of the data. When processing
   // keyed objects with PROOF, the object is already loaded and is available
   // via the fObject pointer.
   //
   // This function should contain the "body" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.
   //
   // The processing can be stopped by calling Abort().
   //
   // Use fStatus to set the return value of TTree::Process().
   //
   // The return value is currently not used.


//    for(list<TSelectorDraw*>::iterator iSelector = fSelectors.begin(); iSelector!=fSelectors.end(); iSelector++)
//      {
//        if((*iSelector)->ProcessCut(entry)) (*iSelector)->ProcessFill(entry);
//      }
//    for(list<TrackSelector*>::iterator iSelector = fTrackSelectors.begin(); iSelector!=fTrackSelectors.end(); iSelector++)
//      {
//          (*iSelector)->Process(entry);
//      }


  for(int i=0; i<nSelectors; i++)       if( fArrSelectors[i]->ProcessCut(entry) )  fArrSelectors[i]->ProcessFill(entry);
  for(int j=0; j<nTrackSelectors; j++)  fArrTrackSelectors[j]->Process(entry);
  for(int j=0; j<nMuonSelectors; j++)   fArrMuonSelectors[j]->Process(entry);
   
   return kTRUE;
}

void TSelectorMultiDraw::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.
}

void TSelectorMultiDraw::Terminate()
{
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.
  
   for(int i=0; i<nSelectors; i++)        fArrSelectors[i]->Terminate();  
   for(int j=0; j<nTrackSelectors; j++)   fArrTrackSelectors[j]->Terminate();
   for(int j=0; j<nMuonSelectors; j++)    fArrMuonSelectors[j]->Terminate();
  
}

void TSelectorMultiDraw::LoadVariables(string varexp, string selection)
{
  TSelectorDraw* thisSelector = new TSelectorDraw();
  TList* input = new TList();
  input->Add(new TNamed("varexp",varexp.c_str()));
  input->Add(new TNamed("selection",selection.c_str()));
  thisSelector->SetInputList(input);
  fSelectors.push_back(thisSelector);

  //  mySelector = thisSelector;
}

void TSelectorMultiDraw::AddTrackSelector(bool isData, TH1D*dataHist, TH1D* mcHistb, TH1D* mcHistc, TH1D* mcHistl, TH1D* mcHistn, informationTrackCuts info){
  TrackSelector *trackSel = new TrackSelector();
  trackSel->SetUp(isData, dataHist, mcHistb, mcHistc, mcHistl, mcHistn, info);
  fTrackSelectors.push_back(trackSel);
}

void TSelectorMultiDraw::AddMuonSelector(bool isData, TH1D*dataHist, TH1D* mcHistb, TH1D* mcHistc, TH1D* mcHistl, TH1D* mcHistn, informationMuonCuts info){
  MuonSelector *muSel = new MuonSelector();
  muSel->MuSetUp(isData, dataHist, mcHistb, mcHistc, mcHistl, mcHistn, info);
  fMuonSelectors.push_back(muSel);
}

void TSelectorMultiDraw::SetupArrays(){

  nSelectors      = fSelectors.size();
  nTrackSelectors = fTrackSelectors.size();
  nMuonSelectors  = fMuonSelectors.size();

  fArrSelectors      = new TSelectorDraw*[nSelectors];
  fArrTrackSelectors = new TrackSelector*[nTrackSelectors];
  fArrMuonSelectors  = new MuonSelector*[nMuonSelectors];


  int iSelCounter = 0;
  for(list<TSelectorDraw*>::iterator iSelector = fSelectors.begin(); iSelector!=fSelectors.end(); iSelector++)
    {
      fArrSelectors[iSelCounter] = *iSelector;
      iSelCounter++;
    }

  int iTrackSelCounter = 0;
  for(list<TrackSelector*>::iterator iSelector = fTrackSelectors.begin(); iSelector!=fTrackSelectors.end(); iSelector++)
    {
      fArrTrackSelectors[iTrackSelCounter] = *iSelector;
      iTrackSelCounter++;
    }

  int iMuonSelCounter = 0;
  for(list<MuonSelector*>::iterator iSelector = fMuonSelectors.begin(); iSelector!=fMuonSelectors.end(); iSelector++)
    {
      fArrMuonSelectors[iMuonSelCounter] = *iSelector;
      iMuonSelCounter++;
    }
}
