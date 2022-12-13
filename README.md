# GWPSC

This is a basic pipeline to compare different population synthesis codes with each other.


## Input
The input format is a csv file with the following format at a specific metallicity:

```
M1,M2,mergertime, (spin), (weight)
M1_ZAMS, M2_ZAMS, P_ZAMS, e_ZAMS, interaction1,
M1_isec, M2_isec, P_isec, e_isec, interaction2,
```

`interaction(1/2)` is the interaction during the relative phase of the evolution. This can be `NON/SMT/CEE`. 1 is before the first SN, while 2 is after the first SN.
If any mass transfer phase is unstable, a system should be tagged as `CEE`.

A limit of 2.5 for NS is chosen, and the input is cut based on these parameters.


## Output
This pipeline generates the following output over the given metallicities. Each will also be split per formation channel:

1. DTDs for BBH, BHNS, BNS. 
2. Mass Distributions
    1. M$_1$,M$_2$,M$_tot$, M$_c$ vs rate
    2. M$_1$ vs M$_2$ (2D density/histogram)
3. q vs rate
4. spin distribution


# Code comparison

Besides generating the plots for each individual code, the distributions are 
compared between each code to the extend that's possible. 

## Current included codes

- BPASS



# Future extensions
1. Cosmic rate calculation (with CSFRD)
2. Detectability 
