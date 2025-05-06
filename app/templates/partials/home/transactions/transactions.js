import Alpine from "alpinejs";
const transactionControl = () => ({
    showModal: false,
    filters: {
        month: "",
        type: "",
        status: "",
    },

    newTransaction: {
        description: "",
        date: "",
        type: "despesa",
        category: "",
        amount: "",
        status: "pendente",
    },

    transactions: [
        {
            id: 1,
            date: "2025-04-10",
            description: "Salário",
            type: "receita",
            category: "Trabalho",
            amount: 5000,
            status: "pago",
        },

        {
            id: 2,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },

        {
            id: 3,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },
        {
            id: 4,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },
        {
            id: 5,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },
        {
            id: 6,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },
        {
            id: 7,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },
        {
            id: 8,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
            status: "pago",
        },
        {
            id: 9,
            date: "2025-04-15",
            description: "Aluguel",
            type: "despesa",
            category: "Casa",
            amount: 1200,
                status: "2/4",
        },
    ],

    get filteredTransactions() {
        return this.transactions.filter((t) => {
            const byMonth = this.filters.month
                ? t.date.startsWith(this.filters.month)
                : true;
            const byType = this.filters.type
                ? t.type === this.filters.type
                : true;
            const byStatus = this.filters.status
                ? t.status === this.filters.status
                : true;
            return byMonth && byType && byStatus;
        });
    },

    saveTransaction() {
        this.transactions.push({ ...this.newTransaction, id: Date.now() });
        this.showModal = false;
        this.resetForm();
    },

    resetForm() {
        this.newTransaction = {
            description: "",
            date: "",
            type: "despesa",
            category: "",
            amount: "",
            status: "pendente",
        };
    },

    formatCurrency(value) {
        return new Intl.NumberFormat("pt-BR", {
            style: "currency",
            currency: "BRL",
        }).format(value);
    },

    editTransaction(transaction) {
        this.newTransaction = { ...transaction };
        this.showModal = true;
    },

    deleteTransaction(id) {
        this.transactions = this.transactions.filter((t) => t.id !== id);
    },
});

Alpine.data("transactionControl", transactionControl);
