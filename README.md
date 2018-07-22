# Market API
Market API with a variety of goals.

- Build and maintain a watchlist
- Generate and offer subscriptions to custom "market reports"
- Leverage the latest Big-Data MachineLearning Hadoop Kubernetes Blockchain technology to transform the world


## Getting Started
- Installation
  - `./initial_install.sh`
- Run Server
  - `./run.sh`

## Validating the API is up
You should leverage the Postman collection for endpoint info.
https://documenter.getpostman.com/view/4908870/RWMHKSYP

## Windows Development Notes

Developing for Windows may pose some struggles.

### Python File Line Ending Formats
Line ending formatting in Windows will cause issues in this project. Be sure to normalize the line endings in your git config. You may see a `^M` line ending in your Python code. Lively discussions about this:
https://help.github.com/articles/dealing-with-line-endings/

Basically do the following:

`git config --global core.autocrlf true`
`git config core.autocrlf true`

Additionally, hide the malformed line endings from the `git diff` view.

`git config --global core.whitespace cr-at-eol`
`git config core.whitespace cr-at-eol`

However, this might lead to some annoying reminders. Still exploring this.
https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important

### Bash File Line Ending Fomats
For Bash files, we are going to want to actual format them ourselves. Use dos2unix

Installation:
`apt-get install dos2unix`

Usage:
`dos2unix filename`
