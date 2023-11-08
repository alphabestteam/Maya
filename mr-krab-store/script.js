
/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/
url = "http://localhost:8000/menu";
async function getData(url) {
  let response = await fetch(url);
  let data = await response.json();
  if (response) {
    document.getElementById('loader').style.display = 'none';
  }
  showData(data);
  }

  getData(url);
  function showData(data) {
  let menu = document.getElementById("menu");
  for (const key in data.items) {
      const itemDiv = document.createElement('div')
      itemDiv.setAttribute('class', 'card');
      const item = data.items[key];
      const price_num = item.price.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
      });
      let menuTitle = document.createElement("h3");
      menuTitle.innerHTML = `${item.name} (${price_num})`;
      let menuDescription = document.createElement("p");
      menuDescription.innerHTML = item.description;
      let quantityDiv = document.createElement("div");
      let menuQuantity = document.createElement("p");
      menuQuantity.innerHTML = "Quantity:";
      let inputQuantity = document.createElement("INPUT");
      inputQuantity.setAttribute("type", "number");
      inputQuantity.setAttribute('placeholder','0');
      inputQuantity.setAttribute('min','0');
      inputQuantity.setAttribute('max','5');
      inputQuantity.style.display = "inline-block";
      menuQuantity.style.display = "inline-block";
      itemDiv.appendChild(menuTitle);
      itemDiv.appendChild(menuDescription);
      quantityDiv.appendChild(menuQuantity);
      quantityDiv.appendChild(inputQuantity);
      itemDiv.appendChild(quantityDiv);
      menu.appendChild(itemDiv);
  }
  
}