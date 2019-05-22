For all languages, I am using VSCode on Windows 10.

# Requirements

* Install Python 3.7.3: [Link](https://www.python.org/downloads/)
* Install VSCode extension Code Runner: [Link](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
* Add a python path to CodeRunner
  * VSCode -> Extensions
  * Code Runner (right click) -> Configure Extension Settings
```json
{
    "...",
    "code-runner.executorMap": {
        "python": "PATH/TO/AppData/Local/Programs/Python/Python37-32/python.exe",
        "...",
    }    
}
```

# New Kata

* Copy Katas/python/__default.py to Katas/python/NewKataName.py
* Replace description
* Replace unit tests

Works with most CodeWars site call methods
```py
test.describe("Addition") # Optional
test.assert_equals(add(2, 2), 4)
```