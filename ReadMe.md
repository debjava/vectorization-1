You don't "run" pyproject.toml directly - it's a configuration file. To install dependencies from it:
pip install -e .

What wil happen if the requirements.txt file does not exist, only pyproject.toml fie exists? How do I build the project?

If only pyproject.toml exists (no requirements.txt), the project works perfectly fine. pyproject.toml is the modern standard and is self-sufficient.

To build/install the project: `pip install -e .`

To build a distribution package (wheel/sdist):

pip install build
python -m build

Difference between pip install -e . and pip install requirements.txt?

Installs the current directory as a package in editable mode
Changes to your code are immediately reflected without reinstalling
Uses pyproject.toml or setup.py for package metadata and dependencies

pip install requirements.txt
Installs packages listed in requirements.txt
Copies packages to site-packages directory

Key Summary
-e .: Install your own project in editable mode for development
requirements.txt: Install external dependencies for deployment

If there is no pyproject.toml but project has "requirements.txt", will this command "pip install -e ." work. Will it install the dependencies?

No, pip install -e . will NOT work without pyproject.toml or setup.py.

In case of python projects, some team members simply declare requirements.txt and they are able to manage and run the application.
Why do we need "pyproject.toml", what is the benefit of using this file?

requirements.txt: Good for simple scripts, deployment, quick prototyping
pyproject.toml: Essential for libraries, packages, distribution, modern Python development
If you're building a library or want to share your code, pyproject.toml is necessary. For a simple internal script, requirements.txt may suffice.















