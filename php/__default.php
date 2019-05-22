<?php
require("main/basic_unit_tests.php");

// DESC
/*
Make a function that adds two numbers
*/
/* --------------- */

function add($n1, $n2) {
    return $n1 + $n2;
}

/* --------------- */
// TEST
class AdditionCases extends TestCase
{
    private function dotest($actual, $expected)
    {
        $this->assertEquals($expected, $actual);
    }
    public function additionBasics()
    {
        $this->dotest(add(2, 2), 4);
    }
}
$test = new AdditionCases();
$test->additionBasics();
