
const iveMembers = [
    {
        name : '안유진',
        year: 2003,
    },
    {
        name : '가을',
        year: 2002,
    },
    {
        name : '레이',
        year: 2004,
    },
    {
        name : '장원영',
        year: 2004,
    },
]

class IdolGroup {
    name;
    members;

    constructor(name, members) {
        this.name = name;
        this.members = members;
    }
}
class Idol {
    name;
    year;

    constructor(name, year) {
        this.name = name;
        this.year = year;
    }
}

class FemailIdol extends Idol {
    sing() {
        return `${this.name}이 노래를 한다`
    }
}

const yuJin =  new FemailIdol('안유진', 2003);
console.log(yuJin);
console.log(yuJin.sing());

const cIveMembers = iveMembers.map(
    (x) => new FemailIdol(x.name, x.year)
)

console.log(cIveMembers);

const cIdolGroup = new IdolGroup(
    'ive',
    cIveMembers,
)

console.log(cIdolGroup)

const cIdolGroup2 = new IdolGroup(
    'ive',
    cIveMembers.map(
        (x) => new FemailIdol(x.name, x.year)
    )
);

console.log(cIdolGroup2);
