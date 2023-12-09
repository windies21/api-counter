from setuptools import setup, find_packages

req_tests = ["pytest"]
req_lint = ["flake8", "flake8-docstrings"]
req_etc = ["black", "isort"]
req_dev = req_tests + req_lint + req_etc

with open('requirements.txt', 'r') as f:
    install_requires = [
        s for s in [
            line.split('#', 1)[0].strip(' \t\n') for line in f
        ] if s != ''
    ]

setup_options = {
    "name": "Url Counter",
    "version": "0.1",
    "description": "Simple Url Counter from Json files or folder.",
    "packages": find_packages(),
    "python_requires": ">=3.11.0",
    "install_requires": install_requires,
    "extras_require": {
        "tests": req_tests,
        "lint": req_lint,
        "dev": req_dev
    },
    "package_dir": {"": "."},
    "entry_points": {
        "console_scripts": [
            "counter=url_counter.main:main",
        ],
    },
}

setup(**setup_options)
