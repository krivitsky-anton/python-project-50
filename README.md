### Hexlet tests and linter status:
[![Actions Status](https://github.com/krivitsky-anton/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/krivitsky-anton/python-project-50/actions)
[![Action Status](https://github.com/krivitsky-anton/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/krivitsky-anton/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/df66c0cbbeca7d822f23/maintainability)](https://codeclimate.com/github/krivitsky-anton/python-project-50)
[![Test Coverage](https://api.codeclimate.com/v1/badges/df66c0cbbeca7d822f23/test_coverage)](https://codeclimate.com/github/krivitsky-anton/python-project-50)

# Gendiff: Configuration Files Comparison Tool

## Description

Gendiff is a command line utility for comparing two configuration files. The tool analyzes the files and displays the differences in a human-readable format. It supports JSON and YAML file formats.

## Installation

To install, clone the repository and install using `poetry`:

```shell
git clone https://github.com/Cur1yB/python-project-50
cd gendiff
poetry install
```

## Usage

To display usage information:

```shell
poetry run gendiff -h
```

Example of comparing two files:

```shell
poetry run gendiff filepath1.json filepath2.json
```

The output will appear in the following format:

```json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Command Line Options

- `-h, --help` — display this help message and exit.
- `-f FORMAT, --format FORMAT` — set the output format (supported formats: `plain`, `json`, `stylish`).
