Linter for CudaLint.
Supports Markdown lexer.

Needs Node.js in PATH: for Windows it's "node.exe", for Linux it's "node" or "nodejs". 
Then install "markdownlint" Node package into the folder of this linter:

$ cd cudatext/py/cuda_lint_markdownlint
$ npm install markdownlint-cli

This must create folder "node_modules" in the linter folder.
Linter doesn't support "global" installation.

Ported from SublimeLinter-contrib-markdownlint by Alexey T.
