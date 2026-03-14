#!/usr/bin/env python
import os
import sys

env = SConscript("redot-cpp/SConstruct")

# For reference:
# - CCFLAGS are compilation flags shared between C and C++
# - CFLAGS are for C-specific compilation flags
# - CXXFLAGS are for C++-specific compilation flags
# - CPPFLAGS are for pre-processor flags
# - CPPDEFINES are for pre-processor defines
# - LINKFLAGS are for linking flags

# tweak this if you want to use different folders, or more folders, to store your source code in.
env.Append(CPPPATH=["src/"])
sources = Glob("src/*.cpp")

import importlib

build_variables = importlib.import_module("build")

if env["platform"] == "macos":
    library = env.SharedLibrary(
        "demo/bin/lib{}.{}.{}.framework/lib{}.{}.{}".format(
            build_variables.PROJECT_NAME, env["platform"], env["target"], env["platform"], env["target"]
        ),
        source=sources,
    )
elif env["platform"] == "ios":
    if env["ios_simulator"]:
        library = env.StaticLibrary(
            "demo/bin/lib{}.{}.{}.simulator.a".format(build_variables.PROJECT_NAME, env["platform"], env["target"]),
            source=sources,
        )
    else:
        library = env.StaticLibrary(
            "demo/bin/lib{}.{}.{}.a".format(build_variables.PROJECT_NAME, env["platform"], env["target"]),
            source=sources,
        )
else:
    library = env.SharedLibrary(
        "demo/bin/lib{}{}{}".format(build_variables.PROJECT_NAME, env["suffix"], env["SHLIBSUFFIX"]),
        source=sources,
    )

Default(library)
