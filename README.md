# URL Checker
A GitHub action to test for broken links on markdown files

### Sample Workflow
```yml
name: Sample Workflow

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check URLs
        uses: paramt/url-checker@master
        with:
          files: [README.md,SUPPORT.md]
          blacklist: []
```

### Arguments
 - `files`: A comma-separated list of files to check
 - `blacklist`: A comma-separated list of URLs to ignore

### Sample Output
[![Example](https://i.imgur.com/35zldHS.png)](https://github.com/paramt/url-checker/commit/093ef6cb5f7e9eff8300887f07eb0c3a55f4aa82/checks)

> Note: url-checker only works on public repositories
