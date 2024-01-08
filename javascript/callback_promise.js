/*
* callback
*/

function waitAndRun() {
    setTimeout(() => {
        console.log('The end');
        setTimeout(() => {
            console.log('The end 2');
        }, 2000)
    }, 2000)
}

waitAndRun();

const timeoutPromise = new Promise((resolve, reject)=> {
    setTimeout(() => {
        resolve('resolve end');
    }, 2000)
})

/* 불완전한 Promise
*/
timeoutPromise.then((res) => {
    console.log('------then');
    console.log(res);
    // timeoutPromise();
}).then((res) => {
    console.log('------then 2');
    console.log(res);
});

/* 완전한 Promise
*/

let flag = 1;

const getPromise = (seconds) => new Promise((resolve, reject) => {
    setTimeout(() => {
        // if (flag == 1) {
        //     flag = 0;
            resolve('resolve end2');
        // } else {
        //     flag = 1;
        // reject('reject end2');
        // }
    }, 2000);
});

getPromise(1)
    .then((res) => {
        console.log('First then');
        console.log(res);
        return getPromise(2);
    })
    .then((res) => {
        console.log('Second then');
        console.log(res);
        return getPromise(2);
    })
    .then((res) => {
        console.log('Third then');
        console.log(res);
        return getPromise(2);
    })
    // .catch((res) => {
    //     console.log('Forth catch');
    //     console.log(res);
    // })
    .finally(() => {
        console.log('finally')
    });

    Promise.all([
        getPromise(1),
        getPromise(2),
        getPromise(1),
    ])
    .then((res) => {
        console.log('4th then');
        console.log(res);
        return getPromise(2);
    }).then((res) => {
        console.log('5th then');
        console.log(res);
        return getPromise(2);
    }).then((res) => {
        console.log('6th then');
        console.log(res);
        return getPromise(2);
    }).finally(() => {
        console.log('Promise all finally')
    });