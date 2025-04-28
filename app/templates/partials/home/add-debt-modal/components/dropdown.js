import Alpine from "alpinejs";

const dropdownControl = () => ({
    openDropdown: false,

    toggle() {
        this.openDropdown = true;
    },
    close() {
        this.openDropdown = false;
    }
});

Alpine.data(dropdownControl, "dropdownControl")