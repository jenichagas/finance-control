import Alpine from "alpinejs";

const sidebarControl = () => ({
    isOpen: true,

    init() {

        const saved = localStorage.getItem("sidebarOpen");
        this.isOpen = saved === null ? true : JSON.parse(saved);
    },

    toggleSidebar() {
      console.log("ai")
        this.isOpen = !this.isOpen;
        localStorage.setItem("sidebarOpen", JSON.stringify(this.isOpen));
    },
});

Alpine.data("sidebarControl", sidebarControl);
