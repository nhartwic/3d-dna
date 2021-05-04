This repo exists to allow for installing 3ddna into a conda environment using pip. To do so, do something like:

```
# install into new environment
wget https://raw.githubusercontent.com/nhartwic/3d-dna/master/conda_install.yml
conda env create -n 3ddna -f conda_install.yml

# install into existing environment (not recomended)
conda install -c conda-forge -c bioconda lastz openjdk python=2.7 scipy numpy matplotlib parallel pip
pip install git+https://github.com/nhartwic/3d-dna.git
```

Once installed, you will get two new scripts added to your path: 
1. run-asm-pipeline
2. run-asm-pipeline-post-review 

These scripts only exist to pass on arguments to their equivalents within 3ddna:
1. run-asm-pipeline.sh
2. run-asm-pipeline-post-review.sh

For more information on these tools, check the [docs for 3ddna](pip_3d_dna/README.md).
