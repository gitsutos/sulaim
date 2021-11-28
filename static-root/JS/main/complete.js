const xhr = new XMLHttpRequest();
const method = "GET";
const url = "/cost-manager-by-tos/list_view_of_costs";
const responseType = "json";

xhr.responseType = responseType;
xhr.open(method, url);
xhr.onload = function () {
    const serverResponse = xhr.response;
    var listedItems = serverResponse.costs_list;
    const completeapp = Vue.createApp({
        delimiters: ["[{", "}]"],
        data: () => {
          return {ListedItems: listedItems};
        },
      });
    completeapp.mount("#complete_cost_table");
};
xhr.send();
