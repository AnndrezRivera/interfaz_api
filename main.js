import React, { useState } from 'react';

function App() {
  const [state, setState] = useState('');
  const [category, setCategory] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch('https://api-recomendaciones.onrender.com');
    const data = await response.json();
    setResults(data);
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          State:
          <input type="text" value={state} onChange={event => setState(event.target.value)} />
        </label>
        <label>
          Category:
          <input type="text" value={category} onChange={event => setCategory(event.target.value)} />
        </label>
        <input type="submit" value="Submit" />
      </form>
      <ul>
        {results.map(result => (
          <li key={result.name}>
            <h2>{result.name}</h2>
            <p>Address: {result.address}</p>
            <p>Average Rating: {result.avg_rating}</p>
            <p>Categories: {result.categories}</p>
            <p>Attributes: {result.attributes}</p>
            <p>Sentiment: {result.Sentimiento}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
