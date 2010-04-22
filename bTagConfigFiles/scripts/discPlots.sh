#!/bin/sh

./jetTags_NormoverlayMCData.py -r p0discr 'TCHP Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r p1discr '10 < p_{T} < 20, TCHP Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r p2discr '20 < p_{T} < 40, TCHP Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r e0discr 'TCHE Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r e1discr '10 < p_{T} < 20, TCHE Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r e2discr '20 < p_{T} < 40, TCHE Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r j0discr 'JetProb Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r j1discr '10 < p_{T} < 20, JetProb Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r j2discr '20 < p_{T} < 40, JetProb Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r b0discr 'JetBProb Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r b1discr '10 < p_{T} < 20, JetBProb Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r b2discr '20 < p_{T} < 40, JetBProb Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r s0discr 'SSV Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r s1discr '10 < p_{T} < 20, SSV Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r s2discr '20 < p_{T} < 40, SSV Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r c0discr 'CSV Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r c1discr '10 < p_{T} < 20, CSV Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r c2discr '20 < p_{T} < 40, CSV Discriminator' 'MC Normalized to Data'

./jetTags_NormoverlayMCData.py -r m0discr 'CSV MVA Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r m1discr '10 < p_{T} < 20, CSV MVA Discriminator' 'MC Normalized to Data'
./jetTags_NormoverlayMCData.py -r m2discr '20 < p_{T} < 40, CSV MVA Discriminator' 'MC Normalized to Data'