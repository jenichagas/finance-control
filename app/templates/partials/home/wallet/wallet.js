import Alpine from "alpinejs";
const walletControl = () => ({
    newSalary: "",
    openModal: "",
    newExtra: "",
    newOtherDesc: "",
    newOtherValue: "",
    newCard: { name: "", limit: "", used: "" },
    salary: 5000,
    extraIncome: 1200,
    totalIncome: 6200,
    reserveEmergency: 800,
    reserveInvestments: 1500,
    committedAmount: 4200,
    monthBalance: 2000,
    creditCards: [
        { name: "Nubank", limit: 2000, used: 500 },
        { name: "Inter", limit: 1000, used: 750 },
    ],

    format(val) {
        return val.toLocaleString("pt-BR", {
            minimumFractionDigits: 2,
        });
    },

    addSalary() {
        this.salary = Number(this.newSalary);
        this.totalIncome = this.salary + this.extraIncome;
        Alpine.store("walletStore").totalIncome = this.totalIncome;
        Alpine.store("walletStore").monthBalance = this.monthBalance;
        Alpine.store("walletStore").committedAmount = this.committedAmount;
        this.openModal = "";
    },

    addExtra() {
        this.salary = Number(this.extraIncome);
        this.totalIncome = this.salary + this.extraIncome;
        Alpine.store("walletStore").totalIncome = this.totalIncome;
        Alpine.store("walletStore").monthBalance = this.monthBalance;
        Alpine.store("walletStore").committedAmount = this.committedAmount;
        this.openModal = "";
    },

    addOther() {
        this.salary = Number(this.newOtherValue);
        this.totalIncome = this.salary + this.extraIncome;
        Alpine.store("walletStore").totalIncome = this.totalIncome;
        Alpine.store("walletStore").monthBalance = this.monthBalance;
        Alpine.store("walletStore").committedAmount = this.committedAmount;
        this.openModal = "";
    },

    addCard() {
        this.creditCards.push({
            name: this.newCard.name,
            limit: Number(this.newCard.limit),
            used: Number(this.newCard.used),
        });
        this.newCard = { name: "", limit: "", used: "" };
        this.openModal = "";
    },
});

Alpine.store("walletStore", {
    committedAmount: 4200,
    monthBalance: 2000,
    totalIncome: 6200,
});

Alpine.data("walletControl", walletControl);
