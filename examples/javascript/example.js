const axios = require('axios')
const res = await axios.get(`https://idiotcreaturehater.pythonanywhere.com/api?input=${question}`)
const answer = res.data.text