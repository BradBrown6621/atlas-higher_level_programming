#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nElems = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      nElems++;
    }
  });
  return nElems;
};
