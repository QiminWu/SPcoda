# SPcoda


![alt tag](https://github.com/echavess/SPcoda/blob/master/Figures/PNCB.Average_Envelope.png)




Earthquake Source Parameters from Coda waves (In progress!!)

This program generates coda envelopes for one event using multiple stations and computes 
earthquake source parameters (corner frequency, stress drop and radiated seismic energy), following:

- Mayeda et al., 2003: "Stable and Transportable Regional Magnitudes Based on 
Coda-Derived Moment-Rate Spectra" [doi: 10.1785/0120020020](http://www.bssaonline.org/content/93/1/224.full)
- Baltay et al., 2010: "Radiated seismic energy from coda measurements and no 
scaling in apparent stress with seismic moment"


Input: 
- Seismic data: any format. Directory structure: EVENT/STNM/DATA
- Instrument response files. Format: RESP

Output(so far):
- Averaged log10 envelopes computed from horizontal components (BHN; HHN and BHE; HHN) 
