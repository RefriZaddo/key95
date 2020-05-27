const fs = require("fs");

var f = 1;
var keys = [];

// FORMAT: XXX-XXXXXXX

for (let i = 0; i <= 999; i++) {
    var site = i.toString().padStart(3, 0); // Pad the site number.

    if (/([3-9])\1\1/.test(site)) continue; // Skip if start with 3 consecutive number.

    for (let j = 0; j <= 9999999; j++) {
        var key = j.toString().padStart(7, 0); // Pad the key.

        if (/[08-9]/.test(key.slice(-1))) continue; // Skip if last digit is 0, 8 or 9.
        var digitSum = key.split('').map(Number).reduce((a, b) => a + b, 0); // Find sum of all digits.

        if (digitSum % 7 !== 0) continue; // Skip if digit sum is not divisible by 7.

        var CDKey = `${site}-${key}`; // Format the key.

        keys.push(CDKey); // Push key into memory.

        if (keys.length === 10000000) {
            fs.writeFileSync(`./CDKeys.${f++}.txt`, keys.join("\r\n"), 'utf8');
            keys = [];

            // Dump 10 million keys from memory to disk and clearing the memory
            // because 10 million keys can take up to 1.5 GB of ram.
            // Total is about 993000000 (993 millions) keys.
        }
    }
}

fs.appendFileSync(`./CDKeys.${f++}.txt`, keys.join("\r\n"), 'utf8');

// Dump the last bit of the keys into disk.
// The final total size should be around 10.923 gigabytes.