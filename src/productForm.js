import React, { useEffect, useState } from "react";

export default function ProductForm() {
  const [owners, setOwners] = useState([]);
  const [product, setProduct] = useState({
    success: "",
    name: "",
    description: "",
    price: "",
    owner: "",
  });

  useEffect(() => {
    fetch("http://localhost:8000/api/salers/")
      .then((response) => response.json())
      .then((data) => setOwners(data));
  }, []);

  function addProduct(event) {
    event.preventDefault(); // لمنع إعادة تحميل الصفحة عند تقديم النموذج

    fetch("http://127.0.0.1:8000/api/products/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(product),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("Network response was not ok.");
      })
      .then((data) => {
        console.log("Success:", data);
        // يمكن هنا إضافة منطق لإعادة تعيين الحقول أو عرض رسالة نجاح
        setProduct({
          success: true,
          name: "",
          description: "",
          price: "",
          owner: "",
        });
      })
      .catch((error) => {
        console.error("There was a problem with your fetch operation:", error);
      });
  }

  return (
    <div>
      {product.success ? <h1>Product created successfully!</h1> : null}
      <form onSubmit={addProduct}>
        <label>Name : </label>
        <br />
        <input
          type="text"
          value={product.name}
          onChange={(event) => {
            setProduct({ ...product, name: event.target.value });
          }}
          required
        />
        <br />
        <br />

        <label>Description : </label>
        <br />
        <input
          type="text"
          value={product.description}
          onChange={(event) => {
            setProduct({ ...product, description: event.target.value });
          }}
          required
        />
        <br />
        <br />

        <label>Price : </label>
        <br />
        <input
          type="number"
          value={product.price}
          onChange={(event) => {
            setProduct({ ...product, price: event.target.value });
          }}
          required
        />
        <br />
        <br />

        <label>The owner : </label>
        <br />
        <select
          value={product.owner}
          onChange={(event) => {
            setProduct({ ...product, owner: event.target.value });
          }}
          required
        >
          <option key="" value="">
            Choose the salesman...
          </option>
          {owners.map((owner) => (
            <option key={owner.id} value={owner.id}>
              {owner.name}
            </option>
          ))}
        </select>
        <br />
        <br />

        <input type="submit" value="Create Product" />
      </form>
    </div>
  );
}
