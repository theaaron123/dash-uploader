import json

import setuptools
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install
from setuptools.command.develop import develop

with open("package.json") as f:
    package = json.load(f)

with open("docs/README-PyPi.md", encoding="utf-8") as f:
    long_description = f.read()

package_name = package["name"].replace(" ", "_").replace("-", "_")


class NPMInstallEgg(egg_info):
    def run(self):
        self.run_command("npm install")
        egg_info.run(self)


class NPMInstall(install):
    def run(self):
        self.run_command("npm install")
        install.run(self)


class NPMInstallDevelop(develop):
    def run(self):
        self.run_command("npm install")
        develop.run(self)


class NPMBuildEgg(egg_info):
    def run(self):
        self.run_command("npm run build")
        egg_info.run(self)


class NPMBuildInstall(install):
    def run(self):
        self.run_command("npm run build")
        install.run(self)


class NPMBuildDevelop(develop):
    def run(self):
        self.run_command("npm run build")
        develop.run(self)


setuptools.setup(
    cmdclass={
        'npm_installI': NPMInstall,
        'npm_installE': NPMInstallEgg,
        'npm_installD': NPMInstallDevelop,
        'npm_buildD': NPMBuildDevelop,
        'npm_buildE': NPMBuildEgg,
        'npm_buildI': NPMBuildInstall,
    },
    name=package_name,
    version=package["version"],
    author=package["author"],
    author_email="niko@pasanen.me",
    url=package["homepage"],
    packages=[
        package_name,
        package_name + "._build",
    ],
    include_package_data=True,
    license=package["license"],
    description=package.get("description", package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["dash>=1.1.0", "packaging>= 21.0"],
    extras_require={
        "dev": [
            "pyyaml~=5.3.1",  # building with dash-generate-components
            # Packages needed to run the tests.
            "black",  # code formatting
            "pytest",  # running tests
            "selenium~=4.1.0",  # running tests
            # Switch into a virtual environment
            # pip install -r requirements.txt
            "dash[testing]>=1.1.0",
            # Automatically get the latest ChromeDriver. If Chrome is of
            # different version, use
            # pip install --upgrade --force-reinstall chromedriver-binary==<version>.*
            # to update/downgrade the chromedriver binary.
            # Needs: import chromedriver_binary to the top of your test script.
            "chromedriver-binary",
            "Werkzeug~=2.0.3",
        ]
    },
    classifiers=[
        "Framework :: Dash",
    ],
)
