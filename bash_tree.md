Converting tree command output to markdown using a bash command directly could be a bit complex and may not always give perfect results because the tree command output uses special characters to draw the tree. But here is a simple approach that can give a good start. 

This bash script replaces the special tree characters with markdown formatting:

```bash
tree | sed 's/│/ /g' | sed 's/├\─\─/-/g' | sed 's/└\─\─/-/g' > output.md
```

In this script:

- `tree` is the command that outputs the directory structure.
- The `sed` commands are used to replace certain characters:
  - `'s/│/ /g'` replaces the pipe characters with spaces.
  - `'s/├\─\─/-/g'` replaces the "├──" characters with a dash.
  - `'s/└\─\─/-/g'` replaces the "└──" characters with a dash.
- The `>` character is used to redirect the output into a file. In this case, the file is called `output.md`.

Please note that this command doesn't create subtitles as Markdown headers. Creating those would require a more complex script because it needs to understand the level of depth in the tree to create the right Markdown header. If you need this, you may want to use a programming language like Python or a complex `awk` script to parse and interpret the tree.
