# From another readme

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).
2. Install `markdownlint` by typing the following in a terminal:
```bash
npm install -g markdownlint-cli
```
3. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in
   `.zshenv` and not `.zshrc`.
4. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plug-in for
   `oh-my-zsh`.

## Markdownlint configuration

In order for `markdownlint` to be executed by SublimeLinter, you must ensure
that its path is available to SublimeLinter. Before going any further, please
read and follow the steps in ["Finding a linter executable"](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable)
through "Validating your PATH" in the documentation.

Once you have installed and configured `markdownlint`, you can proceed to
install the SublimeLinter-contrib-markdownlint plug-in if it is not yet
installed.

