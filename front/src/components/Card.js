import React from "react";
import "./Card.css";

const Card = ({ champion }) => {
  return (
    <div className="card">
      <img
        src={champion["Image URL"]} // Utilisez la clé "Image URL" du JSON
        alt={champion["Name"]} // Utilisez la clé "Name" du JSON
        className="card-image"
      />
      <h3>{champion["Name"]}</h3> {/* Utilisez la clé "Name" */}
      <p>Health: {champion["Health"]}</p> {/* Utilisez la clé "Health" */}
      <p>Attack Damage: {champion["Attack Damage"]}</p> {/* Utilisez la clé "Attack Damage" */}
      <p>Armor: {champion["Armor"]}</p> {/* Utilisez la clé "Armor" */}
      <p>Movement Speed: {champion["Movement Speed"]}</p> {/* Utilisez la clé "Movement Speed" */}
    </div>
  );
};

export default Card;
