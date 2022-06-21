const {Client} = require('pg');

const db = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'DNK',
    password: 'ilidan222',
    port: 5432
});

db.connect();

db.query('SELECT * FROM login_parol', (err, data) => {
    if (err)
        throw new Error(err);
    console.log(data, err);
    db.end();
});