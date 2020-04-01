# RegionResults

This repository provides `visualisation` of parameter analysis for **parametric Discrete Time Markov Chain** using [Storm model checker](http://www.stormchecker.org/).

### 1. Qualitative model checking

Visualisation of qualitative model checking using regional refinement. The Storm tool returns partitioning of the given parameter space to regions satisfying/not satisfying/unknown parts.

Usage:
```
python3 visualise.py <Storm-output-in-a-file> <output-html-file>

Example:
    python3 visualise.py example/storm_stdout.txt picture.html
```
