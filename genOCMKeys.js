const fs = require("fs");

var f = 1;
var OEMKey = [];

// FORMAT: XXXXX-OEM-XXXXXXX-XXXXX
// NOT RECOMMENDED TO GENERATED ALL POSSIBLE COMBINATION!

for (let i = 1; i <= 366; i++) {
    var day = i.toString().padStart(3, 0); // Pad the day number.

    for (let j = 1995; j <= 2003; j++) {
        var year = j.toString().slice(2).padStart(2, 0); // Pad the year number.

        for (let k = 0; k <= 999999; k++) {
            var key = k.toString().padStart(7, 0); // Pad the key.

            if (/[08-9]/.test(key.slice(-1))) continue; // Skip if last digit is 0, 8 or 9.
            var digitSum = key.split('').map(Number).reduce((a, b) => a + b, 0); // Find sum of all digits.

            if (digitSum % 7 !== 0) continue; // Skip if digit sum is not divisible by 7.

            for (let l = 0; l <= 99999; l++) {
                var v = l.toString().padStart(5, 0); // Pad the holder number.

                var OEMKey = `${day}${year}-OEM-${key}-${v}`; // Format the key.

                if (OEMKey.length === 10000000) {
                    fs.writeFileSync(`./OEMKeys.${f++}.txt`, OEMKey.join("\r\n"), 'utf8');
                    OEMKey = [];

                    // Dump 10 million keys from memory to disk and clearing the memory
                    // because 10 million keys can take up to 1.5 GB of ram.
                    // Total is about 32940000000000 (32.94 trillions) keys.
                }

            }
        }
    }
}

fs.appendFileSync(`./OEMKeys.${f++}.txt`, OEMKey.join("\r\n"), 'utf8');

// Dump the last bit of the keys into disk.
// The final total size about 790.56 terabytes!