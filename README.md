# Generate GitHub deploy key using GitHub Apps

* No personal access token required
* It can be done automatically on schedule

1. Create [GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps)
2. Install the app to your GitHub account or organisation
3. Give access and required permits for the app to GitHub repositories, whoch needs to get deploy keys
4. Customize the workflow how the deploy key is genereted and how its private key is securely saved