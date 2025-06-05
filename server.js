const express = require('express');
const path = require('path');
const app = express();

// Middleware to parse JSON
app.use(express.json());

// Serve index.html statically
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Log username and IP address
app.post('/log', (req, res) => {
  const { username } = req.body;
  const userIP = req.headers['x-forwarded-for'] || req.socket.remoteAddress;

  console.log('🔥 Username:', username);
  console.log('🌍 IP Address:', userIP);

  res.sendStatus(200);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
