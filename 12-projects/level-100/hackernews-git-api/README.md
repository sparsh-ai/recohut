# API HackerNews Github

## GitHub API

In this lab, you’ll learn how to write a self-contained program that generates a visualization based on data that it retrieves. Your program will use a web application programming interface (API) to automatically request specific information from a website—rather than entire pages—and then use that information to generate a visualization. Because programs written like this will always use current data to generate a visualization, even when that data might be rapidly changing, it will always be up to date.

We’ll base our visualization on information from GitHub, a site that allows programmers to collaborate on coding projects. We’ll use GitHub’s API to request information about Python projects on the site, and then generate an interactive visualization of the relative popularity of these projects using Plotly.

![repo-plot](https://user-images.githubusercontent.com/62965911/215260573-dee5564c-0c3d-4a94-b259-e9f112d98c12.png)

## The Hacker News API

To explore how to use API calls on other sites, let’s take a quick look at Hacker News (http://news.ycombinator.com/). On Hacker News, people share articles about programming and technology, and engage in lively discussions about those articles. The Hacker News API provides access to data about all submissions and comments on the site, and you can use the API without having to register for a key.