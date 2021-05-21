# Pants Build Tool Tutorial

[![Build Status](https://semaphore-demos.semaphoreci.com/badges/semaphore-demo-python-pants/branches/master.svg)](https://semaphore-demos.semaphoreci.com/projects/semaphore-demo-python-pants)

[Pants](https://www.pantsbuild.org/) is Twitters scalable and performant build tool. Its primary target is Python but more languages can be added via backends.

This repository contains two Python projects, good for getting familiar with Pants and its commands.
## Installing Pants

```bash
$ printf '[GLOBAL]\npants_version = "2.4.1"\n' > pants.toml
$ curl -L -o ./pants https://pantsbuild.github.io/setup/pants && \
    chmod +x ./pants
$ ./pants --version
```

Source: [getting started guide](https://www.pantsbuild.org/docs/installation)
## Configure pants

A basic `pants.toml`

```toml
[GLOBAL]
pants_version = "2.4.1"
backend_packages = ["pants.backend.python"]
```

Config with enabled linters, formatters, and typechecking

```toml
[GLOBAL]
pants_version = "2.4.1"
backend_packages = ["pants.backend.python",
"pants.backend.python.lint.black",
"pants.backend.python.lint.docformatter",
"pants.backend.python.lint.flake8",
"pants.backend.python.lint.pylint",
"pants.backend.python.typecheck.mypy"
]
```

Create initial `BUILD` files
```bash
$ ./pants tailor
```

Add this to `pants.toml` enable binary PEX support for `hello_world`:

```toml
# pants.toml
...

# add support for requirements.txt
python_requirements()

# adds support for binary file generation
pex_binary(
    name="pex_binary",
    entry_point="main.py",
)
```

## Inspecting your code

List available Pants targets for a folder:

```bash
$ ./pants list hello_world/:
hello_world
hello_world:ansicolors
hello_world:pex_binary
hello_world:requirements.txt
hello_world:tests
```

View dependencies for your files:

```bash
$ ./pants dependencies hello_world/:
commons/string_utils.py
hello_world/__init__.py
hello_world/main.py
hello_world/test_main.py:tests
hello_world:ansicolors
hello_world:requirements.txt
```

View dependees (files that depend on this one):

```bash
$ ./pants dependees commons/string_utils.py
commons
commons:tests
commons/string_utils_test.py:tests
hello_world
hello_world/main.py
```


## Running pants

Build PEX files for all projects
```bash
$ ./pants package ::
```

Build and run a file:
```bash
$ ./pants run hello_world/main.py
```

Run linters for everything
```bash
$ ./pants lint ::
```

Format all code
```bash
$ ./pants fmt ::
```

Run typechecker
```bash
$ ./pants typecheck ::
```

Run all unit tests
```bash
$ ./pants test ::
```

Run tests on changed code:
```bash
$ ./pants --changed-since=origin/master \
          --changed-dependees=transitive \
          test
```

## Continuous integration

The `final` branch in this repository includes a continuous integration pipeline to build the projects in Semaphore.

![Sample pipeline](https://raw.githubusercontent.com/semaphoreci-demos/semaphore-demo-python-pants/master/pipeline.png)

## License

MIT License

Copyright (c) 2021 Rendered Text

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



