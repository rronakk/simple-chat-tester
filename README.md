# simple-chat-tester
Test framework to test simple-chat

### Table of Contents
- [Introduction: Installation and Dependencies](#introduction)
- [Running Tests: Getting Started](#running-tests)

## <a name="introduction"></a>Introduction: Installation and Dependencies

This simple-chat UI Automation Framework is compatible with **[python v 3.4+](https://www.python.org/downloads/)+**.

This current installation/dependencies assumes an osx/linux environment.
***
For MacOSX, you can use [homebrew](http://brew.sh/) to install [git](https://git-scm.com/), [python v 3.4+](https://www.python.org/downloads/), and [chromedriver](http://chromedriver.storage.googleapis.com/index.html). 

Then, run the following command to install python3, git, and chromedriver to your machine:
```
brew install git chromedriver python3

``` 
***
On your machine, make a directory for your python projects if you've not already and clone the project:
```
mkdir python_projects; cd python_projects

git clone https://github.com/rronakk/simple-chat-tester/

cd {your_clone_directory_name}
```
***
If you're following along and have downloaded the preceding dependencies, you'll be able to install python packages listed in the `requirements.txt` file by entering the following command in your shell:
```
pip install -r requirements.txt
```
Logs of the packages being downloaded will display in your shell, and you'll be good to go.

One of the key packages you'll have downloaded is a [selenium-python-binding](https://selenium-python.readthedocs.org/). With [selenium](http://www.seleniumhq.org/), we can automate just about any browser interaction via selenium's webdriver protocol. 

This way, we can "create robust, browser-based regression automation suites and tests" (pulled straight from SeleniumHQ's website). 
***
### Test runner for the framework:

In this section, we'll talk about: 
* **[pytest](http://pytest.org/latest)**: *"helps you write better programs"*
* **[selenium](http://docs.seleniumhq.org/)**: "What is Selenium?
Selenium automates browsers. That's it! What you do with that power is entirely up to you." 

This project uses pytest in combination with python-selenium bindings to control and automate browser interactions with our application.

![](http://sweet-momentum-fitness.com/wp-content/uploads/2015/03/how-neat-is-that.jpg)

If you followed installation instructions, you'll already have installed pytest and selenium to your local python virtual environment. If you didn't, refer back to the [installation section](#introduction).

[Pytest](http://pytest.org/latest) is a full-featured python testing framework that allows for flexible fixture declaration and modular "parametrized" test functions. Basically, it makes testing to a specific scenario flexible and manageable. 

[**Selenium(for Python)**](http://selenium-python.readthedocs.org/en/latest/index.html) comes with Firefox webdriver, but not with [Chrome webdriver](http://chromedriver.storage.googleapis.com/index.html) which is why I had you install it earlier. You'll need to have downloaded chromedriver before you're able to run tests using Chrome.

## <a name="running-tests"></a>Running Tests: Getting Started 
Running the tests is straightforward with pytest. For example, I can run all tests in this repo by entering the following command in my shell:
```
py.test --config config.config_qa tests/
```
This command will use the configuration located in the ```config.config_qa``` module and recursively search the `tests` directory for all defined tests and run'em! 
