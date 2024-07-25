#!/usr/bin/node

exports.esrever = function (list) {
  // Copy the input list
  const tsil = list.slice();

  // Establish left/right bounds
  let right = tsil.length - 1;
  let left = 0;

  // Main swapping logic
  while (left <= right / 2) {
    const temp = tsil[left];
    tsil[left] = tsil[right];
    tsil[right] = temp;
    left++;
    right--;
  }

  // Return resulting list
  return tsil;
};
