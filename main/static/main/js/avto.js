const pg = require('pg')
const conString = 'postgres://postgres:ilidan222@ localhost:5432/DNK' // Убедитесь, что вы указали данные от вашей базы данных
pg.connect(conString, function (err, client, done) {
  if (err) {
    return console.error('error fetching client from pool', err)
  }
  client.query('SELECT $1::varchar AS my_first_query', ['DNK'], function (err, result) {
    done()
    if (err) {
      return console.error('error happened during query', err)
    }
    console.log(result.rows[0])
    process.exit(0)
  })
})