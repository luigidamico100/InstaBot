# InstaBot

## What I have done so far...

#### Generating the current environment .yml file 

```
conda env export --name machine-learning-env --from-history --file environment.yml
```
where ```--from-history``` is needed to let the conda environment be indipendent from the current OS in use. 


## To install the environment

```
conda env create --file environment.yml
```

```
conda env create --file environment.yml --prefix ./env
```
