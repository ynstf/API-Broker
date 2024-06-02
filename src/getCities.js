import React, { useEffect, useState } from "react";

export default function CitiesEntery() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/city/")
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);
  return (
    <div className="citySelection">
      <label>Your city : </label>
      <select>
        {items.map((item) => (
          <option key={item.id} value={item.id}>
            {item.name}
          </option>
        ))}
      </select>
    </div>
  );
}
