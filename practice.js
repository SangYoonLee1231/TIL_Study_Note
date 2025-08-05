const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

let [n, r, c] = input[0].split(" ").map(Number);
let grid = input.slice(1, n + 1).map((line) => line.split(" ").map(Number));

// Please Write your code here.
[r, c] = [r - 1, c - 1];

const [dr, dc] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];

// const convertToDirNum = {
//     'N': 0,
//     'S': 1,
//     'W': 2,
//     'E': 3
// };

const answerArr = [grid[r][c]];

function solution() {
  let flag = true;

  while (flag) {
    for (let dirNum = 0; dirNum < 4; dirNum++) {
      const [nr, nc] = [r + dr[dirNum], c + dc[dirNum]];

      if (inRange(nr, nc) && grid[nr][nc] > grid[r][c]) {
        [r, c] = [nr, nc];
        answerArr.push(grid[r][c]);
        break;
      }
    }
    flag = false;
  }

  answerArr.forEach((elem) => {
    process.stdout.write(`${elem} `);
  });
}

function inRange(r, c) {
  return r >= 0 && r < n && c >= 0 && c < n;
}

solution();
