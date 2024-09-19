

var createCounter = function (init) {
    let current = init;
    return {
        reset: function () {
            current = init;
            return init;
        },
        increment: function () {
            return ++current;
        },
        decrement: function () {
            return --current;
        }
    };
};