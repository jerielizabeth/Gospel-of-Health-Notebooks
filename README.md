<!-- 
.. date: 2018-10-01
.. slug: notebooks-overview
.. title: Notebooks for A Gospel of Health and Salvation
 -->

This collection of Jupyter notebooks documents the technical work for my dissertation, *A Gospel of Health and Salvation: Modeling the Religious Culture of Seventh-day Adventism, 1843-1920*. My goal in releasing the code notebooks is three-fold. First, the notebooks document the final versions of the technical work that supports the dissertation, and can be used to examine and reproduce elements of that technical work. Second, the notebooks are part of the argument of the dissertation, demonstrating the ways the intellectual work of computational analysis is found not only in the summary texts, but is also embedded within the logic of the code. And third, I have released the code as a collection of Jupyter notebooks to support the reuse and adaptation of this intellectual work in other contexts. 

The notebooks are organized by seven "tasks" that I relied upon in completing the dissertation - gathering sources, cleaning the data, describing the corpus, preprocessing the texts, modeling the texts, evaluating the model, and analyzing the model results. Each section has its own README file with information on the goals and structure of the member notebooks. While the notebooks build upon each other in order, it is possible to experiment out of the provided order, provided you have the necessary data files in place.

To experiment with the notebooks, see the installation instructions below. You can also upload the .ipynb files to services such as [Azure Notebooks](https://notebooks.azure.com/) to experiment.

A note on code in the dissertation product: There are a variety of opinions on including code as part of the dissertation "product" or whether it is a intermediary research step separate from the final product. To that debate, I would comment that these notebooks do not encompass all of the technical work I did as part of the analysis, nor the myriads of tests and false-starts along the way. Rather these notebooks reflect the final results of the processes of experimentation, editing, and revision that consumed much of my dissertation writing time. The process of preparing these notebooks for publication as part of the dissertation has also required me to clarify and re-examine my technical work, a useful step that would not take place if the code was not also being offered for review. As I note elsewhere in the dissertation, the use of computational methods changes the methods and the type of information needed for evaluation, as small changes in the preparation and parsing of the data can influence the results. Making these transparent and part of the final product enables that sort of evaluation and also is a way of recognizing the intellectual work that is done at the level of code.

## Setup and Running a Notebooks Server

To run the notebooks locally, you will need Python3 as well as the libraries recorded in the `environments.yml` file, included at the root of the project. A number of the notebooks also require my supporting library, [name], which is available via Github. I recommend managing Python and the libraries using [Conda](http://conda.pydata.org). 

To install, first [install Conda](http://conda.pydata.org/docs/install/quick.html). Once you have Conda installed, you can duplicate the environment for these notebooks by running (in the command line):

```bash
conda env create -f environment.yml
```

This will install Python3 as well as all of the supporting libraries for the project. 

If you need to update your local environment from the `environment.yml` file, run:

```bash
conda env update --name=GoH --file=environment.yml
```

Once you have created the environment on your local machine, you must activate it. To activate the environment, run:

```bash
source activate GoH
```

With the environment active, install the [name] library, following the instructions in its Github repository.

You can then launch the notebooks server by running (at the root of the notebooks directory):

```bash
jupyter notebook
```

## Acknowledgements

I have accumulated many debts while learning Python and attempting to apply code it to my dissertation research. A particular thanks to Fred Gibbs, both for introducing "Clio3" to the GMU curriculum (the beginning of my demise) and for being a sounding board, helping me work through some of the stickier parts of the technical work. Thanks also to the [Experimental Humanities Group at ILIFF](http://library.iliff.edu/learning/#/humanities/) for letting me join your calls, helping me work through problems, and inspiring me to write beautiful, well-documented code. 

And, of course, thanks to the generous citizens of [StackOverflow](https://stackoverflow.com/), without whom I don't know how I would ever remember how to write to a file.

## Copyright

All material is copyright of Jeri E. Wieringa (jeri.elizabeth@gmail.com).

The code is released under the MIT license, and the text under the Creative Commons Attribution-NonCommercial 4.0 International license. See [license.md](license.md) for details.



