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

//!https://leetcode.com/problems/array-reduce-transformation/
var reduce = function (nums, fn, init) {
  let x = nums.reduce(fn, init);
  return x;
};

//!https://leetcode.com/problems/apply-transform-over-each-element-in-array/
var map = function (arr, fn) {
  let res = [];
  arr.forEach((item, index) => {
    res.push(fn(item, index));
  });
  return res;
};

//!https://leetcode.com/problems/counter-ii/
var createCounter = function (init) {
  let num = init;

  function increment() {
    num = num + 1;
    return num;
  }

  function reset() {
    num = init;
    return num;
  }

  function decrement() {
    num = num - 1;
    return num;
  }
  return { increment, reset, decrement };
};

//!https://leetcode.com/problems/allow-one-function-call/
var once = function (fn) {
  let ans = true;
  return function (...args) {
    if (ans) {
      ans = false;
      return fn(...args);
    }
  };
};

//!https://leetcode.com/problems/return-length-of-arguments-passed/
var argumentsLength = function (...args) {
  return args.length;
};
