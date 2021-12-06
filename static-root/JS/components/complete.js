const tableDivElement = $("#table_body_element");

//console.log("hi")
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
    if (xhr.status === 200) {
      const serverResponse = xhr.response;
      var listStrTemp = "";
      var listedItems = serverResponse;
      var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
      for (var i = listedItems.length - 1; i > -1; i--) {
        var element = listedItems[i];
        let now = new Date(element.added_date);
        // console.log(element.date)
        // console.log(now.toLocaleDateString("en-US"));
        var currentItem = formatedCostElements(element, now.toLocaleDateString("en-US", options));
        listStrTemp += currentItem;
      }
      tableDivElement.replaceWith(listStrTemp)
    }
  };
  xhr.send();
}
$.get("/cost-manager-by-tos/is_auth_or_no/",
  function (data, textStatus, jqXHR) {
    log(data + "  " + textStatus + ' ' + jqXHR)
  },
  "json"
);
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

function formatedCostElements(costarg, datearg) {
  var formatedcCE =
    "<tr><td>" +
    datearg +
    "</td><td>" +
    costarg.amount +
    "</td><td>" +
    costarg.person_used +
    "</td><td>" +
    costarg.text +
    deleteButton(costarg) +
    "</td></tr>";
  return formatedcCE;
}
if ($(document).ready() === false) {
  log("peep")
}
function log(arg) {
  console.log(arg)
}
