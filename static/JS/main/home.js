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
    const serverResponse = xhr.response;
    var listStrTemp = "";
    var listedItems = serverResponse.costs_list;
    var i;

    for (i = listedItems.length - 1; i > -1; i--) {
      var element = listedItems[i];
      var currentItem = formatedCostElements(element);
      listStrTemp += currentItem;
    }
    costTableEl.replaceWith(listStrTemp);
  };
  xhr.send();
}

loadCostTable(tableDivElement);

function deleteButton(obj) {
  return (
    "<form action='/delete_todo/" +
    obj.id +
    "' method='post'>" +
    "<div class='float-right'>" +
    "<button type='submit' class='btn btn-danger'>Delete</button>" +
    "</div>" +
    "</form>"
  );
}

function formatedCostElements(costarg) {
  var formatedcCE =
    "<tr><td>" +
    costarg.amount +
    "</td><td>" +
    costarg.person_used +
    "</td><td>" +
    costarg.description +
    deleteButton(costarg) +
    "</td></tr>";
  return formatedcCE;
}
