const arr = [10, 20, 30];

for(let i = 0;i < arr.length;i++) {
    console.log(arr[i]);
}

arr.push(50);
console.log(arr);
arr.pop();
console.log(arr);
arr.unshift(0);
console.log(arr);
arr.shift();
console.log(arr);

arr.forEach(function(v) {
    console.log(v);
})

arr.forEach((v) => {
    console.log(v);
})

const date = new Date();

console.log(date)