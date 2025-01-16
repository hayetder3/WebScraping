import React, { useState, useEffect } from "react";
import Card from "./components/Card"; 
import "./App.css"; // Style principal

function App() {
 
  // Utilisation des données provenant du fichier JSON
  const [championData, setChampionData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Effect pour charger les données à partir du fichier JSON
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Charger le fichier JSON depuis le dossier public
        const response = await fetch('/champion_data.json');
        
        // Vérifier si la réponse est valide
        if (!response.ok) {
          throw new Error("Erreur de chargement des données.");
        }
        
        // Convertir la réponse en format JSON
        const data = await response.json();
        
        // Mettre à jour l'état avec les données récupérées
        setChampionData(data);
        setLoading(false);
      } catch (err) {
        setError("Erreur lors de la récupération des données.");
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Affichage de l'écran de chargement ou des erreurs
  if (loading) return <h2>Chargement...</h2>;
  if (error) return <h2 style={{ color: "red" }}>{error}</h2>;

  return (
    <div className="App">
      <h1>Liste des champions</h1>
      <div className="champion-list">
        {championData.map((champion, index) => (
          <Card key={index} champion={champion} />
        ))}
      </div>
    </div>
  );
}

export default App;
