For all languages, I am using VSCode on Windows 10.

# Requirements

* Install XAMPP because it's easier: [Link](https://www.apachefriends.org/index.html)
  * PHP is 7.3.4+
  * Xdebug is 2.7.1+
* Install VSCode extension Code Runner: [Link](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
* Add a PHP path to CodeRunner
  * VSCode -> Extensions
  * Code Runner (right click) -> Configure Extension Settings -> Edit in settings.json
```json
{
    "...",
    "code-runner.executorMap": {
       "php": "C:/xampp/php/php.exe",
        "...",
    }    
}
```
* Setup Xdebug with VSCode: [Link](https://www.codewall.co.uk/debug-php-in-vscode-with-xdebug/)

# New Kata

* Copy Katas/javascript/__default.js to Katas/javascript/NewKataName.js
* Replace description
* Replace unit tests

Works with either the programatic or callback approach on CodeWars
```js
// Programatic
Test.describe("Addition"); // Optional
Test.assertEquals(add(2, 2), 4);

// Callback
Test.describe("Addition",function() { // Optional
    Test.it("Single Digit",function() { // Optional
        Test.assertEquals(add(2, 2), 4)
    })
})
```