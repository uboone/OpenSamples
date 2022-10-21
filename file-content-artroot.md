PROCESS NAME | MODULE_LABEL | PRODUCT INSTANCE NAME | DATA PRODUCT TYPE
Swizzler | pmtreadout | FlasherLogicPulse | std::vector<raw::OpDetWaveform>
Swizzler | ophit |  | std::vector<recob::OpHit>
Swizzler | beamdata |  | raw::BeamInfo
Swizzler | pmtreadout | BNBLogicPulse | std::vector<raw::OpDetWaveform>
Swizzler | opflash |  | "art::Assns<recob::OpFlash,recob::OpHit,void>"
Swizzler | daq |  | raw::ubdaqSoftwareTriggerData
Swizzler | daq |  | raw::BeamInfo
Swizzler | pmtreadout | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
Swizzler | pmtreadout | NUMILogicPulse | std::vector<raw::OpDetWaveform>
Swizzler | daq |  | std::vector<raw::Trigger>
Swizzler | pmtreadout | OpdetBeamLowGain | std::vector<raw::OpDetWaveform>
Swizzler | daq |  | raw::DAQHeader
Swizzler | pmtreadout | Uncategorized | std::vector<raw::OpDetWaveform>
Swizzler | pmtreadout | StrobeLogicPulse | std::vector<raw::OpDetWaveform>
Swizzler | pmtreadout | OpdetCosmicHighGain | std::vector<raw::OpDetWaveform>
Swizzler | pmtreadout | UnspecifiedLogic | std::vector<raw::OpDetWaveform>
Swizzler | pmtreadout | OpdetCosmicLowGain | std::vector<raw::OpDetWaveform>
Swizzler | TriggerResults |  | art::TriggerResults
Swizzler | opflash |  | std::vector<recob::OpFlash>
Swizzler | daq |  | std::vector<raw::RawDigit>
OverlayGen | generator |  | std::vector<simb::MCFlux>
OverlayGen | generator |  | std::vector<simb::MCTruth>
OverlayGen | generator |  | "art::Assns<simb::MCTruth,simb::GTruth,void>"
OverlayGen | generator |  | std::vector<sim::BeamGateInfo>
OverlayGen | rns |  | std::vector<art::RNGsnapshot>
OverlayGen | generator |  | std::vector<simb::GTruth>
OverlayGen | generator |  | "art::Assns<simb::MCTruth,simb::MCFlux,void>"
OverlayGen | TriggerResults |  | art::TriggerResults
G4EDep | rns |  | std::vector<art::RNGsnapshot>
G4EDep | largeant |  | std::vector<simb::MCParticle>
G4EDep | largeant |  | "art::Assns<simb::MCTruth,simb::MCParticle,sim::GeneratedParticleInfo>"
G4EDep | largeant | Other | std::vector<sim::SimEnergyDeposit>
G4EDep | largeant |  | std::vector<sim::AuxDetSimChannel>
G4EDep | largeant | TPCActive | std::vector<sim::SimEnergyDeposit>
G4EDep | mcreco |  | std::vector<sim::MCShower>
G4EDep | largeant |  | std::vector<sim::SimPhotons>
G4EDep | mcreco |  | std::vector<sim::MCTrack>
G4EDep | ionization |  | std::vector<sim::SimEnergyDeposit>
G4EDep | TriggerResults |  | art::TriggerResults
OverlayDetsim | crtdetsim |  | std::vector<crt::CRTSimData>
OverlayDetsim | pmtreadoutnonoise | FlasherLogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsim | pmtreadoutnonoise | OpdetBeamLowGain | std::vector<raw::OpDetWaveform>
OverlayDetsim | pmtreadoutnonoise | NUMILogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsim | optfem |  | std::vector<optdata::PMTTrigger>
OverlayDetsim | pmtreadoutnonoise | UnspecifiedLogic | std::vector<raw::OpDetWaveform>
OverlayDetsim | pmtreadoutnonoise | Uncategorized | std::vector<raw::OpDetWaveform>
OverlayDetsim | pmtreadoutnonoise | OpdetCosmicHighGain | std::vector<raw::OpDetWaveform>
OverlayDetsim | TriggerResults |  | art::TriggerResults
OverlayDetsim | triggersim |  | std::vector<raw::Trigger>
OverlayDetsim | swtriggernonoise |  | raw::ubdaqSoftwareTriggerData
OverlayDetsim | pmtreadoutnonoise | OpdetCosmicLowGain | std::vector<raw::OpDetWaveform>
OverlayDetsim | pmtreadoutnonoise | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
OverlayDetsim | nfbadchannel | badmasks | std::vector<int>
OverlayDetsim | optdigitizer |  | std::vector<sim::BeamGateInfo>
OverlayDetsim | zeroedoutchannels |  | std::vector<raw::RawDigit>
OverlayDetsim | pmtreadoutnonoise | BNBLogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsim | optdigitizer |  | optdata::ChannelDataGroup
OverlayDetsim | optfem |  | std::vector<optdata::FIFOChannel>
OverlayDetsim | crthitsim |  | std::vector<crt::CRTHit>
OverlayDetsim | rns |  | std::vector<art::RNGsnapshot>
OverlayDetsim | pmtreadoutnonoise | StrobeLogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsim | maskedcrthitsim |  | std::vector<crt::CRTHit>
OverlayDetsim | nfbadchannel | badchannels | std::vector<int>
DataOverlay | TriggerResults |  | art::TriggerResults
DataOverlay | mixer |  | std::vector<crt::CRTHit>
DataOverlay | mixer | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
DataOverlay | mixer |  | std::vector<raw::Trigger>
DataOverlay | mixer |  | std::vector<raw::RawDigit>
DataOverlay | mixer | OpdetBeamLowGain | std::vector<raw::OpDetWaveform>
DataOverlay | swtrigger |  | raw::ubdaqSoftwareTriggerData
OverlayStage1a | nfspl1 | threshold | std::vector<double>
OverlayStage1a | saturation | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
OverlayStage1a | simpleFlashBeamLowPE |  | "art::Assns<recob::OpHit,recob::OpFlash,void>"
OverlayStage1a | nfspl1 | badchannels | std::vector<int>
OverlayStage1a | simpleFlashCosmic |  | std::vector<recob::OpFlash>
OverlayStage1a | ophitCosmic |  | std::vector<recob::OpHit>
OverlayStage1a | nfspl1 | raw | std::vector<raw::RawDigit>
OverlayStage1a | nfspl1 | badmasks | std::vector<int>
OverlayStage1a | gaushit |  | std::vector<recob::Hit>
OverlayStage1a | nfspl1 | gauss | std::vector<recob::Wire>
OverlayStage1a | TriggerResults |  | art::TriggerResults
OverlayStage1a | rns |  | std::vector<art::RNGsnapshot>
OverlayStage1a | saturation | OpdetCosmicHighGain | std::vector<raw::OpDetWaveform>
OverlayStage1a | gaushit |  | "art::Assns<recob::Wire,recob::Hit,void>"
OverlayStage1a | simpleFlashBeam |  | std::vector<recob::OpFlash>
OverlayStage1a | simpleFlashCosmic |  | "art::Assns<recob::OpHit,recob::OpFlash,void>"
OverlayStage1a | ophitCosmicNoRemap |  | std::vector<recob::OpHit>
OverlayStage1a | ophitBeam |  | std::vector<recob::OpHit>
OverlayStage1a | simpleFlashBeamLowPE |  | std::vector<recob::OpFlash>
OverlayStage1a | butcher |  | "art::Assns<raw::RawDigit,recob::Wire,void>"
OverlayStage1a | ophitBeamNoRemap |  | std::vector<recob::OpHit>
OverlayStage1a | butcher |  | std::vector<recob::Wire>
OverlayStage1a | simpleFlashBeam |  | "art::Assns<recob::OpHit,recob::OpFlash,void>"
OverlayRecoStage1b | TriggerResults |  | art::TriggerResults
OverlayRecoStage1b | gaushitTruthMatch |  | "art::Assns<simb::MCParticle,recob::Hit,anab::BackTrackerHitMatchingData>"
OverlayRecoStage1c | TriggerResults |  | art::TriggerResults
OverlayRecoStage1c | opfiltercommon |  | uboone::UbooneOpticalFilter
OverlayDetsimOptical | pmtreadoutnonoise | BNBLogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | Uncategorized | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | OpdetCosmicLowGain | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | FlasherLogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | UnspecifiedLogic | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | triggersim |  | std::vector<raw::Trigger>
OverlayDetsimOptical | optdigitizer |  | optdata::ChannelDataGroup
OverlayDetsimOptical | TriggerResults |  | art::TriggerResults
OverlayDetsimOptical | swtriggernonoise |  | raw::ubdaqSoftwareTriggerData
OverlayDetsimOptical | lyscaling |  | std::vector<sim::SimPhotons>
OverlayDetsimOptical | pmtreadoutnonoise | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | StrobeLogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | optdigitizer |  | std::vector<sim::BeamGateInfo>
OverlayDetsimOptical | optfem |  | std::vector<optdata::FIFOChannel>
OverlayDetsimOptical | optfem |  | std::vector<optdata::PMTTrigger>
OverlayDetsimOptical | pmtreadoutnonoise | NUMILogicPulse | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | OpdetBeamLowGain | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | pmtreadoutnonoise | OpdetCosmicHighGain | std::vector<raw::OpDetWaveform>
OverlayDetsimOptical | rns |  | std::vector<art::RNGsnapshot>
DataOverlayNoTPC | swtrigger |  | raw::ubdaqSoftwareTriggerData
DataOverlayNoTPC | mixer |  | std::vector<raw::Trigger>
DataOverlayNoTPC | mixer | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
DataOverlayNoTPC | mixer |  | std::vector<crt::CRTHit>
DataOverlayNoTPC | TriggerResults |  | art::TriggerResults
DataOverlayNoTPC | mixer | OpdetBeamLowGain | std::vector<raw::OpDetWaveform>
OverlayStage1Optical | ophitBeamCalib |  | std::vector<recob::OpHit>
OverlayStage1Optical | TriggerResults |  | art::TriggerResults
OverlayStage1Optical | simpleFlashBeamLowPE |  | "art::Assns<recob::OpHit,recob::OpFlash,void>"
OverlayStage1Optical | ophitCosmicNoRemap |  | std::vector<recob::OpHit>
OverlayStage1Optical | ophitCosmicCalib |  | std::vector<recob::OpHit>
OverlayStage1Optical | simpleFlashBeamLowPE |  | std::vector<recob::OpFlash>
OverlayStage1Optical | rns |  | std::vector<art::RNGsnapshot>
OverlayStage1Optical | ophitBeam |  | std::vector<recob::OpHit>
OverlayStage1Optical | saturation | OpdetBeamHighGain | std::vector<raw::OpDetWaveform>
OverlayStage1Optical | simpleFlashBeam |  | "art::Assns<recob::OpHit,recob::OpFlash,void>"
OverlayStage1Optical | ophitCosmic |  | std::vector<recob::OpHit>
OverlayStage1Optical | simpleFlashCosmic |  | "art::Assns<recob::OpHit,recob::OpFlash,void>"
OverlayStage1Optical | ophitBeamNoRemap |  | std::vector<recob::OpHit>
OverlayStage1Optical | simpleFlashBeam |  | std::vector<recob::OpFlash>
OverlayStage1Optical | opfiltercommon |  | uboone::UbooneOpticalFilter
OverlayStage1Optical | saturation | OpdetCosmicHighGain | std::vector<raw::OpDetWaveform>
OverlayStage1Optical | simpleFlashCosmic |  | std::vector<recob::OpFlash>
OverlayRecoStage2 | pandoracalipidSCE |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoracali |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | pandoraAllOutcomesShower |  | "art::Assns<recob::Shower,recob::PCAxis,void>"
OverlayRecoStage2 | pandoracalipid |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoraKalmanTracktag |  | std::vector<anab::CosmicTag>
OverlayRecoStage2 | shrreco3d |  | "art::Assns<recob::Shower,recob::Hit,void>"
OverlayRecoStage2 | pandoraKalmanTrackcalo |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | pandoraGeomVertexFit |  | "art::Assns<recob::PFParticle,recob::Vertex,void>"
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::Shower,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | std::vector<larpandoraobj::PFParticleMetadata>
OverlayRecoStage2 | crtdistance |  | std::vector<recob::Vertex>
OverlayRecoStage2 | pandoraKalmanShowerpid |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandorapidSCE |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandoracaliSCE |  | std::vector<anab::Calorimetry>
OverlayRecoStage2 | acpttrigtagger |  | std::vector<anab::T0>
OverlayRecoStage2 | crttzero |  | "art::Assns<crt::CRTTzero,crt::CRTHit,void>"
OverlayRecoStage2 | crtt0Correction |  | std::vector<anab::T0>
OverlayRecoStage2 | pandoraKalmanTrackpid |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::PFParticle,recob::Vertex,void>"
OverlayRecoStage2 | pandoraKalmanShowercalo |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | acpttagger |  | "art::Assns<recob::Track,anab::T0,void>"
OverlayRecoStage2 | pandoraAllOutcomesShower |  | std::vector<recob::Shower>
OverlayRecoStage2 | pandoraCrtHitMatch |  | "art::Assns<recob::Track,crt::CRTTzero,void>"
OverlayRecoStage2 | shrreco3d |  | "art::Assns<recob::Shower,recob::PFParticle,void>"
OverlayRecoStage2 | pandoraKalmanTracktag |  | "art::Assns<recob::Track,anab::CosmicTag,void>"
OverlayRecoStage2 | pandoraKalmanTrack |  | "art::Assns<recob::Track,recob::Hit,recob::TrackHitMeta>"
OverlayRecoStage2 | pandora |  | std::vector<recob::Slice>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::Slice,void>"
OverlayRecoStage2 | pandoraAllOutcomesShower |  | "art::Assns<recob::PFParticle,recob::PCAxis,void>"
OverlayRecoStage2 | wcopflash | beam | std::vector<recob::OpFlash>
OverlayRecoStage2 | pandoraGeomVertexFit |  | "art::Assns<recob::Vertex,recob::Track,recob::VertexAssnMeta>"
OverlayRecoStage2 | pandoraAllOutcomesShower |  | "art::Assns<recob::Shower,recob::Hit,void>"
OverlayRecoStage2 | pandora |  | std::vector<larpandoraobj::PFParticleMetadata>
OverlayRecoStage2 | pandoraAllOutcomesTrack |  | std::vector<recob::Track>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::Vertex,void>"
OverlayRecoStage2 | pandoraMCSMuNoSCE |  | std::vector<recob::MCSFitResult>
OverlayRecoStage2 | crttzero |  | std::vector<crt::CRTTzero>
OverlayRecoStage2 | pandoraKalmanShower |  | "art::Assns<recob::PFParticle,recob::Track,void>"
OverlayRecoStage2 | pandoraAllOutcomesShower |  | "art::Assns<recob::PFParticle,recob::Shower,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::PFParticle,recob::Cluster,void>"
OverlayRecoStage2 | pandora |  | std::vector<recob::Shower>
OverlayRecoStage2 | pandoracalipidSCE |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::Cluster,recob::Hit,void>"
OverlayRecoStage2 | pandoraKalmanTrackcali |  | std::vector<anab::Calorimetry>
OverlayRecoStage2 | pandoracaloSCE |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | pandoraKalmanShowercali |  | std::vector<anab::Calorimetry>
OverlayRecoStage2 | pandoraKalmanTrackcalipid |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::SpacePoint,recob::Hit,void>"
OverlayRecoStage2 | crtveto |  | "art::Assns<crt::CRTHit,recob::OpFlash,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | std::vector<recob::Cluster>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::Cluster,void>"
OverlayRecoStage2 | pandoraCrtHitMatch |  | "art::Assns<recob::Track,anab::T0,void>"
OverlayRecoStage2 | wcopflash | cosmic | std::vector<recob::OpFlash>
OverlayRecoStage2 | pandoraPatRec | allOutcomes | std::vector<recob::Slice>
OverlayRecoStage2 | pandoraKalmanShowercalipid |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::Track,recob::Hit,recob::TrackHitMeta>"
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::SpacePoint,void>"
OverlayRecoStage2 | opNoiseCreateMask |  | std::vector<bool>
OverlayRecoStage2 | pandoraKalmanShower |  | "art::Assns<recob::Hit,recob::SpacePoint,void>"
OverlayRecoStage2 | pandoraKalmanTrack |  | std::vector<recob::Track>
OverlayRecoStage2 | pandoraCrtHitMatch |  | "art::Assns<recob::Track,crt::CRTHit,void>"
OverlayRecoStage2 | acpttrigtagger |  | "art::Assns<recob::Track,anab::T0,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::Cluster,recob::Hit,void>"
OverlayRecoStage2 | crttrackmatch |  | std::vector<anab::T0>
OverlayRecoStage2 | acpttagger |  | std::vector<anab::T0>
OverlayRecoStage2 | wcopflash | MergedBeam | std::vector<raw::OpDetWaveform>
OverlayRecoStage2 | pandora |  | std::vector<recob::Vertex>
OverlayRecoStage2 | crthitcorr |  | std::vector<crt::CRTHit>
OverlayRecoStage2 | pandoracalipid |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandoraPatRec | allOutcomes | std::vector<recob::Vertex>
OverlayRecoStage2 | pandora |  | std::vector<recob::PCAxis>
OverlayRecoStage2 | rns |  | std::vector<art::RNGsnapshot>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::Shower,recob::PCAxis,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | std::vector<recob::PFParticle>
OverlayRecoStage2 | pandora |  | "art::Assns<recob::SpacePoint,recob::Hit,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::PFParticle,recob::Slice,void>"
OverlayRecoStage2 | crttrackmatch |  | "art::Assns<recob::Track,crt::CRTHit,void>"
OverlayRecoStage2 | pandora |  | std::vector<recob::Track>
OverlayRecoStage2 | flashmatch |  | std::vector<anab::T0>
OverlayRecoStage2 | pandora |  | std::vector<recob::SpacePoint>
OverlayRecoStage2 | pandoraKalmanShowertag |  | std::vector<anab::CosmicTag>
OverlayRecoStage2 | pandorapidSCE |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoraGeomVertexFit |  | std::vector<recob::Vertex>
OverlayRecoStage2 | pandoracali |  | std::vector<anab::Calorimetry>
OverlayRecoStage2 | acpttrigtagger |  | "art::Assns<recob::Track,recob::OpFlash,void>"
OverlayRecoStage2 | pandoraAllOutcomesTrack |  | "art::Assns<recob::Track,recob::Hit,recob::TrackHitMeta>"
OverlayRecoStage2 | pandoraMCSMu |  | std::vector<recob::MCSFitResult>
OverlayRecoStage2 | shrreco3d |  | std::vector<recob::Shower>
OverlayRecoStage2 | pandoraPatRec | allcandidatevertices | std::vector<recob::Vertex>
OverlayRecoStage2 | pandoraKalmanShowercalipid |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoraKalmanShower |  | "art::Assns<recob::Track,recob::Hit,recob::TrackHitMeta>"
OverlayRecoStage2 | pandora |  | std::vector<recob::PFParticle>
OverlayRecoStage2 | pandora |  | std::vector<recob::Cluster>
OverlayRecoStage2 | pandoraKalmanShowertag |  | "art::Assns<recob::Track,anab::CosmicTag,void>"
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,larpandoraobj::PFParticleMetadata,void>"
OverlayRecoStage2 | crthitcorrFirstPass |  | std::vector<crt::CRTHit>
OverlayRecoStage2 | pandoraKalmanTrackcalipid |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoraPatRec | allcandidatevertices | "art::Assns<recob::Slice,recob::Vertex,void>"
OverlayRecoStage2 | pandoraKalmanTrack |  | "art::Assns<recob::Hit,recob::SpacePoint,void>"
OverlayRecoStage2 | pandoraAllOutcomesTrack |  | "art::Assns<recob::PFParticle,recob::Track,void>"
OverlayRecoStage2 | crttrack |  | std::vector<crt::CRTTrack>
OverlayRecoStage2 | pandoraKalmanTrack |  | "art::Assns<recob::PFParticle,recob::Track,void>"
OverlayRecoStage2 | shrreco3d |  | "art::Assns<recob::Shower,recob::Cluster,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::Slice,recob::Hit,void>"
OverlayRecoStage2 | acpttagger |  | "art::Assns<recob::Track,recob::OpFlash,void>"
OverlayRecoStage2 | wcopflash | MergedCosmic | std::vector<raw::OpDetWaveform>
OverlayRecoStage2 | pandoraAllOutcomesShower |  | std::vector<recob::PCAxis>
OverlayRecoStage2 | pandoracaliSCE |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | pandoraKalmanTrackpid |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandoratag |  | "art::Assns<recob::Track,anab::CosmicTag,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::PFParticle,larpandoraobj::PFParticleMetadata,void>"
OverlayRecoStage2 | pandorapid |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandoraPatRec | allOutcomes | std::vector<recob::SpacePoint>
OverlayRecoStage2 | flashmatch |  | "art::Assns<recob::PFParticle,anab::T0,void>"
OverlayRecoStage2 | crttrackmatch |  | "art::Assns<recob::Track,anab::T0,void>"
OverlayRecoStage2 | pandoraKalmanShowerpid |  | "art::Assns<recob::Track,anab::ParticleID,void>"
OverlayRecoStage2 | pandora |  | "art::Assns<recob::Slice,recob::Hit,void>"
OverlayRecoStage2 | pandoraKalmanShower |  | std::vector<recob::Track>
OverlayRecoStage2 | pandoraContTag |  | std::vector<anab::CosmicTag>
OverlayRecoStage2 | TriggerResults |  | art::TriggerResults
OverlayRecoStage2 | pandoratag |  | std::vector<anab::CosmicTag>
OverlayRecoStage2 | pandoraKalmanShowercali |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | crtdistance |  | "art::Assns<recob::Vertex,recob::Track,void>"
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::Track,void>"
OverlayRecoStage2 | pandoracalo |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
OverlayRecoStage2 | pandoraCrtHitMatch |  | std::vector<anab::T0>
OverlayRecoStage2 | pandorapid |  | std::vector<anab::ParticleID>
OverlayRecoStage2 | pandoraPatRec | allOutcomes | "art::Assns<recob::PFParticle,recob::SpacePoint,void>"
OverlayRecoStage2 | pandora |  | "art::Assns<recob::PFParticle,recob::PCAxis,void>"
OverlayRecoStage2 | pandoraKalmanTrackcali |  | "art::Assns<recob::Track,anab::Calorimetry,void>"
