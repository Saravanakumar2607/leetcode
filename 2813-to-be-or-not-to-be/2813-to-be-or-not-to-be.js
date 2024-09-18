function expect(val) {
    return {
        toBe: function (otherVal) {
            if (val === otherVal) {
                return true; // Values are equal
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function (otherVal) {
            if (val !== otherVal) {
                return true; // Values are not equal
            } else {
                throw new Error("Equal");
            }
        }
    };
}

// Example usage:
try {
    console.log(expect(5).toBe(5)); // Output: true
} catch (error) {
    console.error(error.message);
}

try {
    console.log(expect(5).notToBe(10)); // Output: true
} catch (error) {
    console.error(error.message);
}

try {
    console.log(expect(5).toBe(10)); // This will throw an error
} catch (error) {
    console.error(error.message); // Output: "Not Equal"
}

try {
    console.log(expect(5).notToBe(5)); // This will throw an error
} catch (error) {
    console.error(error.message); // Output: "Equal"
}
