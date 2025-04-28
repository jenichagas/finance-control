import Alpine from "alpinejs";

const navbarControl = () => ({
    openModal: false,

    init() {
        console.log("Navbar control initialized");
    },
});

Alpine.data("navbarControl", navbarControl);
