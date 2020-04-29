[![Build Status](https://travis-ci.org/salilab/imp-sampcon.svg?branch=master)](https://travis-ci.org/salilab/imp-sampcon)
[![codecov](https://codecov.io/gh/salilab/imp-sampcon/branch/master/graph/badge.svg)](https://codecov.io/gh/salilab/imp-sampcon)

imp_sampcon: sampling exhaustiveness test {#imp_sampcon}
=========================================

These scripts implement the sampling exhaustiveness test described in
[Viswanath et al, 2017](https://www.ncbi.nlm.nih.gov/pubmed/29211988).
The protocol is primarily designed to work with models generated by
the [Integrative Modeling Platform (IMP)](https://integrativemodeling.org),
but can probably be adapted for other systems.

## Dependencies:

[pyRMSD](https://github.com/salilab/pyRMSD) is needed. (This is a fork of the
original pyRMSD - which is no longer maintained - to fix bugs and add
Python 3 support.)

In the Sali lab, pyRMSD is already built, so can be used with
`module load python2/pyrmsd` or `module load python3/pyrmsd`.

## Usage:

For a full demonstration of the protocol, see its usage in
IMP's [actin modeling tutorial](https://integrativemodeling.org/tutorials/actin/analysis.html).
