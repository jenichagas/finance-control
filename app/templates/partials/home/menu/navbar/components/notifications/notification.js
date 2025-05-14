import Alpine from "alpinejs";

const notificationControl = () => ({
    open: false,

    notifications: [
        { message: "Novo débito adicionado" },
        { message: "Nova meta cadastrada" },
        {
            message:
                "Organize-se! Adicione novo gasto.",
        },
    ],

    toggle() {
        this.open = !this.open;
    },
});

Alpine.data("notificationDropdown", notificationControl);
