# SPcoda

Earthquake Source Parameters from Coda waves (In progress!!)

This program generates coda envelopes for one event using multiple stations and computes 
earthquake source parameters (corner frequency, stress drop and radiated seismic energy), following:

- Mayeda et al., 2003: "Stable and Transportable Regional Magnitudes Based on 
Coda-Derived Moment-Rate Spectra" 
- Baltay et al., 2010: "Radiated seismic energy from coda measurements and no 
scaling in apparent stress with seismic moment"


Input: 
- Seismic data: any format. Directory structure: EVENT/STNM/DATA (Horizontal components)
- Instrument response files. Format: RESP

Output(so far):
- Averaged log10 envelopes computed from horizontal components (BHN; HHN and BHE; BHE; HHN) 
