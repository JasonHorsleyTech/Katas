For all languages, I am using VSCode on Windows 10.

# Requirements

* Install node 10.15.3+: [Link](https://nodejs.org/en/download/)
* Install npm 6.4.1 (Just incase?): [Link](https://docs.npmjs.com/cli/install)
* Install VSCode extension Code Runner: [Link](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
* (Optional) Replace CodeRunner "run" shortcut with Control Shift Enter (or whatever)

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