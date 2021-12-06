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
    if (xhr.status === 200) {
      const serverResponse = xhr.response;
      var listStrTemp = "";
      var listedItems = serverResponse;

      for (var i = listedItems.length - 1; i > -1; i--) {
        var element = listedItems[i];
        var currentItem = formatedCostElements(element);
        listStrTemp += currentItem;
      }
      costTableEl.replaceWith(listStrTemp);
    };
    if (xhr.status === 401) {
      $("#main_body").replaceWith(`<div class="jumbotron">
        <h1>Login requird</h1>
        <h3><p>you must login to add, delete and see your costs </p></h3>
        <p>if you already have an tos acount then <a href="/login/">login</a> in <br>
        if you don't have click the "<a href="/sign_up">Sign_up</a>" link and create an account and then login</p>
      </div>`)
    }
  }
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
    costarg.text +
    deleteButton(costarg) +
    "</td></tr>";
  return formatedcCE;
}

//div

const app = Vue.createApp({
  delimiters: ["[[", "]]"],
  data: () => {
    return {};
  },
});
