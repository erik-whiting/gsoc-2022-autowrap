For the Google Summer of Code 2022 event, I'll be working with an Open Bioinformatics Foundation (OBF) subgroup called OpenMS. Specifically, I'll be working on the Autowrap project, a tool for making C++ libraries available in Python. This site will be where I keep track of updates and stuff I learn.

My [progress report](progress_page.md) page tracks what I've accomplished so far

The [PR page](pull_requests.md) is a list of my pull requests so far

The [lessons learned](lessons_learned.md) is a collection of things I've learned so far
# Working on this week (22-May-2022)

* Learning the C++ Template classes
* Learning about the array buffer protocol in CPython


# Background Info

Here's an overview of this project in general

## Open Bioinformatics Foundation
From the [OBF website](https://www.open-bio.org/):
> The Open Bioinformatics Foundation (OBF) is a non-profit, volunteer-run group that promotes open source software development and Open Science within the biological research community.

Bioinformatics is formally described as the science of collecting and analyzing biological data. It's most often associated with genomics--the scince of mapping genomes--but includes much more.

## OpenMS
From the [OpenMS website](https://www.openms.de/):
> OpenMS offers an open-source software C++ library (+ python bindings) for LC/MS data management and analyses. It provides an infrastructure for the rapid development of mass spectrometry related software as well as a rich toolset built on top of it.

Mass spectrometry is a tool used in the life sciences to measure the mass-to-charge ratio of ions. This is useful for determing the structure of a compound, identifying unknown compounds, or determining the isotopic composition of elements in a molecule.

OpenMS is part of [deNBI Center for Integrative Bioinformatics](https://www.denbi.de/network/center-for-integrative-bioinformatics-cibi), part of an academic laboratory based in Germany.

## Autowrap
According to the [OpenMS GSoC Project Description](https://www.open-bio.org/events/gsoc/gsoc-project-ideas/#openms-autowrap):
> Autowrap is a python package for the automated wrapping of whole C++ projects into Python via Cython.

Cython is a programming language and superset of Python which supports calling C/C++ functions and types in Python code. The process of properly making C/C++ libraries available as Python modules is a tedious and time consuming process that Autowrap mostly automates for the developer.

## The GSoC project
The GSoC Project description was posted [here](https://www.open-bio.org/events/gsoc/gsoc-project-ideas/#openms-autowrap) and is described as such:
> Autowrap is a python package for the automated wrapping of whole C++ projects into Python via Cython. C++ developers basically need to provide a Cython header file for each C++ header file to specify what needs to be wrapped and how. It then analyses the syntax tree generated by the Cython parser for those “header” files and generates Cython source code for it. Cython then creates the necessary source code to be compiled with e.g. CPython to create a Python extension module to be imported by the end-user. While the wrappers created by autowrap are rather simple, passing templated and nested STL objects like vectors, maps, or tuples between Cython/Python and C++ with autogenerated code can become rather complex. Autowrap offers recursion for nested vectors but cannot handle mixed data structures yet. It also misses support for newer STL containers like tuples and only offers simple vector to (Python) list conversions, while numpy arrays, e.g. via the buffer protocol would sometimes be more suitable. We are seeking for a motivated GSoC contributor proficient in at least Python to tackle those improvements.

Throughout this Summer, I will be working with the helpful developers at OpenMS to complete this project.

## Erik
Hey, I'm Erik, the contributor for this project. I'm a Sr. Software Engineer at CallRail and a PhD student at the University of Nebraska - Lincoln. My research interests include scientific computing, software engineering, and programming langauges.

# Links

[Open Bioinformatics Foundation](https://www.open-bio.org/)

[OpenMS](https://www.openms.de/)

[Autowrap](https://github.com/OpenMS/autowrap#readme)

[Cython](https://cython.org/)

[GSoC](https://summerofcode.withgoogle.com/)

[Erik's blog](https://erikscode.space/)
