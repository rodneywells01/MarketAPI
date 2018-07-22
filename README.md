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
Line ending formatting in Windows will cause issues in this project. Be sure to normalize the line endings in your git config.

`git config --global core.autocrlf true`

Additionally, hide the malformed line endings from the `git diff` view.

`git config --global core.whitespace cr-at-eol`
