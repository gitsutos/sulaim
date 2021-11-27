const xhr = new XMLHttpRequest();
let url = "/cost-manager-by-tos/is_auth_or_no/";
xhr.responseType = "json";
xhr.open("GET", url);
var IsLogged = true;
xhr.onload = () => {
  IsLogged = !xhr.response.is_authenticated;
  let Header = Vue.createApp({
    delimiters: ["[[", "]]"],
    data: () => {
      //console.log("3", IsLogged);
      return { isLogged: IsLogged };
    },
  });
  Header.mount("#header");
  //console.log("1", IsLogged);
};
//console.log("2", IsLogged);
xhr.send();

//return IsLogged
