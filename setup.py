from setuptools import find_packages, setup  # type: ignore


REQUIREMENTS = []

DEV_REQUIREMENTS = [
    "pytest",
    "coverage",
]

setup(
    name="math_editor",
    version="1.0",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    entry_points={
        "console_scripts": []
    },
)
