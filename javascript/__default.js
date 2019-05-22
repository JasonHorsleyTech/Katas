const basic_unit_tests = require('./main/basic_unit_tests');
let Test = new basic_unit_tests();

// DESC
/*
Make a function that adds two numbers
*/
/* --------------- */

function add(n1, n2) {
    return n1+n2;
}

/* --------------- */
// TEST
Test.describe("Addition");
Test.assertEquals(add(2, 2), 4);