/*
* Async / Await
*/

let flag = 1; /* 의미는 없으나 넣어봄 */

const getPromise = (seconds) => new Promise((resolve, reject) => {
    setTimeout(() => {
        if (flag == 1) {
            flag = 0;
            resolve('resolve end');
        } else {
            flag = 1;
            reject('reject end');
        }
    }, seconds * 1000);
});

async function runner() {
    try {
        const result1 = await getPromise(1);
        console.log(result1);
        const result2 = await getPromise(2);
        console.log(result1);
        const result3 = await getPromise(1);
        console.log(result1);
    } catch(e) {
        const result4 = await getPromise(1);
        // console.log(result4);
        console.log(e);
    } finally{
        console.log('finally');
    }
}

runner();
runner();

console.log('실행 끝');