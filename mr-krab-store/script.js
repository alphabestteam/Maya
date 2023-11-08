
/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/
url = "http://localhost:8000/menu"
async function getData(url) {
  const response = await fetch(url);
  let data = await response.json();
  if (response) {
    document.getElementById('loader').style.display = 'none';
  }
  showData(data);
  }

  getData(url);

function showData(data) {
  let menu = document.getElementById("menu");
  for (let item in data.items) {
    menu.setAttribute("id", "order-summary");
    let menuTitle = document.createElement("h3");
    menuTitle.innerHTML = item;
    let menuDescription = document.createElement("p");
    menuDescription.innerHTML = item['description'];
    let menuQuantity = document.createElement("p");
    menuQuantity.setAttribute("id", "order-form button")
    menuQuantity.innerHTML = "Quantity";
    menu.appendChild(menuTitle)
    menu.appendChild(menuDescription)
    menu.appendChild(menuQuantity)
  }
  
}