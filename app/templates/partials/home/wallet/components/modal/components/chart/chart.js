import Alpine from "alpinejs";
import ApexCharts from "apexcharts";

const incomePieChart = () => ({
    chart: null,

    init() {
        this.renderChart();
    },

    renderChart() {
        const store = Alpine.store("walletStore");
        const committed = store.committedAmount;
        const balance = store.monthBalance;
        const total = store.totalIncome;

        const options = {
            chart: {
                type: "donut",
                height: 90,
            },
            // labels: ["Comprometido", "Sobra"],
            series: [(committed / total) * 100, (balance / total) * 100],
            colors: ["#f06543", "#2ed8b6"],
            dataLabels: {
                enabled: true,
                formatter: (val) => `${val.toFixed(1)}%`,
            },
            legend: {
                show: false
            },
            tooltip: {
                y: {
                    formatter: (val) => `${val.toFixed(1)}%`,
                },
            },
        };

        this.chart = new ApexCharts(
            document.getElementById("income-pie-chart"),
            options
        );
        this.chart.render();
    },

    updateChart() {
        const store = Alpine.store("walletStore");
        const committed = store.committedAmount;
        const balance = store.monthBalance;
        const total = store.totalIncome;

        this.chart.updateSeries([
            (committed / total) * 100,
            (balance / total) * 100,
        ]);
    },
});

Alpine.data("incomePieChart", incomePieChart);
