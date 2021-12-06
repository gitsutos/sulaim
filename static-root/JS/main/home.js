const tableDivElement = $("#table_body_element");

function loadCostTable(costTableEl) {
  const xhr = new XMLHttpRequest();
  //xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
  //xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
  const method = "GET";
  const url = "/cost-manager-by-tos/list_view_of_costs";
  const responseType = "json";

  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.onload = function () {
    if (xhr.status === 401) {
      $("#main_body").replaceWith(`<div class="jumbotron">
        <h1>Login requird</h1>
        <h3><p>you must login to add, delete and see your costs </p></h3>
        <p>if you already have an tos acount then <a href="/login/">login</a> in <br>
        if you don't have click the "<a href="/sign_up">Sign_up</a>" link and create an account and then login</p>
      </div>`)
    }
    if (xhr.status === 200) {
      const serverResponse = xhr.response;
      const total_of_month = total_cost_of_m(serverResponse);
      const total_of_year = total_cost_of_y(serverResponse);
      $("#total_cost_of_m").replaceWith(total_of_month)
      $("#total_cost_of_y").replaceWith(total_of_year)
    };
  };
  xhr.send();
}

loadCostTable(tableDivElement);

function total_cost_of_m(listed_items) {
  var total = 0
  for (let i = 0; i < listed_items.length; i++) {
    const element = listed_items[i];
    var date = new Date(element.added_date)
    var today = new Date()
    if (date.getMonth() === today.getMonth()) {
      total = total + element.amount
    }
  }
  return (total);
}
function total_cost_of_y(listed_items) {
  var total = 0
  for (let i = 0; i < listed_items.length; i++) {
    const element = listed_items[i];
    var date = new Date(element.added_date)
    var today = new Date()
    if (date.getFullYear() === today.getFullYear()) {
      total = total + element.amount
    }
  }
  return (total);
}
$("#main_body").css({
  "display": "none",
})
$(document).ready(
  $("#main_body").css({
    "display": "contents",
  }))