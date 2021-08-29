import subprocess

import setuptools
from setuptools.command.develop import develop


class AutomaticallyInstallPreCommit(develop):
    """
    Custom development hook to automatically install pre-commit .githooks into the repository
    .git/hooks/ directory when doing a development install of zentinel.

        pip install -e ".[tests]"
            * installs dependencies
            * installs pre-commit itself
            * actually installs pre-commit hooks (a subsequent step required)
    """

    def run(self):
        super().run()
        subprocess.run(["pre-commit", "install"])


setuptools.setup()
# setuptools.setup(cmdclass={"develop": AutomaticallyInstallPreCommit})
