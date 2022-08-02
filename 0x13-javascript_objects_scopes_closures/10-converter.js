#!/usr/bin/node
exports.converter = function (base) {
  function conversor (num) {
    return num.toString(base);
  }

  return conversor;
};
