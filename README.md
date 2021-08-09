<p align="center">
Store the python return value of commands for the session.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/dyuri/xontrib-pyrtn" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-pyrtn
# or: xpip install -U git+https://github.com/dyuri/xontrib-pyrtn
```

## Usage

```bash
xontrib load xontrib_pyrtn
```

The xontrib adds two functions to the global namespace - `In()` and `Out()`. They are similar to `ipython`'s `In[]` and `Out[]`. (I'm using functions instead of lists to protect the *history* from accidental modifications.)

A new `PROMPT_FIELD` `pyhistnum` is also added, to be able to include the number of the upcoming command (like in `ipython`).

## Example

```bash
$ xontrib load pyrtn
$ $PROMPT = "[{pyhistnum}]$ "
[2]$ [12 * 3 + 6]
[42]
[3]$ In(2)
"[12 * 3 + 6]\n"
[4]$ Out(2) + [1]
[42, 1]
[5]$ 
```

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
