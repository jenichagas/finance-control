function configForm() {
    return {
        user: {
            name: "Jeniffer Chagas",
            email: "jeniffer@email.com",
            gender: "",
            password: "",
        },
        preferences: {
            theme: "light",
            primaryColor: "#00A8CC",
        },
        finance: {
            salary: 5000,
            reserveEmergency: 20,
            reserveInvestments: 30,
        },
        saveAccount() {
            console.log("Conta atualizada:", this.user);
        },
        savePreferences() {
            document.documentElement.style.setProperty(
                "--primary",
                this.preferences.primaryColor
            );
            console.log("Preferências atualizadas:", this.preferences);
        },
        saveFinance() {
            console.log("Financeiro atualizado:", this.finance);
        },
    };
}
