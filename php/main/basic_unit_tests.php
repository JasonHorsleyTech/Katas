<?php
class TestCase
{
    public function assertEquals($expected, $returned)
    {
        $expected_str = strval($expected);
        $returned_str = strval($returned);
        if ($this->testAt == 0) {
            print_c("-- Running tests on $this->kataName --", "blue");
        }
        if ($expected == $returned) {
            print_c("Test $this->testAt passed with $returned", "green");
        } else {
            print_c("Test $this->testAt failed.", "red");
            print_c("  Expected: $expected_str", "red");
            print_c("  Returned: $returned_str", "red");
            if (gettype($expected) !== gettype($returned)) {
                print_c("  !Different Types!", "red");
            }
        }
        $this->testAt++;
    }
    function __construct()
    {
        $this->testAt = 0;
        $this->kataName = get_class($this);
    }
}
function print_c($what, $color)
{
    // colors ref: https://joshtronic.com/2013/09/02/how-to-use-colors-in-command-line-output/
    $colors = [
        "black" => "0;30",
        "white" => "1;37",
        "red" => "0;31",
        // ...
    ];
    $code = isset($colors[$color]) ? $colors[$color] : $colors["white"];
    // Not working in VSCode... something to do with the cygwin64 bash window...
    // echo "\033[31m some colored text \033[0m some white text \n";
    echo "$what \n";
}
