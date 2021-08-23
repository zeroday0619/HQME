import re
from setuptools import setup

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

version = ''
with open('hqme/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


readme = ''
with open('README.md') as md:
    readme = md.read()


packages = [
    'hqme'
]

setup(
    name="HQME",
    author="zeroday0619",
    url="https://github.com/zeroday0619/HQME",
    project_urls={
        "Issue tracker": "https://github.com/zeroday0619/HQME/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="high-quality music extension for discord.py",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8',
)