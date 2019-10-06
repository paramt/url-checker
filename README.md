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
        uses: paramt/LinkChecker@master
        with:
          files: [README.md,SUPPORT.md]
          blacklist: []
```

### Arguments
 - `files`: A comma-separated list of files to check
 - `blacklist`: A comma-separated list of URLs to ignore

### Sample Output
![Example](https://i.imgur.com/35zldHS.png)

> Note: url-checker only works on public repositories
