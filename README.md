# RegionResults

This repository provides `visualisation` of parameter analysis for **parametric Discrete Time Markov Chain** using [Storm model checker](http://www.stormchecker.org/).

### 1. Qualitative model checking

Visualisation of qualitative model checking using regional refinement. The Storm tool returns partitioning of the given parameter space to regions satisfying/not satisfying/unknown parts.

Usage:
```
python3 visualise.py <Storm-output-in-a-file> <output-svg-file>

Example:
    python3 visualise.py example/storm_stdout.txt example/pic.svg
```

---

### 2. Quantitative model checking

Visualisation of quantitative model checking using a sampling of rational function It samples given parameter space (two dimensional!) with a given precision and create a visualisation where colour is assigned to each value.

Usage:
```
python3 sample.py <function-to-sample> <parameters> <output_file>

where <parameters> is a dictionary of type:
    "param-name" : [From, To, Number]
    which will create a linear space 
    with interval (<From>, <To>) and <Number> samples.

Example:
    python3 sample.py '(k1)/(k1+2*k2)' '{"k1" : [5, 10, 10], "k2" : [0, 2, 10]}' sampling.svg
```