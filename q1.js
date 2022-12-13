const compareTriplets = (a, b) => {
  let aScore = 0;
  let bScore = 0;
  for (let i = 0; i < 3; i++) {
    if (a[i] > b[i]) {
      aScore += 1;
    } else {
      if (a[i] < b[i]) {
        bScore += 1;
      }
    }
  }

  let comparison_array = [aScore, bScore];
  return comparison_array;
};

// pseudo code:
// 1. create a function that takes in two arrays
// 2. create a variable that holds the score of a and b
// 3. loop through the arrays
// 4. create a conditional statement that checks if value of a is greater than b
// 5. if a is greater than b, add 1 to a's score
// 6. create a conditional statement that checks if value of b is greater than a
// 7. if b is greater than a, add 1 to b's score
// 8. create a variable that holds an array of a's and b's score
// 9. return the array

// time complexity: O(n)

// testing
const a1 = [5, 6, 7];
const b1 = [3, 6, 10];

console.log(compareTriplets(a1, b1));

// test case 2
const a2 = [17, 28, 30];
const b2 = [99, 16, 8];

console.log(compareTriplets(a2, b2));
