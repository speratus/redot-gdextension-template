# Redot GDExtension Template

This repository provides a template for create GDExtensions. This template provides a basic layout including a demo
project which can be used to test your extension. It also provides a small file (`build.py`) which can generate a
`template.gdextension` file for you. This file should automatically enable your extension within the editor.

This project uses Redot 26.1 as the basis for creating extensions. In the future, there will probably be branches
dedicated to future versions of Redot. This repository is based on the [official GDExtension tutorial][1].

## Using this template

To set up a repository using this template, simply click the "Use this template" button in the top right of this
repository. You will then be presented with a new repository wizard that will guide you through the remaining setup 
steps.

## Building the extension.

To build projects created with this template, you will need to run `scons`. If you have not already setup your system
for developing Redot extensions or extending the core editor, you can find instructions for doing so 
[here](https://docs.redotengine.org/contributing/development/compiling/). These steps are designed to help you build
the entire Redot project, but you will need an understanding of how to do that in order to build extensions.

I also strongly recommend that you read the [guide on C++ GDExtensions][2]
if you have not already done so to get the fullest picture of how GDExtensions are intended to work.

Once you have setup your repository and cloned it to your local machine, you can build the extension by running:
```sh
scons
```

If you would like to build your extension with the help of an IDE, you may want to have `scons` generate a 
`build_commands.json` file by building your project with the `compiledb=yes` option as below:

```sh
scons compiledb=yes
```

## Customizing your build artifact name

By default, this project is configured to output a shared library titled `libgdextension_template`, however you can
easily change this by modifying the `PROJECT_NAME` property in the `build.py` file. `scons` will automatically 
incorporate this variable into your compilation artifact.

## Generating a template.gdextension file

This repository comes with a simple Python script that will generate a `*.gdextension` file and place it
in the `demo` directory. Redot requires this file to load your GDExtension, so using this script will get you started
quickly.

```sh
python build.py
```

The script will also read the value of the `PROJECT_NAME` property so that the `*.gdextension` file will reflect the
name of your extension.

[1]: https://docs.redotengine.org/tutorials/scripting/gdextension/
[2]: https://docs.redotengine.org/tutorials/scripting/gdextension/