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
