# Using Gitpod

**ℹ️ If you've launched this project in a Gitpod workspace, Jupyter Lab should open in another tab - check your browser for blocked popups.**

Gitpod launches both Jupyter Lab and the development webserver; however, you won't be able to access these from localhost like you might be used to. Instead, the port needs to be [exposed](https://www.gitpod.io/docs/config-ports), so we can access it via a url like 1234-a52-myrepo.gitpod.io. This is already configured for you.

## Data science notebooks

For Jupyter Lab, the URL you need to use also contains a security token. This means you can't simply open your browser to the hostname Gitpod provides. Instead, look in the output of the shell command "open jupyter lab", and you should see the recommended URL.

## Development web server

For the website dev server, this should open in a preview tab of VSCode. You can also access the dev server via VSCode's "Remote Explorer". See [configure ports](https://www.gitpod.io/docs/config-ports) for more info.
