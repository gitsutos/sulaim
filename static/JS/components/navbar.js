let Header = Vue.createApp({
    delimiters: ["[[", "]]"],
    data: () => {
        return { isLogged: true,}
    },
});
Header.mount("#header");
