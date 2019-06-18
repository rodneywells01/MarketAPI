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

### A note on the environment
Python 3.7 is required for this project.
https://serverfault.com/questions/918335/best-way-to-run-python-3-7-on-ubuntu-16-04-which-comes-with-python-3-5

## Validating the API is up
You should leverage the Postman collection for endpoint info.
https://documenter.getpostman.com/view/4908870/RWMHKSYP

## Windows Development Notes

Developing for Windows may pose some struggles. Reach out to Rodney Wells for advice

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

## Local Database Development.

We're using MongoDB for our database solution. `mongo-express` lets us easily interact with the database locally.
https://hub.docker.com/_/mongo-express

Visit http://localhost:8081/ once the container is standing.
