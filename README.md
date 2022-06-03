# Pybel
API for interacting with the [library of babel](https://libraryofbabel.info)

## Installation
    # First create  and activate a virtual environment (recommended)
    python -m venv venv
    source venv/bin/activate

    # Clone the project and install it using pip
    git clone https://github.com/Paulsson99/pybel.git
    pip install .

## Usage
Pybel comes with two commands, `get` and `find`.

The `get` command returns the content of a page in the library. 
To get the contents of page 300 in volume 8 on shelf 3 in hexagon hex 
you would use the command

    python -m pybel get hex 1 3 8 300

This will print the contents to your terminal. If you instead want to save the page 
use the flag `--save LOCATION`. 
This will save a file `hex-w1-s3-v8-p300.txt` at the specified location.

The `find` command finds a string of text in a book at the library.
To find a page with the text "Hello" you should use

    python -m pybel find hello

This will print the page location to your terminal. To also print the page contents
specify the flag `--full`. The default is to search for the string at the beginning
of the page. To change this the flag `--location LOCATION` can be used. 
Then the first character in the search string will be found at `LOCATION` instead. 
Default padding around the search string is `" "` but this can be changed with
the `--padding PADDING` flag. Padding can be any of the following characters
`abcdefghijklmnopqrstuvwxyz ,.` or `random`.
The `find` command also has a `--save` flag that works exctaly as for the `get` command.
