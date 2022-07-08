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

