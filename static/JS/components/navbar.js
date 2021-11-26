let Header = Vue.createApp({
  delimiters: ["[[", "]]"],
  data: {
    isLogged: true,
  },
});
Header.mount("#header");
