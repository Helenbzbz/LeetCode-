var twoSum = function (nums, target) {
  var map = {};
  for (let i = 0; i < nums.length; i++) {
    var another = target - nums[i];
    if (another in map) {
      return [map[another], i];
    }
    map[nums[i]] = i;
  }
};

console.log(twoSum([1, 2, 3, 4], 3))

/*
Try to Avoid Loop & Loop 
-> even one empty loop is better than loop + loop
*/