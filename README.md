# devops
Repository for experimenting with all things DevOps

## Auto-Formatting - autopep8

The file setup.cfg specifies settings for for pystyleguide which is used by the autopep8 formatter. When using VCS, the formatter is installed by installing the ms-python formatter, and then selecting autopep8 in the settings.

{
    "python.formatting.provider": "autopep8",
}

## VCS Development Container

Repository is configured to allow for remote development using a container. Configuration is located in .devcontainer, which contains the Dockerfile and devcontainer.json file.

Extensions can be managed in the devcontainer.json file or directly through VCS by right-clicking and adding an extension.

You must remember to prune docker images / containers created for this

Git credentials are automatically added to the container by the extension.

## Documentation

### Sphinx

Sphinx is a library used to help automatically generate documentation from code docstrings.

Sphinx uses directives, which are blocks of markup text which takes arguments, options, etc. Essentially functions. En example is ``.. toctree::``, which is used to generate a table of content.

Resources:

[https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html)
[https://www.youtube.com/watch?v=tXWscUSYdBs](https://www.youtube.com/watch?v=tXWscUSYdBs)

### How to set up Sphinx

Install Sphinx, themes and extensions using pip:

`pip install -r requirements.txt`

Create and move to docs directory:

```
mkdir docs
cd docs
```

Setup Sphinx:

`sphinx-quickstart`

When setting up Sphinx, separate source and build directories.

The file conf.py, found in docs/source/ is used by Sphinx to configure how the output is generated.

The conf.py file must be updated so that Sphinx knows where to look for docstrings. Example for this project:

```
import os
import sys
sys.path.insert(0, os.path.abspath('../../character'))
```

Enable napolen and autodoc extensions to read Google docstrings and auto-generate documentation from docstrings:

```
extensions = [
    'sphinx.ext.autodoc', # Used to automatically generate docstrings
    'sphinx.ext.napoleon' # Allows Sphinx to parse Google-style docstrings
]
```

Change theme to Read the Docs theme:

`html_theme = 'sphinx_rtd_theme'`

### Sphinx directory structure

Structure and explanation:

- ``source``: This is where all `.rst` files will reside.
- ``source/conf.py``: This is the file where all Sphinx configuration settings (including the settings we specified during the ``sphinx-quickstart`` setup) are specified. When any ``make <builder>`` or ``sphinx-build <builder>`` command is called, Sphinx runs this file to extract the desired configuration.
- ``source/index.rst``: This is the file which tells Sphinx how to render our index.html page. In general, each ``source/*.rst`` file is converted to a corresponding ``build/html/*.html`` page when ``make html`` is called.
- `build` : This is the directory where the output of any builder is stored when a ``make <builder>`` or ``sphinx-build <builder>`` command is called.

``make <builder>`` command operates relative to the conf.py location, which is why modifications to pathing is relative to that location. 

### Generate documentation

Sphinx uses the autodoc extension to generate documentation from docstrings. The autodoc extension is invoked in .rst files using the auto~ directives, such as .. automodule::.

Sphinx is able to generate the .rst files containg the autodoc directives using the command:

`sphinx-apidoc -o <out_dir> <src_dir>`

This generates a number of files, including a modules file in the `out_dir`.

There are some issues with the generated files, so it is recommended to either not use the command, and manually add the .rst files, or modify the files after they have been generated. Specifically, imports breaks when Sphinx tries to load the Python modules to read the docstrings.

Alternatively, if the imports in the Python files were changed to use `import <package>.<module>` rather than just `import <module>`, the default behavior of the of the `sphinx-apidoc` command could be used. It is possible that this is the better way to do imports for larger projects anyways.

### Build documentation

After setting up Sphinx, the docs directory should contain a build and source source directory.

Navigate to docs directory:

`cd docs`

Clean previous output:

`make clean`

Build documentation:

`make html`

### Misc

Sphinx supports themes. Third-party themes are installed as pip packages and can be specified in the conf.py file of docs/. See link for more details:
https://www.sphinx-doc.org/en/master/tutorial/more-sphinx-customization.html
