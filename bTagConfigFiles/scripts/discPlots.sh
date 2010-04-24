#!/bin/sh

for category in `echo "loosePF" "standardPF" "looseCalo" "standardCalo"`
do

./jetTags_NormoverlayMCData.py -r TE0discr ${category} 'TCHE Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r TP0discr ${category} 'TCHP Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r JP0discr ${category} 'JetProb Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r JB0discr ${category} 'JetBProb Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r SE0discr ${category} 'SSV High Eff Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r SP0discr ${category} 'SSV High Puity Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r CS0discr ${category} 'CSV Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r CM0discr ${category} 'CSV MVA Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r MI0discr ${category} 'SoftMuonByIP3dBJetTags' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r MP0discr ${category} 'SoftMuonByPtBJetTags' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r MU0discr ${category} 'SoftMuonBJetTags' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r EI0discr ${category} 'SoftElectronByIP3dBJetTags' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r EP0discr ${category} 'SoftElectronByPtBJetTags' 'MC Normalized to Data'

done