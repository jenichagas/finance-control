import Alpine from "alpinejs";

const dropdownControl = () => ({
    openDropdown: false,

    init() {
        console.log("Dropdown initialized");
    },

    toggle() {
        this.openDropdown = true;
    },
    close() {
        this.openDropdown = false;
    }
});

Alpine.data("dropdownControl", dropdownControl)