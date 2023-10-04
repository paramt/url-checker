### Test links
This repo uses url-checker to test for broken links. This file has been added using the `files` input, so all the links in this file will be checked.

#### These links are all working:
 - [My Website](https://www.param.me)
 - [My GitHub profile](https://github.com/paramt)

 
#### This link is broken:
- [Non-existing repository](https://www.github.com/paramt/this-doesnt-exist)

The broken link is blacklisted using the `blacklist` argument, so the workflow on this repo should pass
