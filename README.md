# SPcoda

Earthquake Source Parameters from Coda waves

This program generates coda envelopes for one event using multiple stations, following:

- Mayeda et al., 2003: "Stable and Transportable Regional Magnitudes Based on 
Coda-Derived Moment-Rate Spectra" 
- Baltay et al., 2010: "Radiated seismic energy from coda measurements and no 
scaling in apparent stress with seismic moment"

Input: - Seismic data: any format. Directory structure: EVENT/STNM/DATA (Horizontal components)
       - Instrument response files. Format: RESP
Output:- Text files containing the average log10 envelope computed from the horizontal components. 
