const person = {
    name: {
        firstName: "GilDong",
        lastName: "Hone"
    },
    age: 20,
    likes : ["apple", "samsung"],
    "phone number": "010-3812-0110",
    printHello: function() {
        return "Hello";
    }
}

console.log(person);
console.log(person.age);
console.log(person.likes[0]);
console.log(person["name"]["firstName"]);
console.log(person["phone number"]);