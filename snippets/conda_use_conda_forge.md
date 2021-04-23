# Conda use conda-forge for default channel

```bash
# bash

# ensure conda >=4.9
conda --version
conda update conda

# Add conda-forge as the highest priority channel.
conda config --add channels conda-forge

# Activate strict channel priority (strict will be activated by default in conda 5.0).
conda config --set channel_priority strict

# From now on using conda install <package-name> will also find packages in our conda-forge channels.
# conda install opencv=3.4

```

## Reference

https://conda-forge.org/docs/user/introduction.html
