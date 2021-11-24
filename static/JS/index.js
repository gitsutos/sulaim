
const tableDivElement = $("#table_body_element");
const completeCostElement = $("#complete_cost");

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
    var listedItems = serverResponse.response;
    var i;
    var TempAmount = 0;

    for (i = listedItems.length - 1; i > -1; i--) {
    var element = listedItems[i];
    //console.log(element)
    TempAmount += element.amount;
    var currentItem = formatedCostElements(element);
    listStrTemp += currentItem;
    }
    costTableEl.replaceWith(listStrTemp);
    completeCostElement.replaceWith(completeCostElement);
};
xhr.send();
completeCostElement.replaceWith(completeCostElement);
}

loadCostTable(tableDivElement);

function deleteButton(obj) {
return (
    "<form action='/cost-manager-by-tos/delete_todo/" +
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
    "<tr><td class='col-2'>" +
    costarg.amount +
    "</td><td class='col-4'>" +
    costarg.person_used +
    "</td><td class='col-6'>" +
    costarg.description +
    deleteButton(costarg) +
    "</td></tr>"
return formatedcCE;
}
