# P33-DEI-dashboard-project
This repository is created by Applied Data Fellow Mark on July.27 2022 for P33 DEI dashboard team members to share and collaborate their codings and datasets.
Reach to Mark Zhang : mark.zhang@p33chicago.com if need help

## Making changes via cloud workspace (Gitpod)

To launch the development workspace in your browser, including Jupyter Lab UI, visit: [gitpod](https://gitpod.io/#https://github.com/zhengzhangharris/P33-DEI-dashboard-project). See [docs/gitpod.md](./docs/gitpod.md) for more info.

## Accessing Jupyter Lab and website dev server

Gitpod launches both Jupyter Lab and the development webserver; however, you won't be able to access these from localhost like you might be used to. Instead, the port needs to be [exposed](https://www.gitpod.io/docs/config-ports), so we can access it via a url like 1234-a52-myrepo.gitpod.io. This is already configured for you.

For Jupyter Lab, the URL you need to use also contains a security token. This means you can't simply open your browser to the hostname Gitpod provides. Instead, look in the output of the shell command "open jupyter lab", and you should see the recommended URL.

For the website dev server, this should open in a preview tab of VSCode. You can also access the dev server via VSCode's "Remote Explorer". See [configure ports](https://www.gitpod.io/docs/config-ports) for more info.

## Autoreload

When working with a Jupyter notebook that imports an external Python module, the notebook does not incorporate changes made to external modules. You can:

* Use [%autoreload magic](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) (see [caveats](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html#caveats))
* Restart the notebook
* Use Python's [importlib.reload function](https://docs.python.org/3/library/importlib.html#importlib.reload)
