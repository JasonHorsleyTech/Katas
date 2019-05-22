class basic_unit_tests {
    describe(kataName, cb) {
        this.kataName = kataName || "CodeWar Kata";
        if (cb)
            cb()
    }
    it(testName, cb) {
        this.testName = testName;
        if (cb)
            cb()
    }
    assertEquals(returned, expected, testName = '') {
        let expected_str = expected.toString().toLowerCase();
        let returned_str = returned.toString().toLowerCase();
        if (this.testAt == 0) {
            console.info(`-- Running tests on ${this.kataName} --`);
        }
        if (expected == returned) {
            console.log(`Test ${this.testAt} passed with ${returned}`);
        } else {
            let err = `Test ${this.testAt} failed. \r\n` +
                `  Expected: ${expected_str}\r\n` +
                `  Returned: ${returned_str}`;
            if (typeof expected !== typeof returned) {
                err += `\r\n !Different Types!`;
            }
            console.error(err);
        }
        this.testAt++;
    }
    constructor() {
        this.testAt = 0;

        this.describe = this.describe.bind(this);
        this.assert_equals = this.assertEquals.bind(this);
    }
};
module.exports = basic_unit_tests