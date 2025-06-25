import React, { useEffect, useState } from 'react';

function App() {
  const [time, setTime] = useState('');

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => setTime(data.time));
  }, []);

  return <h1>Server Time: {time}</h1>;
}

export default App;

   
