#!/usr/bin/node

exports.esrever = function (list) {
  // Copy the input list
  const tsil = list.slice();

  console.log("Original list:");
  console.log(list);

  // Establish left/right bounds
  let right = tsil.length - 1;
  let left = 0;

  // Main swapping logic
  while (left <= right / 2 + 1) {
    const temp = tsil[left];
    tsil[left] = tsil[right];
    tsil[right] = temp;
    left++;
    right--;
  }

  // Return resulting list
  return tsil;
};
