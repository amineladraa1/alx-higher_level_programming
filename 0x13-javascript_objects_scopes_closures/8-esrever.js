#!/usr/bin/node
exports.esrever = function (list) {
  const reve = [];
  for (const elem of list) {
    reve.unshift(elem);
  }
  return reve;
};
