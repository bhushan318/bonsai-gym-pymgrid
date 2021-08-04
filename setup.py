import logging
from setuptools import setup, find_packages
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
log.debug("Running setup...")

setup(
    name="bonsai_gym_pymgrid",
    package_dir={"": "bonsai_gym_pymgrid"},
    packages=find_packages("bonsai_gym_pymgrid"),
    version="0.0.1",
    python_requires=">=3.0",
    include_package_data=True,
    install_requires=[
        "gym",
        "bonsai-common",
    ],
)
