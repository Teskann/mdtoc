# Hello World :star:

Welcome to the repository of my hello world project ! :tada:

This consists in a simple tool to write "Hello World" in a file !

[](mdtoc)
[](/mdtoc)

## Features

- Write Hello World in any file !
- Supports normal, uppercase and lowercase writings

## Getting started

### Prerequisites

Please be sure to install [all the dependencies in this list]().

### Installation

#### Get the sources

Start cloning the repository :
```
git clone git@github.com:Nobody/HelloWorld.git
cd HelloWorld
```

#### Configure

```
chmod += configure
./configure
```

#### Install

```
make
make install
```

#### Check if it worked

```
which helloworld
```

## Usage

### Basic

Run hello world on `myfile.txt` to write "Hello World" in the file !

```commandline
helloworld myfile.txt
```

### Advanced

- Write with uppercase letters :

    ```commandline
    helloworld --uppercase myfile.txt
    ```

- Write with lowercase letters :

    ```commandline
    helloworld --lowercase myfile.txt
    ```

## Contribute

Contributions are welcome for this project ! Read [CONTRIBUTE.md]() for more
details.

Do not forget to read the [code documentation]() and to take a look at the
[wiki]().

## Known Issues :exclamations:

There is a known crash if the file does not exists. Should be fixed soon.

## References

1. [How to make a hello world]()
2. [Write to files]()
3. [Make and Makefiles]()