File Entry | Type | N Elements | Description
-- | -- | -- | --
/ | Group |   | Main entry point of the file.
/event_table | Group |   | Table storing information about a single detector readout and a single simulated neutrino interaction.
/event_table/event_id | Dataset | 3 | Run/Subrun/Event number for a detector readout.
/event_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/event_table/is_cc | Dataset | 1 | If 1 the simulated neutrino interaction is charged-current, if 0 it is neutral-current.
/event_table/lep_energy | Dataset | 1 | Simulated energy of the lepton outgoing from the neutrino interaction (in GeV).
/event_table/nu_dir | Dataset | 3 | Initial direction of the simulated neutrino interacting in the detector (3D cartesian coordinates).
/event_table/nu_energy | Dataset | 1 | Simulated energy of the interacting neutrino (in GeV).
/event_table/nu_pdg | Dataset | 1 | Particle Data Group (PDG) particle code for the interacting neutrino. See https://pdg.lbl.gov/2022/reviews/rpp2022-rev-monte-carlo-numbering.pdf.
/event_table/nu_vtx | Dataset | 3 | Simulated position of neutrino interaction (3D cartesian coordinates, in cm). This quantity is to be used to compare with e.g. the detector boundaries.
/event_table/nu_vtx_corr | Dataset | 3 | Simulated position of neutrino interaction (3D cartesian coordinates, in cm), after correcting for detector effects such as space charge. This is the quantity to be used for comparison with reconstructed information.
/event_table/nu_vtx_wire_pos | Dataset | 3 | Simulated position of neutrino interaction (per-plane wire coordinates), after correcting for detector effects such as space charge. This is the quantity to be used for comparison with reconstructed information.
/event_table/nu_vtx_wire_time | Dataset | 1 | Simulated time of neutrino interaction (in ns).#CHECK
/hit_table | Group |   | Table storing information about reconstructed hits, i.e. Gaussian pulses detected on the wire waveform.
/hit_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/hit_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/hit_table/hit_id | Dataset | 1 | Index of this hit in the table, unique for a given event.
/hit_table/integral | Dataset | 1 | Integral (amplitude) of the Gaussian, in ADC units. This quantity is proportional to the energy (ionization charge) deposited by particles in the argon.
/hit_table/local_plane | Dataset | 1 | Id of the plane where the wire is located. Plane 0 and 1 are induction planes with wire orientation +/-60 degress wrt vertical, plane 2 is the collection plane with vertical wire orientation.
/hit_table/local_time | Dataset | 1 | Peak time of the Gaussian pulse, in detector clock units (ticks).
/hit_table/local_wire | Dataset | 1 | Id of the wire where the hit is located. Plane 0 and 1 have ids in the range [0,2399], plane 2 in range [0,3455].
/hit_table/rms | Dataset | 1 | Width of the Gaussian pulse, in detector clock units (ticks).
/hit_table/tpc | Dataset | 1 | Id of the Time Projection Chamber where the planes are located. In MicroBooNE there is only 1 TPC so this should be always 0.
/edep_table | Group |   | Table storing the simulated (true) energy deposit information in the TPC.
/edep_table/energy | Dataset | 1 | Deposited energy.
/edep_table/energy_fraction | Dataset | 1 | Fraction of the hit energy corresponding to this deposity.
/edep_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/edep_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/edep_table/g4_id | Dataset | 1 | Id of the simulated particle that originated this deposit. This index refers to entries in the particle_table.
/edep_table/hit_id | Dataset | 1 | Id of the hit this deposit contributes to. This index refers to entries in the hit_table.
/particle_table | Group | - | Table storing information about particles simulated by Geant4 (https://geant4.web.cern.ch/) as they propagate through in the liquid argon of the detector. In this dataset only the neutrino interaction is simulated, and it is overlaid to cosmics from real data (taken with beam off).
/particle_table/category | Dataset | 1 | Category of this particle (semantic label). See enum "category" definition in detector_utils.py.
/particle_table/end_position | Dataset | 3 | End position of the simulated particle (3D cartesian coordinates, in cm). This quantity is to be used to compare with e.g. the detector boundaries.
/particle_table/end_position_corr | Dataset | 3 | End position of the simulated particle (3D cartesian coordinates, in cm), after correcting for detector effects such as space charge. This is the quantity to be used for comparison with reconstructed information.
/particle_table/end_process | Dataset | 1 | Physics process that terminated the current particle. Format is a string.
/particle_table/end_wire_pos | Dataset | 3 | End position of the simulated particle (per-plane wire coordinates), after correcting for detector effects such as space charge. This is the quantity to be used for comparison with reconstructed information.
/particle_table/end_wire_time | Dataset | 1 | End time of the simulated particle, in detector clock units (ticks).
/particle_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/particle_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/particle_table/g4_id | Dataset | 1 | Id of this particle in the table (as used internally by Geant4), unique for a given event.
/particle_table/g4_pdg | Dataset | 1 | Particle Data Group (PDG) particle code for the simulated particle.
/particle_table/instance | Dataset | 1 | Particle instance counting. Only certain categories are counted: pion, muon, kaon, proton, electron, michel, photon.
/particle_table/momentum | Dataset | 1 | Momentum of the simulated particle (in GeV). #CHECK
/particle_table/parent_id | Dataset | 1 | Id of the parent particle that generated the current one (via decay, interaction, or other processes). The index refers to the g4_id in this same table (for the same event_id). Index -1 refers to particles that are coming into the detector (e.g. neutrinos from the beam).
/particle_table/start_position | Dataset | 3 | Start position of the simulated particle (3D cartesian coordinates, in cm). This quantity is to be used to compare with e.g. the detector boundaries.
/particle_table/start_position_corr | Dataset | 3 | Start position of the simulated particle (3D cartesian coordinates, in cm), after correcting for detector effects such as space charge. This is the quantity to be used for comparison with reconstructed information.
/particle_table/start_process | Dataset | 1 | Physics process that originated the current particle. Format is a string. Here "Primary" has a different meaning than what used in the pandoraPrimary table, and refers to particles directly emerging from the neutrino-nucleus interaction (as opposed to those decaying or interacting in the argon).
/particle_table/start_wire_pos | Dataset | 3 | Start position of the simulated particle (per-plane wire coordinates), after correcting for detector effects such as space charge. This is the quantity to be used for comparison with reconstructed information.
/particle_table/start_wire_time | Dataset | 1 | Start time of the simulated particle, in detector clock units (ticks).
/opflash_table | Group |   | Table storing information about reconstructed flashes of light detected by the photomultiplier tubes (PMTs) in coincence with the beam.
/opflash_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/opflash_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/opflash_table/flash_id | Dataset | 1 | Index of this flash in the table, unique for a given event.
/opflash_table/time | Dataset | 1 | Time of this flash (in µs).
/opflash_table/time_width | Dataset | 1 | Width of the flash time.
/opflash_table/totalpe | Dataset | 1 | Total number of PE in the flash.
/opflash_table/wire_pos | Dataset | 3 | Barycenter PE position of the flash (per-plane wire coordinates). Obtained by weighting the position of each PMT by its PE in the flash.
/opflash_table/y_center | Dataset | 1 | Barycenter position of the flash in the Y cartesian coordinate (vertical, parallel to plane 2 wires). Obtained by weighting the position of each PMT by its PE in the flash.
/opflash_table/y_width | Dataset | 1 | Width (RMS) of the Y position.
/opflash_table/z_center | Dataset | 1 | Barycenter position of the flash in the Z cartesian coordinate (longitudinal to the beam, orthogonal to plane 2 wires). Obtained by weighting the position of each PMT by its PE in the flash.
/opflash_table/z_width | Dataset | 1 | Width (RMS) of the Z position.
/opflashsumpe_table | Group |   | Number of photoelectrons (PE) recorded by a flash in each of the 32 PMT. This quantity combines contributions from multiple OpHits and is after calibration and pedestal subtraction.
/opflashsumpe_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/opflashsumpe_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/opflashsumpe_table/flash_id | Dataset | 1 | Id of the flash to which this quantity refers to, referring to entries in the opflash_table.
/opflashsumpe_table/pmt_channel | Dataset | 1 | Id of the PMT from where the quantity comes from.
/opflashsumpe_table/sumpe | Dataset | 1 | Value of the PE sum.
/opflashsumpe_table/sumpe_id | Dataset | 1 | Index of this entry in the table, unique for a given event.
/ophit_table | Group |   | Table storing information about reconstructed hits in the optical detectors, i.e. Gaussian pulses detected on the photomultiplier tube (PMT) waveform.
/ophit_table/amplitude | Dataset | 1 | Amplitude of the Gaussian pulse, in ADC units. #CHECK
/ophit_table/area | Dataset | 1 | Area of the Gaussian curve. #CHECK units
/ophit_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/ophit_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/ophit_table/hit_channel | Dataset | 1 | Id of the PMT where the OpHit is located.
/ophit_table/hit_id | Dataset | 1 | Index of this ophit in the table, unique for a given event.
/ophit_table/pe | Dataset | 1 | Number of photoelectrons (PE) detected in this hit. This quantity is before calibration and pedestal subtraction.
/ophit_table/peaktime | Dataset | 1 | Peak time of the Gaussian pulse, in detector clock units (ticks).#CHECK
/ophit_table/sumpe_id | Dataset | 1 | Id of the "sum PE" to which this OpHit contributes to, referring to entries in the opflashsumpe_table. If -1, then the OpHit is not used in any sum PE nor in any flash.
/ophit_table/width | Dataset | 1 | Width of the Gaussian pulse, in detector clock units (ticks).#CHECK
/ophit_table/wire_pos | Dataset | 3 | Position of the PMT (in per-plane wire coordinates).
/pandoraHit_table | Group | - | Table storing information about how hits are classified and clustered by Pandora.
/pandoraHit_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/pandoraHit_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/pandoraHit_table/hit_id | Dataset | 1 | Id of the hit this entry refers to. This index refers to entries in the hit_table.
/pandoraHit_table/pfp_id | Dataset | 1 | Id of the PFP this entry refers to. This index refers to entries in the pandoraPfp_table.
/pandoraHit_table/slice_id | Dataset | 1 | Id of the slice this entry refers to. This index refers to entries in the pandoraPrimary_table.
/pandoraPfp_table | Group |   | Table storing information about PFParticles, i.e. clusters of hits in the wire planes that are matched in 3D. This is limited to PFParticles that Pandora classifies as originating from the neutrino interaction.
/pandoraPfp_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/pandoraPfp_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/pandoraPfp_table/pfp_id | Dataset | 1 | Index of this PFP in the table, unique for a given event.#CHECK what about a given slice?
/pandoraPfp_table/pfp_pdg | Dataset | 1 | Particle Data Group (PDG) particle code for the PFP. Only two values are used: 11 (electron, i.e. shower-like PFP) and 13 (muon, i.e. track-like PFP).
/pandoraPfp_table/trkshr_score | Dataset | 1 | Discriminator for classifiying the PFP as track-like (values >0.5) or shower-like (values <0.5).
/pandoraPfp_table/vtx | Dataset | 3 | Vertex (i.e. starting point) position of the PFP (3D cartesian coordinates, in cm).
/pandoraPfp_table/vtx_wire_pos | Dataset | 3 | Vertex (i.e. starting point) position of the PFP (per-plane wire coordinates).
/pandoraPfp_table/vtx_wire_time | Dataset | 1 | Time of the PFP vertex, in detector clock units (ticks).
/pandoraPrimary_table | Group |   | Table storing information about particles initiating an interaction (primary) in the detector as identified by Pandora. These could be cosmic rays entering the detector or neutrinos in the beam.
/pandoraPrimary_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/pandoraPrimary_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/pandoraPrimary_table/flashmatch_score | Dataset | 1 | Discriminator for matching the interaction initiated by this primary (as detected in the TPC by Pandora) with the beam flash. Lower values indicate a better match.
/pandoraPrimary_table/nu_score | Dataset | 1 | Discriminator to separate interactions initiated by neutrinos (values close to 1) vs those initiated by cosmics (values close to 0), based on the TPC information reconstructed by Pandora.
/pandoraPrimary_table/slice_id | Dataset | 1 | Id of the slice where the primary PFP is located. The id is per event, but not necessarily unique in terms of primary PFP. Pandora separates TPC hits in different time slices. Each slice contains hits from different planes. Typically each slice contains one interaction (i.e. one primary), but in some cases moren than one cosmic primary are grouped in the same slice. Neutrino primary PFP are always the only primary in their slice.
/pandoraPrimary_table/slice_pdg | Dataset | 1 | Particle Data Group (PDG) particle code for the Primary PFP. Only three values are used: 12 (electron neutrino), 13 (muon, used for cosmics), and 14 (muon neutrino).
/pandoraPrimary_table/vtx | Dataset | 3 | Vertex (i.e. interaction point) position of the Primary PFP (3D cartesian coordinates, in cm).
/pandoraPrimary_table/vtx_wire_pos | Dataset | 3 | Vertex (i.e. interaction point) position of the Primary PFP (per-plane wire coordinates).
/pandoraPrimary_table/vtx_wire_time | Dataset | 1 | Time of the Primary PFP vertex, in detector clock units (ticks).
/wire_table | Group |   | Table storing information about the waveform recorded at each Wire. This information is only available in the samples labeled as "With Wire".
/wire_table/adc | Dataset | 6400 | Value of the waveform amplitude, as measured at the analog-to-digital converter (ADC), at each of the 6400 time ticks that are saved.
/wire_table/event_id | Dataset | 3 | Run/Subrun/Event number, referring to entries in the event_table.
/wire_table/event_id.seq_cnt | Dataset | 2 | Auxiliary information added in post-processing step for simple grouping and fast access of table entries separated by event.
/wire_table/local_plane | Dataset | 1 | Id of the plane where the wire is located. Plane 0 and 1 are induction planes with wire orientation +/-60 degress wrt vertical, plane 2 is the collection plane with vertical wire orientation.
/wire_table/local_wire | Dataset | 1 | Id of the wire where the hit is located. Plane 0 and 1 have ids in the range [0,2399], plane 2 in range [0,3455].
/wire_table/tpc | Dataset | 1 | Id of the Time Projection Chamber where the planes are located. In MicroBooNE there is only 1 TPC so this should be always 0.
