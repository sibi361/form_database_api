const users = {
    name: "John Deo",
    email: 'test123@gmail.com" or drop table pandasrgood;--',
    emailLearner: "asdfgh@learner.manipal.edu.com",
    reg: "530872345",
    year: "1",
    phone: "9876543210",
    domains: "money,bin,management",
    notes: 'hi i am xyz" or drop table pandasrgood;--',
};

const encodedData = encodeURIComponent(JSON.stringify(users));
// console.log(encodedData);

fetch(`http://127.0.0.1:9876/api?q=${encodedData}`)
    .then((res) => res.text())
    .then((res) => console.log(res))
    .catch((err) => console.error(err));
