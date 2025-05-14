import Alpine from "alpinejs";
import ApexCharts from "apexcharts";

const chartControl = () => ({
    chart: null,

    init() {
        const options = {
            chart: {
                type: "bar",
                height: 300,
            },
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "50%",
                    distributed: true,
                },
            },
            dataLabels: {
                enabled: true,
                style: {
                    fontSize: "12px",
                },
                formatter: (val) => `R$ ${val.toFixed(2)}`,
            },
            series: [
                {
                    data: [1350, 900, 700, 400,400, 300,300, 200],
                },
            ],
            xaxis: {
                categories: [
                    "Alimentação",
                    "Transporte",
                    "Lazer",
                    "Educação",
                    "Alimentação",
                    "Transporte",
                    "Lazer", 
                ],

                labels: {
                    style: {
                        fontSize: "14px",
                    },
                },

                title: {
                    text: "Valor gasto (R$)",
                },
            },
            colors: ["#00a8cc", "#2ed8b6", "#f06543", "#db5e5e"],
            legend: {
                show: false,
            },
        };

        this.chart = new ApexCharts(
            document.getElementById("column-chart"),
            options
        );
        this.chart.render();
    },
});

Alpine.data("chartControl", chartControl);
