const staircase = (n) => {
  var line = "";
  for (let i = 1; i < n + 1; i++) {
    line += Array(n - i)
      .fill(" ")
      .join("");
    line += Array(i).fill("#").join("");
    console.log(line);
    line = "";
  }
};

// pseudo code:
// 1. create a function that takes in a number
// 2. loop through the number
// 3. create a variable that holds a string of spaces
// 4. create a variable that holds a string of hashes
// 5. create a variable that holds a string of spaces and hashes
// 6. print the string of spaces and hashes


// time complexity: O(n)


// testing
staircase(6);

// test case 2
staircase(10);
