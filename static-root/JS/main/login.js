const loginapp = Vue.createApp({});
const url = "/login";
const xhr = new XMLHttpRequest();
xhr.responseType = "json";
xhr.open("GET", url);
xhr.onload = () => {
    if (xhr.status === 401) {
        const loginapp = Vue.createApp({
            data: () => {
                return { isNotValid: true };
            },
        });
        loginapp.mount("#login_form")
        console.log("if")
    }
    else{
        const loginapp = Vue.createApp({
            data: () => {
                return { isNotValid: false };
            },
        });
        loginapp.mount("#login_form")
        console.log("else")
    }
};
