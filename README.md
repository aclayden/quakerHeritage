# quakerHeritage

## Introduction

Project to support the collation of PDF data on the
[**Quaker Meeting House Heritage Project**](https://heritage.quaker.org.uk/)
into a database.

[![Python 3.10.7](https://img.shields.io/badge/python-3.10.7-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![PyPI](https://img.shields.io/badge/PyPI-v1.0.1-blue)
![status](https://img.shields.io/badge/status-released-green)

### Disclaimer

This project has been specifically coded for the *Quaker Meeting House*
*Heritage Project*, both in hard-coded variables and parameters for
extracting text. It is a tool to suit a very specific use-case and may
not work if used otherwise. The project further depends on the files
required being listed online at the URLs provided. If *Britain Yearly*
*Meeting* takes down the website and associated PDFs, back-ups are
available on the **Internet Archive's Wayback Machine**. The code can
also be adapted to work with locally downloaded PDFs. Go to *Appendix:*
*Hosting Errors* to note the required changes.

## Getting Started

- Install the project.

### From PIP

```console
$ pip install quackerheritage
```

### From the source

- Clone the repository.

```console
$ git clone "https://github.com/aclayden/quakerHeritage.git"
$ cd "quakerHeritage"
```

- Install the project dependencies.

```console
$ pip install -r "requirements.txt"
```

## How-To Use

Simply run the following command:

```console
$ python -m quakerheritage.build
```

You will be prompted to select a location for the csv output to be
placed. Once chosen, the code will run quietly in the background until
complete, and the `.csv` available at your chosen directory as
'quakerHeritageDB.csv'. Further documentation can be found
[here.](https://github.com/aclayden/quakerHeritage/blob/main/docs/index.md)

## Contributing

Feedback is both welcome and encouraged. If you use the code, or just
find issues while browsing, please report them by
[clicking here.](github.com/aclayden/quakerHeritage/issues)

## Licence

Distributed under [AGPL version 3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

## Contact

For queries please reach out via GitHub by either raising an issue
or [contacting me directly](https://github.com/aclayden).
