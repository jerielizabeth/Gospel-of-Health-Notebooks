# Notebooks for *A Gospel of Health and Salvation*

This repository contains [Jupyter notebooks](http://jupyter.org/) which document the technical work for my dissertation, *A Gospel of Health and Salvation*. It will be divided into five modules, each of which corresponds to a section of my dissertation site (to be released in 2018). 

For a project overview of *A Gospel of Health and Salvation*, please read "[Updating the Dissertation Description](http://jeriwieringa.com/2017/04/21/updated-dissertation-description/)" at [jeriwieringa.com](http://jeriwieringa.com).

These notebooks will be incorporated into the dissertation, but I am making them available here for ease of evaluation and use. They can be run locally by cloning the repository and opening the .ipynb files via a notebook server (see the next section for more details). 

I share them in hopes that they prove useful to others taking on similar projects and that "[given enough eyeballs, all bugs are shallow](https://en.wikipedia.org/wiki/Linus%27s_Law)."


## Setup and Running a Notebooks Server

To run the notebooks locally, you will need **Python3** as well as the libraries recorded in the `environments.yml` file, included at the root of the project. I recommend managing Python and the libraries using [Conda](). 

First, [install Conda](http://conda.pydata.org/docs/install/quick.html). Once you have Conda installed, you can duplicate the environment for these notebooks by running (in the command line):

```bash
conda env create -f environment.yml
```

If you need to update your local environment from the `environment.yml` file, run:

```bash
conda env update --name=GoH --file=environment.yml
```

To load the environment, run:

```bash
source activate GoH
```

You can then launch the notebooks server by running (at the root of the notebooks directory):

```bash
jupyter notebook
```

## Outline of the project

The notebooks are organized into modules which correspond to the different sections of the dissertation. The descriptions will be updated as the modules are released.

### Module 2: Of Making Many Books
This module is focused on the print culture of the S.D.A. and the selection and processing of the materials used in the dissertation. The notebooks document the code used to download the corpus PDF files and extract, evaluate, and clean the text from those PDF files.

## Copyright
All material is copyright of Jeri E. Wieringa (jeri.elizabeth@gmail.com).

The code is released under the MIT license, and the text under the Creative Commons Attribution-NonCommercial 4.0 International license. See [license.md](license.md) for details.



