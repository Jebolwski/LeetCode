//!https://leetcode.com/problems/counter/
var createCounter = function (n) {
  return function () {
    return n++;
  };
};

//!https://leetcode.com/problems/array-prototype-last/
Array.prototype.last = function () {
  if (this.length > 0) {
    return this[this.length - 1];
  }
  return -1;
};

//!https://leetcode.com/problems/convert-object-to-json-string/submissions/937317485/
var jsonStringify = function (object) {
  return JSON.stringify(object);
};

//!https://leetcode.com/problems/filter-elements-from-array/
var filter = function (arr, fn) {
  return arr.filter((n, i) => {
    return fn(n, i);
  });
};

//!https://leetcode.com/problems/function-composition/
var compose = function (functions) {
  return function (x) {
    functions = functions.reverse();
    functions.forEach((func) => {
      x = func(x);
      console.log(x);
    });
    return x;
  };
};
